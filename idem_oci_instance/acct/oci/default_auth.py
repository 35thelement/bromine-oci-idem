import base64
import hashlib

from typing import Any
from typing import Dict
from datetime import datetime

from dict_tools.data import NamespaceDict

DEFAULT_ENDPOINT_URL = "/20160918"


async def gather(hub, profiles) -> Dict[str, Any]:
    """
    Generate token with basic auth

    Example:
    .. code-block:: yaml

        oci:
          profile_name:
            username: my_user
            password: my_token
            endpoint_url: https://oci.com
    """
    sub_profiles = {}
    for (
        profile,
        ctx,
    ) in profiles.get("oci", {}).items():
        endpoint_url = ctx.get("endpoint_url")

        keyId = (
            f"{ctx.get('tenancy_ocid')}/{ctx.get('user_ocid')}/{ctx.get('fingerprint')}"
        )
        toBeHashed = f"{ctx.get('private_key')}".encode("utf-8")
        hashed = hashlib.sha256(toBeHashed).hexdigest()

        utcdate = datetime.utcnow()

        # temp_ctx = NamespaceDict(
        #     acct={
        #         "endpoint_url": endpoint_url,
        #         "headers": {
        #             "Date": f"{utcdate}",
        #             "Authorization": f"Signature version=\"1\", keyId=\"{base64.b64encode(keyId.encode('utf-8')).decode('ascii')}\", algorithm=\"rsa-sha256\",headers=\"(request-target) date host\",signature=\"{base64.b64encode(hashed.encode('utf-8')).decode('ascii')}\"",
        #         },
        #     }
        # )

        # ret = await hub.tool.oci.session.request(
        #     temp_ctx,
        #     method="post",
        #     # TODO: Change Login path
        #     path="TODO".format(**{}),
        #     data={},
        # )

        # if not ret["result"]:
        #     error = f"Unable to authenticate: {ret.get('comment', '')}"
        #     hub.log.error(error)
        #     raise ConnectionError(error)

        # TODO: Find the token value in response
        # access_token = ret["ret"]["token"]
        sub_profiles[profile] = dict(
            endpoint_url=endpoint_url,
            # TODO: Replace the header that should be passed to future requests
            headers={
                "Date": f"{utcdate}",
                "Authorization": f"Signature version=\"1\", keyId=\"{base64.b64encode(keyId.encode('utf-8')).decode('ascii')}\", algorithm=\"rsa-sha256\",headers=\"(request-target) date host\",signature=\"{base64.b64encode(hashed.encode('utf-8')).decode('ascii')}\"",
            },
        )
    return sub_profiles
