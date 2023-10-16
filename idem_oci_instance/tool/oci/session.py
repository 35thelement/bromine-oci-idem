import base64
import hashlib
import json
import httpsig_cffi.sign
import six
from datetime import datetime
from typing import Any
from typing import Dict
from urllib import parse
from urllib.parse import urlparse

import aiohttp
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding


async def request(
    hub,
    ctx,
    method: str,
    path: str,
    query_params: Dict[str, str] = {},
    data: Dict[str, Any] = {},
    headers: Dict[str, Any] = {},
):
    # Enable trace logging listener for the http client
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(hub.tool.oci.session.on_request_start)
    trace_config.on_request_end.append(hub.tool.oci.session.on_request_end)

    # path usually starts with "/" in openapi spec
    url = "".join((ctx.acct.endpoint_url.rstrip("/"), path))

    async with aiohttp.ClientSession(
        loop=hub.pop.Loop,
        trace_configs=[trace_config],
    ) as session:
        result = dict(ret=None, result=True, status=200, comment=[], headers={})

        if not headers.get("content-type"):
            headers["content-type"] = "application/json"
            headers["accept"] = "application/json"

        if "headers" in ctx.acct:
            # The acct login could set authorization and other headers
            headers.update(ctx.acct.headers)

        query_params_sanitized = {
            k: v for k, v in query_params.items() if v is not None
        }

        payload = json.dumps(data)
        headers = _headers(ctx, url, method, query_params_sanitized, payload)

        async with session.request(
            url=url,
            method=method.lower(),
            ssl=False,
            allow_redirects=True,
            params=query_params_sanitized,
            data=payload,
            headers=headers,
        ) as response:
            result["status"] = response.status
            result["result"] = 200 <= response.status <= 204
            result["comment"].append(response.reason)
            result["headers"].update(response.headers)
            try:
                resp_data = await response.read()
                result["ret"] = hub.tool.type.dict.namespaced(json.loads(resp_data))
                response.raise_for_status()
            except Exception as err:
                result["comment"].append(result["ret"])
                result["comment"].append(f"{err.__class__.__name__}: {err}")
                result["result"] = False
                if response.status != 404:
                    try:
                        ret = await response.read()
                        result["ret"] = ret.decode() if hasattr(ret, "decode") else ret
                    except Exception as ex_read_err:
                        result["comment"].append(
                            f"Failed to read response: {ex_read_err.__class__.__name__}: {ex_read_err}"
                        )

            return result


async def on_request_start(hub, session, trace_config_ctx, params):
    hub.log.debug("Starting %s" % params)


async def on_request_end(hub, session, trace_config_ctx, params):
    hub.log.debug("Ending %s" % params)


def _headers(ctx, raw_url, method, query_params={}, payload=""):
    # Get Host
    url_host = urlparse(raw_url)
    host = url_host.netloc
    path = url_host.path

    # Current date
    # Note: Maximum clock skew is 5 minutes
    current_date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

    # Headers
    host_header = f"host: {host}"
    date_header = f"date: {current_date}"
    escaped_target = (
        path + "?" + parse.urlencode(query_params) if query_params else path
    )
    request_target_header = f"(request-target): {method} {escaped_target}"

    # Signing String
    signing_string_array = [date_header, request_target_header, host_header]

    headers_to_sign = ["date", "(request-target)", "host"]

    # Handles requests with body (POST, PUT, and PATCH)
    methods_that_require_extra_headers = ["POST", "PUT", "PATCH"]
    if method.upper() in methods_that_require_extra_headers:
        body = payload.encode("utf-8")
        body_hash = hashlib.sha256(body).digest()
        base64_encoded_body_hash = base64.b64encode(body_hash).decode("utf-8")
        content_sha256_header = f"x-content-sha256: {base64_encoded_body_hash}"
        signing_string_array.extend(
            [
                f"content-length: {len(body)}",
                "content-type: application/json",
                content_sha256_header,
            ]
        )

        headers_to_sign.extend(["content-length", "content-type", "x-content-sha256"])

    # Joins
    headers = " ".join(headers_to_sign)
    signing_string = "\n".join(signing_string_array)

    # Generates OCI Signature for Authorization
    private_key_bytes = ctx.acct.private_key.encode("utf-8")

    if ctx.acct.passphrase is None or ctx.acct.passphrase == "":
        private_key = serialization.load_pem_private_key(
            private_key_bytes, password=None
        )
    else:
        private_key = serialization.load_pem_private_key(
            private_key_bytes, password=ctx.acct.passphrase.encode("utf-8")
        )

    signature = private_key.sign(
        signing_string.encode(), padding.PKCS1v15(), hashes.SHA256()
    )

    base64_encoded_signature = base64.b64encode(signature).decode("utf-8")
    response = f'Signature version="1",keyId="{ctx.acct.api_key}",algorithm="rsa-sha256",headers="{headers}",signature="{base64_encoded_signature}"'
    header_dict = {
        "Date": current_date,
        "Authorization": response,
    }

    if method.upper() in methods_that_require_extra_headers:
        header_dict["Content-Type"] = "application/json"
        header_dict["x-content-sha256"] = base64_encoded_body_hash

    return header_dict
