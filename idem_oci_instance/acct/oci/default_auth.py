from typing import Any
from typing import Dict

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
        endpoint_url = f"{ctx.get('endpoint_url').replace('{region_name}', ctx.get('region'))}{DEFAULT_ENDPOINT_URL}"
        sub_profiles[profile] = dict(
            endpoint_url=endpoint_url,
            compartment_id=ctx.get("compartment"),
            api_key=f"{ctx.get('tenancy_ocid')}/{ctx.get('user_ocid')}/{ctx.get('fingerprint')}",
        )
    return sub_profiles
