"""Utility functions for Virtual Networks. """
from collections import OrderedDict
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import Dict
from typing import List


async def list_allowed_peer_regions_for_remote_peering(hub, ctx) -> Dict[str, Any]:
    r"""

    ListAllowedPeerRegionsForRemotePeering
        Lists the regions that support remote VCN peering (which is peering across regions).
    For more information, see [VCN Peering](/iaas/Content/Network/Tasks/VCNpeering.htm).


    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/allowedPeerRegionsForRemotePeering".format(**{}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_byoip_ranges(
    hub,
    ctx,
    compartment_id: str,
    opc_request_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    lifecycle_state: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

    ListByoipRanges
        Lists the `ByoipRange` resources in the specified compartment.
    You can filter the list using query parameters.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the given lifecycle state name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/byoipRanges".format(**{}),
        query_params={
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "lifecycleState": lifecycle_state,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "compartmentId": compartment_id,
        },
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict({"items": "items"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def create_byoip_range(
    hub,
    ctx,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    cidr_block: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    ipv6_cidr_block: str = None,
) -> Dict[str, Any]:
    r"""

    CreateByoipRange
        Creates a subrange of the BYOIP CIDR block.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the BYOIP CIDR block.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        cidr_block(str, Optional):
            The BYOIP CIDR block. You can assign some or all of it to a public IP pool after it is validated.
            Example: `10.0.1.0/24`
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        ipv6_cidr_block(str, Optional):
            The BYOIPv6 prefix. You can assign some or all of it to a VCN after it is validated.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "cidr_block": "cidrBlock",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "ipv6_cidr_block": "ipv6CidrBlock",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/byoipRanges".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "byoipRangeVcnIpv6Allocations": "byoip_range_vcn_ipv6_allocations",
            "cidrBlock": "cidr_block",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipv6CidrBlock": "ipv6_cidr_block",
            "lifecycleDetails": "lifecycle_details",
            "lifecycleState": "lifecycle_state",
            "timeAdvertised": "time_advertised",
            "timeCreated": "time_created",
            "timeValidated": "time_validated",
            "timeWithdrawn": "time_withdrawn",
            "validationToken": "validation_token",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_byoip_range(
    hub, ctx, byoip_range_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetByoipRange
        Gets the `ByoipRange` resource. You must specify the [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    Args:
        byoip_range_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR block.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/byoipRanges/{byoipRangeId}".format(**{"byoipRangeId": byoip_range_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "byoipRangeVcnIpv6Allocations": "byoip_range_vcn_ipv6_allocations",
            "cidrBlock": "cidr_block",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipv6CidrBlock": "ipv6_cidr_block",
            "lifecycleDetails": "lifecycle_details",
            "lifecycleState": "lifecycle_state",
            "timeAdvertised": "time_advertised",
            "timeCreated": "time_created",
            "timeValidated": "time_validated",
            "timeWithdrawn": "time_withdrawn",
            "validationToken": "validation_token",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_byoip_range(
    hub,
    ctx,
    byoip_range_id: str,
    opc_request_id: str = None,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    UpdateByoipRange
        Updates the tags or display name associated to the specified BYOIP CIDR block.

    Args:
        byoip_range_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR block.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/byoipRanges/{byoipRangeId}".format(**{"byoipRangeId": byoip_range_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "byoipRangeVcnIpv6Allocations": "byoip_range_vcn_ipv6_allocations",
            "cidrBlock": "cidr_block",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipv6CidrBlock": "ipv6_cidr_block",
            "lifecycleDetails": "lifecycle_details",
            "lifecycleState": "lifecycle_state",
            "timeAdvertised": "time_advertised",
            "timeCreated": "time_created",
            "timeValidated": "time_validated",
            "timeWithdrawn": "time_withdrawn",
            "validationToken": "validation_token",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_byoip_range(
    hub, ctx, byoip_range_id: str, opc_request_id: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteByoipRange
        Deletes the specified `ByoipRange` resource.
    The resource must be in one of the following states: CREATING, PROVISIONED, ACTIVE, or FAILED.
    It must not have any subranges currently allocated to a PublicIpPool object or the deletion will fail.
    You must specify the [OCID](/iaas/Content/General/Concepts/identifiers.htm).
    If the `ByoipRange` resource is currently in the PROVISIONED or ACTIVE state, it will be de-provisioned and then deleted.

    Args:
        byoip_range_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR block.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/byoipRanges/{byoipRangeId}".format(**{"byoipRangeId": byoip_range_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def advertise_byoip_range(
    hub, ctx, byoip_range_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    AdvertiseByoipRange
        Begins BGP route advertisements for the BYOIP CIDR block you imported to the Oracle Cloud.
    The `ByoipRange` resource must be in the PROVISIONED state before the BYOIP CIDR block routes can be advertised with BGP.

    Args:
        byoip_range_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR block.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/byoipRanges/{byoipRangeId}/actions/advertise".format(
            **{"byoipRangeId": byoip_range_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_byoip_range_compartment(
    hub,
    ctx,
    byoip_range_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeByoipRangeCompartment
        Moves a BYOIP CIDR block to a different compartment. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        byoip_range_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR block.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the destination compartment for the BYOIP CIDR block move.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/byoipRanges/{byoipRangeId}/actions/changeCompartment".format(
            **{"byoipRangeId": byoip_range_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def validate_byoip_range(
    hub, ctx, byoip_range_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    ValidateByoipRange
        Submits the BYOIP CIDR block you are importing for validation. Do not submit to Oracle for validation if you have not already
    modified the information for the BYOIP CIDR block with your Regional Internet Registry. See [To import a CIDR block](/iaas/Content/Network/Concepts/BYOIP.htm#import_cidr) for details.

    Args:
        byoip_range_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR block.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/byoipRanges/{byoipRangeId}/actions/validate".format(
            **{"byoipRangeId": byoip_range_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def withdraw_byoip_range(
    hub, ctx, byoip_range_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    WithdrawByoipRange
        Withdraws BGP route advertisement for the BYOIP CIDR block.

    Args:
        byoip_range_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR block.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/byoipRanges/{byoipRangeId}/actions/withdraw".format(
            **{"byoipRangeId": byoip_range_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_byoip_allocated_ranges(
    hub,
    ctx,
    byoip_range_id: str,
    opc_request_id: str = None,
    limit: int = None,
    page: str = None,
) -> Dict[str, Any]:
    r"""

    ListByoipAllocatedRanges
        Lists the subranges of a BYOIP CIDR block currently allocated to an IP pool.
    Each `ByoipAllocatedRange` object also lists the IP pool where it is allocated.

    Args:
        byoip_range_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR block.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/byoipRanges/{byoipRangeId}/byoipAllocatedRanges".format(
            **{"byoipRangeId": byoip_range_id}
        ),
        query_params={"limit": limit, "page": page},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict({"items": "items"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_capture_filters(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    opc_request_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
    display_name: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListCaptureFilters
        Lists the capture filters in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the given capture filter lifecycle state.
            The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/captureFilters".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "displayName": display_name,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_capture_filter(
    hub,
    ctx,
    compartment_id: str,
    filter_type: str,
    opc_retry_token: str = None,
    opc_request_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    vtap_capture_filter_rules: List[
        make_dataclass(
            "vtap_capture_filter_rules",
            [
                ("traffic_direction", str),
                ("destination_cidr", str, field(default=None)),
                (
                    "icmp_options",
                    make_dataclass(
                        "icmp_options",
                        [("type", int), ("code", int, field(default=None))],
                    ),
                    field(default=None),
                ),
                ("protocol", str, field(default=None)),
                ("rule_action", str, field(default=None)),
                ("source_cidr", str, field(default=None)),
                (
                    "tcp_options",
                    make_dataclass(
                        "tcp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "udp_options",
                    make_dataclass(
                        "udp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    CreateCaptureFilter
        Creates a virtual test access point (VTAP) capture filter in the specified compartment.

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains
    the VTAP. For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).
    For information about OCIDs, see [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the VTAP, otherwise a default is provided.
    It does not have to be unique, and you can change it.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the capture filter.


        filter_type(str):
            Indicates which service will use this capture filter.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        vtap_capture_filter_rules(List[dict[str, Any]], Optional):
            The set of rules governing what traffic a VTAP mirrors.
            Defaults to None.

            * destination_cidr (str, Optional):
                Traffic sent to this CIDR block through the VTAP source will be mirrored to the VTAP target.
                Defaults to None.

            * icmp_options (dict[str, Any], Optional):
                icmpOptions. Defaults to None.

                * code (int, Optional):
                    The ICMP code (optional). Defaults to None.

                * type (int):
                    The ICMP type.

            * protocol (str, Optional):
                The transport protocol used in the filter. If do not choose a protocol, all protocols will be used in the filter.
                Supported options are:
                  * 1 = ICMP
                  * 6 = TCP
                  * 17 = UDP
                Defaults to None.

            * rule_action (str, Optional):
                Include or exclude packets meeting this definition from mirrored traffic.
                Defaults to None.

            * source_cidr (str, Optional):
                Traffic from this CIDR block to the VTAP source will be mirrored to the VTAP target.
                Defaults to None.

            * tcp_options (dict[str, Any], Optional):
                tcpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


            * traffic_direction (str):
                The traffic direction the VTAP is configured to mirror.


            * udp_options (dict[str, Any], Optional):
                udpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "filter_type": "filterType",
        "freeform_tags": "freeformTags",
        "vtap_capture_filter_rules": "vtapCaptureFilterRules",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/captureFilters".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "filterType": "filter_type",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vtapCaptureFilterRules": "vtap_capture_filter_rules",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_capture_filter(
    hub, ctx, capture_filter_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetCaptureFilter
        Gets information about the specified VTAP capture filter.

    Args:
        capture_filter_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the capture filter.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/captureFilters/{captureFilterId}".format(
            **{"captureFilterId": capture_filter_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "filterType": "filter_type",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vtapCaptureFilterRules": "vtap_capture_filter_rules",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_capture_filter(
    hub,
    ctx,
    capture_filter_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    vtap_capture_filter_rules: List[
        make_dataclass(
            "vtap_capture_filter_rules",
            [
                ("traffic_direction", str),
                ("destination_cidr", str, field(default=None)),
                (
                    "icmp_options",
                    make_dataclass(
                        "icmp_options",
                        [("type", int), ("code", int, field(default=None))],
                    ),
                    field(default=None),
                ),
                ("protocol", str, field(default=None)),
                ("rule_action", str, field(default=None)),
                ("source_cidr", str, field(default=None)),
                (
                    "tcp_options",
                    make_dataclass(
                        "tcp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "udp_options",
                    make_dataclass(
                        "udp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    UpdateCaptureFilter
        Updates the specified VTAP capture filter's display name or tags.

    Args:
        capture_filter_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the capture filter.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        vtap_capture_filter_rules(List[dict[str, Any]], Optional):
            The set of rules governing what traffic a VTAP mirrors.
            Defaults to None.

            * destination_cidr (str, Optional):
                Traffic sent to this CIDR block through the VTAP source will be mirrored to the VTAP target.
                Defaults to None.

            * icmp_options (dict[str, Any], Optional):
                icmpOptions. Defaults to None.

                * code (int, Optional):
                    The ICMP code (optional). Defaults to None.

                * type (int):
                    The ICMP type.

            * protocol (str, Optional):
                The transport protocol used in the filter. If do not choose a protocol, all protocols will be used in the filter.
                Supported options are:
                  * 1 = ICMP
                  * 6 = TCP
                  * 17 = UDP
                Defaults to None.

            * rule_action (str, Optional):
                Include or exclude packets meeting this definition from mirrored traffic.
                Defaults to None.

            * source_cidr (str, Optional):
                Traffic from this CIDR block to the VTAP source will be mirrored to the VTAP target.
                Defaults to None.

            * tcp_options (dict[str, Any], Optional):
                tcpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


            * traffic_direction (str):
                The traffic direction the VTAP is configured to mirror.


            * udp_options (dict[str, Any], Optional):
                udpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "vtap_capture_filter_rules": "vtapCaptureFilterRules",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/captureFilters/{captureFilterId}".format(
            **{"captureFilterId": capture_filter_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "filterType": "filter_type",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vtapCaptureFilterRules": "vtap_capture_filter_rules",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_capture_filter(
    hub, ctx, capture_filter_id: str, if_match: str = None, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    DeleteCaptureFilter
        Deletes the specified VTAP capture filter. This is an asynchronous operation. The VTAP capture filter's `lifecycleState` will
    change to TERMINATING temporarily until the VTAP capture filter is completely removed.

    Args:
        capture_filter_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the capture filter.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/captureFilters/{captureFilterId}".format(
            **{"captureFilterId": capture_filter_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_capture_filter_compartment(
    hub,
    ctx,
    capture_filter_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeCaptureFilterCompartment
        Moves a capture filter to a new compartment in the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        capture_filter_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the capture filter.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the destination compartment for the VTAP
            capture filter move.


        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/captureFilters/{captureFilterId}/actions/changeCompartment".format(
            **{"captureFilterId": capture_filter_id}
        ),
        query_params={},
        data=payload,
        headers={
            "if-match": if_match,
            "opc-request-id": opc_request_id,
            "opc-retry-token": opc_retry_token,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_cpe_device_shapes(
    hub, ctx, limit: int = None, page: str = None, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    ListCpeDeviceShapes
        Lists the CPE device types that the Networking service provides CPE configuration
    content for (example: Cisco ASA). The content helps a network engineer configure
    the actual CPE device represented by a [Cpe](#/en/iaas/latest/Cpe/) object.

    If you want to generate CPE configuration content for one of the returned CPE device types,
    ensure that the [Cpe](#/en/iaas/latest/Cpe/) object's `cpeDeviceShapeId` attribute is set
    to the CPE device type's [OCID](/iaas/Content/General/Concepts/identifiers.htm) (returned by this operation).

    For information about generating CPE configuration content, see these operations:

      * [GetCpeDeviceConfigContent](#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
      * [GetIpsecCpeDeviceConfigContent](#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
      * [GetTunnelCpeDeviceConfigContent](#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)

    Args:
        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/cpeDeviceShapes".format(**{}),
        query_params={"limit": limit, "page": page},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_cpe_device_shape(
    hub, ctx, cpe_device_shape_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetCpeDeviceShape
        Gets the detailed information about the specified CPE device type. This might include a set of questions
    that are specific to the particular CPE device type. The customer must supply answers to those questions
    (see [UpdateTunnelCpeDeviceConfig](#/en/iaas/latest/TunnelCpeDeviceConfig/UpdateTunnelCpeDeviceConfig)).
    The service merges the answers with a template of other information for the CPE device type. The following
    operations return the merged content:

      * [GetCpeDeviceConfigContent](#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
      * [GetIpsecCpeDeviceConfigContent](#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
      * [GetTunnelCpeDeviceConfigContent](#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)

    Args:
        cpe_device_shape_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the CPE device shape.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/cpeDeviceShapes/{cpeDeviceShapeId}".format(
            **{"cpeDeviceShapeId": cpe_device_shape_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "cpeDeviceInfo": "cpe_device_info",
            "cpeDeviceShapeId": "cpe_device_shape_id",
            "parameters": "parameters",
            "template": "template",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_cpes(
    hub, ctx, compartment_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListCpes
        Lists the customer-premises equipment objects (CPEs) in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/cpes".format(**{}),
        query_params={"compartmentId": compartment_id, "limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_cpe(
    hub,
    ctx,
    compartment_id: str,
    ip_address: str,
    opc_retry_token: str = None,
    cpe_device_shape_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    is_private: bool = None,
) -> Dict[str, Any]:
    r"""

    CreateCpe
        Creates a new virtual customer-premises equipment (CPE) object in the specified compartment. For
    more information, see [Site-to-Site VPN Overview](/iaas/Content/Network/Tasks/overviewIPsec.htm).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want
    the CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec
    connection or other Networking Service components. If you're not sure which compartment to
    use, put the CPE in the same compartment as the DRG. For more information about
    compartments and access control, see [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).
    For information about OCIDs, see [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You must provide the public IP address of your on-premises router. See
    [CPE Configuration](/iaas/Content/Network/Tasks/configuringCPE.htm).

    You may optionally specify a *display name* for the CPE, otherwise a default is provided. It does not have to
    be unique, and you can change it. Avoid entering confidential information.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the CPE.

        ip_address(str):
            The public IP address of the on-premises router.

            Example: `203.0.113.2`


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        cpe_device_shape_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the CPE device type. You can provide
            a value if you want to later generate CPE device configuration content for IPSec connections
            that use this CPE. You can also call [UpdateCpe](#/en/iaas/latest/Cpe/UpdateCpe) later to
            provide a value. For a list of possible values, see
            [ListCpeDeviceShapes](#/en/iaas/latest/CpeDeviceShapeSummary/ListCpeDeviceShapes).

            For more information about generating CPE device configuration content, see:

              * [GetCpeDeviceConfigContent](#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
              * [GetIpsecCpeDeviceConfigContent](#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
              * [GetTunnelCpeDeviceConfigContent](#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)
              * [GetTunnelCpeDeviceConfig](#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfig)
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        is_private(bool, Optional):
            Indicates whether this CPE is of type `private` or not.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "cpe_device_shape_id": "cpeDeviceShapeId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "ip_address": "ipAddress",
        "is_private": "isPrivate",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/cpes".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "cpeDeviceShapeId": "cpe_device_shape_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "isPrivate": "is_private",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_cpe(hub, ctx, cpe_id: str) -> Dict[str, Any]:
    r"""

    GetCpe
        Gets the specified CPE's information.

    Args:
        cpe_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the CPE.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/cpes/{cpeId}".format(**{"cpeId": cpe_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "cpeDeviceShapeId": "cpe_device_shape_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "isPrivate": "is_private",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_cpe(
    hub,
    ctx,
    cpe_id: str,
    if_match: str = None,
    cpe_device_shape_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    UpdateCpe
        Updates the specified CPE's display name or tags.
    Avoid entering confidential information.

    Args:
        cpe_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the CPE.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        cpe_device_shape_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the CPE device type. You can provide
            a value if you want to generate CPE device configuration content for IPSec connections
            that use this CPE. For a list of possible values, see
            [ListCpeDeviceShapes](#/en/iaas/latest/CpeDeviceShapeSummary/ListCpeDeviceShapes).

            For more information about generating CPE device configuration content, see:

              * [GetCpeDeviceConfigContent](#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
              * [GetIpsecCpeDeviceConfigContent](#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
              * [GetTunnelCpeDeviceConfigContent](#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)
              * [GetTunnelCpeDeviceConfig](#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfig)
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "cpe_device_shape_id": "cpeDeviceShapeId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/cpes/{cpeId}".format(**{"cpeId": cpe_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "cpeDeviceShapeId": "cpe_device_shape_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "isPrivate": "is_private",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_cpe(hub, ctx, cpe_id: str, if_match: str = None) -> Dict[str, Any]:
    r"""

    DeleteCpe
        Deletes the specified CPE object. The CPE must not be connected to a DRG. This is an asynchronous
    operation. The CPE's `lifecycleState` will change to TERMINATING temporarily until the CPE is completely
    removed.

    Args:
        cpe_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the CPE.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/cpes/{cpeId}".format(**{"cpeId": cpe_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_cpe_compartment(
    hub,
    ctx,
    cpe_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeCpeCompartment
        Moves a CPE object into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        cpe_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the CPE.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            CPE object to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/cpes/{cpeId}/actions/changeCompartment".format(**{"cpeId": cpe_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_cpe_device_config_content(
    hub, ctx, cpe_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetCpeDeviceConfigContent
        Renders a set of CPE configuration content that can help a network engineer configure the actual
    CPE device (for example, a hardware router) represented by the specified [Cpe](#/en/iaas/latest/Cpe/)
    object.

    The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the
    [Cpe](#/en/iaas/latest/Cpe/) must have the CPE's device type specified by the `cpeDeviceShapeId`
    attribute. The content optionally includes answers that the customer provides (see
    [UpdateTunnelCpeDeviceConfig](#/en/iaas/latest/TunnelCpeDeviceConfig/UpdateTunnelCpeDeviceConfig)),
    merged with a template of other information specific to the CPE device type.

    The operation returns configuration information for *all* of the
    [IPSecConnection](#/en/iaas/latest/IPSecConnection/) objects that use the specified CPE.
    Here are similar operations:

      * [GetIpsecCpeDeviceConfigContent](#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
      returns CPE configuration content for all IPSec tunnels in a single IPSec connection.
      * [GetTunnelCpeDeviceConfigContent](#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)
      returns CPE configuration content for a specific IPSec tunnel in an IPSec connection.

    Args:
        cpe_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the CPE.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/cpes/{cpeId}/cpeConfigContent".format(**{"cpeId": cpe_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_cross_connect_groups(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListCrossConnectGroups
        Lists the cross-connect groups in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the specified lifecycle
            state. The value is case insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/crossConnectGroups".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_cross_connect_group(
    hub,
    ctx,
    compartment_id: str,
    opc_retry_token: str = None,
    customer_reference_name: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    macsec_properties: make_dataclass(
        "macsec_properties",
        [
            ("state", str),
            ("encryption_cipher", str, field(default=None)),
            ("is_unprotected_traffic_allowed", bool, field(default=None)),
            (
                "primary_key",
                make_dataclass(
                    "primary_key",
                    [
                        ("connectivity_association_key_secret_id", str),
                        ("connectivity_association_name_secret_id", str),
                    ],
                ),
                field(default=None),
            ),
        ],
    ) = None,
) -> Dict[str, Any]:
    r"""

    CreateCrossConnectGroup
        Creates a new cross-connect group to use with Oracle Cloud Infrastructure
    FastConnect. For more information, see
    [FastConnect Overview](/iaas/Content/Network/Concepts/fastconnect.htm).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the
    compartment where you want the cross-connect group to reside. If you're
    not sure which compartment to use, put the cross-connect group in the
    same compartment with your VCN. For more information about
    compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).
    For information about OCIDs, see
    [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the cross-connect group.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the cross-connect group.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        customer_reference_name(str, Optional):
            A reference name or identifier for the physical fiber connection that this cross-connect
            group uses.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        macsec_properties(dict[str, Any], Optional):
            macsecProperties. Defaults to None.

            * encryption_cipher (str, Optional):
                Type of encryption cipher suite to use for the MACsec connection. Defaults to None.

            * is_unprotected_traffic_allowed (bool, Optional):
                Indicates whether unencrypted traffic is allowed if MACsec Key Agreement protocol (MKA) fails. Defaults to None.

            * primary_key (dict[str, Any], Optional):
                primaryKey. Defaults to None.

                * connectivity_association_key_secret_id (str):
                    Secret [OCID](/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity Association Key (CAK) of this MACsec key.

                    NOTE: Only the latest secret version will be used.


                * connectivity_association_name_secret_id (str):
                    Secret [OCID](/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity association Key Name (CKN) of this MACsec key.

                    NOTE: Only the latest secret version will be used.


            * state (str):
                Indicates whether or not MACsec is enabled.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "customer_reference_name": "customerReferenceName",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "macsec_properties": "macsecProperties",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/crossConnectGroups".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "customerReferenceName": "customer_reference_name",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "macsecProperties": "macsec_properties",
            "ociLogicalDeviceName": "oci_logical_device_name",
            "ociPhysicalDeviceName": "oci_physical_device_name",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_cross_connect_group(
    hub, ctx, cross_connect_group_id: str
) -> Dict[str, Any]:
    r"""

    GetCrossConnectGroups
        Gets the specified cross-connect group's information.

    Args:
        cross_connect_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect group.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/crossConnectGroups/{crossConnectGroupId}".format(
            **{"crossConnectGroupId": cross_connect_group_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "customerReferenceName": "customer_reference_name",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "macsecProperties": "macsec_properties",
            "ociLogicalDeviceName": "oci_logical_device_name",
            "ociPhysicalDeviceName": "oci_physical_device_name",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_cross_connect_group(
    hub,
    ctx,
    cross_connect_group_id: str,
    if_match: str = None,
    customer_reference_name: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    macsec_properties: make_dataclass(
        "macsec_properties",
        [
            ("state", str),
            ("encryption_cipher", str, field(default=None)),
            ("is_unprotected_traffic_allowed", bool, field(default=None)),
            (
                "primary_key",
                make_dataclass(
                    "primary_key",
                    [
                        ("connectivity_association_key_secret_id", str),
                        ("connectivity_association_key_secret_version", int),
                        ("connectivity_association_name_secret_id", str),
                        ("connectivity_association_name_secret_version", int),
                    ],
                ),
                field(default=None),
            ),
        ],
    ) = None,
) -> Dict[str, Any]:
    r"""

    UpdateCrossConnectGroup
        Updates the specified cross-connect group's display name.
    Avoid entering confidential information.

    Args:
        cross_connect_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect group.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        customer_reference_name(str, Optional):
            A reference name or identifier for the physical fiber connection this cross-connect group uses.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        macsec_properties(dict[str, Any], Optional):
            macsecProperties. Defaults to None.

            * encryption_cipher (str, Optional):
                Type of encryption cipher suite to use for the MACsec connection. Defaults to None.

            * is_unprotected_traffic_allowed (bool, Optional):
                Indicates whether unencrypted traffic is allowed if MACsec Key Agreement protocol (MKA) fails. Defaults to None.

            * primary_key (dict[str, Any], Optional):
                primaryKey. Defaults to None.

                * connectivity_association_key_secret_id (str):
                    Secret [OCID](/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity Association Key (CAK) of this MACsec key.


                * connectivity_association_key_secret_version (int):
                    The secret version of the connectivityAssociationKey secret in Vault.

                * connectivity_association_name_secret_id (str):
                    Secret [OCID](/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity Association Key Name (CKN) of this MACsec key.


                * connectivity_association_name_secret_version (int):
                    The secret version of the connectivity association name secret in Vault.

            * state (str):
                Indicates whether or not MACsec is enabled.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "customer_reference_name": "customerReferenceName",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "macsec_properties": "macsecProperties",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/crossConnectGroups/{crossConnectGroupId}".format(
            **{"crossConnectGroupId": cross_connect_group_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "customerReferenceName": "customer_reference_name",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "macsecProperties": "macsec_properties",
            "ociLogicalDeviceName": "oci_logical_device_name",
            "ociPhysicalDeviceName": "oci_physical_device_name",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_cross_connect_group(
    hub, ctx, cross_connect_group_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteCrossConnectGroup
        Deletes the specified cross-connect group. It must not contain any
    cross-connects, and it cannot be mapped to a
    [VirtualCircuit](#/en/iaas/latest/VirtualCircuit/).

    Args:
        cross_connect_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect group.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/crossConnectGroups/{crossConnectGroupId}".format(
            **{"crossConnectGroupId": cross_connect_group_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_cross_connect_group_compartment(
    hub,
    ctx,
    cross_connect_group_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeCrossConnectGroupCompartment
        Moves a cross-connect group into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        cross_connect_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect group.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            cross-connect group to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/crossConnectGroups/{crossConnectGroupId}/actions/changeCompartment".format(
            **{"crossConnectGroupId": cross_connect_group_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_cross_connect_locations(
    hub, ctx, compartment_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListCrossConnectLocations
        Lists the available FastConnect locations for cross-connect installation. You need
    this information so you can specify your desired location when you create a cross-connect.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/crossConnectLocations".format(**{}),
        query_params={"compartmentId": compartment_id, "limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_crossconnect_port_speed_shapes(
    hub, ctx, compartment_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListCrossConnectPortSpeedShapes
        Lists the available port speeds for cross-connects. You need this information
    so you can specify your desired port speed (that is, shape) when you create a
    cross-connect.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/crossConnectPortSpeedShapes".format(**{}),
        query_params={"compartmentId": compartment_id, "limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_cross_connects(
    hub,
    ctx,
    compartment_id: str,
    cross_connect_group_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListCrossConnects
        Lists the cross-connects in the specified compartment. You can filter the list
    by specifying the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of a cross-connect group.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        cross_connect_group_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect group. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the specified lifecycle
            state. The value is case insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/crossConnects".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "crossConnectGroupId": cross_connect_group_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_cross_connect(
    hub,
    ctx,
    compartment_id: str,
    location_name: str,
    port_speed_shape_name: str,
    opc_retry_token: str = None,
    cross_connect_group_id: str = None,
    customer_reference_name: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    far_cross_connect_or_cross_connect_group_id: str = None,
    freeform_tags: Dict = None,
    macsec_properties: make_dataclass(
        "macsec_properties",
        [
            ("state", str),
            ("encryption_cipher", str, field(default=None)),
            ("is_unprotected_traffic_allowed", bool, field(default=None)),
            (
                "primary_key",
                make_dataclass(
                    "primary_key",
                    [
                        ("connectivity_association_key_secret_id", str),
                        ("connectivity_association_name_secret_id", str),
                    ],
                ),
                field(default=None),
            ),
        ],
    ) = None,
    near_cross_connect_or_cross_connect_group_id: str = None,
) -> Dict[str, Any]:
    r"""

    CreateCrossConnect
        Creates a new cross-connect. Oracle recommends you create each cross-connect in a
    [CrossConnectGroup](#/en/iaas/latest/CrossConnectGroup) so you can use link aggregation
    with the connection.

    After creating the `CrossConnect` object, you need to go the FastConnect location
    and request to have the physical cable installed. For more information, see
    [FastConnect Overview](/iaas/Content/Network/Concepts/fastconnect.htm).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the
    compartment where you want the cross-connect to reside. If you're
    not sure which compartment to use, put the cross-connect in the
    same compartment with your VCN. For more information about
    compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).
    For information about OCIDs, see
    [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the cross-connect.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the cross-connect.

        location_name(str):
            The name of the FastConnect location where this cross-connect will be installed.
            To get a list of the available locations, see
            [ListCrossConnectLocations](#/en/iaas/latest/CrossConnectLocation/ListCrossConnectLocations).

            Example: `CyrusOne, Chandler, AZ`


        port_speed_shape_name(str):
            The port speed for this cross-connect. To get a list of the available port speeds, see
            [ListCrossConnectPortSpeedShapes](#/en/iaas/latest/CrossConnectPortSpeedShape/ListCrossconnectPortSpeedShapes).

            Example: `10 Gbps`


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        cross_connect_group_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect group to put this cross-connect in.
            Defaults to None.

        customer_reference_name(str, Optional):
            A reference name or identifier for the physical fiber connection that this cross-connect
            uses.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        far_cross_connect_or_cross_connect_group_id(str, Optional):
            If you already have an existing cross-connect or cross-connect group at this FastConnect
            location, and you want this new cross-connect to be on a different router (for the
            purposes of redundancy), provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of that existing cross-connect or
            cross-connect group.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        macsec_properties(dict[str, Any], Optional):
            macsecProperties. Defaults to None.

            * encryption_cipher (str, Optional):
                Type of encryption cipher suite to use for the MACsec connection. Defaults to None.

            * is_unprotected_traffic_allowed (bool, Optional):
                Indicates whether unencrypted traffic is allowed if MACsec Key Agreement protocol (MKA) fails. Defaults to None.

            * primary_key (dict[str, Any], Optional):
                primaryKey. Defaults to None.

                * connectivity_association_key_secret_id (str):
                    Secret [OCID](/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity Association Key (CAK) of this MACsec key.

                    NOTE: Only the latest secret version will be used.


                * connectivity_association_name_secret_id (str):
                    Secret [OCID](/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity association Key Name (CKN) of this MACsec key.

                    NOTE: Only the latest secret version will be used.


            * state (str):
                Indicates whether or not MACsec is enabled.

        near_cross_connect_or_cross_connect_group_id(str, Optional):
            If you already have an existing cross-connect or cross-connect group at this FastConnect
            location, and you want this new cross-connect to be on the same router, provide the
            [OCID](/iaas/Content/General/Concepts/identifiers.htm) of that existing cross-connect or cross-connect group.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "cross_connect_group_id": "crossConnectGroupId",
        "customer_reference_name": "customerReferenceName",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "far_cross_connect_or_cross_connect_group_id": "farCrossConnectOrCrossConnectGroupId",
        "freeform_tags": "freeformTags",
        "location_name": "locationName",
        "macsec_properties": "macsecProperties",
        "near_cross_connect_or_cross_connect_group_id": "nearCrossConnectOrCrossConnectGroupId",
        "port_speed_shape_name": "portSpeedShapeName",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/crossConnects".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "crossConnectGroupId": "cross_connect_group_id",
            "customerReferenceName": "customer_reference_name",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "locationName": "location_name",
            "macsecProperties": "macsec_properties",
            "ociLogicalDeviceName": "oci_logical_device_name",
            "ociPhysicalDeviceName": "oci_physical_device_name",
            "portName": "port_name",
            "portSpeedShapeName": "port_speed_shape_name",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_cross_connect(hub, ctx, cross_connect_id: str) -> Dict[str, Any]:
    r"""

    GetCrossConnect
        Gets the specified cross-connect's information.

    Args:
        cross_connect_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/crossConnects/{crossConnectId}".format(
            **{"crossConnectId": cross_connect_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "crossConnectGroupId": "cross_connect_group_id",
            "customerReferenceName": "customer_reference_name",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "locationName": "location_name",
            "macsecProperties": "macsec_properties",
            "ociLogicalDeviceName": "oci_logical_device_name",
            "ociPhysicalDeviceName": "oci_physical_device_name",
            "portName": "port_name",
            "portSpeedShapeName": "port_speed_shape_name",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_cross_connect(
    hub,
    ctx,
    cross_connect_id: str,
    if_match: str = None,
    customer_reference_name: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    is_active: bool = None,
    macsec_properties: make_dataclass(
        "macsec_properties",
        [
            ("state", str),
            ("encryption_cipher", str, field(default=None)),
            ("is_unprotected_traffic_allowed", bool, field(default=None)),
            (
                "primary_key",
                make_dataclass(
                    "primary_key",
                    [
                        ("connectivity_association_key_secret_id", str),
                        ("connectivity_association_key_secret_version", int),
                        ("connectivity_association_name_secret_id", str),
                        ("connectivity_association_name_secret_version", int),
                    ],
                ),
                field(default=None),
            ),
        ],
    ) = None,
) -> Dict[str, Any]:
    r"""

    UpdateCrossConnect
        Updates the specified cross-connect.

    Args:
        cross_connect_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        customer_reference_name(str, Optional):
            A reference name or identifier for the physical fiber connection this cross-connect uses.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        is_active(bool, Optional):
            Set to true to activate the cross-connect. You activate it after the physical cabling
            is complete, and you've confirmed the cross-connect's light levels are good and your side
            of the interface is up. Activation indicates to Oracle that the physical connection is ready.

            Example: `true`
            Defaults to None.

        macsec_properties(dict[str, Any], Optional):
            macsecProperties. Defaults to None.

            * encryption_cipher (str, Optional):
                Type of encryption cipher suite to use for the MACsec connection. Defaults to None.

            * is_unprotected_traffic_allowed (bool, Optional):
                Indicates whether unencrypted traffic is allowed if MACsec Key Agreement protocol (MKA) fails. Defaults to None.

            * primary_key (dict[str, Any], Optional):
                primaryKey. Defaults to None.

                * connectivity_association_key_secret_id (str):
                    Secret [OCID](/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity Association Key (CAK) of this MACsec key.


                * connectivity_association_key_secret_version (int):
                    The secret version of the connectivityAssociationKey secret in Vault.

                * connectivity_association_name_secret_id (str):
                    Secret [OCID](/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity Association Key Name (CKN) of this MACsec key.


                * connectivity_association_name_secret_version (int):
                    The secret version of the connectivity association name secret in Vault.

            * state (str):
                Indicates whether or not MACsec is enabled.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "customer_reference_name": "customerReferenceName",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "is_active": "isActive",
        "macsec_properties": "macsecProperties",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/crossConnects/{crossConnectId}".format(
            **{"crossConnectId": cross_connect_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "crossConnectGroupId": "cross_connect_group_id",
            "customerReferenceName": "customer_reference_name",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "locationName": "location_name",
            "macsecProperties": "macsec_properties",
            "ociLogicalDeviceName": "oci_logical_device_name",
            "ociPhysicalDeviceName": "oci_physical_device_name",
            "portName": "port_name",
            "portSpeedShapeName": "port_speed_shape_name",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_cross_connect(
    hub, ctx, cross_connect_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteCrossConnect
        Deletes the specified cross-connect. It must not be mapped to a
    [VirtualCircuit](#/en/iaas/latest/VirtualCircuit/).

    Args:
        cross_connect_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/crossConnects/{crossConnectId}".format(
            **{"crossConnectId": cross_connect_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_cross_connect_compartment(
    hub,
    ctx,
    cross_connect_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeCrossConnectCompartment
        Moves a cross-connect into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        cross_connect_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            cross-connect to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/crossConnects/{crossConnectId}/actions/changeCompartment".format(
            **{"crossConnectId": cross_connect_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_cross_connect_letter_of_authority(
    hub, ctx, cross_connect_id: str
) -> Dict[str, Any]:
    r"""

    GetCrossConnectLetterOfAuthority
        Gets the Letter of Authority for the specified cross-connect.

    Args:
        cross_connect_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/crossConnects/{crossConnectId}/letterOfAuthority".format(
            **{"crossConnectId": cross_connect_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "authorizedEntityName": "authorized_entity_name",
            "circuitType": "circuit_type",
            "crossConnectId": "cross_connect_id",
            "facilityLocation": "facility_location",
            "portName": "port_name",
            "timeExpires": "time_expires",
            "timeIssued": "time_issued",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_cross_connect_status(hub, ctx, cross_connect_id: str) -> Dict[str, Any]:
    r"""

    GetCrossConnectStatus
        Gets the status of the specified cross-connect.

    Args:
        cross_connect_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/crossConnects/{crossConnectId}/status".format(
            **{"crossConnectId": cross_connect_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "crossConnectId": "cross_connect_id",
            "encryptionStatus": "encryption_status",
            "interfaceState": "interface_state",
            "lightLevelIndBm": "light_level_ind_bm",
            "lightLevelIndicator": "light_level_indicator",
            "lightLevelsInDBm": "light_levels_in_d_bm",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_dhcp_options(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListDhcpOptions
        Lists the sets of DHCP options in the specified VCN and specified compartment.
    If the VCN ID is not provided, then the list includes the sets of DHCP options from all VCNs in the specified compartment.
    The response includes the default set of options that automatically comes with each VCN,
    plus any other sets you've created.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to only return resources that match the given lifecycle
            state. The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/dhcps".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_dhcp_options(
    hub,
    ctx,
    compartment_id: str,
    options: List[make_dataclass("options", [("type", str)])],
    vcn_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    CreateDhcpOptions
        Creates a new set of DHCP options for the specified VCN. For more information, see
    [DhcpOptions](#/en/iaas/latest/DhcpOptions/).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want the set of
    DHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN,
    subnets, or other Networking Service components. If you're not sure which compartment to use, put the set
    of DHCP options in the same compartment as the VCN. For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
    [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the set of DHCP options, otherwise a default is provided.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the set of DHCP options.

        options(List[dict[str, Any]]):
            A set of DHCP options.

            * type (str):
                The specific DHCP option. Either `DomainNameServer`
                (for [DhcpDnsOption](#/en/iaas/latest/DhcpDnsOption/)) or
                `SearchDomain` (for [DhcpSearchDomainOption](#/en/iaas/latest/DhcpSearchDomainOption/)).


        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN the set of DHCP options belongs to.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "options": "options",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/dhcps".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "options": "options",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_dhcp_options(hub, ctx, dhcp_id: str) -> Dict[str, Any]:
    r"""

    GetDhcpOptions
        Gets the specified set of DHCP options.

    Args:
        dhcp_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the set of DHCP options.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/dhcps/{dhcpId}".format(**{"dhcpId": dhcp_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "options": "options",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_dhcp_options(
    hub,
    ctx,
    dhcp_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    options: List[make_dataclass("options", [("type", str)])] = None,
) -> Dict[str, Any]:
    r"""

    UpdateDhcpOptions
        Updates the specified set of DHCP options. You can update the display name or the options
    themselves. Avoid entering confidential information.

    Note that the `options` object you provide replaces the entire existing set of options.

    Args:
        dhcp_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the set of DHCP options.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        options(List[dict[str, Any]], Optional):
            options. Defaults to None.

            * type (str):
                The specific DHCP option. Either `DomainNameServer`
                (for [DhcpDnsOption](#/en/iaas/latest/DhcpDnsOption/)) or
                `SearchDomain` (for [DhcpSearchDomainOption](#/en/iaas/latest/DhcpSearchDomainOption/)).

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "options": "options",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/dhcps/{dhcpId}".format(**{"dhcpId": dhcp_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "options": "options",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_dhcp_options(
    hub, ctx, dhcp_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteDhcpOptions
        Deletes the specified set of DHCP options, but only if it's not associated with a subnet. You can't delete a
    VCN's default set of DHCP options.

    This is an asynchronous operation. The state of the set of options will switch to TERMINATING temporarily
    until the set is completely removed.

    Args:
        dhcp_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the set of DHCP options.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/dhcps/{dhcpId}".format(**{"dhcpId": dhcp_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_dhcp_options_compartment(
    hub,
    ctx,
    dhcp_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeDhcpOptionsCompartment
        Moves a set of DHCP options into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        dhcp_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the set of DHCP options.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            set of DHCP options to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/dhcps/{dhcpId}/actions/changeCompartment".format(**{"dhcpId": dhcp_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_drg_attachments(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str = None,
    drg_id: str = None,
    limit: int = None,
    page: str = None,
    network_id: str = None,
    attachment_type: str = None,
    drg_route_table_id: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListDrgAttachments
        Lists the `DrgAttachment` resource for the specified compartment. You can filter the
    results by DRG, attached network, attachment type, DRG route table or
    VCN route table.

    The LIST API lists DRG attachments by attachment type. It will default to list VCN attachments,
    but you may request to list ALL attachments of ALL types.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        drg_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        network_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the resource (virtual circuit, VCN, IPSec tunnel, or remote peering connection) attached to the DRG. Defaults to None.

        attachment_type(str, Optional):
            The type for the network resource attached to the DRG. Defaults to None.

        drg_route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table assigned to the DRG attachment. Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the specified lifecycle
            state. The value is case insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgAttachments".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "drgId": drg_id,
            "limit": limit,
            "page": page,
            "networkId": network_id,
            "attachmentType": attachment_type,
            "drgRouteTableId": drg_route_table_id,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_drg_attachment(
    hub,
    ctx,
    drg_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    drg_route_table_id: str = None,
    freeform_tags: Dict = None,
    network_details: make_dataclass(
        "network_details", [("type", str), ("id", str, field(default=None))]
    ) = None,
    route_table_id: str = None,
    vcn_id: str = None,
) -> Dict[str, Any]:
    r"""

    CreateDrgAttachment
        Attaches the specified DRG to the specified network resource. A VCN can be attached to only one DRG
    at a time, but a DRG can be attached to more than one VCN. The response includes a `DrgAttachment`
    object with its own [OCID](/iaas/Content/General/Concepts/identifiers.htm). For more information about DRGs, see
    [Dynamic Routing Gateways (DRGs)](/iaas/Content/Network/Tasks/managingDRGs.htm).

    You may optionally specify a *display name* for the attachment, otherwise a default is provided.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    For the purposes of access control, the DRG attachment is automatically placed into the currently selected compartment.
    For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        drg_route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table that is assigned to this attachment.

            The DRG route table manages traffic inside the DRG.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        network_details(dict[str, Any], Optional):
            networkDetails. Defaults to None.

            * id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network attached to the DRG.
                Defaults to None.

            * type (str):
                type.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the DRG attachment.

            If you don't specify a route table here, the DRG attachment is created without an associated route
            table. The Networking service does NOT automatically associate the attached VCN's default route table
            with the DRG attachment.
            For information about why you would associate a route table with a DRG attachment, see:

              * [Transit Routing: Access to Multiple VCNs in Same Region](/iaas/Content/Network/Tasks/transitrouting.htm)
              * [Transit Routing: Private Access to Oracle Services](/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
            This field is deprecated. Instead, use the networkDetails field to specify the VCN route table for this attachment.
            Defaults to None.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
            This field is deprecated. Instead, use the `networkDetails` field to specify the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the attached resource.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "drg_id": "drgId",
        "drg_route_table_id": "drgRouteTableId",
        "freeform_tags": "freeformTags",
        "network_details": "networkDetails",
        "route_table_id": "routeTableId",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgAttachments".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "drgRouteTableId": "drg_route_table_id",
            "exportDrgRouteDistributionId": "export_drg_route_distribution_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancy": "is_cross_tenancy",
            "lifecycleState": "lifecycle_state",
            "networkDetails": "network_details",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_drg_attachment(hub, ctx, drg_attachment_id: str) -> Dict[str, Any]:
    r"""

    GetDrgAttachment
        Gets the `DrgAttachment` resource.

    Args:
        drg_attachment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgAttachments/{drgAttachmentId}".format(
            **{"drgAttachmentId": drg_attachment_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "drgRouteTableId": "drg_route_table_id",
            "exportDrgRouteDistributionId": "export_drg_route_distribution_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancy": "is_cross_tenancy",
            "lifecycleState": "lifecycle_state",
            "networkDetails": "network_details",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_drg_attachment(
    hub,
    ctx,
    drg_attachment_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    drg_route_table_id: str = None,
    export_drg_route_distribution_id: str = None,
    freeform_tags: Dict = None,
    network_details: make_dataclass("network_details", [("type", str)]) = None,
    route_table_id: str = None,
) -> Dict[str, Any]:
    r"""

    UpdateDrgAttachment
        Updates the display name and routing information for the specified `DrgAttachment`.
    Avoid entering confidential information.

    Args:
        drg_attachment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        drg_route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table that is assigned to this attachment.

            The DRG route table manages traffic inside the DRG.

            You can't remove a DRG route table from a DRG attachment, but you can reassign which
            DRG route table it uses.
            Defaults to None.

        export_drg_route_distribution_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the export route distribution used to specify how routes in the assigned DRG route table
            are advertised out through the attachment.
            If this value is null, no routes are advertised through this attachment.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        network_details(dict[str, Any], Optional):
            networkDetails. Defaults to None.

            * type (str):
                type.

        route_table_id(str, Optional):
            This is the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table that is used to route the traffic as it enters a VCN through this attachment.

            For information about why you would associate a route table with a DRG attachment, see:

              * [Transit Routing: Access to Multiple VCNs in Same Region](/iaas/Content/Network/Tasks/transitrouting.htm)
              * [Transit Routing: Private Access to Oracle Services](/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "drg_route_table_id": "drgRouteTableId",
        "export_drg_route_distribution_id": "exportDrgRouteDistributionId",
        "freeform_tags": "freeformTags",
        "network_details": "networkDetails",
        "route_table_id": "routeTableId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/drgAttachments/{drgAttachmentId}".format(
            **{"drgAttachmentId": drg_attachment_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "drgRouteTableId": "drg_route_table_id",
            "exportDrgRouteDistributionId": "export_drg_route_distribution_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancy": "is_cross_tenancy",
            "lifecycleState": "lifecycle_state",
            "networkDetails": "network_details",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_drg_attachment(
    hub, ctx, drg_attachment_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteDrgAttachment
        Detaches a DRG from a network resource by deleting the corresponding `DrgAttachment` resource. This is an asynchronous
    operation. The attachment's `lifecycleState` will temporarily change to DETACHING until the attachment
    is completely removed.

    Args:
        drg_attachment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/drgAttachments/{drgAttachmentId}".format(
            **{"drgAttachmentId": drg_attachment_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def remove_export_drg_route_distribution(
    hub, ctx, drg_attachment_id: str, opc_request_id: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

    RemoveExportDrgRouteDistribution
        Removes the export route distribution from the DRG attachment so no routes are advertised to it.

    Args:
        drg_attachment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgAttachments/{drgAttachmentId}/actions/removeExportDrgRouteDistribution".format(
            **{"drgAttachmentId": drg_attachment_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "drgRouteTableId": "drg_route_table_id",
            "exportDrgRouteDistributionId": "export_drg_route_distribution_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancy": "is_cross_tenancy",
            "lifecycleState": "lifecycle_state",
            "networkDetails": "network_details",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_drg_route_distributions(
    hub,
    ctx,
    drg_id: str,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListDrgRouteDistributionStatements
        Lists the route distributions in the specified DRG.

    To retrieve the statements in a distribution, use the
    ListDrgRouteDistributionStatements operation.

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter that only returns resources that match the specified lifecycle
            state. The value is case insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgRouteDistributions".format(**{}),
        query_params={
            "drgId": drg_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_drg_route_distribution(
    hub,
    ctx,
    distribution_type: str,
    drg_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    CreateDrgRouteDistribution
        Creates a new route distribution for the specified DRG.
    Assign the route distribution as an import distribution to a DRG route table using the `UpdateDrgRouteTable` or `CreateDrgRouteTable` operations.
    Assign the route distribution as an export distribution to a DRG attachment
    using the `UpdateDrgAttachment` or `CreateDrgAttachment` operations.

    Args:
        distribution_type(str):
            Whether this distribution defines how routes get imported into route tables or exported through DRG Attachments


        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG the DRG route table belongs to.


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "distribution_type": "distributionType",
        "drg_id": "drgId",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgRouteDistributions".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "distributionType": "distribution_type",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_drg_route_distribution(
    hub, ctx, drg_route_distribution_id: str
) -> Dict[str, Any]:
    r"""

    GetDrgRouteDistribution
        Gets the specified route distribution's information.

    Args:
        drg_route_distribution_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route distribution.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgRouteDistributions/{drgRouteDistributionId}".format(
            **{"drgRouteDistributionId": drg_route_distribution_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "distributionType": "distribution_type",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_drg_route_distribution(
    hub,
    ctx,
    drg_route_distribution_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    UpdateDrgRouteDistribution
        Updates the specified route distribution

    Args:
        drg_route_distribution_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route distribution.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/drgRouteDistributions/{drgRouteDistributionId}".format(
            **{"drgRouteDistributionId": drg_route_distribution_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "distributionType": "distribution_type",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_drg_route_distribution(
    hub, ctx, drg_route_distribution_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteDrgRouteDistribution
        Deletes the specified route distribution. You can't delete a route distribution currently in use by a DRG attachment or DRG route table.

    Remove the DRG route distribution from a DRG attachment or DRG route table by using the "RemoveExportDrgRouteDistribution" or "RemoveImportDrgRouteDistribution' operations.

    Args:
        drg_route_distribution_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route distribution.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/drgRouteDistributions/{drgRouteDistributionId}".format(
            **{"drgRouteDistributionId": drg_route_distribution_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def add_drg_route_distribution_statements(
    hub,
    ctx,
    drg_route_distribution_id: str,
    statements: List[
        make_dataclass(
            "statements",
            [
                ("action", str),
                (
                    "match_criteria",
                    List[make_dataclass("match_criteria", [("match_type", str)])],
                ),
                ("priority", int),
            ],
        )
    ],
) -> Dict[str, Any]:
    r"""

    AddDrgRouteDistributionStatements
        Adds one or more route distribution statements to the specified route distribution.

    Args:
        drg_route_distribution_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route distribution.

        statements(List[dict[str, Any]]):
            The collection of route distribution statements to insert into the route distribution.


            * action (str):
                Accept: import/export the route "as is"


            * match_criteria (List[dict[str, Any]]):
                The action is applied only if all of the match criteria is met.


                * match_type (str):
                    The type of the match criteria for a route distribution statement.


            * priority (int):
                This field is used to specify the priority of each statement in a route distribution.
                The priority will be represented as a number between 0 and 65535 where a lower number
                indicates a higher priority. When a route is processed, statements are applied in the order
                defined by their priority. The first matching rule dictates the action that will be taken
                on the route.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"statements": "statements"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgRouteDistributions/{drgRouteDistributionId}/actions/addDrgRouteDistributionStatements".format(
            **{"drgRouteDistributionId": drg_route_distribution_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def remove_drg_route_distribution_statements(
    hub, ctx, drg_route_distribution_id: str, statement_ids: List[str] = None
) -> Dict[str, Any]:
    r"""

    RemoveDrgRouteDistributionStatements
        Removes one or more route distribution statements from the specified route distribution's map.

    Args:
        drg_route_distribution_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route distribution.

        statement_ids(List[str], Optional):
            The Oracle-assigned ID of each route distribution to remove.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"statement_ids": "statementIds"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgRouteDistributions/{drgRouteDistributionId}/actions/removeDrgRouteDistributionStatements".format(
            **{"drgRouteDistributionId": drg_route_distribution_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def update_drg_route_distribution_statements(
    hub,
    ctx,
    drg_route_distribution_id: str,
    statements: List[
        make_dataclass(
            "statements",
            [
                ("id", str),
                (
                    "match_criteria",
                    List[make_dataclass("match_criteria", [("match_type", str)])],
                    field(default=None),
                ),
                ("priority", int, field(default=None)),
            ],
        )
    ],
) -> Dict[str, Any]:
    r"""

    UpdateDrgRouteDistributionStatements
        Updates one or more route distribution statements in the specified route distribution.

    Args:
        drg_route_distribution_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route distribution.

        statements(List[dict[str, Any]]):
            The route distribution statements to update, and the details to be updated.


            * id (str):
                The Oracle-assigned ID of each route distribution statement to be updated.


            * match_criteria (List[dict[str, Any]], Optional):
                The action is applied only if all of the match criteria is met.
                Defaults to None.

                * match_type (str):
                    The type of the match criteria for a route distribution statement.


            * priority (int, Optional):
                The priority of the statement you'd like to update.
                Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"statements": "statements"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgRouteDistributions/{drgRouteDistributionId}/actions/updateDrgRouteDistributionStatements".format(
            **{"drgRouteDistributionId": drg_route_distribution_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_drg_route_distribution_statements(
    hub,
    ctx,
    drg_route_distribution_id: str,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

    ListDrgRouteDistributionStatements
        Lists the statements for the specified route distribution.

    Args:
        drg_route_distribution_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route distribution.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgRouteDistributions/{drgRouteDistributionId}/drgRouteDistributionStatements".format(
            **{"drgRouteDistributionId": drg_route_distribution_id}
        ),
        query_params={
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_drg_route_tables(
    hub,
    ctx,
    drg_id: str,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    import_drg_route_distribution_id: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListDrgRouteTables
        Lists the DRG route tables for the specified DRG.

    Use the `ListDrgRouteRules` operation to retrieve the route rules in a table.

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        import_drg_route_distribution_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the import route distribution.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter that only returns matches for the specified lifecycle
            state. The value is case insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgRouteTables".format(**{}),
        query_params={
            "drgId": drg_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "importDrgRouteDistributionId": import_drg_route_distribution_id,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_drg_route_table(
    hub,
    ctx,
    drg_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    import_drg_route_distribution_id: str = None,
    is_ecmp_enabled: bool = None,
) -> Dict[str, Any]:
    r"""

    CreateDrgRouteTable
        Creates a new DRG route table for the specified DRG. Assign the DRG route table to a DRG attachment
    using the `UpdateDrgAttachment` or `CreateDrgAttachment` operations.

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG the DRG route table belongs to.


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        import_drg_route_distribution_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the import route distribution used to specify how incoming route advertisements through
            referenced attachments are inserted into the DRG route table.
            Defaults to None.

        is_ecmp_enabled(bool, Optional):
            If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to
            your on-premises networks, enable ECMP on the DRG route table.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "drg_id": "drgId",
        "freeform_tags": "freeformTags",
        "import_drg_route_distribution_id": "importDrgRouteDistributionId",
        "is_ecmp_enabled": "isEcmpEnabled",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgRouteTables".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "importDrgRouteDistributionId": "import_drg_route_distribution_id",
            "isEcmpEnabled": "is_ecmp_enabled",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_drg_route_table(hub, ctx, drg_route_table_id: str) -> Dict[str, Any]:
    r"""

    GetDrgRouteTable
        Gets the specified DRG route table's information.

    Args:
        drg_route_table_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgRouteTables/{drgRouteTableId}".format(
            **{"drgRouteTableId": drg_route_table_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "importDrgRouteDistributionId": "import_drg_route_distribution_id",
            "isEcmpEnabled": "is_ecmp_enabled",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_drg_route_table(
    hub,
    ctx,
    drg_route_table_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    import_drg_route_distribution_id: str = None,
    is_ecmp_enabled: bool = None,
) -> Dict[str, Any]:
    r"""

    UpdateDrgRouteTable
        Updates the specified DRG route table.

    Args:
        drg_route_table_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        import_drg_route_distribution_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the import route distribution used to specify how incoming route advertisements through
            referenced attachements are inserted into the DRG route table.
            Defaults to None.

        is_ecmp_enabled(bool, Optional):
            If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to
            your on-prem networks, set this value to true on the route table.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "import_drg_route_distribution_id": "importDrgRouteDistributionId",
        "is_ecmp_enabled": "isEcmpEnabled",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/drgRouteTables/{drgRouteTableId}".format(
            **{"drgRouteTableId": drg_route_table_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "importDrgRouteDistributionId": "import_drg_route_distribution_id",
            "isEcmpEnabled": "is_ecmp_enabled",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_drg_route_table(
    hub, ctx, drg_route_table_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteDrgRouteTable
        Deletes the specified DRG route table. There must not be any DRG attachments assigned.

    Args:
        drg_route_table_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/drgRouteTables/{drgRouteTableId}".format(
            **{"drgRouteTableId": drg_route_table_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def add_drg_route_rules(
    hub,
    ctx,
    drg_route_table_id: str,
    opc_retry_token: str = None,
    route_rules: List[
        make_dataclass(
            "route_rules",
            [
                ("destination", str),
                ("destination_type", str),
                ("next_hop_drg_attachment_id", str),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    AddDrgRouteRules
        Adds one or more static route rules to the specified DRG route table.

    Args:
        drg_route_table_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        route_rules(List[dict[str, Any]], Optional):
            The collection of static rules used to insert routes into the DRG route table.
            Defaults to None.

            * destination (str):
                This is the range of IP addresses used for matching when routing
                traffic. Only CIDR_BLOCK values are allowed.

                Potential values:
                  * IP address range in CIDR notation. This can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24`
                  or `2001:0db8:0123:45::/56`.


            * destination_type (str):
                Type of destination for the rule.
                Allowed values:
                  * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.


            * next_hop_drg_attachment_id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible
                for reaching the network destination.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"route_rules": "routeRules"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgRouteTables/{drgRouteTableId}/actions/addDrgRouteRules".format(
            **{"drgRouteTableId": drg_route_table_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def remove_drg_route_rules(
    hub, ctx, drg_route_table_id: str, route_rule_ids: List[str] = None
) -> Dict[str, Any]:
    r"""

    RemoveDrgRouteRules
        Removes one or more route rules from the specified DRG route table.

    Args:
        drg_route_table_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        route_rule_ids(List[str], Optional):
            The Oracle-assigned ID of each DRG route rule to be deleted.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"route_rule_ids": "routeRuleIds"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgRouteTables/{drgRouteTableId}/actions/removeDrgRouteRules".format(
            **{"drgRouteTableId": drg_route_table_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def remove_import_drg_route_distribution(
    hub, ctx, drg_route_table_id: str, opc_request_id: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

    RemoveImportDrgRouteDistribution
        Removes the import route distribution from the DRG route table so no routes are imported
    into it.

    Args:
        drg_route_table_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgRouteTables/{drgRouteTableId}/actions/removeImportDrgRouteDistribution".format(
            **{"drgRouteTableId": drg_route_table_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "importDrgRouteDistributionId": "import_drg_route_distribution_id",
            "isEcmpEnabled": "is_ecmp_enabled",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_drg_route_rules(
    hub,
    ctx,
    drg_route_table_id: str,
    route_rules: List[
        make_dataclass(
            "route_rules",
            [
                ("id", str),
                ("destination", str, field(default=None)),
                ("destination_type", str, field(default=None)),
                ("next_hop_drg_attachment_id", str, field(default=None)),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    UpdateDrgRouteRules
        Updates one or more route rules in the specified DRG route table.

    Args:
        drg_route_table_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        route_rules(List[dict[str, Any]], Optional):
            The DRG rute rules to update. Defaults to None.

            * destination (str, Optional):
                The range of IP addresses used for matching when routing traffic.

                Potential values:
                  * IP address range in CIDR notation. Can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24`
                  or `2001:0db8:0123:45::/56`.
                Defaults to None.

            * destination_type (str, Optional):
                Type of destination for the rule.
                Allowed values:
                  * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.
                Defaults to None.

            * id (str):
                The Oracle-assigned ID of each DRG route rule to update.


            * next_hop_drg_attachment_id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible
                for reaching the network destination.
                Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"route_rules": "routeRules"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgRouteTables/{drgRouteTableId}/actions/updateDrgRouteRules".format(
            **{"drgRouteTableId": drg_route_table_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_drg_route_rules(
    hub,
    ctx,
    drg_route_table_id: str,
    limit: int = None,
    page: str = None,
    route_type: str = None,
) -> Dict[str, Any]:
    r"""

    ListDrgRouteRules
        Lists the route rules in the specified DRG route table.

    Args:
        drg_route_table_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        route_type(str, Optional):
            Static routes are specified through the DRG route table API.
            Dynamic routes are learned by the DRG from the DRG attachments through various routing protocols.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgRouteTables/{drgRouteTableId}/drgRouteRules".format(
            **{"drgRouteTableId": drg_route_table_id}
        ),
        query_params={"limit": limit, "page": page, "routeType": route_type},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_drgs(
    hub, ctx, compartment_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListDrgs
        Lists the DRGs in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgs".format(**{}),
        query_params={"compartmentId": compartment_id, "limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_drg(
    hub,
    ctx,
    compartment_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    CreateDrg
        Creates a new dynamic routing gateway (DRG) in the specified compartment. For more information,
    see [Dynamic Routing Gateways (DRGs)](/iaas/Content/Network/Tasks/managingDRGs.htm).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want
    the DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN,
    the DRG attachment, or other Networking Service components. If you're not sure which compartment
    to use, put the DRG in the same compartment as the VCN. For more information about compartments
    and access control, see [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).
    For information about OCIDs, see [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the DRG, otherwise a default is provided.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the DRG.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgs".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "defaultDrgRouteTables": "default_drg_route_tables",
            "defaultExportDrgRouteDistributionId": "default_export_drg_route_distribution_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_drg(hub, ctx, drg_id: str) -> Dict[str, Any]:
    r"""

    GetDrg
        Gets the specified DRG's information.

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgs/{drgId}".format(**{"drgId": drg_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "defaultDrgRouteTables": "default_drg_route_tables",
            "defaultExportDrgRouteDistributionId": "default_export_drg_route_distribution_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_drg(
    hub,
    ctx,
    drg_id: str,
    if_match: str = None,
    default_drg_route_tables: make_dataclass(
        "default_drg_route_tables",
        [
            ("ipsec_tunnel", str, field(default=None)),
            ("remote_peering_connection", str, field(default=None)),
            ("vcn", str, field(default=None)),
            ("virtual_circuit", str, field(default=None)),
        ],
    ) = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    UpdateDrg
        Updates the specified DRG's display name or tags. Avoid entering confidential information.

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        default_drg_route_tables(dict[str, Any], Optional):
            defaultDrgRouteTables. Defaults to None.

            * ipsec_tunnel (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the default DRG route table assigned to DRG attachments
                of type IPSEC_TUNNEL on creation.
                Defaults to None.

            * remote_peering_connection (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the default DRG route table to be assigned to DRG attachments
                of type REMOTE_PEERING_CONNECTION on creation.
                Defaults to None.

            * vcn (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the default DRG route table to be assigned to DRG attachments
                of type VCN on creation.
                Defaults to None.

            * virtual_circuit (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the default DRG route table to be assigned to DRG attachments
                of type VIRTUAL_CIRCUIT on creation.
                Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "default_drg_route_tables": "defaultDrgRouteTables",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/drgs/{drgId}".format(**{"drgId": drg_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "defaultDrgRouteTables": "default_drg_route_tables",
            "defaultExportDrgRouteDistributionId": "default_export_drg_route_distribution_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_drg(hub, ctx, drg_id: str, if_match: str = None) -> Dict[str, Any]:
    r"""

    DeleteDrg
        Deletes the specified DRG. The DRG must not be attached to a VCN or be connected to your on-premise
    network. Also, there must not be a route table that lists the DRG as a target. This is an asynchronous
    operation. The DRG's `lifecycleState` will change to TERMINATING temporarily until the DRG is completely
    removed.

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/drgs/{drgId}".format(**{"drgId": drg_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_all_drg_attachments(
    hub,
    ctx,
    drg_id: str,
    opc_request_id: str = None,
    limit: int = None,
    page: str = None,
    attachment_type: str = None,
    is_cross_tenancy: bool = None,
) -> Dict[str, Any]:
    r"""

    GetAllDrgAttachments
        Returns a complete list of DRG attachments that belong to a particular DRG.

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        attachment_type(str, Optional):
            The type for the network resource attached to the DRG. Defaults to None.

        is_cross_tenancy(bool, Optional):
            Whether the DRG attachment lives in a different tenancy than the DRG. Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgs/{drgId}/actions/getAllDrgAttachments".format(**{"drgId": drg_id}),
        query_params={
            "limit": limit,
            "page": page,
            "attachmentType": attachment_type,
            "isCrossTenancy": is_cross_tenancy,
        },
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def upgrade_drg(
    hub, ctx, drg_id: str, opc_request_id: str = None, opc_retry_token: str = None
) -> Dict[str, Any]:
    r"""

    UpgradeDrg
        Upgrades the DRG. After upgrade, you can control routing inside your DRG
    via DRG attachments, route distributions, and DRG route tables.

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/drgs/{drgId}/actions/upgrade".format(**{"drgId": drg_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_upgrade_status(
    hub, ctx, drg_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    UpgradeStatus
        Returns the DRG upgrade status. The status can be not updated, in progress, or updated. Also indicates how much of the upgrade is completed.

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgs/{drgId}/actions/upgradeStatus".format(**{"drgId": drg_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "drgId": "drg_id",
            "status": "status",
            "upgradedConnections": "upgraded_connections",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_drg_redundancy_status(
    hub, ctx, drg_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetDrgRedundancyStatus
        Gets the redundancy status for the specified DRG. For more information, see
    [Redundancy Remedies](/iaas/Content/Network/Troubleshoot/drgredundancy.htm).

    Args:
        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/drgs/{drgId}/redundancyStatus".format(**{"drgId": drg_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict({"id": "id", "status": "status"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_fast_connect_provider_services(
    hub, ctx, compartment_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListFastConnectProviderServices
        Lists the service offerings from supported providers. You need this
    information so you can specify your desired provider and service
    offering when you create a virtual circuit.

    For the compartment ID, provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of your tenancy (the root compartment).

    For more information, see [FastConnect Overview](/iaas/Content/Network/Concepts/fastconnect.htm).

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/fastConnectProviderServices".format(**{}),
        query_params={"compartmentId": compartment_id, "limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_fast_connect_provider_service(
    hub, ctx, provider_service_id: str
) -> Dict[str, Any]:
    r"""

    GetFastConnectProviderService
        Gets the specified provider service.
    For more information, see [FastConnect Overview](/iaas/Content/Network/Concepts/fastconnect.htm).

    Args:
        provider_service_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the provider service.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/fastConnectProviderServices/{providerServiceId}".format(
            **{"providerServiceId": provider_service_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "bandwithShapeManagement": "bandwith_shape_management",
            "customerAsnManagement": "customer_asn_management",
            "description": "description",
            "id": "id",
            "privatePeeringBgpManagement": "private_peering_bgp_management",
            "providerName": "provider_name",
            "providerServiceKeyManagement": "provider_service_key_management",
            "providerServiceName": "provider_service_name",
            "publicPeeringBgpManagement": "public_peering_bgp_management",
            "requiredTotalCrossConnects": "required_total_cross_connects",
            "supportedVirtualCircuitTypes": "supported_virtual_circuit_types",
            "type": "type",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_fast_connect_provider_service_key(
    hub, ctx, provider_service_id: str, provider_service_key_name: str
) -> Dict[str, Any]:
    r"""

    GetFastConnectProviderServiceKey
        Gets the specified provider service key's information. Use this operation to validate a
    provider service key. An invalid key returns a 404 error.

    Args:
        provider_service_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the provider service.

        provider_service_key_name(str):
            The provider service key that the provider gives you when you set up a virtual circuit connection
            from the provider to Oracle Cloud Infrastructure. You can set up that connection and get your
            provider service key at the provider's website or portal. For the portal location, see the `description`
            attribute of the [FastConnectProviderService](#/en/iaas/latest/FastConnectProviderService/).

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/fastConnectProviderServices/{providerServiceId}/providerServiceKeys/{providerServiceKeyName}".format(
            **{
                "providerServiceId": provider_service_id,
                "providerServiceKeyName": provider_service_key_name,
            }
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "bandwidthShapeName": "bandwidth_shape_name",
            "name": "name",
            "peeringLocation": "peering_location",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
    hub, ctx, provider_service_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListFastConnectProviderVirtualCircuitBandwidthShapes
        Gets the list of available virtual circuit bandwidth levels for a provider.
    You need this information so you can specify your desired bandwidth level (shape) when you create a virtual circuit.

    For more information about virtual circuits, see [FastConnect Overview](/iaas/Content/Network/Concepts/fastconnect.htm).

    Args:
        provider_service_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the provider service.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/fastConnectProviderServices/{providerServiceId}/virtualCircuitBandwidthShapes".format(
            **{"providerServiceId": provider_service_id}
        ),
        query_params={"limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_internet_gateways(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListInternetGateways
        Lists the internet gateways in the specified VCN and the specified compartment.
    If the VCN ID is not provided, then the list includes the internet gateways from all VCNs in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to only return resources that match the given lifecycle
            state. The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/internetGateways".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_internet_gateway(
    hub,
    ctx,
    compartment_id: str,
    is_enabled: bool,
    vcn_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    route_table_id: str = None,
) -> Dict[str, Any]:
    r"""

    CreateInternetGateway
        Creates a new internet gateway for the specified VCN. For more information, see
    [Access to the Internet](/iaas/Content/Network/Tasks/managingIGs.htm).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want the Internet
    Gateway to reside. Notice that the internet gateway doesn't have to be in the same compartment as the VCN or
    other Networking Service components. If you're not sure which compartment to use, put the Internet
    Gateway in the same compartment with the VCN. For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).

    You may optionally specify a *display name* for the internet gateway, otherwise a default is provided. It
    does not have to be unique, and you can change it. Avoid entering confidential information.

    For traffic to flow between a subnet and an internet gateway, you must create a route rule accordingly in
    the subnet's route table (for example, 0.0.0.0/0 > internet gateway). See
    [UpdateRouteTable](#/en/iaas/latest/RouteTable/UpdateRouteTable).

    You must specify whether the internet gateway is enabled when you create it. If it's disabled, that means no
    traffic will flow to/from the internet even if there's a route rule that enables that traffic. You can later
    use [UpdateInternetGateway](#/en/iaas/latest/InternetGateway/UpdateInternetGateway) to easily disable/enable
    the gateway without changing the route rule.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the internet gateway.

        is_enabled(bool):
            Whether the gateway is enabled upon creation.

        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN the Internet Gateway is attached to.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the Internet Gateway is using. Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "is_enabled": "isEnabled",
        "route_table_id": "routeTableId",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/internetGateways".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isEnabled": "is_enabled",
            "lifecycleState": "lifecycle_state",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_internet_gateway(hub, ctx, ig_id: str) -> Dict[str, Any]:
    r"""

    GetInternetGateway
        Gets the specified internet gateway's information.

    Args:
        ig_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the internet gateway.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/internetGateways/{igId}".format(**{"igId": ig_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isEnabled": "is_enabled",
            "lifecycleState": "lifecycle_state",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_internet_gateway(
    hub,
    ctx,
    ig_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    is_enabled: bool = None,
    route_table_id: str = None,
) -> Dict[str, Any]:
    r"""

    UpdateInternetGateway
        Updates the specified internet gateway. You can disable/enable it, or change its display name
    or tags. Avoid entering confidential information.

    If the gateway is disabled, that means no traffic will flow to/from the internet even if there's
    a route rule that enables that traffic.

    Args:
        ig_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the internet gateway.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        is_enabled(bool, Optional):
            Whether the gateway is enabled. Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the Internet Gateway is using. Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "is_enabled": "isEnabled",
        "route_table_id": "routeTableId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/internetGateways/{igId}".format(**{"igId": ig_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isEnabled": "is_enabled",
            "lifecycleState": "lifecycle_state",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_internet_gateway(
    hub, ctx, ig_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteInternetGateway
        Deletes the specified internet gateway. The internet gateway does not have to be disabled, but
    there must not be a route table that lists it as a target.

    This is an asynchronous operation. The gateway's `lifecycleState` will change to TERMINATING temporarily
    until the gateway is completely removed.

    Args:
        ig_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the internet gateway.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/internetGateways/{igId}".format(**{"igId": ig_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_internet_gateway_compartment(
    hub,
    ctx,
    ig_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeInternetGatewayCompartment
        Moves an internet gateway into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        ig_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the internet gateway.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            internet gateway to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/internetGateways/{igId}/actions/changeCompartment".format(
            **{"igId": ig_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_allowed_ike_ip_sec_parameters(
    hub, ctx, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetAllowedIkeIPSecParameters
        The parameters allowed for IKE IPSec tunnels.

    Args:
        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecAlgorithms".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "allowedPhaseOneParameters": "allowed_phase_one_parameters",
            "allowedPhaseTwoParameters": "allowed_phase_two_parameters",
            "defaultPhaseOneParameters": "default_phase_one_parameters",
            "defaultPhaseTwoParameters": "default_phase_two_parameters",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_ip_sec_connections(
    hub,
    ctx,
    compartment_id: str,
    drg_id: str = None,
    cpe_id: str = None,
    limit: int = None,
    page: str = None,
) -> Dict[str, Any]:
    r"""

    ListIPSecConnections
        Lists the IPSec connections for the specified compartment. You can filter the
    results by DRG or CPE.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        drg_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG. Defaults to None.

        cpe_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the CPE. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "drgId": drg_id,
            "cpeId": cpe_id,
            "limit": limit,
            "page": page,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_ip_sec_connection(
    hub,
    ctx,
    compartment_id: str,
    cpe_id: str,
    drg_id: str,
    static_routes: List[str],
    opc_retry_token: str = None,
    cpe_local_identifier: str = None,
    cpe_local_identifier_type: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    tunnel_configuration: List[
        make_dataclass(
            "tunnel_configuration",
            [
                ("associated_virtual_circuits", List[str], field(default=None)),
                (
                    "bgp_session_config",
                    make_dataclass(
                        "bgp_session_config",
                        [
                            ("customer_bgp_asn", str, field(default=None)),
                            ("customer_interface_ip", str, field(default=None)),
                            ("customer_interface_ipv6", str, field(default=None)),
                            ("oracle_interface_ip", str, field(default=None)),
                            ("oracle_interface_ipv6", str, field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
                ("display_name", str, field(default=None)),
                (
                    "dpd_config",
                    make_dataclass(
                        "dpd_config",
                        [
                            ("dpd_mode", str, field(default=None)),
                            ("dpd_timeout_in_sec", int, field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
                ("drg_route_table_id", str, field(default=None)),
                (
                    "encryption_domain_config",
                    make_dataclass(
                        "encryption_domain_config",
                        [
                            ("cpe_traffic_selector", List[str], field(default=None)),
                            ("oracle_traffic_selector", List[str], field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
                ("nat_translation_enabled", str, field(default=None)),
                ("oracle_initiation", str, field(default=None)),
                ("oracle_tunnel_ip", str, field(default=None)),
                (
                    "phase_one_config",
                    make_dataclass(
                        "phase_one_config",
                        [
                            ("authentication_algorithm", str, field(default=None)),
                            ("diffie_helman_group", str, field(default=None)),
                            ("encryption_algorithm", str, field(default=None)),
                            ("is_custom_phase_one_config", bool, field(default=None)),
                            ("lifetime_in_seconds", int, field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "phase_two_config",
                    make_dataclass(
                        "phase_two_config",
                        [
                            ("authentication_algorithm", str, field(default=None)),
                            ("encryption_algorithm", str, field(default=None)),
                            ("is_custom_phase_two_config", bool, field(default=None)),
                            ("is_pfs_enabled", bool, field(default=None)),
                            ("lifetime_in_seconds", int, field(default=None)),
                            ("pfs_dh_group", str, field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
                ("routing", str, field(default=None)),
                ("shared_secret", str, field(default=None)),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    CreateIPSecConnection
        Creates a new IPSec connection between the specified DRG and CPE. For more information, see
    [Site-to-Site VPN Overview](/iaas/Content/Network/Tasks/overviewIPsec.htm).

    If you configure at least one tunnel to use static routing, then in the request you must provide
    at least one valid static route (you're allowed a maximum of 10). For example: 10.0.0.0/16.
    If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for
    the static routes. For more information, see the important note in
    [IPSecConnection](#/en/iaas/latest/IPSecConnection/).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want the
    IPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment
    as the DRG, CPE, or other Networking Service components. If you're not sure which compartment to
    use, put the IPSec connection in the same compartment as the DRG. For more information about
    compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).

    You may optionally specify a *display name* for the IPSec connection, otherwise a default is provided.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    After creating the IPSec connection, you need to configure your on-premises router
    with tunnel-specific information. For tunnel status and the required configuration information, see:

      * [IPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/)
      * [IPSecConnectionTunnelSharedSecret](#/en/iaas/latest/IPSecConnectionTunnelSharedSecret/)

    For each tunnel, you need the IP address of Oracle's VPN headend and the shared secret
    (that is, the pre-shared key). For more information, see
    [CPE Configuration](/iaas/Content/Network/Tasks/configuringCPE.htm).

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the IPSec connection.

        cpe_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the [Cpe](#/en/iaas/latest/Cpe/) object.

        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

        static_routes(List[str]):
            Static routes to the CPE. A static route's CIDR must not be a
            multicast address or class E address.

            Used for routing a given IPSec tunnel's traffic only if the tunnel
            is using static routing. If you configure at least one tunnel to use static routing, then
            you must provide at least one valid static route. If you configure both
            tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.
            For more information, see the important note in [IPSecConnection](#/en/iaas/latest/IPSecConnection/).

            The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions.
            See [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

            Example: `10.0.1.0/24`

            Example: `2001:db8::/32`


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        cpe_local_identifier(str, Optional):
            Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the
            fully qualified domain name (FQDN)). The type of identifier you provide here must correspond
            to the value for `cpeLocalIdentifierType`.

            If you don't provide a value, the `ipAddress` attribute for the [Cpe](#/en/iaas/latest/Cpe/)
            object specified by `cpeId` is used as the `cpeLocalIdentifier`.

            For information about why you'd provide this value, see
            [If Your CPE Is Behind a NAT Device](/iaas/Content/Network/Tasks/overviewIPsec.htm#nat).

            Example IP address: `10.0.3.3`

            Example hostname: `cpe.example.com`
            Defaults to None.

        cpe_local_identifier_type(str, Optional):
            The type of identifier for your CPE device. The value you provide here must correspond to the value
            for `cpeLocalIdentifier`.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        tunnel_configuration(List[dict[str, Any]], Optional):
            Information for creating the individual tunnels in the IPSec connection. You can provide a
            maximum of 2 `tunnelConfiguration` objects in the array (one for each of the
            two tunnels).
            Defaults to None.

            * associated_virtual_circuits (List[str], Optional):
                The list of virtual circuit [OCID](/iaas/Content/General/Concepts/identifiers.htm)s over which your network can reach this tunnel.
                Defaults to None.

            * bgp_session_config (dict[str, Any], Optional):
                bgpSessionConfig. Defaults to None.

                * customer_bgp_asn (str, Optional):
                    If the tunnel's `routing` attribute is set to `BGP`
                    (see [IPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/)), this ASN
                    is required and used for the tunnel's BGP session. This is the ASN of the network on the
                    CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses "asplain" format.

                    If the tunnel's `routing` attribute is set to `STATIC`, the `customerBgpAsn` must be null.

                    Example: `12345` (2-byte) or `1587232876` (4-byte)
                    Defaults to None.

                * customer_interface_ip (str, Optional):
                    The IP address for the CPE end of the inside tunnel interface.

                    If the tunnel's `routing` attribute is set to `BGP`
                    (see [IPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                    is required and used for the tunnel's BGP session.

                    If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                    address to troubleshoot or monitor the tunnel.

                    The value must be a /30 or /31.

                    Example: `10.0.0.5/31`
                    Defaults to None.

                * customer_interface_ipv6 (str, Optional):
                    The IPv6 address for the CPE end of the inside tunnel interface. This IP address is optional.

                    If the tunnel's `routing` attribute is set to `BGP`
                    (see [IPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                    is used for the tunnel's BGP session.

                    If `routing` is instead set to `STATIC`, you can set this IP
                    address to troubleshoot or monitor the tunnel.

                    Only subnet masks from /64 up to /127 are allowed.

                    Example: `2001:db8::1/64`
                    Defaults to None.

                * oracle_interface_ip (str, Optional):
                    The IP address for the Oracle end of the inside tunnel interface.

                    If the tunnel's `routing` attribute is set to `BGP`
                    (see [IPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                    is required and used for the tunnel's BGP session.

                    If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                    address to troubleshoot or monitor the tunnel.

                    The value must be a /30 or /31.

                    Example: `10.0.0.4/31`
                    Defaults to None.

                * oracle_interface_ipv6 (str, Optional):
                    The IPv6 address for the Oracle end of the inside tunnel interface. This IP address is optional.

                    If the tunnel's `routing` attribute is set to `BGP`
                    (see [IPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                    is used for the tunnel's BGP session.

                    If `routing` is instead set to `STATIC`, you can set this IP
                    address to troubleshoot or monitor the tunnel.

                    Only subnet masks from /64 up to /127 are allowed.

                    Example: `2001:db8::1/64`
                    Defaults to None.

            * display_name (str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
                Avoid entering confidential information.
                Defaults to None.

            * dpd_config (dict[str, Any], Optional):
                dpdConfig. Defaults to None.

                * dpd_mode (str, Optional):
                    This option defines whether DPD can be initiated from the Oracle side of the connection.
                    Defaults to None.

                * dpd_timeout_in_sec (int, Optional):
                    DPD timeout in seconds. This sets the longest interval between CPE device health messages before the IPSec connection indicates it has lost contact with the CPE. The default is 20 seconds.
                    Defaults to None.

            * drg_route_table_id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table assigned to this attachment.

                The DRG route table manages traffic inside the DRG.
                Defaults to None.

            * encryption_domain_config (dict[str, Any], Optional):
                encryptionDomainConfig. Defaults to None.

                * cpe_traffic_selector (List[str], Optional):
                    Lists IPv4 or IPv6-enabled subnets in your on-premises network. Defaults to None.

                * oracle_traffic_selector (List[str], Optional):
                    Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy. Defaults to None.

            * nat_translation_enabled (str, Optional):
                By default (the `AUTO` setting), IKE sends packets with a source and destination port set to 500,
                and when it detects that the port used to forward packets has changed (most likely because a NAT device
                is between the CPE device and the Oracle VPN headend) it will try to negotiate the use of NAT-T.

                The `ENABLED` option sets the IKE protocol to use port 4500 instead of 500 and forces encapsulating traffic with the ESP protocol inside UDP packets.

                The `DISABLED` option directs IKE to completely refuse to negotiate NAT-T
                even if it senses there may be a NAT device in use.
                Defaults to None.

            * oracle_initiation (str, Optional):
                Indicates whether the Oracle end of the IPSec connection is able to initiate starting up the IPSec tunnel.
                Defaults to None.

            * oracle_tunnel_ip (str, Optional):
                The headend IP that you can choose on the Oracle side to terminate your private IPSec tunnel.
                Defaults to None.

            * phase_one_config (dict[str, Any], Optional):
                phaseOneConfig. Defaults to None.

                * authentication_algorithm (str, Optional):
                    The custom authentication algorithm proposed during phase one tunnel negotiation.
                    Defaults to None.

                * diffie_helman_group (str, Optional):
                    The custom Diffie-Hellman group proposed during phase one tunnel negotiation.
                    Defaults to None.

                * encryption_algorithm (str, Optional):
                    The custom encryption algorithm proposed during phase one tunnel negotiation.
                    Defaults to None.

                * is_custom_phase_one_config (bool, Optional):
                    Indicates whether custom configuration is enabled for phase one options. Defaults to None.

                * lifetime_in_seconds (int, Optional):
                    Internet key association (IKE) session key lifetime in seconds for IPSec phase one. The default is 28800 which is equivalent to 8 hours.
                    Defaults to None.

            * phase_two_config (dict[str, Any], Optional):
                phaseTwoConfig. Defaults to None.

                * authentication_algorithm (str, Optional):
                    The authentication algorithm proposed during phase two tunnel negotiation.
                    Defaults to None.

                * encryption_algorithm (str, Optional):
                    The encryption algorithm proposed during phase two tunnel negotiation.
                    Defaults to None.

                * is_custom_phase_two_config (bool, Optional):
                    Indicates whether custom configuration is enabled for phase two options. Defaults to None.

                * is_pfs_enabled (bool, Optional):
                    Indicates whether perfect forward secrecy (PFS) is enabled. Defaults to None.

                * lifetime_in_seconds (int, Optional):
                    Lifetime in seconds for the IPSec session key set in phase two. The default is 3600 which is equivalent to 1 hour.
                    Defaults to None.

                * pfs_dh_group (str, Optional):
                    The Diffie-Hellman group used for PFS, if PFS is enabled. Defaults to None.

            * routing (str, Optional):
                The type of routing to use for this tunnel (BGP dynamic routing, static routing, or policy-based routing).
                Defaults to None.

            * shared_secret (str, Optional):
                The shared secret (pre-shared key) to use for the IPSec tunnel. Only numbers, letters, and
                spaces are allowed. If you don't provide a value,
                Oracle generates a value for you. You can specify your own shared secret later if
                you like with [UpdateIPSecConnectionTunnelSharedSecret](#/en/iaas/latest/IPSecConnectionTunnelSharedSecret/UpdateIPSecConnectionTunnelSharedSecret).
                Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "cpe_id": "cpeId",
        "cpe_local_identifier": "cpeLocalIdentifier",
        "cpe_local_identifier_type": "cpeLocalIdentifierType",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "drg_id": "drgId",
        "freeform_tags": "freeformTags",
        "static_routes": "staticRoutes",
        "tunnel_configuration": "tunnelConfiguration",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/ipsecConnections".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "cpeId": "cpe_id",
            "cpeLocalIdentifier": "cpe_local_identifier",
            "cpeLocalIdentifierType": "cpe_local_identifier_type",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "staticRoutes": "static_routes",
            "timeCreated": "time_created",
            "transportType": "transport_type",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_ip_sec_connection(hub, ctx, ipsc_id: str) -> Dict[str, Any]:
    r"""

    GetIPSecConnection
        Gets the specified IPSec connection's basic information, including the static routes for the
    on-premises router. If you want the status of the connection (whether it's up or down), use
    [GetIPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/GetIPSecConnectionTunnel).

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}".format(**{"ipscId": ipsc_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "cpeId": "cpe_id",
            "cpeLocalIdentifier": "cpe_local_identifier",
            "cpeLocalIdentifierType": "cpe_local_identifier_type",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "staticRoutes": "static_routes",
            "timeCreated": "time_created",
            "transportType": "transport_type",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_ip_sec_connection(
    hub,
    ctx,
    ipsc_id: str,
    if_match: str = None,
    cpe_local_identifier: str = None,
    cpe_local_identifier_type: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    static_routes: List[str] = None,
) -> Dict[str, Any]:
    r"""

    UpdateIPSecConnection
        Updates the specified IPSec connection.

    To update an individual IPSec tunnel's attributes, use
    [UpdateIPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/UpdateIPSecConnectionTunnel).

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        cpe_local_identifier(str, Optional):
            Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the
            fully qualified domain name (FQDN)). The type of identifier you provide here must correspond
            to the value for `cpeLocalIdentifierType`.

            For information about why you'd provide this value, see
            [If Your CPE Is Behind a NAT Device](/iaas/Content/Network/Tasks/overviewIPsec.htm#nat).

            Example IP address: `10.0.3.3`

            Example hostname: `cpe.example.com`
            Defaults to None.

        cpe_local_identifier_type(str, Optional):
            The type of identifier for your CPE device. The value you provide here must correspond to the value
            for `cpeLocalIdentifier`.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        static_routes(List[str], Optional):
            Static routes to the CPE. If you provide this attribute, it replaces the entire current set of
            static routes. A static route's CIDR must not be a multicast address or class E address.
            The CIDR can be either IPv4 or IPv6.
            IPv6 addressing is supported for all commercial and government regions.
            See [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

            Example: `10.0.1.0/24`

            Example: `2001:db8::/32`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "cpe_local_identifier": "cpeLocalIdentifier",
        "cpe_local_identifier_type": "cpeLocalIdentifierType",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "static_routes": "staticRoutes",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/ipsecConnections/{ipscId}".format(**{"ipscId": ipsc_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "cpeId": "cpe_id",
            "cpeLocalIdentifier": "cpe_local_identifier",
            "cpeLocalIdentifierType": "cpe_local_identifier_type",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "staticRoutes": "static_routes",
            "timeCreated": "time_created",
            "transportType": "transport_type",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_ip_sec_connection(
    hub, ctx, ipsc_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteIPSecConnection
        Deletes the specified IPSec connection. If your goal is to disable the Site-to-Site VPN between your VCN and
    on-premises network, it's easiest to simply detach the DRG but keep all the Site-to-Site VPN components intact.
    If you were to delete all the components and then later need to create an Site-to-Site VPN again, you would
    need to configure your on-premises router again with the new information returned from
    [CreateIPSecConnection](#/en/iaas/latest/IPSecConnection/CreateIPSecConnection).

    This is an asynchronous operation. The connection's `lifecycleState` will change to TERMINATING temporarily
    until the connection is completely removed.

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/ipsecConnections/{ipscId}".format(**{"ipscId": ipsc_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_ip_sec_connection_compartment(
    hub,
    ctx,
    ipsc_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeIPSecConnectionCompartment
        Moves an IPSec connection into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            IPSec connection to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/ipsecConnections/{ipscId}/actions/changeCompartment".format(
            **{"ipscId": ipsc_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_ipsec_cpe_device_config_content(
    hub, ctx, ipsc_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetIpsecCpeDeviceConfigContent
        Renders a set of CPE configuration content for the specified IPSec connection (for all the
    tunnels in the connection). The content helps a network engineer configure the actual CPE
    device (for example, a hardware router) that the specified IPSec connection terminates on.

    The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the
    [Cpe](#/en/iaas/latest/Cpe/) used by the specified [IPSecConnection](#/en/iaas/latest/IPSecConnection/)
    must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content
    optionally includes answers that the customer provides (see
    [UpdateTunnelCpeDeviceConfig](#/en/iaas/latest/TunnelCpeDeviceConfig/UpdateTunnelCpeDeviceConfig)),
    merged with a template of other information specific to the CPE device type.

    The operation returns configuration information for all tunnels in the single specified
    [IPSecConnection](#/en/iaas/latest/IPSecConnection/) object. Here are other similar
    operations:

      * [GetTunnelCpeDeviceConfigContent](#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)
      returns CPE configuration content for a specific tunnel within an IPSec connection.
      * [GetCpeDeviceConfigContent](#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
      returns CPE configuration content for *all* IPSec connections that use a specific CPE.

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/cpeConfigContent".format(
            **{"ipscId": ipsc_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_ip_sec_connection_device_config(hub, ctx, ipsc_id: str) -> Dict[str, Any]:
    r"""

    GetIPSecConnectionDeviceConfig
        Deprecated. To get tunnel information, instead use:

    * [GetIPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/GetIPSecConnectionTunnel)
    * [GetIPSecConnectionTunnelSharedSecret](#/en/iaas/latest/IPSecConnectionTunnelSharedSecret/GetIPSecConnectionTunnelSharedSecret)

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/deviceConfig".format(**{"ipscId": ipsc_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "id": "id",
            "timeCreated": "time_created",
            "tunnels": "tunnels",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_ip_sec_connection_device_status(hub, ctx, ipsc_id: str) -> Dict[str, Any]:
    r"""

    GetIPSecConnectionDeviceStatus
        Deprecated. To get the tunnel status, instead use
    [GetIPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/GetIPSecConnectionTunnel).

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/deviceStatus".format(**{"ipscId": ipsc_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "id": "id",
            "timeCreated": "time_created",
            "tunnels": "tunnels",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_ip_sec_connection_tunnels(
    hub, ctx, ipsc_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListIPSecConnectionTunnels
        Lists the tunnel information for the specified IPSec connection.

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/tunnels".format(**{"ipscId": ipsc_id}),
        query_params={"limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_ip_sec_connection_tunnel(
    hub, ctx, ipsc_id: str, tunnel_id: str
) -> Dict[str, Any]:
    r"""

    GetIPSecConnectionTunnel
        Gets the specified tunnel's information. The resulting object does not include the tunnel's
    shared secret (pre-shared key). To retrieve that, use
    [GetIPSecConnectionTunnelSharedSecret](#/en/iaas/latest/IPSecConnectionTunnelSharedSecret/GetIPSecConnectionTunnelSharedSecret).

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "associatedVirtualCircuits": "associated_virtual_circuits",
            "bgpSessionInfo": "bgp_session_info",
            "compartmentId": "compartment_id",
            "cpeIp": "cpe_ip",
            "displayName": "display_name",
            "dpdMode": "dpd_mode",
            "dpdTimeoutInSec": "dpd_timeout_in_sec",
            "encryptionDomainConfig": "encryption_domain_config",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "natTranslationEnabled": "nat_translation_enabled",
            "oracleCanInitiate": "oracle_can_initiate",
            "phaseOneDetails": "phase_one_details",
            "phaseTwoDetails": "phase_two_details",
            "routing": "routing",
            "status": "status",
            "timeCreated": "time_created",
            "timeStatusUpdated": "time_status_updated",
            "vpnIp": "vpn_ip",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_ip_sec_connection_tunnel(
    hub,
    ctx,
    ipsc_id: str,
    tunnel_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    bgp_session_config: make_dataclass(
        "bgp_session_config",
        [
            ("customer_bgp_asn", str, field(default=None)),
            ("customer_interface_ip", str, field(default=None)),
            ("customer_interface_ipv6", str, field(default=None)),
            ("oracle_interface_ip", str, field(default=None)),
            ("oracle_interface_ipv6", str, field(default=None)),
        ],
    ) = None,
    display_name: str = None,
    dpd_config: make_dataclass(
        "dpd_config",
        [
            ("dpd_mode", str, field(default=None)),
            ("dpd_timeout_in_sec", int, field(default=None)),
        ],
    ) = None,
    encryption_domain_config: make_dataclass(
        "encryption_domain_config",
        [
            ("cpe_traffic_selector", List[str], field(default=None)),
            ("oracle_traffic_selector", List[str], field(default=None)),
        ],
    ) = None,
    nat_translation_enabled: str = None,
    oracle_initiation: str = None,
    phase_one_config: make_dataclass(
        "phase_one_config",
        [
            ("authentication_algorithm", str, field(default=None)),
            ("diffie_helman_group", str, field(default=None)),
            ("encryption_algorithm", str, field(default=None)),
            ("is_custom_phase_one_config", bool, field(default=None)),
            ("lifetime_in_seconds", int, field(default=None)),
        ],
    ) = None,
    phase_two_config: make_dataclass(
        "phase_two_config",
        [
            ("authentication_algorithm", str, field(default=None)),
            ("encryption_algorithm", str, field(default=None)),
            ("is_custom_phase_two_config", bool, field(default=None)),
            ("is_pfs_enabled", bool, field(default=None)),
            ("lifetime_in_seconds", int, field(default=None)),
            ("pfs_dh_group", str, field(default=None)),
        ],
    ) = None,
    routing: str = None,
) -> Dict[str, Any]:
    r"""

    UpdateIPSecConnectionTunnelDetails
        Updates the specified tunnel. This operation lets you change tunnel attributes such as the
    routing type (BGP dynamic routing or static routing). Here are some important notes:

      * If you change the tunnel's routing type or BGP session configuration, the tunnel will go
        down while it's reprovisioned.

      * If you want to switch the tunnel's `routing` from `STATIC` to `BGP`, make sure the tunnel's
        BGP session configuration attributes have been set ([bgpSessionConfig](#/en/iaas/latest/datatypes/BgpSessionInfo)).

      * If you want to switch the tunnel's `routing` from `BGP` to `STATIC`, make sure the
        [IPSecConnection](#/en/iaas/latest/IPSecConnection/) already has at least one valid CIDR
        static route.

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        bgp_session_config(dict[str, Any], Optional):
            bgpSessionConfig. Defaults to None.

            * customer_bgp_asn (str, Optional):
                The BGP ASN of the network on the CPE end of the BGP session. Can be a 2-byte or 4-byte ASN.
                Uses "asplain" format.

                If you are switching the tunnel from using BGP dynamic routing to static routing, the
                `customerBgpAsn` must be null.

                Example: `12345` (2-byte) or `1587232876` (4-byte)
                Defaults to None.

            * customer_interface_ip (str, Optional):
                The IP address for the CPE end of the inside tunnel interface.

                If the tunnel's `routing` attribute is set to `BGP`
                (see [UpdateIPSecConnectionTunnelDetails](#/en/iaas/latest/datatypes/UpdateIPSecConnectionTunnelDetails)), this IP address
                is used for the tunnel's BGP session.

                If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or
                monitor the tunnel.

                The value must be a /30 or /31.

                If you are switching the tunnel from using BGP dynamic routing to static routing and want
                to remove the value for `customerInterfaceIp`, you can set the value to an empty string.

                Example: `10.0.0.5/31`
                Defaults to None.

            * customer_interface_ipv6 (str, Optional):
                The IPv6 address for the CPE end of the inside tunnel interface. This IP address is optional.

                If the tunnel's `routing` attribute is set to `BGP`
                (see [IPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                is used for the tunnel's BGP session.

                If `routing` is instead set to `STATIC`, you can set this IP
                address to troubleshoot or monitor the tunnel.

                Only subnet masks from /64 up to /127 are allowed.

                Example: `2001:db8::1/64`
                Defaults to None.

            * oracle_interface_ip (str, Optional):
                The IP address for the Oracle end of the inside tunnel interface.

                If the tunnel's `routing` attribute is set to `BGP`
                (see [UpdateIPSecConnectionTunnelDetails](#/en/iaas/latest/datatypes/UpdateIPSecConnectionTunnelDetails)), this IP address
                is used for the tunnel's BGP session.

                If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or
                monitor the tunnel.

                The value must be a /30 or /31.

                If you are switching the tunnel from using BGP dynamic routing to static routing and want
                to remove the value for `oracleInterfaceIp`, you can set the value to an empty string.

                Example: `10.0.0.4/31`
                Defaults to None.

            * oracle_interface_ipv6 (str, Optional):
                The IPv6 address for the Oracle end of the inside tunnel interface. This IP address is optional.

                If the tunnel's `routing` attribute is set to `BGP`
                (see [IPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                is used for the tunnel's BGP session.

                If `routing` is instead set to `STATIC`, you can set this IP
                address to troubleshoot or monitor the tunnel.

                Only subnet masks from /64 up to /127 are allowed.

                Example: `2001:db8::1/64`
                Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        dpd_config(dict[str, Any], Optional):
            dpdConfig. Defaults to None.

            * dpd_mode (str, Optional):
                This option defines whether DPD can be initiated from the Oracle side of the connection.
                Defaults to None.

            * dpd_timeout_in_sec (int, Optional):
                DPD timeout in seconds. This sets the longest interval between CPE device health messages before the IPSec connection indicates it has lost contact with the CPE. The default is 20 seconds.
                Defaults to None.

        encryption_domain_config(dict[str, Any], Optional):
            encryptionDomainConfig. Defaults to None.

            * cpe_traffic_selector (List[str], Optional):
                Lists IPv4 or IPv6-enabled subnets in your on-premises network. Defaults to None.

            * oracle_traffic_selector (List[str], Optional):
                Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy. Defaults to None.

        nat_translation_enabled(str, Optional):
            By default (the `AUTO` setting), IKE sends packets with a source and destination port set to 500,
            and when it detects that the port used to forward packets has changed (most likely because a NAT device
            is between the CPE device and the Oracle VPN headend) it will try to negotiate the use of NAT-T.

            The `ENABLED` option sets the IKE protocol to use port 4500 instead of 500 and forces encapsulating traffic with the ESP protocol inside UDP packets.

            The `DISABLED` option directs IKE to completely refuse to negotiate NAT-T
            even if it senses there may be a NAT device in use.
            Defaults to None.

        oracle_initiation(str, Optional):
            Indicates whether the Oracle end of the IPSec connection is able to initiate starting up the IPSec tunnel.
            Defaults to None.

        phase_one_config(dict[str, Any], Optional):
            phaseOneConfig. Defaults to None.

            * authentication_algorithm (str, Optional):
                The custom authentication algorithm proposed during phase one tunnel negotiation.
                Defaults to None.

            * diffie_helman_group (str, Optional):
                The custom Diffie-Hellman group proposed during phase one tunnel negotiation.
                Defaults to None.

            * encryption_algorithm (str, Optional):
                The custom encryption algorithm proposed during phase one tunnel negotiation.
                Defaults to None.

            * is_custom_phase_one_config (bool, Optional):
                Indicates whether custom configuration is enabled for phase one options. Defaults to None.

            * lifetime_in_seconds (int, Optional):
                Internet key association (IKE) session key lifetime in seconds for IPSec phase one. The default is 28800 which is equivalent to 8 hours.
                Defaults to None.

        phase_two_config(dict[str, Any], Optional):
            phaseTwoConfig. Defaults to None.

            * authentication_algorithm (str, Optional):
                The authentication algorithm proposed during phase two tunnel negotiation.
                Defaults to None.

            * encryption_algorithm (str, Optional):
                The encryption algorithm proposed during phase two tunnel negotiation.
                Defaults to None.

            * is_custom_phase_two_config (bool, Optional):
                Indicates whether custom configuration is enabled for phase two options. Defaults to None.

            * is_pfs_enabled (bool, Optional):
                Indicates whether perfect forward secrecy (PFS) is enabled. Defaults to None.

            * lifetime_in_seconds (int, Optional):
                Lifetime in seconds for the IPSec session key set in phase two. The default is 3600 which is equivalent to 1 hour.
                Defaults to None.

            * pfs_dh_group (str, Optional):
                The Diffie-Hellman group used for PFS, if PFS is enabled. Defaults to None.

        routing(str, Optional):
            The type of routing to use for this tunnel (BGP dynamic routing, static routing, or policy-based routing).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "bgp_session_config": "bgpSessionConfig",
        "display_name": "displayName",
        "dpd_config": "dpdConfig",
        "encryption_domain_config": "encryptionDomainConfig",
        "nat_translation_enabled": "natTranslationEnabled",
        "oracle_initiation": "oracleInitiation",
        "phase_one_config": "phaseOneConfig",
        "phase_two_config": "phaseTwoConfig",
        "routing": "routing",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "associatedVirtualCircuits": "associated_virtual_circuits",
            "bgpSessionInfo": "bgp_session_info",
            "compartmentId": "compartment_id",
            "cpeIp": "cpe_ip",
            "displayName": "display_name",
            "dpdMode": "dpd_mode",
            "dpdTimeoutInSec": "dpd_timeout_in_sec",
            "encryptionDomainConfig": "encryption_domain_config",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "natTranslationEnabled": "nat_translation_enabled",
            "oracleCanInitiate": "oracle_can_initiate",
            "phaseOneDetails": "phase_one_details",
            "phaseTwoDetails": "phase_two_details",
            "routing": "routing",
            "status": "status",
            "timeCreated": "time_created",
            "timeStatusUpdated": "time_status_updated",
            "vpnIp": "vpn_ip",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_ip_sec_connection_tunnel_error(
    hub, ctx, ipsc_id: str, tunnel_id: str
) -> Dict[str, Any]:
    r"""

    GetIPSecConnectionTunnelError
        Gets the identified error for the specified IPSec tunnel ID.

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}/error".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "errorCode": "error_code",
            "errorDescription": "error_description",
            "id": "id",
            "ociResourcesLink": "oci_resources_link",
            "solution": "solution",
            "timestamp": "timestamp",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_ip_sec_connection_tunnel_routes(
    hub,
    ctx,
    ipsc_id: str,
    tunnel_id: str,
    limit: int = None,
    page: str = None,
    advertiser: str = None,
) -> Dict[str, Any]:
    r"""

    ListIPSecConnectionTunnelRoutes
        The routes advertised to the on-premises network and the routes received from the on-premises network.

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        advertiser(str, Optional):
            Specifies the advertiser of the routes. If set to `ORACLE`, this returns only the
            routes advertised by Oracle. When set to `CUSTOMER`, this returns only the
            routes advertised by the CPE.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}/routes".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={"limit": limit, "page": page, "advertiser": advertiser},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_ip_sec_connection_tunnel_shared_secret(
    hub, ctx, ipsc_id: str, tunnel_id: str
) -> Dict[str, Any]:
    r"""

    GetIPSecConnectionTunnelSharedSecret
        Gets the specified tunnel's shared secret (pre-shared key). To get other information
    about the tunnel, use [GetIPSecConnectionTunnel](#/en/iaas/latest/IPSecConnectionTunnel/GetIPSecConnectionTunnel).

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}/sharedSecret".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict({"sharedSecret": "shared_secret"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_ip_sec_connection_tunnel_shared_secret(
    hub,
    ctx,
    ipsc_id: str,
    tunnel_id: str,
    if_match: str = None,
    shared_secret: str = None,
) -> Dict[str, Any]:
    r"""

    UpdateIPSecConnectionTunnelSharedSecret
        Updates the shared secret (pre-shared key) for the specified tunnel.

    **Important:** If you change the shared secret, the tunnel will go down while it's reprovisioned.

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        shared_secret(str, Optional):
            The shared secret (pre-shared key) to use for the tunnel. Only numbers, letters, and spaces
            are allowed.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"shared_secret": "sharedSecret"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}/sharedSecret".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict({"sharedSecret": "shared_secret"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_tunnel_cpe_device_config(
    hub, ctx, ipsc_id: str, tunnel_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetTunnelCpeDeviceConfig
        Gets the set of CPE configuration answers for the tunnel, which the customer provided in
    [UpdateTunnelCpeDeviceConfig](#/en/iaas/latest/TunnelCpeDeviceConfig/UpdateTunnelCpeDeviceConfig).
    To get the full set of content for the tunnel (any answers merged with the template of other
    information specific to the CPE device type), use
    [GetTunnelCpeDeviceConfigContent](#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent).

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}/tunnelDeviceConfig".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {"tunnelCpeDeviceConfigParameter": "tunnel_cpe_device_config_parameter"}
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_tunnel_cpe_device_config(
    hub,
    ctx,
    ipsc_id: str,
    tunnel_id: str,
    if_match: str = None,
    opc_retry_token: str = None,
    opc_request_id: str = None,
    tunnel_cpe_device_config: List[
        make_dataclass(
            "tunnel_cpe_device_config",
            [("key", str, field(default=None)), ("value", str, field(default=None))],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    UpdateTunnelCpeDeviceConfig
        Creates or updates the set of CPE configuration answers for the specified tunnel.
    The answers correlate to the questions that are specific to the CPE device type (see the
    `parameters` attribute of [CpeDeviceShapeDetail](#/en/iaas/latest/CpeDeviceShapeDetail/)).

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        tunnel_cpe_device_config(List[dict[str, Any]], Optional):
            The set of configuration answers for a CPE device.
            Defaults to None.

            * key (str, Optional):
                A string that identifies the question to be answered. See the `key` attribute in
                [CpeDeviceConfigQuestion](#/en/iaas/latest/datatypes/CpeDeviceConfigQuestion).
                Defaults to None.

            * value (str, Optional):
                The answer to the question. Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"tunnel_cpe_device_config": "tunnelCpeDeviceConfig"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}/tunnelDeviceConfig".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={},
        data=payload,
        headers={
            "if-match": if_match,
            "opc-retry-token": opc_retry_token,
            "opc-request-id": opc_request_id,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {"tunnelCpeDeviceConfigParameter": "tunnel_cpe_device_config_parameter"}
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_tunnel_cpe_device_config_content(
    hub, ctx, ipsc_id: str, tunnel_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetTunnelCpeDeviceConfigContent
        Renders a set of CPE configuration content for the specified IPSec tunnel. The content helps a
    network engineer configure the actual CPE device (for example, a hardware router) that the specified
    IPSec tunnel terminates on.

    The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the
    [Cpe](#/en/iaas/latest/Cpe/) used by the specified [IPSecConnection](#/en/iaas/latest/IPSecConnection/)
    must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content
    optionally includes answers that the customer provides (see
    [UpdateTunnelCpeDeviceConfig](#/en/iaas/latest/TunnelCpeDeviceConfig/UpdateTunnelCpeDeviceConfig)),
    merged with a template of other information specific to the CPE device type.

    The operation returns configuration information for only the specified IPSec tunnel.
    Here are other similar operations:

      * [GetIpsecCpeDeviceConfigContent](#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
      returns CPE configuration content for all tunnels in a single IPSec connection.
      * [GetCpeDeviceConfigContent](#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
      returns CPE configuration content for *all* IPSec connections that use a specific CPE.

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}/tunnelDeviceConfig/content".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_ip_sec_connection_tunnel_security_associations(
    hub, ctx, ipsc_id: str, tunnel_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListIPSecConnectionTunnelSecurityAssociations
        Lists the tunnel security associations information for the specified IPSec tunnel ID.

    Args:
        ipsc_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.

        tunnel_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipsecConnections/{ipscId}/tunnels/{tunnelId}/tunnelSecurityAssociations".format(
            **{"ipscId": ipsc_id, "tunnelId": tunnel_id}
        ),
        query_params={"limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_ipv6s(
    hub,
    ctx,
    limit: int = None,
    page: str = None,
    ip_address: str = None,
    subnet_id: str = None,
    vnic_id: str = None,
    opc_request_id: str = None,
) -> Dict[str, Any]:
    r"""

    ListIpv6s
        Lists the [IPv6](#/en/iaas/latest/Ipv6/) objects based
    on one of these filters:

      * Subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm).
      * VNIC [OCID](/iaas/Content/General/Concepts/identifiers.htm).
      * Both IPv6 address and subnet OCID: This lets you get an `Ipv6` object based on its private
      IPv6 address (for example, 2001:0db8:0123:1111:abcd:ef01:2345:6789) and not its [OCID](/iaas/Content/General/Concepts/identifiers.htm). For comparison,
      [GetIpv6](#/en/iaas/latest/Ipv6/GetIpv6) requires the [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    Args:
        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        ip_address(str, Optional):
            An IP address. This could be either IPv4 or IPv6, depending on the resource.
            Example: `10.0.3.3`
            Defaults to None.

        subnet_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet. Defaults to None.

        vnic_id(str, Optional):
            The OCID of the VNIC. Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipv6".format(**{}),
        query_params={
            "limit": limit,
            "page": page,
            "ipAddress": ip_address,
            "subnetId": subnet_id,
            "vnicId": vnic_id,
        },
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_ipv6(
    hub,
    ctx,
    vnic_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    ip_address: str = None,
    ipv6_subnet_cidr: str = None,
    is_internet_access_allowed: bool = None,
) -> Dict[str, Any]:
    r"""

    CreateIpv6
        Creates an IPv6 for the specified VNIC.

    Args:
        vnic_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VNIC to assign the IPv6 to. The
            IPv6 will be in the VNIC's subnet.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        ip_address(str, Optional):
            An IPv6 address of your choice. Must be an available IP address within
            the subnet's CIDR. If you don't specify a value, Oracle automatically
            assigns an IPv6 address from the subnet. The subnet is the one that
            contains the VNIC you specify in `vnicId`.

            Example: `2001:DB8::`
            Defaults to None.

        ipv6_subnet_cidr(str, Optional):
            The IPv6 prefix allocated to the subnet. This is required if more than one IPv6 prefix exists on the subnet.
            Defaults to None.

        is_internet_access_allowed(bool, Optional):
            Whether the IPv6 can be used for internet communication. Allowed by default for an IPv6 in
            a public subnet. Never allowed for an IPv6 in a private subnet. If the value is `true`, the
            IPv6 uses its public IP address for internet communication.

            If `isInternetAccessAllowed` is set to `false`, the resulting `publicIpAddress` attribute
            for the `Ipv6` is null.

            Example: `true`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "ip_address": "ipAddress",
        "ipv6_subnet_cidr": "ipv6SubnetCidr",
        "is_internet_access_allowed": "isInternetAccessAllowed",
        "vnic_id": "vnicId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/ipv6".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "isInternetAccessAllowed": "is_internet_access_allowed",
            "lifecycleState": "lifecycle_state",
            "publicIpAddress": "public_ip_address",
            "subnetId": "subnet_id",
            "timeCreated": "time_created",
            "vnicId": "vnic_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_ipv6(
    hub, ctx, ipv6_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetIpv6
        Gets the specified IPv6. You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm).
    Alternatively, you can get the object by using
    [ListIpv6s](#/en/iaas/latest/Ipv6/ListIpv6s)
    with the IPv6 address (for example, 2001:0db8:0123:1111:98fe:dcba:9876:4321) and subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    Args:
        ipv6_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPv6.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/ipv6/{ipv6Id}".format(**{"ipv6Id": ipv6_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "isInternetAccessAllowed": "is_internet_access_allowed",
            "lifecycleState": "lifecycle_state",
            "publicIpAddress": "public_ip_address",
            "subnetId": "subnet_id",
            "timeCreated": "time_created",
            "vnicId": "vnic_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_ipv6(
    hub,
    ctx,
    ipv6_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    is_internet_access_allowed: bool = None,
    vnic_id: str = None,
) -> Dict[str, Any]:
    r"""

    UpdateIpv6
        Updates the specified IPv6. You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm).
    Use this operation if you want to:

      * Move an IPv6 to a different VNIC in the same subnet.
      * Enable/disable internet access for an IPv6.
      * Change the display name for an IPv6.
      * Update resource tags for an IPv6.

    Args:
        ipv6_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPv6.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        is_internet_access_allowed(bool, Optional):
            Whether the IPv6 can be used for internet communication. Allowed by default for an IPv6 in
            a public subnet. Never allowed for an IPv6 in a private subnet. If the value is `true`, the
            IPv6 uses its public IP address for internet communication.

            If you switch this from `true` to `false`, the `publicIpAddress` attribute for the IPv6
            becomes null.

            Example: `false`
            Defaults to None.

        vnic_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VNIC to reassign the IPv6 to.
            The VNIC must be in the same subnet as the current VNIC.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "is_internet_access_allowed": "isInternetAccessAllowed",
        "vnic_id": "vnicId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/ipv6/{ipv6Id}".format(**{"ipv6Id": ipv6_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "isInternetAccessAllowed": "is_internet_access_allowed",
            "lifecycleState": "lifecycle_state",
            "publicIpAddress": "public_ip_address",
            "subnetId": "subnet_id",
            "timeCreated": "time_created",
            "vnicId": "vnic_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_ipv6(
    hub, ctx, ipv6_id: str, if_match: str = None, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    DeleteIpv6
        Unassigns and deletes the specified IPv6. You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm).
    The IPv6 address is returned to the subnet's pool of available addresses.

    Args:
        ipv6_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the IPv6.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/ipv6/{ipv6Id}".format(**{"ipv6Id": ipv6_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_local_peering_gateways(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    vcn_id: str = None,
) -> Dict[str, Any]:
    r"""

    ListLocalPeeringGateways
        Lists the local peering gateways (LPGs) for the specified VCN and specified compartment.
    If the VCN ID is not provided, then the list includes the LPGs from all VCNs in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/localPeeringGateways".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "vcnId": vcn_id,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_local_peering_gateway(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    route_table_id: str = None,
) -> Dict[str, Any]:
    r"""

    CreateLocalPeeringGateway
        Creates a new local peering gateway (LPG) for the specified VCN.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the local peering gateway (LPG).


        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN the LPG belongs to.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the LPG will use.

            If you don't specify a route table here, the LPG is created without an associated route
            table. The Networking service does NOT automatically associate the attached VCN's default route table
            with the LPG.

            For information about why you would associate a route table with an LPG, see
            [Transit Routing: Access to Multiple VCNs in Same Region](/iaas/Content/Network/Tasks/transitrouting.htm).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "route_table_id": "routeTableId",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/localPeeringGateways".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancyPeering": "is_cross_tenancy_peering",
            "lifecycleState": "lifecycle_state",
            "peerAdvertisedCidr": "peer_advertised_cidr",
            "peerAdvertisedCidrDetails": "peer_advertised_cidr_details",
            "peerId": "peer_id",
            "peeringStatus": "peering_status",
            "peeringStatusDetails": "peering_status_details",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_local_peering_gateway(
    hub, ctx, local_peering_gateway_id: str
) -> Dict[str, Any]:
    r"""

    GetLocalPeeringGateway
        Gets the specified local peering gateway's information.

    Args:
        local_peering_gateway_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the local peering gateway.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/localPeeringGateways/{localPeeringGatewayId}".format(
            **{"localPeeringGatewayId": local_peering_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancyPeering": "is_cross_tenancy_peering",
            "lifecycleState": "lifecycle_state",
            "peerAdvertisedCidr": "peer_advertised_cidr",
            "peerAdvertisedCidrDetails": "peer_advertised_cidr_details",
            "peerId": "peer_id",
            "peeringStatus": "peering_status",
            "peeringStatusDetails": "peering_status_details",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_local_peering_gateway(
    hub,
    ctx,
    local_peering_gateway_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    route_table_id: str = None,
) -> Dict[str, Any]:
    r"""

    UpdateLocalPeeringGateway
        Updates the specified local peering gateway (LPG).

    Args:
        local_peering_gateway_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the local peering gateway.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the LPG will use.

            For information about why you would associate a route table with an LPG, see
            [Transit Routing: Access to Multiple VCNs in Same Region](/iaas/Content/Network/Tasks/transitrouting.htm).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "route_table_id": "routeTableId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/localPeeringGateways/{localPeeringGatewayId}".format(
            **{"localPeeringGatewayId": local_peering_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancyPeering": "is_cross_tenancy_peering",
            "lifecycleState": "lifecycle_state",
            "peerAdvertisedCidr": "peer_advertised_cidr",
            "peerAdvertisedCidrDetails": "peer_advertised_cidr_details",
            "peerId": "peer_id",
            "peeringStatus": "peering_status",
            "peeringStatusDetails": "peering_status_details",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_local_peering_gateway(
    hub, ctx, local_peering_gateway_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteLocalPeeringGateway
        Deletes the specified local peering gateway (LPG).

    This is an asynchronous operation; the local peering gateway's `lifecycleState` changes to TERMINATING temporarily
    until the local peering gateway is completely removed.

    Args:
        local_peering_gateway_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the local peering gateway.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/localPeeringGateways/{localPeeringGatewayId}".format(
            **{"localPeeringGatewayId": local_peering_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_local_peering_gateway_compartment(
    hub,
    ctx,
    local_peering_gateway_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeLocalPeeringGatewayCompartment
        Moves a local peering gateway into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        local_peering_gateway_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the local peering gateway.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            local peering gateway to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/localPeeringGateways/{localPeeringGatewayId}/actions/changeCompartment".format(
            **{"localPeeringGatewayId": local_peering_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def connect_local_peering_gateways(
    hub, ctx, local_peering_gateway_id: str, peer_id: str
) -> Dict[str, Any]:
    r"""

    ConnectLocalPeeringGateways
        Connects this local peering gateway (LPG) to another one in the same region.

    This operation must be called by the VCN administrator who is designated as
    the *requestor* in the peering relationship. The *acceptor* must implement
    an Identity and Access Management (IAM) policy that gives the requestor permission
    to connect to LPGs in the acceptor's compartment. Without that permission, this
    operation will fail. For more information, see
    [VCN Peering](/iaas/Content/Network/Tasks/VCNpeering.htm).

    Args:
        local_peering_gateway_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the local peering gateway.

        peer_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the LPG you want to peer with.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"peer_id": "peerId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/localPeeringGateways/{localPeeringGatewayId}/actions/connect".format(
            **{"localPeeringGatewayId": local_peering_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_nat_gateways(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListNatGateways
        Lists the NAT gateways in the specified compartment. You may optionally specify a VCN OCID
    to filter the results by VCN.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the specified lifecycle
            state. The value is case insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/natGateways".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_nat_gateway(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str,
    opc_retry_token: str = None,
    block_traffic: bool = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    public_ip_id: str = None,
    route_table_id: str = None,
) -> Dict[str, Any]:
    r"""

    CreateNatGateway
        Creates a new NAT gateway for the specified VCN. You must also set up a route rule with the
    NAT gateway as the rule's target. See [Route Table](#/en/iaas/latest/RouteTable/).

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the
            NAT gateway.


        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN the gateway belongs to.


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        block_traffic(bool, Optional):
            Whether the NAT gateway blocks traffic through it. The default is `false`.

            Example: `true`
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        public_ip_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP address associated with the NAT gateway.
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the NAT gateway.

            If you don't specify a route table here, the NAT gateway is created without an associated route
            table. The Networking service does NOT automatically associate the attached VCN's default route table
            with the NAT gateway.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "block_traffic": "blockTraffic",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "public_ip_id": "publicIpId",
        "route_table_id": "routeTableId",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/natGateways".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "blockTraffic": "block_traffic",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "natIp": "nat_ip",
            "publicIpId": "public_ip_id",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_nat_gateway(hub, ctx, nat_gateway_id: str) -> Dict[str, Any]:
    r"""

    GetNatGateway
        Gets the specified NAT gateway's information.

    Args:
        nat_gateway_id(str):
            The NAT gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/natGateways/{natGatewayId}".format(**{"natGatewayId": nat_gateway_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "blockTraffic": "block_traffic",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "natIp": "nat_ip",
            "publicIpId": "public_ip_id",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_nat_gateway(
    hub,
    ctx,
    nat_gateway_id: str,
    if_match: str = None,
    block_traffic: bool = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    route_table_id: str = None,
) -> Dict[str, Any]:
    r"""

    UpdateNatGateway
        Updates the specified NAT gateway.

    Args:
        nat_gateway_id(str):
            The NAT gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        block_traffic(bool, Optional):
            Whether the NAT gateway blocks traffic through it. The default is `false`.

            Example: `true`
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the NAT gateway.

            If you don't specify a route table here, the NAT gateway is created without an associated route
            table. The Networking service does NOT automatically associate the attached VCN's default route
            table with the NAT gateway.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "block_traffic": "blockTraffic",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "route_table_id": "routeTableId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/natGateways/{natGatewayId}".format(**{"natGatewayId": nat_gateway_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "blockTraffic": "block_traffic",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "natIp": "nat_ip",
            "publicIpId": "public_ip_id",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_nat_gateway(
    hub, ctx, nat_gateway_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteNatGateway
        Deletes the specified NAT gateway. The NAT gateway does not have to be disabled, but there
    must not be a route rule that lists the NAT gateway as a target.

    This is an asynchronous operation. The NAT gateway's `lifecycleState` will change to
    TERMINATING temporarily until the NAT gateway is completely removed.

    Args:
        nat_gateway_id(str):
            The NAT gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/natGateways/{natGatewayId}".format(**{"natGatewayId": nat_gateway_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_nat_gateway_compartment(
    hub,
    ctx,
    nat_gateway_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeNatGatewayCompartment
        Moves a NAT gateway into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        nat_gateway_id(str):
            The NAT gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the NAT gateway to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/natGateways/{natGatewayId}/actions/changeCompartment".format(
            **{"natGatewayId": nat_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_network_security_groups(
    hub,
    ctx,
    compartment_id: str = None,
    vlan_id: str = None,
    vcn_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListNetworkSecurityGroups
        Lists either the network security groups in the specified compartment, or those associated with the specified VLAN.
    You must specify either a `vlanId` or a `compartmentId`, but not both. If you specify a `vlanId`, all other parameters are ignored.

    Args:
        compartment_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment. Defaults to None.

        vlan_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VLAN. Defaults to None.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the specified lifecycle
            state. The value is case insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/networkSecurityGroups".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "vlanId": vlan_id,
            "vcnId": vcn_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_network_security_group(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    CreateNetworkSecurityGroup
        Creates a new network security group for the specified VCN.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the
            network security group.


        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN to create the network
            security group in.


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/networkSecurityGroups".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_network_security_group(
    hub, ctx, network_security_group_id: str
) -> Dict[str, Any]:
    r"""

    GetNetworkSecurityGroup
        Gets the specified network security group's information.

    To list the VNICs in an NSG, see
    [ListNetworkSecurityGroupVnics](#/en/iaas/latest/NetworkSecurityGroupVnic/ListNetworkSecurityGroupVnics).

    To list the security rules in an NSG, see
    [ListNetworkSecurityGroupSecurityRules](#/en/iaas/latest/SecurityRule/ListNetworkSecurityGroupSecurityRules).

    Args:
        network_security_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/networkSecurityGroups/{networkSecurityGroupId}".format(
            **{"networkSecurityGroupId": network_security_group_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_network_security_group(
    hub,
    ctx,
    network_security_group_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    UpdateNetworkSecurityGroup
        Updates the specified network security group.

    To add or remove an existing VNIC from the group, use
    [UpdateVnic](#/en/iaas/latest/Vnic/UpdateVnic).

    To add a VNIC to the group *when you create the VNIC*, specify the NSG's [OCID](/iaas/Content/General/Concepts/identifiers.htm) during creation.
    For example, see the `nsgIds` attribute in [CreateVnicDetails](#/en/iaas/latest/datatypes/CreateVnicDetails).

    To add or remove security rules from the group, use
    [AddNetworkSecurityGroupSecurityRules](#/en/iaas/latest/SecurityRule/AddNetworkSecurityGroupSecurityRules)
    or
    [RemoveNetworkSecurityGroupSecurityRules](#/en/iaas/latest/SecurityRule/RemoveNetworkSecurityGroupSecurityRules).

    To edit the contents of existing security rules in the group, use
    [UpdateNetworkSecurityGroupSecurityRules](#/en/iaas/latest/SecurityRule/UpdateNetworkSecurityGroupSecurityRules).

    Args:
        network_security_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/networkSecurityGroups/{networkSecurityGroupId}".format(
            **{"networkSecurityGroupId": network_security_group_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_network_security_group(
    hub, ctx, network_security_group_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteNetworkSecurityGroup
        Deletes the specified network security group. The group must not contain any VNICs.

    To get a list of the VNICs in a network security group, use
    [ListNetworkSecurityGroupVnics](#/en/iaas/latest/NetworkSecurityGroupVnic/ListNetworkSecurityGroupVnics).
    Each returned [NetworkSecurityGroupVnic](#/en/iaas/latest/NetworkSecurityGroupVnic/) object
    contains both the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VNIC and the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VNIC's parent resource (for example,
    the Compute instance that the VNIC is attached to).

    Args:
        network_security_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/networkSecurityGroups/{networkSecurityGroupId}".format(
            **{"networkSecurityGroupId": network_security_group_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def add_network_security_group_security_rules(
    hub,
    ctx,
    network_security_group_id: str,
    security_rules: List[
        make_dataclass(
            "security_rules",
            [
                ("direction", str),
                ("protocol", str),
                ("description", str, field(default=None)),
                ("destination", str, field(default=None)),
                ("destination_type", str, field(default=None)),
                (
                    "icmp_options",
                    make_dataclass(
                        "icmp_options",
                        [("type", int), ("code", int, field(default=None))],
                    ),
                    field(default=None),
                ),
                ("is_stateless", bool, field(default=None)),
                ("source", str, field(default=None)),
                ("source_type", str, field(default=None)),
                (
                    "tcp_options",
                    make_dataclass(
                        "tcp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "udp_options",
                    make_dataclass(
                        "udp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    AddNetworkSecurityGroupSecurityRules
        Adds one or more security rules to the specified network security group.

    Args:
        network_security_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

        security_rules(List[dict[str, Any]], Optional):
            The NSG security rules to add. Defaults to None.

            * description (str, Optional):
                An optional description of your choice for the rule. Avoid entering confidential information.
                Defaults to None.

            * destination (str, Optional):
                Conceptually, this is the range of IP addresses that a packet originating from the instance
                can go to.

                Allowed values:

                  * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                    IPv6 addressing is supported for all commercial and government regions. See
                    [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a security rule for traffic destined for a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.

                  * The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of a [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/) in the same
                    VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                    traffic between VNICs in the same NSG.
                Defaults to None.

            * destination_type (str, Optional):
                Type of destination for the rule. Required if `direction` = `EGRESS`.

                Allowed values:

                  * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                    particular `Service` through a service gateway).

                  * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of a
                    [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/).
                Defaults to None.

            * direction (str):
                Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets,
                or `INGRESS` for rules to allow inbound IP packets.


            * icmp_options (dict[str, Any], Optional):
                icmpOptions. Defaults to None.

                * code (int, Optional):
                    The ICMP code (optional). Defaults to None.

                * type (int):
                    The ICMP type.

            * is_stateless (bool, Optional):
                A stateless rule allows traffic in one direction. Remember to add a corresponding
                stateless rule in the other direction if you need to support bidirectional traffic. For
                example, if egress traffic allows TCP destination port 80, there should be an ingress
                rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                and a corresponding rule is not necessary for bidirectional traffic.
                Defaults to None.

            * protocol (str):
                The transport protocol. Specify either `all` or an IPv4 protocol number as
                defined in
                [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                Options are supported only for ICMP ("1"), TCP ("6"), UDP ("17"), and ICMPv6 ("58").


            * source (str, Optional):
                Conceptually, this is the range of IP addresses that a packet coming into the instance
                can come from.

                Allowed values:

                  * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                    IPv6 addressing is supported for all commercial and government regions. See
                    [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a security rule for traffic coming from a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.

                  * The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of a [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/) in the same
                    VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                    traffic between VNICs in the same NSG.
                Defaults to None.

            * source_type (str, Optional):
                Type of source for the rule. Required if `direction` = `INGRESS`.

                  * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic coming from a
                    particular `Service` through a service gateway).

                  * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of a
                    [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/).
                Defaults to None.

            * tcp_options (dict[str, Any], Optional):
                tcpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


            * udp_options (dict[str, Any], Optional):
                udpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"security_rules": "securityRules"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/networkSecurityGroups/{networkSecurityGroupId}/actions/addSecurityRules".format(
            **{"networkSecurityGroupId": network_security_group_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict({"securityRules": "security_rules"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def change_network_security_group_compartment(
    hub,
    ctx,
    network_security_group_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeNetworkSecurityGroupCompartment
        Moves a network security group into a different compartment within the same tenancy. For
    information about moving resources between compartments, see [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        network_security_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the network
            security group to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/networkSecurityGroups/{networkSecurityGroupId}/actions/changeCompartment".format(
            **{"networkSecurityGroupId": network_security_group_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def remove_network_security_group_security_rules(
    hub, ctx, network_security_group_id: str, security_rule_ids: List[str] = None
) -> Dict[str, Any]:
    r"""

    RemoveNetworkSecurityGroupSecurityRules
        Removes one or more security rules from the specified network security group.

    Args:
        network_security_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

        security_rule_ids(List[str], Optional):
            The Oracle-assigned ID of each [SecurityRule](#/en/iaas/latest/SecurityRule/) to be deleted.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"security_rule_ids": "securityRuleIds"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/networkSecurityGroups/{networkSecurityGroupId}/actions/removeSecurityRules".format(
            **{"networkSecurityGroupId": network_security_group_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def update_network_security_group_security_rules(
    hub,
    ctx,
    network_security_group_id: str,
    security_rules: List[
        make_dataclass(
            "security_rules",
            [
                ("direction", str),
                ("id", str),
                ("protocol", str),
                ("description", str, field(default=None)),
                ("destination", str, field(default=None)),
                ("destination_type", str, field(default=None)),
                (
                    "icmp_options",
                    make_dataclass(
                        "icmp_options",
                        [("type", int), ("code", int, field(default=None))],
                    ),
                    field(default=None),
                ),
                ("is_stateless", bool, field(default=None)),
                ("source", str, field(default=None)),
                ("source_type", str, field(default=None)),
                (
                    "tcp_options",
                    make_dataclass(
                        "tcp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "udp_options",
                    make_dataclass(
                        "udp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    UpdateNetworkSecurityGroupSecurityRules
        Updates one or more security rules in the specified network security group.

    Args:
        network_security_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

        security_rules(List[dict[str, Any]], Optional):
            The NSG security rules to update. Defaults to None.

            * description (str, Optional):
                An optional description of your choice for the rule. Avoid entering confidential information.
                Defaults to None.

            * destination (str, Optional):
                Conceptually, this is the range of IP addresses that a packet originating from the instance
                can go to.

                Allowed values:

                  * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                    IPv6 addressing is supported for all commercial and government regions. See
                    [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a security rule for traffic destined for a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.

                  * The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of a [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/) in the same
                    VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                    traffic between VNICs in the same NSG.
                Defaults to None.

            * destination_type (str, Optional):
                Type of destination for the rule. Required if `direction` = `EGRESS`.

                Allowed values:

                  * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                    particular `Service` through a service gateway).

                  * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of a
                    [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/).
                Defaults to None.

            * direction (str):
                Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets,
                or `INGRESS` for rules to allow inbound IP packets.


            * icmp_options (dict[str, Any], Optional):
                icmpOptions. Defaults to None.

                * code (int, Optional):
                    The ICMP code (optional). Defaults to None.

                * type (int):
                    The ICMP type.

            * id (str):
                The Oracle-assigned ID of the security rule that you want to update. You can't change this value.

                Example: `04ABEC`


            * is_stateless (bool, Optional):
                A stateless rule allows traffic in one direction. Remember to add a corresponding
                stateless rule in the other direction if you need to support bidirectional traffic. For
                example, if egress traffic allows TCP destination port 80, there should be an ingress
                rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                and a corresponding rule is not necessary for bidirectional traffic.
                Defaults to None.

            * protocol (str):
                The transport protocol. Specify either `all` or an IPv4 protocol number as
                defined in
                [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                Options are supported only for ICMP ("1"), TCP ("6"), UDP ("17"), and ICMPv6 ("58").


            * source (str, Optional):
                Conceptually, this is the range of IP addresses that a packet coming into the instance
                can come from.

                Allowed values:

                  * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                    IPv6 addressing is supported for all commercial and government regions. See
                    [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a security rule for traffic coming from a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.

                  * The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of a [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/) in the same
                    VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                    traffic between VNICs in the same NSG.
                Defaults to None.

            * source_type (str, Optional):
                Type of source for the rule. Required if `direction` = `INGRESS`.

                  * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic coming from a
                    particular `Service` through a service gateway).

                  * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of a
                    [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/).
                Defaults to None.

            * tcp_options (dict[str, Any], Optional):
                tcpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


            * udp_options (dict[str, Any], Optional):
                udpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"security_rules": "securityRules"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/networkSecurityGroups/{networkSecurityGroupId}/actions/updateSecurityRules".format(
            **{"networkSecurityGroupId": network_security_group_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict({"securityRules": "security_rules"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_network_security_group_security_rules(
    hub,
    ctx,
    network_security_group_id: str,
    direction: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

    ListNetworkSecurityGroupSecurityRules
        Lists the security rules in the specified network security group.

    Args:
        network_security_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

        direction(str, Optional):
            Direction of the security rule. Set to `EGRESS` for rules that allow outbound IP packets,
            or `INGRESS` for rules that allow inbound IP packets.
            Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/networkSecurityGroups/{networkSecurityGroupId}/securityRules".format(
            **{"networkSecurityGroupId": network_security_group_id}
        ),
        query_params={
            "direction": direction,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_network_security_group_vnics(
    hub,
    ctx,
    network_security_group_id: str,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

    ListNetworkSecurityGroupVnics
        Lists the VNICs in the specified network security group.

    Args:
        network_security_group_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/networkSecurityGroups/{networkSecurityGroupId}/vnics".format(
            **{"networkSecurityGroupId": network_security_group_id}
        ),
        query_params={
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_networking_topology(
    hub,
    ctx,
    compartment_id: str,
    access_level: str = None,
    query_compartment_subtree: bool = None,
    opc_request_id: str = None,
    if_none_match: str = None,
    cache_control: str = None,
) -> Dict[str, Any]:
    r"""

    Get a Virtual Networking topology for the current region
        Gets a virtual networking topology for the current region.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        access_level(str, Optional):
            Valid values are `ANY` and `ACCESSIBLE`. The default is `ANY`.
            Setting this to `ACCESSIBLE` returns only compartments for which a
            user has INSPECT permissions, either directly or indirectly (permissions can be on a
            resource in a subcompartment). A restricted set of fields is returned for compartments in which a user has
            indirect INSPECT permissions.

            When set to `ANY` permissions are not checked.
            Defaults to None.

        query_compartment_subtree(bool, Optional):
            When set to true, the hierarchy of compartments is traversed
            and the specified compartment and its subcompartments are
            inspected depending on the the setting of `accessLevel`.
            Default is false.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        if_none_match(str, Optional):
            For querying if there is a cached value on the server. The If-None-Match HTTP request header
            makes the request conditional. For GET and HEAD methods, the server will send back the requested
            resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            For other methods, the request will be processed only if the eventually existing resource's
            ETag doesn't match any of the values listed.
            Defaults to None.

        cache_control(str, Optional):
            The Cache-Control HTTP header holds directives (instructions)
            for caching in both requests and responses.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/networkingTopology".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "accessLevel": access_level,
            "queryCompartmentSubtree": query_compartment_subtree,
        },
        data=payload,
        headers={
            "opc-request-id": opc_request_id,
            "if-none-match": if_none_match,
            "cache-control": cache_control,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "entities": "entities",
            "limitedEntities": "limited_entities",
            "relationships": "relationships",
            "timeCreated": "time_created",
            "type": "type",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_private_ips(
    hub,
    ctx,
    limit: int = None,
    page: str = None,
    ip_address: str = None,
    subnet_id: str = None,
    vnic_id: str = None,
    vlan_id: str = None,
) -> Dict[str, Any]:
    r"""

    ListPrivateIps
        Lists the [PrivateIp](#/en/iaas/latest/PrivateIp/) objects based
    on one of these filters:

      - Subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm).
      - VNIC [OCID](/iaas/Content/General/Concepts/identifiers.htm).
      - Both private IP address and subnet OCID: This lets
      you get a `privateIP` object based on its private IP
      address (for example, 10.0.3.3) and not its [OCID](/iaas/Content/General/Concepts/identifiers.htm). For comparison,
      [GetPrivateIp](#/en/iaas/latest/PrivateIp/GetPrivateIp)
      requires the [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    If you're listing all the private IPs associated with a given subnet
    or VNIC, the response includes both primary and secondary private IPs.

    If you are an Oracle Cloud VMware Solution customer and have VLANs
    in your VCN, you can filter the list by VLAN [OCID](/iaas/Content/General/Concepts/identifiers.htm). See [Vlan](#/en/iaas/latest/Vlan).

    Args:
        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        ip_address(str, Optional):
            An IP address. This could be either IPv4 or IPv6, depending on the resource.
            Example: `10.0.3.3`
            Defaults to None.

        subnet_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet. Defaults to None.

        vnic_id(str, Optional):
            The OCID of the VNIC. Defaults to None.

        vlan_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VLAN. Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/privateIps".format(**{}),
        query_params={
            "limit": limit,
            "page": page,
            "ipAddress": ip_address,
            "subnetId": subnet_id,
            "vnicId": vnic_id,
            "vlanId": vlan_id,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_private_ip(
    hub,
    ctx,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    hostname_label: str = None,
    ip_address: str = None,
    vlan_id: str = None,
    vnic_id: str = None,
) -> Dict[str, Any]:
    r"""

    CreatePrivateIp
        Creates a secondary private IP for the specified VNIC.
    For more information about secondary private IPs, see
    [IP Addresses](/iaas/Content/Network/Tasks/managingIPaddresses.htm).

    Args:
        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        hostname_label(str, Optional):
            The hostname for the private IP. Used for DNS. The value
            is the hostname portion of the private IP's fully qualified domain name (FQDN)
            (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`).
            Must be unique across all VNICs in the subnet and comply with
            [RFC 952](https://tools.ietf.org/html/rfc952) and
            [RFC 1123](https://tools.ietf.org/html/rfc1123).

            For more information, see
            [DNS in Your Virtual Cloud Network](/iaas/Content/Network/Concepts/dns.htm).

            Example: `bminstance1`
            Defaults to None.

        ip_address(str, Optional):
            A private IP address of your choice. Must be an available IP address within
            the subnet's CIDR. If you don't specify a value, Oracle automatically
            assigns a private IP address from the subnet.

            Example: `10.0.3.3`
            Defaults to None.

        vlan_id(str, Optional):
            Use this attribute only with the Oracle Cloud VMware Solution.

            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VLAN from which the private IP is to be drawn. The IP address,
            *if supplied*, must be valid for the given VLAN. See [Vlan](#/en/iaas/latest/Vlan).
            Defaults to None.

        vnic_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VNIC to assign the private IP to. The VNIC and private IP
            must be in the same subnet.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "hostname_label": "hostnameLabel",
        "ip_address": "ipAddress",
        "vlan_id": "vlanId",
        "vnic_id": "vnicId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/privateIps".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "hostnameLabel": "hostname_label",
            "id": "id",
            "ipAddress": "ip_address",
            "isPrimary": "is_primary",
            "subnetId": "subnet_id",
            "timeCreated": "time_created",
            "vlanId": "vlan_id",
            "vnicId": "vnic_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_private_ip(hub, ctx, private_ip_id: str) -> Dict[str, Any]:
    r"""

    GetPrivateIp
        Gets the specified private IP. You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm).
    Alternatively, you can get the object by using
    [ListPrivateIps](#/en/iaas/latest/PrivateIp/ListPrivateIps)
    with the private IP address (for example, 10.0.3.3) and subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    Args:
        private_ip_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the private IP or IPv6.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/privateIps/{privateIpId}".format(**{"privateIpId": private_ip_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "hostnameLabel": "hostname_label",
            "id": "id",
            "ipAddress": "ip_address",
            "isPrimary": "is_primary",
            "subnetId": "subnet_id",
            "timeCreated": "time_created",
            "vlanId": "vlan_id",
            "vnicId": "vnic_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_private_ip(
    hub,
    ctx,
    private_ip_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    hostname_label: str = None,
    vnic_id: str = None,
) -> Dict[str, Any]:
    r"""

    UpdatePrivateIp
        Updates the specified private IP. You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm).
    Use this operation if you want to:

      - Move a secondary private IP to a different VNIC in the same subnet.
      - Change the display name for a secondary private IP.
      - Change the hostname for a secondary private IP.

    This operation cannot be used with primary private IPs.
    To update the hostname for the primary IP on a VNIC, use
    [UpdateVnic](#/en/iaas/latest/Vnic/UpdateVnic).

    Args:
        private_ip_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the private IP or IPv6.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        hostname_label(str, Optional):
            The hostname for the private IP. Used for DNS. The value
            is the hostname portion of the private IP's fully qualified domain name (FQDN)
            (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`).
            Must be unique across all VNICs in the subnet and comply with
            [RFC 952](https://tools.ietf.org/html/rfc952) and
            [RFC 1123](https://tools.ietf.org/html/rfc1123).

            For more information, see
            [DNS in Your Virtual Cloud Network](/iaas/Content/Network/Concepts/dns.htm).

            Example: `bminstance1`
            Defaults to None.

        vnic_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VNIC to reassign the private IP to. The VNIC must
            be in the same subnet as the current VNIC.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "hostname_label": "hostnameLabel",
        "vnic_id": "vnicId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/privateIps/{privateIpId}".format(**{"privateIpId": private_ip_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "hostnameLabel": "hostname_label",
            "id": "id",
            "ipAddress": "ip_address",
            "isPrimary": "is_primary",
            "subnetId": "subnet_id",
            "timeCreated": "time_created",
            "vlanId": "vlan_id",
            "vnicId": "vnic_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_private_ip(
    hub, ctx, private_ip_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeletePrivateIp
        Unassigns and deletes the specified private IP. You must
    specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm). The private IP address is returned to
    the subnet's pool of available addresses.

    This operation cannot be used with primary private IPs, which are
    automatically unassigned and deleted when the VNIC is terminated.

    **Important:** If a secondary private IP is the
    [target of a route rule](/iaas/Content/Network/Tasks/managingroutetables.htm#privateip),
    unassigning it from the VNIC causes that route rule to blackhole and the traffic
    will be dropped.

    Args:
        private_ip_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the private IP or IPv6.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/privateIps/{privateIpId}".format(**{"privateIpId": private_ip_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_public_ip_pools(
    hub,
    ctx,
    compartment_id: str,
    opc_request_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    byoip_range_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

    ListPublicIpPools
        Lists the public IP pools in the specified compartment.
    You can filter the list using query parameters.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        byoip_range_id(str, Optional):
            A filter to return only resources that match the given BYOIP CIDR block.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/publicIpPools".format(**{}),
        query_params={
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "byoipRangeId": byoip_range_id,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "compartmentId": compartment_id,
        },
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict({"items": "items"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def create_public_ip_pool(
    hub,
    ctx,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    CreatePublicIpPool
        Creates a public IP pool.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the public IP pool.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/publicIpPools".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "cidrBlocks": "cidr_blocks",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_public_ip_pool(
    hub, ctx, public_ip_pool_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetPublicIpPool
        Gets the specified `PublicIpPool` object. You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    Args:
        public_ip_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/publicIpPools/{publicIpPoolId}".format(
            **{"publicIpPoolId": public_ip_pool_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "cidrBlocks": "cidr_blocks",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_public_ip_pool(
    hub,
    ctx,
    public_ip_pool_id: str,
    opc_request_id: str = None,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    UpdatePublicIpPool
        Updates the specified public IP pool.

    Args:
        public_ip_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/publicIpPools/{publicIpPoolId}".format(
            **{"publicIpPoolId": public_ip_pool_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "cidrBlocks": "cidr_blocks",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_public_ip_pool(
    hub, ctx, public_ip_pool_id: str, opc_request_id: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeletePublicIpPool
        Deletes the specified public IP pool.
    To delete a public IP pool it must not have any active IP address allocations.
    You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm) when deleting an IP pool.

    Args:
        public_ip_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/publicIpPools/{publicIpPoolId}".format(
            **{"publicIpPoolId": public_ip_pool_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def add_public_ip_pool_capacity(
    hub,
    ctx,
    public_ip_pool_id: str,
    byoip_range_id: str,
    cidr_block: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    AddPublicIpPoolCapacity
        Adds some or all of a CIDR block to a public IP pool.

    The CIDR block (or subrange) must not overlap with any other CIDR block already added to this or any other public IP pool.

    Args:
        public_ip_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.

        byoip_range_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource to which the CIDR block belongs.

        cidr_block(str):
            The CIDR block to add to the public IP pool. It could be all of the CIDR block identified in `byoipRangeId`, or a subrange.
            Example: `10.0.1.0/24`


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"byoip_range_id": "byoipRangeId", "cidr_block": "cidrBlock"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/publicIpPools/{publicIpPoolId}/actions/addCapacity".format(
            **{"publicIpPoolId": public_ip_pool_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "cidrBlocks": "cidr_blocks",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def change_public_ip_pool_compartment(
    hub,
    ctx,
    public_ip_pool_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangePublicIpPoolCompartment
        Moves a public IP pool to a different compartment. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        public_ip_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the destination compartment for the public IP pool move.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/publicIpPools/{publicIpPoolId}/actions/changeCompartment".format(
            **{"publicIpPoolId": public_ip_pool_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def remove_public_ip_pool_capacity(
    hub,
    ctx,
    public_ip_pool_id: str,
    cidr_block: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    RemovePublicIpPoolCapacity
        Removes a CIDR block from the referenced public IP pool.

    Args:
        public_ip_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.

        cidr_block(str):
            The CIDR block to remove from the  public IP pool.
            Example: `10.0.1.0/24`


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"cidr_block": "cidrBlock"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/publicIpPools/{publicIpPoolId}/actions/removeCapacity".format(
            **{"publicIpPoolId": public_ip_pool_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "cidrBlocks": "cidr_blocks",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_public_ips(
    hub,
    ctx,
    scope: str,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    availability_domain: str = None,
    lifetime: str = None,
    public_ip_pool_id: str = None,
) -> Dict[str, Any]:
    r"""

    ListPublicIps
        Lists the [PublicIp](#/en/iaas/latest/PublicIp/) objects
    in the specified compartment. You can filter the list by using query parameters.

    To list your reserved public IPs:
      * Set `scope` = `REGION`  (required)
      * Leave the `availabilityDomain` parameter empty
      * Set `lifetime` = `RESERVED`

    To list the ephemeral public IPs assigned to a regional entity such as a NAT gateway:
      * Set `scope` = `REGION`  (required)
      * Leave the `availabilityDomain` parameter empty
      * Set `lifetime` = `EPHEMERAL`

    To list the ephemeral public IPs assigned to private IPs:
      * Set `scope` = `AVAILABILITY_DOMAIN` (required)
      * Set the `availabilityDomain` parameter to the desired availability domain (required)
      * Set `lifetime` = `EPHEMERAL`

    **Note:** An ephemeral public IP assigned to a private IP
    is always in the same availability domain and compartment as the private IP.

    Args:
        scope(str):
            Whether the public IP is regional or specific to a particular availability domain.

            * `REGION`: The public IP exists within a region and is assigned to a regional entity
            (such as a [NatGateway](#/en/iaas/latest/NatGateway/)), or can be assigned to a private IP
            in any availability domain in the region. Reserved public IPs have `scope` = `REGION`, as do
            ephemeral public IPs assigned to a regional entity.

            * `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the entity
            it's assigned to, which is specified by the `availabilityDomain` property of the public IP object.
            Ephemeral public IPs that are assigned to private IPs have `scope` = `AVAILABILITY_DOMAIN`.


        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        availability_domain(str, Optional):
            The name of the availability domain.

            Example: `Uocm:PHX-AD-1`
            Defaults to None.

        lifetime(str, Optional):
            A filter to return only public IPs that match given lifetime.
            Defaults to None.

        public_ip_pool_id(str, Optional):
            A filter to return only resources that belong to the given public IP pool.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/publicIps".format(**{}),
        query_params={
            "limit": limit,
            "page": page,
            "scope": scope,
            "availabilityDomain": availability_domain,
            "lifetime": lifetime,
            "compartmentId": compartment_id,
            "publicIpPoolId": public_ip_pool_id,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_public_ip(
    hub,
    ctx,
    compartment_id: str,
    lifetime: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    private_ip_id: str = None,
    public_ip_pool_id: str = None,
) -> Dict[str, Any]:
    r"""

    CreatePublicIp
        Creates a public IP. Use the `lifetime` property to specify whether it's an ephemeral or
    reserved public IP. For information about limits on how many you can create, see
    [Public IP Addresses](/iaas/Content/Network/Tasks/managingpublicIPs.htm).

    * **For an ephemeral public IP assigned to a private IP:** You must also specify a `privateIpId`
    with the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the primary private IP you want to assign the public IP to. The public IP is
    created in the same availability domain as the private IP. An ephemeral public IP must always be
    assigned to a private IP, and only to the *primary* private IP on a VNIC, not a secondary
    private IP. Exception: If you create a [NatGateway](#/en/iaas/latest/NatGateway/), Oracle
    automatically assigns the NAT gateway a regional ephemeral public IP that you cannot remove.

    * **For a reserved public IP:** You may also optionally assign the public IP to a private
    IP by specifying `privateIpId`. Or you can later assign the public IP with
    [UpdatePublicIp](#/en/iaas/latest/PublicIp/UpdatePublicIp).

    **Note:** When assigning a public IP to a private IP, the private IP must not already have
    a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned.

    Also, for reserved public IPs, the optional assignment part of this operation is
    asynchronous. Poll the public IP's `lifecycleState` to determine if the assignment
    succeeded.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the public IP. For ephemeral public IPs,
            you must set this to the private IP's compartment [OCID](/iaas/Content/General/Concepts/identifiers.htm).


        lifetime(str):
            Defines when the public IP is deleted and released back to the Oracle Cloud
            Infrastructure public IP pool. For more information, see
            [Public IP Addresses](/iaas/Content/Network/Tasks/managingpublicIPs.htm).


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        private_ip_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the private IP to assign the public IP to.

            Required for an ephemeral public IP because it must always be assigned to a private IP
            (specifically a *primary* private IP).

            Optional for a reserved public IP. If you don't provide it, the public IP is created but not
            assigned to a private IP. You can later assign the public IP with
            [UpdatePublicIp](#/en/iaas/latest/PublicIp/UpdatePublicIp).
            Defaults to None.

        public_ip_pool_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool. Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "lifetime": "lifetime",
        "private_ip_id": "privateIpId",
        "public_ip_pool_id": "publicIpPoolId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/publicIps".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "assignedEntityId": "assigned_entity_id",
            "assignedEntityType": "assigned_entity_type",
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "lifecycleState": "lifecycle_state",
            "lifetime": "lifetime",
            "privateIpId": "private_ip_id",
            "publicIpPoolId": "public_ip_pool_id",
            "scope": "scope",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_public_ip_by_ip_address(hub, ctx, ip_address: str) -> Dict[str, Any]:
    r"""

    GetPublicIpByIpAddress
        Gets the public IP based on the public IP address (for example, 203.0.113.2).

    **Note:** If you're fetching a reserved public IP that is in the process of being
    moved to a different private IP, the service returns the public IP object with
    `lifecycleState` = ASSIGNING and `assignedEntityId` = [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the target private IP.

    Args:
        ip_address(str):
            The public IP address.
            Example: 203.0.113.2

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"ip_address": "ipAddress"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/publicIps/actions/getByIpAddress".format(**{}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "assignedEntityId": "assigned_entity_id",
            "assignedEntityType": "assigned_entity_type",
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "lifecycleState": "lifecycle_state",
            "lifetime": "lifetime",
            "privateIpId": "private_ip_id",
            "publicIpPoolId": "public_ip_pool_id",
            "scope": "scope",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_public_ip_by_private_ip_id(
    hub, ctx, private_ip_id: str
) -> Dict[str, Any]:
    r"""

    GetPublicIpByPrivateIpId
        Gets the public IP assigned to the specified private IP. You must specify the OCID
    of the private IP. If no public IP is assigned, a 404 is returned.

    **Note:** If you're fetching a reserved public IP that is in the process of being
    moved to a different private IP, and you provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the original private
    IP, this operation returns a 404. If you instead provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the target
    private IP, or if you instead call
    [GetPublicIp](#/en/iaas/latest/PublicIp/GetPublicIp) or
    [GetPublicIpByIpAddress](#/en/iaas/latest/PublicIp/GetPublicIpByIpAddress), the
    service returns the public IP object with `lifecycleState` = ASSIGNING and
    `assignedEntityId` = [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the target private IP.

    Args:
        private_ip_id(str):
            [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the private IP.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"private_ip_id": "privateIpId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/publicIps/actions/getByPrivateIpId".format(**{}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "assignedEntityId": "assigned_entity_id",
            "assignedEntityType": "assigned_entity_type",
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "lifecycleState": "lifecycle_state",
            "lifetime": "lifetime",
            "privateIpId": "private_ip_id",
            "publicIpPoolId": "public_ip_pool_id",
            "scope": "scope",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_public_ip(hub, ctx, public_ip_id: str) -> Dict[str, Any]:
    r"""

    GetPublicIp
        Gets the specified public IP. You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    Alternatively, you can get the object by using [GetPublicIpByIpAddress](#/en/iaas/latest/PublicIp/GetPublicIpByIpAddress)
    with the public IP address (for example, 203.0.113.2).

    Or you can use [GetPublicIpByPrivateIpId](#/en/iaas/latest/PublicIp/GetPublicIpByPrivateIpId)
    with the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the private IP that the public IP is assigned to.

    **Note:** If you're fetching a reserved public IP that is in the process of being
    moved to a different private IP, the service returns the public IP object with
    `lifecycleState` = ASSIGNING and `assignedEntityId` = [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the target private IP.

    Args:
        public_ip_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/publicIps/{publicIpId}".format(**{"publicIpId": public_ip_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "assignedEntityId": "assigned_entity_id",
            "assignedEntityType": "assigned_entity_type",
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "lifecycleState": "lifecycle_state",
            "lifetime": "lifetime",
            "privateIpId": "private_ip_id",
            "publicIpPoolId": "public_ip_pool_id",
            "scope": "scope",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_public_ip(
    hub,
    ctx,
    public_ip_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    private_ip_id: str = None,
) -> Dict[str, Any]:
    r"""

    UpdatePublicIp
        Updates the specified public IP. You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm). Use this operation if you want to:

    * Assign a reserved public IP in your pool to a private IP.
    * Move a reserved public IP to a different private IP.
    * Unassign a reserved public IP from a private IP (which returns it to your pool
    of reserved public IPs).
    * Change the display name or tags for a public IP.

    Assigning, moving, and unassigning a reserved public IP are asynchronous
    operations. Poll the public IP's `lifecycleState` to determine if the operation
    succeeded.

    **Note:** When moving a reserved public IP, the target private IP
    must not already have a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it
    does, an error is returned. Also, the initial unassignment from the original
    private IP always succeeds, but the assignment to the target private IP is asynchronous and
    could fail silently (for example, if the target private IP is deleted or has a different public IP
    assigned to it in the interim). If that occurs, the public IP remains unassigned and its
    `lifecycleState` switches to AVAILABLE (it is not reassigned to its original private IP).
    You must poll the public IP's `lifecycleState` to determine if the move succeeded.

    Regarding ephemeral public IPs:

    * If you want to assign an ephemeral public IP to a primary private IP, use
    [CreatePublicIp](#/en/iaas/latest/PublicIp/CreatePublicIp).
    * You can't move an ephemeral public IP to a different private IP.
    * If you want to unassign an ephemeral public IP from its private IP, use
    [DeletePublicIp](#/en/iaas/latest/PublicIp/DeletePublicIp), which
    unassigns and deletes the ephemeral public IP.

    **Note:** If a public IP is assigned to a secondary private
    IP (see [PrivateIp](#/en/iaas/latest/PrivateIp)), and you move that secondary
    private IP to another VNIC, the public IP moves with it.

    **Note:** There's a limit to the number of [public IPs](#/en/iaas/latest/PublicIp/)
    a VNIC or instance can have. If you try to move a reserved public IP
    to a VNIC or instance that has already reached its public IP limit, an error is
    returned. For information about the public IP limits, see
    [Public IP Addresses](/iaas/Content/Network/Tasks/managingpublicIPs.htm).

    Args:
        public_ip_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        private_ip_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the private IP to assign the public IP to.
            * If the public IP is already assigned to a different private IP, it will be unassigned
            and then reassigned to the specified private IP.
            * If you set this field to an empty string, the public IP will be unassigned from the
            private IP it is currently assigned to.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "private_ip_id": "privateIpId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/publicIps/{publicIpId}".format(**{"publicIpId": public_ip_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "assignedEntityId": "assigned_entity_id",
            "assignedEntityType": "assigned_entity_type",
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipAddress": "ip_address",
            "lifecycleState": "lifecycle_state",
            "lifetime": "lifetime",
            "privateIpId": "private_ip_id",
            "publicIpPoolId": "public_ip_pool_id",
            "scope": "scope",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_public_ip(
    hub, ctx, public_ip_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeletePublicIp
        Unassigns and deletes the specified public IP (either ephemeral or reserved).
    You must specify the object's [OCID](/iaas/Content/General/Concepts/identifiers.htm). The public IP address is returned to the
    Oracle Cloud Infrastructure public IP pool.

    **Note:** You cannot update, unassign, or delete the public IP that Oracle automatically
    assigned to an entity for you (such as a load balancer or NAT gateway). The public IP is
    automatically deleted if the assigned entity is terminated.

    For an assigned reserved public IP, the initial unassignment portion of this operation
    is asynchronous. Poll the public IP's `lifecycleState` to determine
    if the operation succeeded.

    If you want to simply unassign a reserved public IP and return it to your pool
    of reserved public IPs, instead use
    [UpdatePublicIp](#/en/iaas/latest/PublicIp/UpdatePublicIp).

    Args:
        public_ip_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/publicIps/{publicIpId}".format(**{"publicIpId": public_ip_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_public_ip_compartment(
    hub,
    ctx,
    public_ip_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangePublicIpCompartment
        Moves a public IP into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    This operation applies only to reserved public IPs. Ephemeral public IPs always belong to the
    same compartment as their VNIC and move accordingly.

    Args:
        public_ip_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the public IP.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            public IP to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/publicIps/{publicIpId}/actions/changeCompartment".format(
            **{"publicIpId": public_ip_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_remote_peering_connections(
    hub,
    ctx,
    compartment_id: str,
    drg_id: str = None,
    limit: int = None,
    page: str = None,
) -> Dict[str, Any]:
    r"""

    ListRemotePeeringConnections
        Lists the remote peering connections (RPCs) for the specified DRG and compartment
    (the RPC's compartment).

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        drg_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/remotePeeringConnections".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "drgId": drg_id,
            "limit": limit,
            "page": page,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_remote_peering_connection(
    hub,
    ctx,
    compartment_id: str,
    drg_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    CreateRemotePeeringConnection
        Creates a new remote peering connection (RPC) for the specified DRG.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the RPC.

        drg_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the DRG the RPC belongs to.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "drg_id": "drgId",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/remotePeeringConnections".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancyPeering": "is_cross_tenancy_peering",
            "lifecycleState": "lifecycle_state",
            "peerId": "peer_id",
            "peerRegionName": "peer_region_name",
            "peerTenancyId": "peer_tenancy_id",
            "peeringStatus": "peering_status",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_remote_peering_connection(
    hub, ctx, remote_peering_connection_id: str
) -> Dict[str, Any]:
    r"""

    GetRemotePeeringConnection
        Get the specified remote peering connection's information.

    Args:
        remote_peering_connection_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the remote peering connection (RPC).

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/remotePeeringConnections/{remotePeeringConnectionId}".format(
            **{"remotePeeringConnectionId": remote_peering_connection_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancyPeering": "is_cross_tenancy_peering",
            "lifecycleState": "lifecycle_state",
            "peerId": "peer_id",
            "peerRegionName": "peer_region_name",
            "peerTenancyId": "peer_tenancy_id",
            "peeringStatus": "peering_status",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_remote_peering_connection(
    hub,
    ctx,
    remote_peering_connection_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    UpdateRemotePeeringConnection
        Updates the specified remote peering connection (RPC).

    Args:
        remote_peering_connection_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the remote peering connection (RPC).

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/remotePeeringConnections/{remotePeeringConnectionId}".format(
            **{"remotePeeringConnectionId": remote_peering_connection_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "drgId": "drg_id",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isCrossTenancyPeering": "is_cross_tenancy_peering",
            "lifecycleState": "lifecycle_state",
            "peerId": "peer_id",
            "peerRegionName": "peer_region_name",
            "peerTenancyId": "peer_tenancy_id",
            "peeringStatus": "peering_status",
            "timeCreated": "time_created",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_remote_peering_connection(
    hub, ctx, remote_peering_connection_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteRemotePeeringConnection
        Deletes the remote peering connection (RPC).

    This is an asynchronous operation; the RPC's `lifecycleState` changes to TERMINATING temporarily
    until the RPC is completely removed.

    Args:
        remote_peering_connection_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the remote peering connection (RPC).

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/remotePeeringConnections/{remotePeeringConnectionId}".format(
            **{"remotePeeringConnectionId": remote_peering_connection_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_remote_peering_connection_compartment(
    hub,
    ctx,
    remote_peering_connection_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeRemotePeeringConnectionCompartment
        Moves a remote peering connection (RPC) into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        remote_peering_connection_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the remote peering connection (RPC).

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            remote peering connection to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/remotePeeringConnections/{remotePeeringConnectionId}/actions/changeCompartment".format(
            **{"remotePeeringConnectionId": remote_peering_connection_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def connect_remote_peering_connections(
    hub, ctx, remote_peering_connection_id: str, peer_id: str, peer_region_name: str
) -> Dict[str, Any]:
    r"""

    ConnectRemotePeeringConnections
        Connects this RPC to another one in a different region.

    This operation must be called by the VCN administrator who is designated as
    the *requestor* in the peering relationship. The *acceptor* must implement
    an Identity and Access Management (IAM) policy that gives the requestor permission
    to connect to RPCs in the acceptor's compartment. Without that permission, this
    operation will fail. For more information, see
    [VCN Peering](/iaas/Content/Network/Tasks/VCNpeering.htm).

    Args:
        remote_peering_connection_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the remote peering connection (RPC).

        peer_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the RPC you want to peer with.

        peer_region_name(str):
            The name of the region that contains the RPC you want to peer with.

            Example: `us-ashburn-1`

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"peer_id": "peerId", "peer_region_name": "peerRegionName"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/remotePeeringConnections/{remotePeeringConnectionId}/actions/connect".format(
            **{"remotePeeringConnectionId": remote_peering_connection_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_route_tables(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    vcn_id: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListRouteTables
        Lists the route tables in the specified VCN and specified compartment.
    If the VCN ID is not provided, then the list includes the route tables from all VCNs in the specified compartment.
    The response includes the default route table that automatically comes with
    each VCN in the specified compartment, plus any route tables you've created.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to only return resources that match the given lifecycle
            state. The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/routeTables".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "vcnId": vcn_id,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_route_table(
    hub,
    ctx,
    compartment_id: str,
    route_rules: List[
        make_dataclass(
            "route_rules",
            [
                ("network_entity_id", str),
                ("cidr_block", str, field(default=None)),
                ("description", str, field(default=None)),
                ("destination", str, field(default=None)),
                ("destination_type", str, field(default=None)),
                ("route_type", str, field(default=None)),
            ],
        )
    ],
    vcn_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    CreateRouteTable
        Creates a new route table for the specified VCN. In the request you must also include at least one route
    rule for the new route table. For information on the number of rules you can have in a route table, see
    [Service Limits](/iaas/Content/General/Concepts/servicelimits.htm). For general information about route
    tables in your VCN and the types of targets you can use in route rules,
    see [Route Tables](/iaas/Content/Network/Tasks/managingroutetables.htm).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want the route
    table to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets,
    or other Networking Service components. If you're not sure which compartment to use, put the route
    table in the same compartment as the VCN. For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
    [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the route table, otherwise a default is provided.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the route table.

        route_rules(List[dict[str, Any]]):
            The collection of rules used for routing destination IPs to network devices.


            * cidr_block (str, Optional):
                Deprecated. Instead use `destination` and `destinationType`. Requests that include both
                `cidrBlock` and `destination` will be rejected.

                A destination IP address range in CIDR notation. Matching packets will
                be routed to the indicated network entity (the target).

                Cannot be an IPv6 prefix.

                Example: `0.0.0.0/0`
                Defaults to None.

            * description (str, Optional):
                An optional description of your choice for the rule.
                Defaults to None.

            * destination (str, Optional):
                Conceptually, this is the range of IP addresses used for matching when routing
                traffic. Required if you provide a `destinationType`.

                Allowed values:

                  * IP address range in CIDR notation. Can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24`
                  or `2001:0db8:0123:45::/56`. If you set this to an IPv6 prefix, the route rule's target
                  can only be a DRG or internet gateway.
                  IPv6 addressing is supported for all commercial and government regions.
                  See [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a route rule for traffic destined for a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.
                Defaults to None.

            * destination_type (str, Optional):
                Type of destination for the rule. Required if you provide a `destination`.

                  * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                    particular `Service` through a service gateway).
                Defaults to None.

            * network_entity_id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the route rule's target. For information about the type of
                targets you can specify, see
                [Route Tables](/iaas/Content/Network/Tasks/managingroutetables.htm).


            * route_type (str, Optional):
                A route rule can be STATIC if manually added to the route table, LOCAL if added by OCI to the route table.
                Defaults to None.

        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN the route table belongs to.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "route_rules": "routeRules",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/routeTables".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "routeRules": "route_rules",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_route_table(hub, ctx, rt_id: str) -> Dict[str, Any]:
    r"""

    GetRouteTable
        Gets the specified route table's information.

    Args:
        rt_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/routeTables/{rtId}".format(**{"rtId": rt_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "routeRules": "route_rules",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_route_table(
    hub,
    ctx,
    rt_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    route_rules: List[
        make_dataclass(
            "route_rules",
            [
                ("network_entity_id", str),
                ("cidr_block", str, field(default=None)),
                ("description", str, field(default=None)),
                ("destination", str, field(default=None)),
                ("destination_type", str, field(default=None)),
                ("route_type", str, field(default=None)),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    UpdateRouteTable
        Updates the specified route table's display name or route rules.
    Avoid entering confidential information.

    Note that the `routeRules` object you provide replaces the entire existing set of rules.

    Args:
        rt_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        route_rules(List[dict[str, Any]], Optional):
            The collection of rules used for routing destination IPs to network devices.
            Defaults to None.

            * cidr_block (str, Optional):
                Deprecated. Instead use `destination` and `destinationType`. Requests that include both
                `cidrBlock` and `destination` will be rejected.

                A destination IP address range in CIDR notation. Matching packets will
                be routed to the indicated network entity (the target).

                Cannot be an IPv6 prefix.

                Example: `0.0.0.0/0`
                Defaults to None.

            * description (str, Optional):
                An optional description of your choice for the rule.
                Defaults to None.

            * destination (str, Optional):
                Conceptually, this is the range of IP addresses used for matching when routing
                traffic. Required if you provide a `destinationType`.

                Allowed values:

                  * IP address range in CIDR notation. Can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24`
                  or `2001:0db8:0123:45::/56`. If you set this to an IPv6 prefix, the route rule's target
                  can only be a DRG or internet gateway.
                  IPv6 addressing is supported for all commercial and government regions.
                  See [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a route rule for traffic destined for a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.
                Defaults to None.

            * destination_type (str, Optional):
                Type of destination for the rule. Required if you provide a `destination`.

                  * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                    particular `Service` through a service gateway).
                Defaults to None.

            * network_entity_id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the route rule's target. For information about the type of
                targets you can specify, see
                [Route Tables](/iaas/Content/Network/Tasks/managingroutetables.htm).


            * route_type (str, Optional):
                A route rule can be STATIC if manually added to the route table, LOCAL if added by OCI to the route table.
                Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "route_rules": "routeRules",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/routeTables/{rtId}".format(**{"rtId": rt_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "routeRules": "route_rules",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_route_table(
    hub, ctx, rt_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteRouteTable
        Deletes the specified route table, but only if it's not associated with a subnet. You can't delete a
    VCN's default route table.

    This is an asynchronous operation. The route table's `lifecycleState` will change to TERMINATING temporarily
    until the route table is completely removed.

    Args:
        rt_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/routeTables/{rtId}".format(**{"rtId": rt_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_route_table_compartment(
    hub,
    ctx,
    rt_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeRouteTableCompartment
        Moves a route table into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        rt_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            route table to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/routeTables/{rtId}/actions/changeCompartment".format(**{"rtId": rt_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_security_lists(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    vcn_id: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListSecurityLists
        Lists the security lists in the specified VCN and compartment.
    If the VCN ID is not provided, then the list includes the security lists from all VCNs in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to only return resources that match the given lifecycle
            state. The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/securityLists".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "vcnId": vcn_id,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_security_list(
    hub,
    ctx,
    compartment_id: str,
    egress_security_rules: List[
        make_dataclass(
            "egress_security_rules",
            [
                ("destination", str),
                ("protocol", str),
                ("description", str, field(default=None)),
                ("destination_type", str, field(default=None)),
                (
                    "icmp_options",
                    make_dataclass(
                        "icmp_options",
                        [("type", int), ("code", int, field(default=None))],
                    ),
                    field(default=None),
                ),
                ("is_stateless", bool, field(default=None)),
                (
                    "tcp_options",
                    make_dataclass(
                        "tcp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "udp_options",
                    make_dataclass(
                        "udp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ],
    ingress_security_rules: List[
        make_dataclass(
            "ingress_security_rules",
            [
                ("protocol", str),
                ("source", str),
                ("description", str, field(default=None)),
                (
                    "icmp_options",
                    make_dataclass(
                        "icmp_options",
                        [("type", int), ("code", int, field(default=None))],
                    ),
                    field(default=None),
                ),
                ("is_stateless", bool, field(default=None)),
                ("source_type", str, field(default=None)),
                (
                    "tcp_options",
                    make_dataclass(
                        "tcp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "udp_options",
                    make_dataclass(
                        "udp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ],
    vcn_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    CreateSecurityList
        Creates a new security list for the specified VCN. For more information
    about security lists, see [Security Lists](/iaas/Content/Network/Concepts/securitylists.htm).
    For information on the number of rules you can have in a security list, see
    [Service Limits](/iaas/Content/General/Concepts/servicelimits.htm).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want the security
    list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets,
    or other Networking Service components. If you're not sure which compartment to use, put the security
    list in the same compartment as the VCN. For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
    [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the security list, otherwise a default is provided.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the security list.

        egress_security_rules(List[dict[str, Any]]):
            Rules for allowing egress IP packets.

            * description (str, Optional):
                An optional description of your choice for the rule.
                Defaults to None.

            * destination (str):
                Conceptually, this is the range of IP addresses that a packet originating from the instance
                can go to.

                Allowed values:

                  * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                    Note that IPv6 addressing is currently supported only in certain regions. See
                    [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a security list rule for traffic destined for a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.


            * destination_type (str, Optional):
                Type of destination for the rule. The default is `CIDR_BLOCK`.

                Allowed values:

                  * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                    particular `Service` through a service gateway).
                Defaults to None.

            * icmp_options (dict[str, Any], Optional):
                icmpOptions. Defaults to None.

                * code (int, Optional):
                    The ICMP code (optional). Defaults to None.

                * type (int):
                    The ICMP type.

            * is_stateless (bool, Optional):
                A stateless rule allows traffic in one direction. Remember to add a corresponding
                stateless rule in the other direction if you need to support bidirectional traffic. For
                example, if egress traffic allows TCP destination port 80, there should be an ingress
                rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                and a corresponding rule is not necessary for bidirectional traffic.
                Defaults to None.

            * protocol (str):
                The transport protocol. Specify either `all` or an IPv4 protocol number as
                defined in
                [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                Options are supported only for ICMP ("1"), TCP ("6"), UDP ("17"), and ICMPv6 ("58").


            * tcp_options (dict[str, Any], Optional):
                tcpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


            * udp_options (dict[str, Any], Optional):
                udpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


        ingress_security_rules(List[dict[str, Any]]):
            Rules for allowing ingress IP packets.

            * description (str, Optional):
                An optional description of your choice for the rule.
                Defaults to None.

            * icmp_options (dict[str, Any], Optional):
                icmpOptions. Defaults to None.

                * code (int, Optional):
                    The ICMP code (optional). Defaults to None.

                * type (int):
                    The ICMP type.

            * is_stateless (bool, Optional):
                A stateless rule allows traffic in one direction. Remember to add a corresponding
                stateless rule in the other direction if you need to support bidirectional traffic. For
                example, if ingress traffic allows TCP destination port 80, there should be an egress
                rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                and a corresponding rule is not necessary for bidirectional traffic.
                Defaults to None.

            * protocol (str):
                The transport protocol. Specify either `all` or an IPv4 protocol number as
                defined in
                [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                Options are supported only for ICMP ("1"), TCP ("6"), UDP ("17"), and ICMPv6 ("58").


            * source (str):
                Conceptually, this is the range of IP addresses that a packet coming into the instance
                can come from.

                Allowed values:

                  * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
                    IPv6 addressing is supported for all commercial and government regions. See
                    [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a security list rule for traffic coming from a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.


            * source_type (str, Optional):
                Type of source for the rule. The default is `CIDR_BLOCK`.

                  * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic coming from a
                    particular `Service` through a service gateway).
                Defaults to None.

            * tcp_options (dict[str, Any], Optional):
                tcpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


            * udp_options (dict[str, Any], Optional):
                udpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN the security list belongs to.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "egress_security_rules": "egressSecurityRules",
        "freeform_tags": "freeformTags",
        "ingress_security_rules": "ingressSecurityRules",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/securityLists".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "egressSecurityRules": "egress_security_rules",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ingressSecurityRules": "ingress_security_rules",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_security_list(hub, ctx, security_list_id: str) -> Dict[str, Any]:
    r"""

    GetSecurityList
        Gets the specified security list's information.

    Args:
        security_list_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the security list.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/securityLists/{securityListId}".format(
            **{"securityListId": security_list_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "egressSecurityRules": "egress_security_rules",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ingressSecurityRules": "ingress_security_rules",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_security_list(
    hub,
    ctx,
    security_list_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    egress_security_rules: List[
        make_dataclass(
            "egress_security_rules",
            [
                ("destination", str),
                ("protocol", str),
                ("description", str, field(default=None)),
                ("destination_type", str, field(default=None)),
                (
                    "icmp_options",
                    make_dataclass(
                        "icmp_options",
                        [("type", int), ("code", int, field(default=None))],
                    ),
                    field(default=None),
                ),
                ("is_stateless", bool, field(default=None)),
                (
                    "tcp_options",
                    make_dataclass(
                        "tcp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "udp_options",
                    make_dataclass(
                        "udp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ] = None,
    freeform_tags: Dict = None,
    ingress_security_rules: List[
        make_dataclass(
            "ingress_security_rules",
            [
                ("protocol", str),
                ("source", str),
                ("description", str, field(default=None)),
                (
                    "icmp_options",
                    make_dataclass(
                        "icmp_options",
                        [("type", int), ("code", int, field(default=None))],
                    ),
                    field(default=None),
                ),
                ("is_stateless", bool, field(default=None)),
                ("source_type", str, field(default=None)),
                (
                    "tcp_options",
                    make_dataclass(
                        "tcp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "udp_options",
                    make_dataclass(
                        "udp_options",
                        [
                            (
                                "destination_port_range",
                                make_dataclass(
                                    "destination_port_range",
                                    [("max", int), ("min", int)],
                                ),
                                field(default=None),
                            ),
                            (
                                "source_port_range",
                                make_dataclass(
                                    "source_port_range", [("max", int), ("min", int)]
                                ),
                                field(default=None),
                            ),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    UpdateSecurityList
        Updates the specified security list's display name or rules.
    Avoid entering confidential information.

    Note that the `egressSecurityRules` or `ingressSecurityRules` objects you provide replace the entire
    existing objects.

    Args:
        security_list_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the security list.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        egress_security_rules(List[dict[str, Any]], Optional):
            Rules for allowing egress IP packets. Defaults to None.

            * description (str, Optional):
                An optional description of your choice for the rule.
                Defaults to None.

            * destination (str):
                Conceptually, this is the range of IP addresses that a packet originating from the instance
                can go to.

                Allowed values:

                  * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                    Note that IPv6 addressing is currently supported only in certain regions. See
                    [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a security list rule for traffic destined for a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.


            * destination_type (str, Optional):
                Type of destination for the rule. The default is `CIDR_BLOCK`.

                Allowed values:

                  * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                    particular `Service` through a service gateway).
                Defaults to None.

            * icmp_options (dict[str, Any], Optional):
                icmpOptions. Defaults to None.

                * code (int, Optional):
                    The ICMP code (optional). Defaults to None.

                * type (int):
                    The ICMP type.

            * is_stateless (bool, Optional):
                A stateless rule allows traffic in one direction. Remember to add a corresponding
                stateless rule in the other direction if you need to support bidirectional traffic. For
                example, if egress traffic allows TCP destination port 80, there should be an ingress
                rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                and a corresponding rule is not necessary for bidirectional traffic.
                Defaults to None.

            * protocol (str):
                The transport protocol. Specify either `all` or an IPv4 protocol number as
                defined in
                [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                Options are supported only for ICMP ("1"), TCP ("6"), UDP ("17"), and ICMPv6 ("58").


            * tcp_options (dict[str, Any], Optional):
                tcpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


            * udp_options (dict[str, Any], Optional):
                udpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        ingress_security_rules(List[dict[str, Any]], Optional):
            Rules for allowing ingress IP packets. Defaults to None.

            * description (str, Optional):
                An optional description of your choice for the rule.
                Defaults to None.

            * icmp_options (dict[str, Any], Optional):
                icmpOptions. Defaults to None.

                * code (int, Optional):
                    The ICMP code (optional). Defaults to None.

                * type (int):
                    The ICMP type.

            * is_stateless (bool, Optional):
                A stateless rule allows traffic in one direction. Remember to add a corresponding
                stateless rule in the other direction if you need to support bidirectional traffic. For
                example, if ingress traffic allows TCP destination port 80, there should be an egress
                rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                and a corresponding rule is not necessary for bidirectional traffic.
                Defaults to None.

            * protocol (str):
                The transport protocol. Specify either `all` or an IPv4 protocol number as
                defined in
                [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                Options are supported only for ICMP ("1"), TCP ("6"), UDP ("17"), and ICMPv6 ("58").


            * source (str):
                Conceptually, this is the range of IP addresses that a packet coming into the instance
                can come from.

                Allowed values:

                  * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
                    IPv6 addressing is supported for all commercial and government regions. See
                    [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                  * The `cidrBlock` value for a [Service](#/en/iaas/latest/Service/), if you're
                    setting up a security list rule for traffic coming from a particular `Service` through
                    a service gateway. For example: `oci-phx-objectstorage`.


            * source_type (str, Optional):
                Type of source for the rule. The default is `CIDR_BLOCK`.

                  * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

                  * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
                    [Service](#/en/iaas/latest/Service/) (the rule is for traffic coming from a
                    particular `Service` through a service gateway).
                Defaults to None.

            * tcp_options (dict[str, Any], Optional):
                tcpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


            * udp_options (dict[str, Any], Optional):
                udpOptions. Defaults to None.

                * destination_port_range (dict[str, Any], Optional):
                    destinationPortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.


                * source_port_range (dict[str, Any], Optional):
                    sourcePortRange. Defaults to None.

                    * max (int):
                        The maximum port number, which must not be less than the minimum port number. To specify
                        a single port number, set both the min and max to the same value.


                    * min (int):
                        The minimum port number, which must not be greater than the maximum port number.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "egress_security_rules": "egressSecurityRules",
        "freeform_tags": "freeformTags",
        "ingress_security_rules": "ingressSecurityRules",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/securityLists/{securityListId}".format(
            **{"securityListId": security_list_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "egressSecurityRules": "egress_security_rules",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ingressSecurityRules": "ingress_security_rules",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_security_list(
    hub, ctx, security_list_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteSecurityList
        Deletes the specified security list, but only if it's not associated with a subnet. You can't delete
    a VCN's default security list.

    This is an asynchronous operation. The security list's `lifecycleState` will change to TERMINATING temporarily
    until the security list is completely removed.

    Args:
        security_list_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the security list.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/securityLists/{securityListId}".format(
            **{"securityListId": security_list_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_security_list_compartment(
    hub,
    ctx,
    security_list_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeSecurityListCompartment
        Moves a security list into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        security_list_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the security list.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            security list to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/securityLists/{securityListId}/actions/changeCompartment".format(
            **{"securityListId": security_list_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_service_gateways(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListServiceGateways
        Lists the service gateways in the specified compartment. You may optionally specify a VCN OCID
    to filter the results by VCN.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the given lifecycle
            state. The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/serviceGateways".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_service_gateway(
    hub,
    ctx,
    compartment_id: str,
    services: List[make_dataclass("services", [("service_id", str)])],
    vcn_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    route_table_id: str = None,
) -> Dict[str, Any]:
    r"""

    CreateServiceGateway
        Creates a new service gateway in the specified compartment.

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want
    the service gateway to reside. For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).
    For information about OCIDs, see [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the service gateway, otherwise a default is provided.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    Args:
        compartment_id(str):
            The [OCID] (/Content/General/Concepts/identifiers.htm) of the compartment to contain the service gateway.


        services(List[dict[str, Any]]):
            List of the OCIDs of the [Service](#/en/iaas/latest/Service/) objects to
            enable for the service gateway. This list can be empty if you don't want to enable any
            `Service` objects when you create the gateway. You can enable a `Service`
            object later by using either [AttachServiceId](#/en/iaas/latest/ServiceGateway/AttachServiceId)
            or [UpdateServiceGateway](#/en/iaas/latest/ServiceGateway/UpdateServiceGateway).

            For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock`
            as the rule's destination and the service gateway as the rule's target. See
            [Route Table](#/en/iaas/latest/RouteTable/).


            * service_id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the [Service](#/en/iaas/latest/Service/).


        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the service gateway will use.

            If you don't specify a route table here, the service gateway is created without an associated route
            table. The Networking service does NOT automatically associate the attached VCN's default route table
            with the service gateway.

            For information about why you would associate a route table with a service gateway, see
            [Transit Routing: Private Access to Oracle Services](/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "route_table_id": "routeTableId",
        "services": "services",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/serviceGateways".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "blockTraffic": "block_traffic",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "routeTableId": "route_table_id",
            "services": "services",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_service_gateway(hub, ctx, service_gateway_id: str) -> Dict[str, Any]:
    r"""

    GetServiceGateway
        Gets the specified service gateway's information.

    Args:
        service_gateway_id(str):
            The service gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/serviceGateways/{serviceGatewayId}".format(
            **{"serviceGatewayId": service_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "blockTraffic": "block_traffic",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "routeTableId": "route_table_id",
            "services": "services",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_service_gateway(
    hub,
    ctx,
    service_gateway_id: str,
    if_match: str = None,
    block_traffic: bool = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    route_table_id: str = None,
    services: List[make_dataclass("services", [("service_id", str)])] = None,
) -> Dict[str, Any]:
    r"""

    UpdateServiceGateway
        Updates the specified service gateway. The information you provide overwrites the existing
    attributes of the gateway.

    Args:
        service_gateway_id(str):
            The service gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        block_traffic(bool, Optional):
            Whether the service gateway blocks all traffic through it. The default is `false`. When
            this is `true`, traffic is not routed to any services, regardless of route rules.

            Example: `true`
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the service gateway will use.
            For information about why you would associate a route table with a service gateway, see
            [Transit Routing: Private Access to Oracle Services](/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).
            Defaults to None.

        services(List[dict[str, Any]], Optional):
            List of all the `Service` objects you want enabled on this service gateway. Sending an empty list
            means you want to disable all services. Omitting this parameter entirely keeps the
            existing list of services intact.

            You can also enable or disable a particular `Service` by using
            [AttachServiceId](#/en/iaas/latest/ServiceGateway/AttachServiceId) or
            [DetachServiceId](#/en/iaas/latest/ServiceGateway/DetachServiceId).

            For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock`
            as the rule's destination and the service gateway as the rule's target. See
            [Route Table](#/en/iaas/latest/RouteTable/).
            Defaults to None.

            * service_id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the [Service](#/en/iaas/latest/Service/).

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "block_traffic": "blockTraffic",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "route_table_id": "routeTableId",
        "services": "services",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/serviceGateways/{serviceGatewayId}".format(
            **{"serviceGatewayId": service_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "blockTraffic": "block_traffic",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "routeTableId": "route_table_id",
            "services": "services",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_service_gateway(
    hub, ctx, service_gateway_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteServiceGateway
        Deletes the specified service gateway. There must not be a route table that lists the service
    gateway as a target.

    Args:
        service_gateway_id(str):
            The service gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/serviceGateways/{serviceGatewayId}".format(
            **{"serviceGatewayId": service_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def attach_service_id(
    hub, ctx, service_gateway_id: str, service_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    AttachService
        Adds the specified [Service](#/en/iaas/latest/Service/) to the list of enabled
    `Service` objects for the specified gateway. You must also set up a route rule with the
    `cidrBlock` of the `Service` as the rule's destination and the service gateway as the rule's
    target. See [Route Table](#/en/iaas/latest/RouteTable/).

    **Note:** The `AttachServiceId` operation is an easy way to add an individual `Service` to
    the service gateway. Compare it with
    [UpdateServiceGateway](#/en/iaas/latest/ServiceGateway/UpdateServiceGateway), which replaces
    the entire existing list of enabled `Service` objects with the list that you provide in the
    `Update` call.

    Args:
        service_gateway_id(str):
            The service gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

        service_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the [Service](#/en/iaas/latest/Service/).


        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"service_id": "serviceId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/serviceGateways/{serviceGatewayId}/actions/attachService".format(
            **{"serviceGatewayId": service_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "blockTraffic": "block_traffic",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "routeTableId": "route_table_id",
            "services": "services",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def change_service_gateway_compartment(
    hub,
    ctx,
    service_gateway_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeServiceGatewayCompartment
        Moves a service gateway into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        service_gateway_id(str):
            The service gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            service gateway to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/serviceGateways/{serviceGatewayId}/actions/changeCompartment".format(
            **{"serviceGatewayId": service_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def detach_service_id(
    hub, ctx, service_gateway_id: str, service_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DetachService
        Removes the specified [Service](#/en/iaas/latest/Service/) from the list of enabled
    `Service` objects for the specified gateway. You do not need to remove any route
    rules that specify this `Service` object's `cidrBlock` as the destination CIDR. However, consider
    removing the rules if your intent is to permanently disable use of the `Service` through this
    service gateway.

    **Note:** The `DetachServiceId` operation is an easy way to remove an individual `Service` from
    the service gateway. Compare it with
    [UpdateServiceGateway](#/en/iaas/latest/ServiceGateway/UpdateServiceGateway), which replaces
    the entire existing list of enabled `Service` objects with the list that you provide in the
    `Update` call. `UpdateServiceGateway` also lets you block all traffic through the service
    gateway without having to remove each of the individual `Service` objects.

    Args:
        service_gateway_id(str):
            The service gateway's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

        service_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the [Service](#/en/iaas/latest/Service/).


        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"service_id": "serviceId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/serviceGateways/{serviceGatewayId}/actions/detachService".format(
            **{"serviceGatewayId": service_gateway_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "blockTraffic": "block_traffic",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "routeTableId": "route_table_id",
            "services": "services",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_services(
    hub, ctx, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListServices
        Lists the available [Service](#/en/iaas/latest/Service/) objects that you can enable for a
    service gateway in this region.

    Args:
        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/services".format(**{}),
        query_params={"limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_service(hub, ctx, service_id: str) -> Dict[str, Any]:
    r"""

    GetService
        Gets the specified [Service](#/en/iaas/latest/Service/) object.

    Args:
        service_id(str):
            The service's [OCID](/iaas/Content/General/Concepts/identifiers.htm).

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/services/{serviceId}".format(**{"serviceId": service_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "cidrBlock": "cidr_block",
            "description": "description",
            "id": "id",
            "name": "name",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_subnet_topology(
    hub,
    ctx,
    compartment_id: str,
    subnet_id: str,
    access_level: str = None,
    query_compartment_subtree: bool = None,
    opc_request_id: str = None,
    if_none_match: str = None,
    cache_control: str = None,
) -> Dict[str, Any]:
    r"""

    Get virtual network subnet topology
        Gets a topology for a given subnet.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        subnet_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet.

        access_level(str, Optional):
            Valid values are `ANY` and `ACCESSIBLE`. The default is `ANY`.
            Setting this to `ACCESSIBLE` returns only compartments for which a
            user has INSPECT permissions, either directly or indirectly (permissions can be on a
            resource in a subcompartment). A restricted set of fields is returned for compartments in which a user has
            indirect INSPECT permissions.

            When set to `ANY` permissions are not checked.
            Defaults to None.

        query_compartment_subtree(bool, Optional):
            When set to true, the hierarchy of compartments is traversed
            and the specified compartment and its subcompartments are
            inspected depending on the the setting of `accessLevel`.
            Default is false.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        if_none_match(str, Optional):
            For querying if there is a cached value on the server. The If-None-Match HTTP request header
            makes the request conditional. For GET and HEAD methods, the server will send back the requested
            resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            For other methods, the request will be processed only if the eventually existing resource's
            ETag doesn't match any of the values listed.
            Defaults to None.

        cache_control(str, Optional):
            The Cache-Control HTTP header holds directives (instructions)
            for caching in both requests and responses.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/subnetTopology".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "accessLevel": access_level,
            "queryCompartmentSubtree": query_compartment_subtree,
            "subnetId": subnet_id,
        },
        data=payload,
        headers={
            "opc-request-id": opc_request_id,
            "if-none-match": if_none_match,
            "cache-control": cache_control,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "entities": "entities",
            "limitedEntities": "limited_entities",
            "relationships": "relationships",
            "subnetId": "subnet_id",
            "timeCreated": "time_created",
            "type": "type",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_subnets(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    vcn_id: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListSubnets
        Lists the subnets in the specified VCN and the specified compartment.
    If the VCN ID is not provided, then the list includes the subnets from all VCNs in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to only return resources that match the given lifecycle
            state. The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/subnets".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "vcnId": vcn_id,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_subnet(
    hub,
    ctx,
    cidr_block: str,
    compartment_id: str,
    vcn_id: str,
    opc_retry_token: str = None,
    availability_domain: str = None,
    defined_tags: Dict = None,
    dhcp_options_id: str = None,
    display_name: str = None,
    dns_label: str = None,
    freeform_tags: Dict = None,
    ipv6_cidr_block: str = None,
    ipv6_cidr_blocks: List[str] = None,
    prohibit_public_ip_on_vnic: bool = None,
    route_table_id: str = None,
    security_list_ids: List[str] = None,
) -> Dict[str, Any]:
    r"""

    CreateSubnet
        Creates a new subnet in the specified VCN. You can't change the size of the subnet after creation,
    so it's important to think about the size of subnets you need before creating them.
    For more information, see [VCNs and Subnets](/iaas/Content/Network/Tasks/managingVCNs.htm).
    For information on the number of subnets you can have in a VCN, see
    [Service Limits](/iaas/Content/General/Concepts/servicelimits.htm).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want the subnet
    to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or
    other Networking Service components. If you're not sure which compartment to use, put the subnet in
    the same compartment as the VCN. For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs,
    see [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally associate a route table with the subnet. If you don't, the subnet will use the
    VCN's default route table. For more information about route tables, see
    [Route Tables](/iaas/Content/Network/Tasks/managingroutetables.htm).

    You may optionally associate a security list with the subnet. If you don't, the subnet will use the
    VCN's default security list. For more information about security lists, see
    [Security Lists](/iaas/Content/Network/Concepts/securitylists.htm).

    You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the
    VCN's default set. For more information about DHCP options, see
    [DHCP Options](/iaas/Content/Network/Tasks/managingDHCP.htm).

    You may optionally specify a *display name* for the subnet, otherwise a default is provided.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    You can also add a DNS label for the subnet, which is required if you want the Internet and
    VCN Resolver to resolve hostnames for instances in the subnet. For more information, see
    [DNS in Your Virtual Cloud Network](/iaas/Content/Network/Concepts/dns.htm).

    Args:
        cidr_block(str):
            The CIDR IP address range of the subnet. The CIDR must maintain the following rules -

            a. The CIDR block is valid and correctly formatted.
            b. The new range is within one of the parent VCN ranges.

            Example: `10.0.1.0/24`


        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the subnet.

        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN to contain the subnet.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        availability_domain(str, Optional):
            Controls whether the subnet is regional or specific to an availability domain. Oracle
            recommends creating regional subnets because they're more flexible and make it easier to
            implement failover across availability domains. Originally, AD-specific subnets were the
            only kind available to use.

            To create a regional subnet, omit this attribute. Then any resources later created in this
            subnet (such as a Compute instance) can be created in any availability domain in the region.

            To instead create an AD-specific subnet, set this attribute to the availability domain you
            want this subnet to be in. Then any resources later created in this subnet can only be
            created in that availability domain.

            Example: `Uocm:PHX-AD-1`
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        dhcp_options_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the set of DHCP options the subnet will use. If you don't
            provide a value, the subnet uses the VCN's default set of DHCP options.
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        dns_label(str, Optional):
            A DNS label for the subnet, used in conjunction with the VNIC's hostname and
            VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC
            within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`).
            Must be an alphanumeric string that begins with a letter and is unique within the VCN.
            The value cannot be changed.

            This value must be set if you want to use the Internet and VCN Resolver to resolve the
            hostnames of instances in the subnet. It can only be set if the VCN itself
            was created with a DNS label.

            For more information, see
            [DNS in Your Virtual Cloud Network](/iaas/Content/Network/Concepts/dns.htm).

            Example: `subnet123`
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        ipv6_cidr_block(str, Optional):
            Use this to enable IPv6 addressing for this subnet. The VCN must be enabled for IPv6.
            You can't change this subnet characteristic later. All subnets are /64 in size. The subnet
            portion of the IPv6 address is the fourth hextet from the left (1111 in the following example).

            For important details about IPv6 addressing in a VCN, see [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

            Example: `2001:0db8:0123:1111::/64`
            Defaults to None.

        ipv6_cidr_blocks(List[str], Optional):
            The list of all IPv6 prefixes (Oracle allocated IPv6 GUA, ULA or private IPv6 prefixes, BYOIPv6 prefixes) for the subnet that meets the following criteria:
            - The prefixes must be valid.
            - Multiple prefixes must not overlap each other or the on-premises network prefix.
            - The number of prefixes must not exceed the limit of IPv6 prefixes allowed to a subnet.
            Defaults to None.

        prohibit_public_ip_on_vnic(bool, Optional):
            Whether VNICs within this subnet can have public IP addresses.
            Defaults to false, which means VNICs created in this subnet will
            automatically be assigned public IP addresses unless specified
            otherwise during instance launch or VNIC creation (with the
            `assignPublicIp` flag in [CreateVnicDetails](#/en/iaas/latest/CreateVnicDetails/)).
            If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
            subnet cannot have public IP addresses (that is, it's a private
            subnet).

            For IPv6, if `prohibitPublicIpOnVnic` is set to `true`, internet access is not allowed for any
            IPv6s assigned to VNICs in the subnet.

            Example: `true`
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the subnet will use. If you don't provide a value,
            the subnet uses the VCN's default route table.
            Defaults to None.

        security_list_ids(List[str], Optional):
            The OCIDs of the security list or lists the subnet will use. If you don't
            provide a value, the subnet uses the VCN's default security list.
            Remember that security lists are associated *with the subnet*, but the
            rules are applied to the individual VNICs in the subnet.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "availability_domain": "availabilityDomain",
        "cidr_block": "cidrBlock",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "dhcp_options_id": "dhcpOptionsId",
        "display_name": "displayName",
        "dns_label": "dnsLabel",
        "freeform_tags": "freeformTags",
        "ipv6_cidr_block": "ipv6CidrBlock",
        "ipv6_cidr_blocks": "ipv6CidrBlocks",
        "prohibit_public_ip_on_vnic": "prohibitPublicIpOnVnic",
        "route_table_id": "routeTableId",
        "security_list_ids": "securityListIds",
        "vcn_id": "vcnId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/subnets".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "cidrBlock": "cidr_block",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "dhcpOptionsId": "dhcp_options_id",
            "displayName": "display_name",
            "dnsLabel": "dns_label",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipv6CidrBlock": "ipv6_cidr_block",
            "ipv6CidrBlocks": "ipv6_cidr_blocks",
            "ipv6PublicCidrBlock": "ipv6_public_cidr_block",
            "ipv6VirtualRouterIp": "ipv6_virtual_router_ip",
            "lifecycleState": "lifecycle_state",
            "prohibitPublicIpOnVnic": "prohibit_public_ip_on_vnic",
            "routeTableId": "route_table_id",
            "securityListIds": "security_list_ids",
            "subnetDomainName": "subnet_domain_name",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
            "virtualRouterIp": "virtual_router_ip",
            "virtualRouterMac": "virtual_router_mac",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_subnet(hub, ctx, subnet_id: str) -> Dict[str, Any]:
    r"""

    GetSubnet
        Gets the specified subnet's information.

    Args:
        subnet_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/subnets/{subnetId}".format(**{"subnetId": subnet_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "cidrBlock": "cidr_block",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "dhcpOptionsId": "dhcp_options_id",
            "displayName": "display_name",
            "dnsLabel": "dns_label",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipv6CidrBlock": "ipv6_cidr_block",
            "ipv6CidrBlocks": "ipv6_cidr_blocks",
            "ipv6PublicCidrBlock": "ipv6_public_cidr_block",
            "ipv6VirtualRouterIp": "ipv6_virtual_router_ip",
            "lifecycleState": "lifecycle_state",
            "prohibitPublicIpOnVnic": "prohibit_public_ip_on_vnic",
            "routeTableId": "route_table_id",
            "securityListIds": "security_list_ids",
            "subnetDomainName": "subnet_domain_name",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
            "virtualRouterIp": "virtual_router_ip",
            "virtualRouterMac": "virtual_router_mac",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_subnet(
    hub,
    ctx,
    subnet_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    dhcp_options_id: str = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    ipv6_cidr_block: str = None,
    ipv6_cidr_blocks: List[str] = None,
    route_table_id: str = None,
    security_list_ids: List[str] = None,
) -> Dict[str, Any]:
    r"""

    UpdateSubnet
        Updates the specified subnet.

    Args:
        subnet_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        dhcp_options_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the set of DHCP options the subnet will use.
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        ipv6_cidr_block(str, Optional):
            This is the IPv6 prefix for the subnet's private IP address space.
            The subnet size is always /64.
            See [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).
            The provided prefix must maintain the following rules -

            a. The IPv6 prefix is valid and correctly formatted.
            b. The IPv6 prefix is within the parent VCN IPv6 range.

            Example: `2001:0db8:0123:1111::/64`
            Defaults to None.

        ipv6_cidr_blocks(List[str], Optional):
            The list of all IPv6 prefixes (Oracle allocated IPv6 GUA, ULA or private IPv6 prefix, BYOIPv6 prefixes) for the subnet that meets the following criteria:
            - The prefixes must be valid.
            - Multiple prefixes must not overlap each other or the on-premises network prefix.
            - The number of prefixes must not exceed the limit of IPv6 prefixes allowed to a subnet.
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the subnet will use.
            Defaults to None.

        security_list_ids(List[str], Optional):
            The OCIDs of the security list or lists the subnet will use. This
            replaces the entire current set of security lists. Remember that
            security lists are associated *with the subnet*, but the rules are
            applied to the individual VNICs in the subnet.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "dhcp_options_id": "dhcpOptionsId",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "ipv6_cidr_block": "ipv6CidrBlock",
        "ipv6_cidr_blocks": "ipv6CidrBlocks",
        "route_table_id": "routeTableId",
        "security_list_ids": "securityListIds",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/subnets/{subnetId}".format(**{"subnetId": subnet_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "cidrBlock": "cidr_block",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "dhcpOptionsId": "dhcp_options_id",
            "displayName": "display_name",
            "dnsLabel": "dns_label",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipv6CidrBlock": "ipv6_cidr_block",
            "ipv6CidrBlocks": "ipv6_cidr_blocks",
            "ipv6PublicCidrBlock": "ipv6_public_cidr_block",
            "ipv6VirtualRouterIp": "ipv6_virtual_router_ip",
            "lifecycleState": "lifecycle_state",
            "prohibitPublicIpOnVnic": "prohibit_public_ip_on_vnic",
            "routeTableId": "route_table_id",
            "securityListIds": "security_list_ids",
            "subnetDomainName": "subnet_domain_name",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
            "virtualRouterIp": "virtual_router_ip",
            "virtualRouterMac": "virtual_router_mac",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_subnet(
    hub, ctx, subnet_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteSubnet
        Deletes the specified subnet, but only if there are no instances in the subnet. This is an asynchronous
    operation. The subnet's `lifecycleState` will change to TERMINATING temporarily. If there are any
    instances in the subnet, the state will instead change back to AVAILABLE.

    Args:
        subnet_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/subnets/{subnetId}".format(**{"subnetId": subnet_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def add_ipv6_subnet_cidr(
    hub,
    ctx,
    subnet_id: str,
    ipv6_cidr_block: str,
    opc_retry_token: str = None,
    if_match: str = None,
    opc_request_id: str = None,
) -> Dict[str, Any]:
    r"""

    AddIpv6SubnetCidr
        Add an IPv6 prefix to a subnet.

    Args:
        subnet_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet.

        ipv6_cidr_block(str):
            This field is not required and should only be specified when adding an IPv6 prefix
            to a subnet's IPv6 address space.
            See[IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

            Example: `2001:0db8:0123::/64`


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"ipv6_cidr_block": "ipv6CidrBlock"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/subnets/{subnetId}/actions/addIpv6Cidr".format(
            **{"subnetId": subnet_id}
        ),
        query_params={},
        data=payload,
        headers={
            "opc-retry-token": opc_retry_token,
            "if-match": if_match,
            "opc-request-id": opc_request_id,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_subnet_compartment(
    hub,
    ctx,
    subnet_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeSubnetCompartment
        Moves a subnet into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        subnet_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            subnet to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/subnets/{subnetId}/actions/changeCompartment".format(
            **{"subnetId": subnet_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def remove_ipv6_subnet_cidr(
    hub,
    ctx,
    subnet_id: str,
    ipv6_cidr_block: str,
    opc_retry_token: str = None,
    if_match: str = None,
    opc_request_id: str = None,
) -> Dict[str, Any]:
    r"""

    RemoveIpv6SubnetCidr
        Remove an IPv6 prefix from a subnet. At least one IPv6 CIDR should remain.

    Args:
        subnet_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet.

        ipv6_cidr_block(str):
            This field is not required and should only be specified when removing an IPv6 prefix
            from a subnet's IPv6 address space.
            See[IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

            Example: `2001:0db8:0123::/64`


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"ipv6_cidr_block": "ipv6CidrBlock"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/subnets/{subnetId}/actions/removeIpv6Cidr".format(
            **{"subnetId": subnet_id}
        ),
        query_params={},
        data=payload,
        headers={
            "opc-retry-token": opc_retry_token,
            "if-match": if_match,
            "opc-request-id": opc_request_id,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_vcn_topology(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str,
    access_level: str = None,
    query_compartment_subtree: bool = None,
    opc_request_id: str = None,
    if_none_match: str = None,
    cache_control: str = None,
) -> Dict[str, Any]:
    r"""

    Get Virtual Network VCN topology
        Gets a virtual network topology for a given VCN.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        access_level(str, Optional):
            Valid values are `ANY` and `ACCESSIBLE`. The default is `ANY`.
            Setting this to `ACCESSIBLE` returns only compartments for which a
            user has INSPECT permissions, either directly or indirectly (permissions can be on a
            resource in a subcompartment). A restricted set of fields is returned for compartments in which a user has
            indirect INSPECT permissions.

            When set to `ANY` permissions are not checked.
            Defaults to None.

        query_compartment_subtree(bool, Optional):
            When set to true, the hierarchy of compartments is traversed
            and the specified compartment and its subcompartments are
            inspected depending on the the setting of `accessLevel`.
            Default is false.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        if_none_match(str, Optional):
            For querying if there is a cached value on the server. The If-None-Match HTTP request header
            makes the request conditional. For GET and HEAD methods, the server will send back the requested
            resource, with a 200 status, only if it doesn't have an ETag matching the given ones.
            For other methods, the request will be processed only if the eventually existing resource's
            ETag doesn't match any of the values listed.
            Defaults to None.

        cache_control(str, Optional):
            The Cache-Control HTTP header holds directives (instructions)
            for caching in both requests and responses.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vcnTopology".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "accessLevel": access_level,
            "queryCompartmentSubtree": query_compartment_subtree,
            "vcnId": vcn_id,
        },
        data=payload,
        headers={
            "opc-request-id": opc_request_id,
            "if-none-match": if_none_match,
            "cache-control": cache_control,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "entities": "entities",
            "limitedEntities": "limited_entities",
            "relationships": "relationships",
            "timeCreated": "time_created",
            "type": "type",
            "vcnId": "vcn_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_vcns(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListVcns
        Lists the virtual cloud networks (VCNs) in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to only return resources that match the given lifecycle
            state. The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vcns".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_vcn(
    hub,
    ctx,
    compartment_id: str,
    opc_retry_token: str = None,
    byoipv6_cidr_details: List[
        make_dataclass(
            "byoipv6_cidr_details",
            [("byoipv6_range_id", str), ("ipv6_cidr_block", str)],
        )
    ] = None,
    cidr_block: str = None,
    cidr_blocks: List[str] = None,
    defined_tags: Dict = None,
    display_name: str = None,
    dns_label: str = None,
    freeform_tags: Dict = None,
    ipv6_cidr_block: str = None,
    ipv6_private_cidr_blocks: List[str] = None,
    is_ipv6_enabled: bool = None,
    is_oracle_gua_allocation_enabled: bool = None,
) -> Dict[str, Any]:
    r"""

    CreateVcn
        Creates a new virtual cloud network (VCN). For more information, see
    [VCNs and Subnets](/iaas/Content/Network/Tasks/managingVCNs.htm).

    For the VCN, you specify a list of one or more IPv4 CIDR blocks that meet the following criteria:

    - The CIDR blocks must be valid.
    - They must not overlap with each other or with the on-premises network CIDR block.
    - The number of CIDR blocks does not exceed the limit of CIDR blocks allowed per VCN.

    For a CIDR block, Oracle recommends that you use one of the private IP address ranges specified in [RFC 1918](https://tools.ietf.org/html/rfc1918) (10.0.0.0/8, 172.16/12, and 192.168/16). Example:
    172.16.0.0/16. The CIDR blocks can range from /16 to /30.

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want the VCN to
    reside. Consult an Oracle Cloud Infrastructure administrator in your organization if you're not sure which
    compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other
    Networking Service components. For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
    [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to
    be unique, and you can change it. Avoid entering confidential information.

    You can also add a DNS label for the VCN, which is required if you want the instances to use the
    Interent and VCN Resolver option for DNS in the VCN. For more information, see
    [DNS in Your Virtual Cloud Network](/iaas/Content/Network/Concepts/dns.htm).

    The VCN automatically comes with a default route table, default security list, and default set of DHCP options.
    The [OCID](/iaas/Content/General/Concepts/identifiers.htm) for each is returned in the response. You can't delete these default objects, but you can change their
    contents (that is, change the route rules, security list rules, and so on).

    The VCN and subnets you create are not accessible until you attach an internet gateway or set up a Site-to-Site VPN
    or FastConnect. For more information, see
    [Overview of the Networking Service](/iaas/Content/Network/Concepts/overview.htm).

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the VCN.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        byoipv6_cidr_details(List[dict[str, Any]], Optional):
            The list of BYOIPv6 OCIDs and BYOIPv6 prefixes required to create a VCN that uses BYOIPv6 address ranges.
            Defaults to None.

            * byoipv6_range_id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource to which the CIDR block belongs.

            * ipv6_cidr_block (str):
                An IPv6 prefix required to create a VCN with a BYOIP prefix. It could be the whole prefix identified in `byoipv6RangeId`, or a subrange.
                Example: `2001:0db8:0123::/48`


        cidr_block(str, Optional):
            **Deprecated.** Do *not* set this value. Use `cidrBlocks` instead.
            Example: `10.0.0.0/16`
            Defaults to None.

        cidr_blocks(List[str], Optional):
            The list of one or more IPv4 CIDR blocks for the VCN that meet the following criteria:
            - The CIDR blocks must be valid.
            - They must not overlap with each other or with the on-premises network CIDR block.
            - The number of CIDR blocks must not exceed the limit of CIDR blocks allowed per VCN.

            **Important:** Do *not* specify a value for `cidrBlock`. Use this parameter instead.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        dns_label(str, Optional):
            A DNS label for the VCN, used in conjunction with the VNIC's hostname and
            subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC
            within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`).
            Not required to be unique, but it's a best practice to set unique DNS labels
            for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter.
            The value cannot be changed.

            You must set this value if you want instances to be able to use hostnames to
            resolve other instances in the VCN. Otherwise the Internet and VCN Resolver
            will not work.

            For more information, see
            [DNS in Your Virtual Cloud Network](/iaas/Content/Network/Concepts/dns.htm).

            Example: `vcn1`
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        ipv6_cidr_block(str, Optional):
            If you enable IPv6 for the VCN (see `isIpv6Enabled`), you may optionally provide an IPv6
            /56 prefix from the supported ranges (see [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).
            The addresses in this block will be considered private and cannot be accessed
            from the internet. The documentation refers to this as a *custom CIDR* for the VCN.

            If you don't provide a custom CIDR for the VCN, Oracle assigns the VCN's IPv6 /56 prefix.

            Regardless of whether you or Oracle assigns the `ipv6CidrBlock`,
            Oracle *also* assigns the VCN an IPv6 prefix for the VCN's public IP address space
            (see the `ipv6PublicCidrBlock` of the [Vcn](#/en/iaas/latest/Vcn/) object). If you do
            not assign a custom prefix, Oracle uses the *same* Oracle-assigned prefix for both the private
            IP address space (`ipv6CidrBlock` in the `Vcn` object) and the public IP addreses space
            (`ipv6PublicCidrBlock` in the `Vcn` object). This means that a given VNIC might use the same
            IPv6 IP address for both private and public (internet) communication. You control whether
            an IPv6 address can be used for internet communication by using the `isInternetAccessAllowed`
            attribute in the [Ipv6](#/en/iaas/latest/Ipv6/) object.

            For important details about IPv6 addressing in a VCN, see [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

            Example: `2001:0db8:0123::/48`
            Defaults to None.

        ipv6_private_cidr_blocks(List[str], Optional):
            The list of one or more ULA or Private IPv6 prefixes for the VCN that meets the following criteria:
            - The CIDR blocks must be valid.
            - Multiple CIDR blocks must not overlap each other or the on-premises network prefix.
            - The number of CIDR blocks must not exceed the limit of IPv6 prefixes allowed to a VCN.

            **Important:** Do *not* specify a value for `ipv6CidrBlock`. Use this parameter instead.
            Defaults to None.

        is_ipv6_enabled(bool, Optional):
            Whether IPv6 is enabled for the VCN. Default is `false`.
            If enabled, Oracle will assign the VCN a IPv6 /56 CIDR block.
            You may skip having Oracle allocate the VCN a IPv6 /56 CIDR block by setting isOracleGuaAllocationEnabled to `false`.
            For important details about IPv6 addressing in a VCN, see [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

            Example: `true`
            Defaults to None.

        is_oracle_gua_allocation_enabled(bool, Optional):
            Specifies whether to skip Oracle allocated IPv6 GUA. By default, Oracle will allocate one GUA of /56
            size for an IPv6 enabled VCN.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "byoipv6_cidr_details": "byoipv6CidrDetails",
        "cidr_block": "cidrBlock",
        "cidr_blocks": "cidrBlocks",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "dns_label": "dnsLabel",
        "freeform_tags": "freeformTags",
        "ipv6_cidr_block": "ipv6CidrBlock",
        "ipv6_private_cidr_blocks": "ipv6PrivateCidrBlocks",
        "is_ipv6_enabled": "isIpv6Enabled",
        "is_oracle_gua_allocation_enabled": "isOracleGuaAllocationEnabled",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vcns".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "byoipv6CidrBlocks": "byoipv6_cidr_blocks",
            "cidrBlock": "cidr_block",
            "cidrBlocks": "cidr_blocks",
            "compartmentId": "compartment_id",
            "defaultDhcpOptionsId": "default_dhcp_options_id",
            "defaultRouteTableId": "default_route_table_id",
            "defaultSecurityListId": "default_security_list_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "dnsLabel": "dns_label",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipv6CidrBlock": "ipv6_cidr_block",
            "ipv6PrivateCidrBlocks": "ipv6_private_cidr_blocks",
            "ipv6PublicCidrBlock": "ipv6_public_cidr_block",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vcnDomainName": "vcn_domain_name",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_vcn(hub, ctx, vcn_id: str) -> Dict[str, Any]:
    r"""

    GetVcn
        Gets the specified VCN's information.

    Args:
        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vcns/{vcnId}".format(**{"vcnId": vcn_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "byoipv6CidrBlocks": "byoipv6_cidr_blocks",
            "cidrBlock": "cidr_block",
            "cidrBlocks": "cidr_blocks",
            "compartmentId": "compartment_id",
            "defaultDhcpOptionsId": "default_dhcp_options_id",
            "defaultRouteTableId": "default_route_table_id",
            "defaultSecurityListId": "default_security_list_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "dnsLabel": "dns_label",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipv6CidrBlock": "ipv6_cidr_block",
            "ipv6PrivateCidrBlocks": "ipv6_private_cidr_blocks",
            "ipv6PublicCidrBlock": "ipv6_public_cidr_block",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vcnDomainName": "vcn_domain_name",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_vcn(
    hub,
    ctx,
    vcn_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    UpdateVcn
        Updates the specified VCN.

    Args:
        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/vcns/{vcnId}".format(**{"vcnId": vcn_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "byoipv6CidrBlocks": "byoipv6_cidr_blocks",
            "cidrBlock": "cidr_block",
            "cidrBlocks": "cidr_blocks",
            "compartmentId": "compartment_id",
            "defaultDhcpOptionsId": "default_dhcp_options_id",
            "defaultRouteTableId": "default_route_table_id",
            "defaultSecurityListId": "default_security_list_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "dnsLabel": "dns_label",
            "freeformTags": "freeform_tags",
            "id": "id",
            "ipv6CidrBlock": "ipv6_cidr_block",
            "ipv6PrivateCidrBlocks": "ipv6_private_cidr_blocks",
            "ipv6PublicCidrBlock": "ipv6_public_cidr_block",
            "lifecycleState": "lifecycle_state",
            "timeCreated": "time_created",
            "vcnDomainName": "vcn_domain_name",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_vcn(hub, ctx, vcn_id: str, if_match: str = None) -> Dict[str, Any]:
    r"""

    DeleteVcn
        Deletes the specified VCN. The VCN must be completely empty and have no attached gateways. This is an asynchronous
    operation.

    A deleted VCN's `lifecycleState` changes to TERMINATING and then TERMINATED temporarily until the VCN is completely
    removed. A completely removed VCN does not appear in the results of a `ListVcns` operation and can't be used in a
    `GetVcn` operation.

    Args:
        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/vcns/{vcnId}".format(**{"vcnId": vcn_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def add_vcn_cidr(
    hub,
    ctx,
    vcn_id: str,
    cidr_block: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    if_match: str = None,
) -> Dict[str, Any]:
    r"""

    AddVcnCidr
        Adds a CIDR block to a VCN. The CIDR block you add:

    - Must be valid.
    - Must not overlap with another CIDR block in the VCN, a CIDR block of a peered VCN, or the on-premises network CIDR block.
    - Must not exceed the limit of CIDR blocks allowed per VCN.

    **Note:** Adding a CIDR block places your VCN in an updating state until the changes are complete. You cannot create or update the VCN's subnets, VLANs, LPGs, or route tables during this operation. The time to completion can take a few minutes. You can use the `GetWorkRequest` operation to check the status of the update.

    Args:
        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        cidr_block(str):
            The CIDR block to add.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"cidr_block": "cidrBlock"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vcns/{vcnId}/actions/addCidr".format(**{"vcnId": vcn_id}),
        query_params={},
        data=payload,
        headers={
            "opc-request-id": opc_request_id,
            "opc-retry-token": opc_retry_token,
            "if-match": if_match,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def add_ipv6_vcn_cidr(
    hub,
    ctx,
    vcn_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    if_match: str = None,
    byoipv6_cidr_detail: make_dataclass(
        "byoipv6_cidr_detail", [("byoipv6_range_id", str), ("ipv6_cidr_block", str)]
    ) = None,
    ipv6_private_cidr_block: str = None,
    is_oracle_gua_allocation_enabled: bool = None,
) -> Dict[str, Any]:
    r"""

    AddVcnIpv6Cidr
        Add an IPv6 prefix to a VCN. The VCN size is always /56.
    AddIpv6VcnCidr supports adding Private IPv6 Prefix i.e. ULA or an IPv6 GUA assigned by Oracle or BYOIPv6 Prefix, only one of these per request.
    Once added the IPv6 prefix cannot be removed or modified.

    Args:
        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        byoipv6_cidr_detail(dict[str, Any], Optional):
            byoipv6CidrDetail. Defaults to None.

            * byoipv6_range_id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource to which the CIDR block belongs.

            * ipv6_cidr_block (str):
                An IPv6 prefix required to create a VCN with a BYOIP prefix. It could be the whole prefix identified in `byoipv6RangeId`, or a subrange.
                Example: `2001:0db8:0123::/48`


        ipv6_private_cidr_block(str, Optional):
            This field is not required and should only be specified if a ULA or private IPv6 prefix is desired for VCN's private IP address space.
            See[IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

            Example: `2001:0db8:0123::/48` or `fd00:1000:0:1::/64`
            Defaults to None.

        is_oracle_gua_allocation_enabled(bool, Optional):
            Indicates whether Oracle will allocate an IPv6 GUA. Only one prefix of /56 size can be allocated by Oracle as a GUA.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "byoipv6_cidr_detail": "byoipv6CidrDetail",
        "ipv6_private_cidr_block": "ipv6PrivateCidrBlock",
        "is_oracle_gua_allocation_enabled": "isOracleGuaAllocationEnabled",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vcns/{vcnId}/actions/addIpv6Cidr".format(**{"vcnId": vcn_id}),
        query_params={},
        data=payload,
        headers={
            "opc-request-id": opc_request_id,
            "opc-retry-token": opc_retry_token,
            "if-match": if_match,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_vcn_compartment(
    hub,
    ctx,
    vcn_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeVcnCompartment
        Moves a VCN into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            VCN to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vcns/{vcnId}/actions/changeCompartment".format(**{"vcnId": vcn_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def modify_vcn_cidr(
    hub,
    ctx,
    vcn_id: str,
    new_cidr_block: str,
    original_cidr_block: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    if_match: str = None,
) -> Dict[str, Any]:
    r"""

    ModifyVcnCidr
        Updates the specified CIDR block of a VCN. The new CIDR IP range must meet the following criteria:

    - Must be valid.
    - Must not overlap with another CIDR block in the VCN, a CIDR block of a peered VCN, or the on-premises network CIDR block.
    - Must not exceed the limit of CIDR blocks allowed per VCN.
    - Must include IP addresses from the original CIDR block that are used in the VCN's existing route rules.
    - No IP address in an existing subnet should be outside of the new CIDR block range.

    **Note:** Modifying a CIDR block places your VCN in an updating state until the changes are complete. You cannot create or update the VCN's subnets, VLANs, LPGs, or route tables during this operation. The time to completion can vary depending on the size of your network. Updating a small network could take about a minute, and updating a large network could take up to an hour. You can use the `GetWorkRequest` operation to check the status of the update.

    Args:
        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        new_cidr_block(str):
            The new CIDR IP address.


        original_cidr_block(str):
            The CIDR IP address to update.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "new_cidr_block": "newCidrBlock",
        "original_cidr_block": "originalCidrBlock",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vcns/{vcnId}/actions/modifyCidr".format(**{"vcnId": vcn_id}),
        query_params={},
        data=payload,
        headers={
            "opc-request-id": opc_request_id,
            "opc-retry-token": opc_retry_token,
            "if-match": if_match,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def remove_vcn_cidr(
    hub,
    ctx,
    vcn_id: str,
    cidr_block: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    if_match: str = None,
) -> Dict[str, Any]:
    r"""

    RemoveVcnCidr
        Removes a specified CIDR block from a VCN.

    **Notes:**
    - You cannot remove a CIDR block if an IP address in its range is in use.
    - Removing a CIDR block places your VCN in an updating state until the changes are complete. You cannot create or update the VCN's subnets, VLANs, LPGs, or route tables during this operation. The time to completion can take a few minutes. You can use the `GetWorkRequest` operation to check the status of the update.

    Args:
        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        cidr_block(str):
            The CIDR block to remove.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"cidr_block": "cidrBlock"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vcns/{vcnId}/actions/removeCidr".format(**{"vcnId": vcn_id}),
        query_params={},
        data=payload,
        headers={
            "opc-request-id": opc_request_id,
            "opc-retry-token": opc_retry_token,
            "if-match": if_match,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def remove_ipv6_vcn_cidr(
    hub,
    ctx,
    vcn_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    if_match: str = None,
    ipv6_cidr_block: str = None,
) -> Dict[str, Any]:
    r"""

    RemoveIpv6VcnCidr
        Removing an existing IPv6 prefix from a VCN.

    Args:
        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        ipv6_cidr_block(str, Optional):
            This field is not required and should only be specified when removing ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or BYOIPv6 prefix
            from a VCN's IPv6 address space.
            See[IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

            Example: `2001:0db8:0123::/56`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"ipv6_cidr_block": "ipv6CidrBlock"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vcns/{vcnId}/actions/removeIpv6Cidr".format(**{"vcnId": vcn_id}),
        query_params={},
        data=payload,
        headers={
            "opc-request-id": opc_request_id,
            "opc-retry-token": opc_retry_token,
            "if-match": if_match,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_virtual_circuit_bandwidth_shapes(
    hub, ctx, compartment_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListVirtualCircuitBandwidthShapes
        The deprecated operation lists available bandwidth levels for virtual circuits. For the compartment ID, provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of your tenancy (the root compartment).

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/virtualCircuitBandwidthShapes".format(**{}),
        query_params={"compartmentId": compartment_id, "limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_virtual_circuits(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListVirtualCircuits
        Lists the virtual circuits in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the specified lifecycle
            state. The value is case insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/virtualCircuits".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_virtual_circuit(
    hub,
    ctx,
    compartment_id: str,
    type_: str,
    opc_retry_token: str = None,
    bandwidth_shape_name: str = None,
    bgp_admin_state: str = None,
    cross_connect_mappings: List[
        make_dataclass(
            "cross_connect_mappings",
            [
                ("bgp_md5_auth_key", str, field(default=None)),
                ("cross_connect_or_cross_connect_group_id", str, field(default=None)),
                ("customer_bgp_peering_ip", str, field(default=None)),
                ("customer_bgp_peering_ipv6", str, field(default=None)),
                ("oracle_bgp_peering_ip", str, field(default=None)),
                ("oracle_bgp_peering_ipv6", str, field(default=None)),
                ("vlan", int, field(default=None)),
            ],
        )
    ] = None,
    customer_bgp_asn: int = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    gateway_id: str = None,
    ip_mtu: str = None,
    is_bfd_enabled: bool = None,
    is_transport_mode: bool = None,
    provider_name: str = None,
    provider_service_id: str = None,
    provider_service_key_name: str = None,
    provider_service_name: str = None,
    public_prefixes: List[
        make_dataclass("public_prefixes", [("cidr_block", str)])
    ] = None,
    region: str = None,
    routing_policy: List[str] = None,
) -> Dict[str, Any]:
    r"""

    CreateVirtualCircuit
        Creates a new virtual circuit to use with Oracle Cloud
    Infrastructure FastConnect. For more information, see
    [FastConnect Overview](/iaas/Content/Network/Concepts/fastconnect.htm).

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the
    compartment where you want the virtual circuit to reside. If you're
    not sure which compartment to use, put the virtual circuit in the
    same compartment with the DRG it's using. For more information about
    compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).
    For information about OCIDs, see
    [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the virtual circuit.
    It does not have to be unique, and you can change it. Avoid entering confidential information.

    **Important:** When creating a virtual circuit, you specify a DRG for
    the traffic to flow through. Make sure you attach the DRG to your
    VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise
    traffic will not flow. For more information, see
    [Route Tables](/iaas/Content/Network/Tasks/managingroutetables.htm).

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the virtual circuit.


        type_(str):
            The type of IP addresses used in this virtual circuit. PRIVATE
            means [RFC 1918](https://tools.ietf.org/html/rfc1918) addresses
            (10.0.0.0/8, 172.16/12, and 192.168/16).


        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        bandwidth_shape_name(str, Optional):
            The provisioned data rate of the connection. To get a list of the
            available bandwidth levels (that is, shapes), see
            [ListFastConnectProviderServiceVirtualCircuitBandwidthShapes](#/en/iaas/latest/FastConnectProviderService/ListFastConnectProviderVirtualCircuitBandwidthShapes).

            Example: `10 Gbps`
            Defaults to None.

        bgp_admin_state(str, Optional):
            Set to `ENABLED` (the default) to activate the BGP session of the virtual circuit, set to `DISABLED` to deactivate the virtual circuit.
            Defaults to None.

        cross_connect_mappings(List[dict[str, Any]], Optional):
            Create a `CrossConnectMapping` for each cross-connect or cross-connect
            group this virtual circuit will run on.
            Defaults to None.

            * bgp_md5_auth_key (str, Optional):
                The key for BGP MD5 authentication. Only applicable if your system
                requires MD5 authentication. If empty or not set (null), that
                means you don't use BGP MD5 authentication.
                Defaults to None.

            * cross_connect_or_cross_connect_group_id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect or cross-connect group for this mapping.
                Specified by the owner of the cross-connect or cross-connect group (the
                customer if the customer is colocated with Oracle, or the provider if the
                customer is connecting via provider).
                Defaults to None.

            * customer_bgp_peering_ip (str, Optional):
                The BGP IPv4 address for the router on the other end of the BGP session from
                Oracle. Specified by the owner of that router. If the session goes from Oracle
                to a customer, this is the BGP IPv4 address of the customer's edge router. If the
                session goes from Oracle to a provider, this is the BGP IPv4 address of the
                provider's edge router. Must use a subnet mask from /28 to /31.

                There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses.

                Example: `10.0.0.18/31`
                Defaults to None.

            * customer_bgp_peering_ipv6 (str, Optional):
                The BGP IPv6 address for the router on the other end of the BGP session from
                Oracle. Specified by the owner of that router. If the session goes from Oracle
                to a customer, this is the BGP IPv6 address of the customer's edge router. If the
                session goes from Oracle to a provider, this is the BGP IPv6 address of the
                provider's edge router. Only subnet masks from /64 up to /127 are allowed.

                There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses.

                IPv6 addressing is supported for all commercial and government regions. See
                [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                Example: `2001:db8::1/64`
                Defaults to None.

            * oracle_bgp_peering_ip (str, Optional):
                The IPv4 address for Oracle's end of the BGP session. Must use a subnet mask from /28 to /31.
                If the session goes from Oracle to a customer's edge router,
                the customer specifies this information. If the session goes from Oracle to
                a provider's edge router, the provider specifies this.

                There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses.

                Example: `10.0.0.19/31`
                Defaults to None.

            * oracle_bgp_peering_ipv6 (str, Optional):
                The IPv6 address for Oracle's end of the BGP session. Only subnet masks from /64 up to /127 are allowed.
                If the session goes from Oracle to a customer's edge router,
                the customer specifies this information. If the session goes from Oracle to
                a provider's edge router, the provider specifies this.

                There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses.

                Note that IPv6 addressing is currently supported only in certain regions. See
                [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                Example: `2001:db8::2/64`
                Defaults to None.

            * vlan (int, Optional):
                The number of the specific VLAN (on the cross-connect or cross-connect group)
                that is assigned to this virtual circuit. Specified by the owner of the cross-connect
                or cross-connect group (the customer if the customer is colocated with Oracle, or
                the provider if the customer is connecting via provider).

                Example: `200`
                Defaults to None.

        customer_bgp_asn(int, Optional):
            Your BGP ASN (either public or private). Provide this value only if
            there's a BGP session that goes from your edge router to Oracle.
            Otherwise, leave this empty or null.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        gateway_id(str, Optional):
            For private virtual circuits only. The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the [dynamic routing gateway (DRG)](#/en/iaas/latest/Drg)
            that this virtual circuit uses.
            Defaults to None.

        ip_mtu(str, Optional):
            The layer 3 IP MTU to use with this virtual circuit. Defaults to None.

        is_bfd_enabled(bool, Optional):
            Set to `true` to enable BFD for IPv4 BGP peering, or set to `false` to disable BFD. If this is not set, the default is `false`.
            Defaults to None.

        is_transport_mode(bool, Optional):
            Set to `true` for the virtual circuit to carry only encrypted traffic, or set to `false` for the virtual circuit to carry unencrypted traffic. If this is not set, the default is `false`.
            Defaults to None.

        provider_name(str, Optional):
            Deprecated. Instead use `providerServiceId`.
            To get a list of the provider names, see
            [ListFastConnectProviderServices](#/en/iaas/latest/FastConnectProviderService/ListFastConnectProviderServices).
            Defaults to None.

        provider_service_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the service offered by the provider (if you're connecting
            via a provider). To get a list of the available service offerings, see
            [ListFastConnectProviderServices](#/en/iaas/latest/FastConnectProviderService/ListFastConnectProviderServices).
            Defaults to None.

        provider_service_key_name(str, Optional):
            The service key name offered by the provider (if the customer is connecting via a provider).
            Defaults to None.

        provider_service_name(str, Optional):
            Deprecated. Instead use `providerServiceId`.
            To get a list of the provider names, see
            [ListFastConnectProviderServices](#/en/iaas/latest/FastConnectProviderService/ListFastConnectProviderServices).
            Defaults to None.

        public_prefixes(List[dict[str, Any]], Optional):
            For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to
            advertise across the connection.
            Defaults to None.

            * cidr_block (str):
                An individual public IP prefix (CIDR) to add to the public virtual circuit.
                All prefix sizes are allowed.


        region(str, Optional):
            The Oracle Cloud Infrastructure region where this virtual
            circuit is located.
            Example: `phx`
            Defaults to None.

        routing_policy(List[str], Optional):
            The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit.
            Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`.
            See [Route Filtering](/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering) for details.
            By default, routing information is shared for all routes in the same market.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "bandwidth_shape_name": "bandwidthShapeName",
        "bgp_admin_state": "bgpAdminState",
        "compartment_id": "compartmentId",
        "cross_connect_mappings": "crossConnectMappings",
        "customer_bgp_asn": "customerBgpAsn",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "gateway_id": "gatewayId",
        "ip_mtu": "ipMtu",
        "is_bfd_enabled": "isBfdEnabled",
        "is_transport_mode": "isTransportMode",
        "provider_name": "providerName",
        "provider_service_id": "providerServiceId",
        "provider_service_key_name": "providerServiceKeyName",
        "provider_service_name": "providerServiceName",
        "public_prefixes": "publicPrefixes",
        "region": "region",
        "routing_policy": "routingPolicy",
        "type": "type",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/virtualCircuits".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "bandwidthShapeName": "bandwidth_shape_name",
            "bgpAdminState": "bgp_admin_state",
            "bgpIpv6SessionState": "bgp_ipv6_session_state",
            "bgpManagement": "bgp_management",
            "bgpSessionState": "bgp_session_state",
            "compartmentId": "compartment_id",
            "crossConnectMappings": "cross_connect_mappings",
            "customerBgpAsn": "customer_bgp_asn",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "gatewayId": "gateway_id",
            "id": "id",
            "ipMtu": "ip_mtu",
            "isBfdEnabled": "is_bfd_enabled",
            "isTransportMode": "is_transport_mode",
            "lifecycleState": "lifecycle_state",
            "oracleBgpAsn": "oracle_bgp_asn",
            "providerName": "provider_name",
            "providerServiceId": "provider_service_id",
            "providerServiceKeyName": "provider_service_key_name",
            "providerServiceName": "provider_service_name",
            "providerState": "provider_state",
            "publicPrefixes": "public_prefixes",
            "referenceComment": "reference_comment",
            "region": "region",
            "routingPolicy": "routing_policy",
            "serviceType": "service_type",
            "timeCreated": "time_created",
            "type": "type",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_virtual_circuit(hub, ctx, virtual_circuit_id: str) -> Dict[str, Any]:
    r"""

    GetVirtualCircuit
        Gets the specified virtual circuit's information.

    Args:
        virtual_circuit_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the virtual circuit.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/virtualCircuits/{virtualCircuitId}".format(
            **{"virtualCircuitId": virtual_circuit_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "bandwidthShapeName": "bandwidth_shape_name",
            "bgpAdminState": "bgp_admin_state",
            "bgpIpv6SessionState": "bgp_ipv6_session_state",
            "bgpManagement": "bgp_management",
            "bgpSessionState": "bgp_session_state",
            "compartmentId": "compartment_id",
            "crossConnectMappings": "cross_connect_mappings",
            "customerBgpAsn": "customer_bgp_asn",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "gatewayId": "gateway_id",
            "id": "id",
            "ipMtu": "ip_mtu",
            "isBfdEnabled": "is_bfd_enabled",
            "isTransportMode": "is_transport_mode",
            "lifecycleState": "lifecycle_state",
            "oracleBgpAsn": "oracle_bgp_asn",
            "providerName": "provider_name",
            "providerServiceId": "provider_service_id",
            "providerServiceKeyName": "provider_service_key_name",
            "providerServiceName": "provider_service_name",
            "providerState": "provider_state",
            "publicPrefixes": "public_prefixes",
            "referenceComment": "reference_comment",
            "region": "region",
            "routingPolicy": "routing_policy",
            "serviceType": "service_type",
            "timeCreated": "time_created",
            "type": "type",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_virtual_circuit(
    hub,
    ctx,
    virtual_circuit_id: str,
    if_match: str = None,
    bandwidth_shape_name: str = None,
    bgp_admin_state: str = None,
    cross_connect_mappings: List[
        make_dataclass(
            "cross_connect_mappings",
            [
                ("bgp_md5_auth_key", str, field(default=None)),
                ("cross_connect_or_cross_connect_group_id", str, field(default=None)),
                ("customer_bgp_peering_ip", str, field(default=None)),
                ("customer_bgp_peering_ipv6", str, field(default=None)),
                ("oracle_bgp_peering_ip", str, field(default=None)),
                ("oracle_bgp_peering_ipv6", str, field(default=None)),
                ("vlan", int, field(default=None)),
            ],
        )
    ] = None,
    customer_bgp_asn: int = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    gateway_id: str = None,
    ip_mtu: str = None,
    is_bfd_enabled: bool = None,
    is_transport_mode: bool = None,
    provider_service_key_name: str = None,
    provider_state: str = None,
    reference_comment: str = None,
    routing_policy: List[str] = None,
) -> Dict[str, Any]:
    r"""

    UpdateVirtualCircuit
        Updates the specified virtual circuit. This can be called by
    either the customer who owns the virtual circuit, or the
    provider (when provisioning or de-provisioning the virtual
    circuit from their end). The documentation for
    [UpdateVirtualCircuitDetails](#/en/iaas/latest/requests/UpdateVirtualCircuitDetails)
    indicates who can update each property of the virtual circuit.

    **Important:** If the virtual circuit is working and in the
    PROVISIONED state, updating any of the network-related properties
    (such as the DRG being used, the BGP ASN, and so on) will cause the virtual
    circuit's state to switch to PROVISIONING and the related BGP
    session to go down. After Oracle re-provisions the virtual circuit,
    its state will return to PROVISIONED. Make sure you confirm that
    the associated BGP session is back up. For more information
    about the various states and how to test connectivity, see
    [FastConnect Overview](/iaas/Content/Network/Concepts/fastconnect.htm).

    To change the list of public IP prefixes for a public virtual circuit,
    use [BulkAddVirtualCircuitPublicPrefixes](#/en/iaas/latest/VirtualCircuitPublicPrefix/BulkAddVirtualCircuitPublicPrefixes)
    and
    [BulkDeleteVirtualCircuitPublicPrefixes](#/en/iaas/latest/VirtualCircuitPublicPrefix/BulkDeleteVirtualCircuitPublicPrefixes).
    Updating the list of prefixes does NOT cause the BGP session to go down. However,
    Oracle must verify the customer's ownership of each added prefix before
    traffic for that prefix will flow across the virtual circuit.

    Args:
        virtual_circuit_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the virtual circuit.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        bandwidth_shape_name(str, Optional):
            The provisioned data rate of the connection. To get a list of the
            available bandwidth levels (that is, shapes), see
            [ListFastConnectProviderVirtualCircuitBandwidthShapes](#/en/iaas/latest/FastConnectProviderService/ListFastConnectProviderVirtualCircuitBandwidthShapes).
            To be updated only by the customer who owns the virtual circuit.
            Defaults to None.

        bgp_admin_state(str, Optional):
            Set to `ENABLED` (the default) to activate the BGP session of the virtual circuit, set to `DISABLED` to deactivate the virtual circuit.
            Defaults to None.

        cross_connect_mappings(List[dict[str, Any]], Optional):
            An array of mappings, each containing properties for a cross-connect or
            cross-connect group associated with this virtual circuit.

            The customer and provider can update different properties in the mapping
            depending on the situation. See the description of the
            [CrossConnectMapping](#/en/iaas/latest/CrossConnectMapping/).
            Defaults to None.

            * bgp_md5_auth_key (str, Optional):
                The key for BGP MD5 authentication. Only applicable if your system
                requires MD5 authentication. If empty or not set (null), that
                means you don't use BGP MD5 authentication.
                Defaults to None.

            * cross_connect_or_cross_connect_group_id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect or cross-connect group for this mapping.
                Specified by the owner of the cross-connect or cross-connect group (the
                customer if the customer is colocated with Oracle, or the provider if the
                customer is connecting via provider).
                Defaults to None.

            * customer_bgp_peering_ip (str, Optional):
                The BGP IPv4 address for the router on the other end of the BGP session from
                Oracle. Specified by the owner of that router. If the session goes from Oracle
                to a customer, this is the BGP IPv4 address of the customer's edge router. If the
                session goes from Oracle to a provider, this is the BGP IPv4 address of the
                provider's edge router. Must use a subnet mask from /28 to /31.

                There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses.

                Example: `10.0.0.18/31`
                Defaults to None.

            * customer_bgp_peering_ipv6 (str, Optional):
                The BGP IPv6 address for the router on the other end of the BGP session from
                Oracle. Specified by the owner of that router. If the session goes from Oracle
                to a customer, this is the BGP IPv6 address of the customer's edge router. If the
                session goes from Oracle to a provider, this is the BGP IPv6 address of the
                provider's edge router. Only subnet masks from /64 up to /127 are allowed.

                There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses.

                IPv6 addressing is supported for all commercial and government regions. See
                [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                Example: `2001:db8::1/64`
                Defaults to None.

            * oracle_bgp_peering_ip (str, Optional):
                The IPv4 address for Oracle's end of the BGP session. Must use a subnet mask from /28 to /31.
                If the session goes from Oracle to a customer's edge router,
                the customer specifies this information. If the session goes from Oracle to
                a provider's edge router, the provider specifies this.

                There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses.

                Example: `10.0.0.19/31`
                Defaults to None.

            * oracle_bgp_peering_ipv6 (str, Optional):
                The IPv6 address for Oracle's end of the BGP session. Only subnet masks from /64 up to /127 are allowed.
                If the session goes from Oracle to a customer's edge router,
                the customer specifies this information. If the session goes from Oracle to
                a provider's edge router, the provider specifies this.

                There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses.

                Note that IPv6 addressing is currently supported only in certain regions. See
                [IPv6 Addresses](/iaas/Content/Network/Concepts/ipv6.htm).

                Example: `2001:db8::2/64`
                Defaults to None.

            * vlan (int, Optional):
                The number of the specific VLAN (on the cross-connect or cross-connect group)
                that is assigned to this virtual circuit. Specified by the owner of the cross-connect
                or cross-connect group (the customer if the customer is colocated with Oracle, or
                the provider if the customer is connecting via provider).

                Example: `200`
                Defaults to None.

        customer_bgp_asn(int, Optional):
            The BGP ASN of the network at the other end of the BGP
            session from Oracle.

            If the BGP session is from the customer's edge router to Oracle, the
            required value is the customer's ASN, and it can be updated only
            by the customer.

            If the BGP session is from the provider's edge router to Oracle, the
            required value is the provider's ASN, and it can be updated only
            by the provider.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        gateway_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the [dynamic routing gateway (DRG)](#/en/iaas/latest/Drg)
            that this private virtual circuit uses.

            To be updated only by the customer who owns the virtual circuit.
            Defaults to None.

        ip_mtu(str, Optional):
            The layer 3 IP MTU to use on this virtual circuit. Defaults to None.

        is_bfd_enabled(bool, Optional):
            Set to `true` to enable BFD for IPv4 BGP peering, or set to `false` to disable BFD. If this is not set, the default is `false`.
            Defaults to None.

        is_transport_mode(bool, Optional):
            Set to `true` for the virtual circuit to carry only encrypted traffic, or set to `false` for the virtual circuit to carry unencrypted traffic. If this is not set, the default is `false`.
            Defaults to None.

        provider_service_key_name(str, Optional):
            The service key name offered by the provider (if the customer is connecting via a provider).
            Defaults to None.

        provider_state(str, Optional):
            The provider's state in relation to this virtual circuit. Relevant only
            if the customer is using FastConnect via a provider. ACTIVE
            means the provider has provisioned the virtual circuit from their
            end. INACTIVE means the provider has not yet provisioned the virtual
            circuit, or has de-provisioned it.

            To be updated only by the provider.
            Defaults to None.

        reference_comment(str, Optional):
            Provider-supplied reference information about this virtual circuit.
            Relevant only if the customer is using FastConnect via a provider.

            To be updated only by the provider.
            Defaults to None.

        routing_policy(List[str], Optional):
            The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit.
            Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`.
            See [Route Filtering](/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering) for details.
            By default, routing information is shared for all routes in the same market.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "bandwidth_shape_name": "bandwidthShapeName",
        "bgp_admin_state": "bgpAdminState",
        "cross_connect_mappings": "crossConnectMappings",
        "customer_bgp_asn": "customerBgpAsn",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "gateway_id": "gatewayId",
        "ip_mtu": "ipMtu",
        "is_bfd_enabled": "isBfdEnabled",
        "is_transport_mode": "isTransportMode",
        "provider_service_key_name": "providerServiceKeyName",
        "provider_state": "providerState",
        "reference_comment": "referenceComment",
        "routing_policy": "routingPolicy",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/virtualCircuits/{virtualCircuitId}".format(
            **{"virtualCircuitId": virtual_circuit_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "bandwidthShapeName": "bandwidth_shape_name",
            "bgpAdminState": "bgp_admin_state",
            "bgpIpv6SessionState": "bgp_ipv6_session_state",
            "bgpManagement": "bgp_management",
            "bgpSessionState": "bgp_session_state",
            "compartmentId": "compartment_id",
            "crossConnectMappings": "cross_connect_mappings",
            "customerBgpAsn": "customer_bgp_asn",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "gatewayId": "gateway_id",
            "id": "id",
            "ipMtu": "ip_mtu",
            "isBfdEnabled": "is_bfd_enabled",
            "isTransportMode": "is_transport_mode",
            "lifecycleState": "lifecycle_state",
            "oracleBgpAsn": "oracle_bgp_asn",
            "providerName": "provider_name",
            "providerServiceId": "provider_service_id",
            "providerServiceKeyName": "provider_service_key_name",
            "providerServiceName": "provider_service_name",
            "providerState": "provider_state",
            "publicPrefixes": "public_prefixes",
            "referenceComment": "reference_comment",
            "region": "region",
            "routingPolicy": "routing_policy",
            "serviceType": "service_type",
            "timeCreated": "time_created",
            "type": "type",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_virtual_circuit(
    hub, ctx, virtual_circuit_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteVirtualCircuit
        Deletes the specified virtual circuit.

    **Important:** If you're using FastConnect via a provider,
    make sure to also terminate the connection with
    the provider, or else the provider may continue to bill you.

    Args:
        virtual_circuit_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the virtual circuit.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/virtualCircuits/{virtualCircuitId}".format(
            **{"virtualCircuitId": virtual_circuit_id}
        ),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def bulk_add_virtual_circuit_public_prefixes(
    hub,
    ctx,
    virtual_circuit_id: str,
    public_prefixes: List[make_dataclass("public_prefixes", [("cidr_block", str)])],
) -> Dict[str, Any]:
    r"""

    BulkAddVirtualCircuitPublicPrefixes
        Adds one or more customer public IP prefixes to the specified public virtual circuit.
    Use this operation (and not [UpdateVirtualCircuit](#/en/iaas/latest/VirtualCircuit/UpdateVirtualCircuit))
    to add prefixes to the virtual circuit. Oracle must verify the customer's ownership
    of each prefix before traffic for that prefix will flow across the virtual circuit.

    Args:
        virtual_circuit_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the virtual circuit.

        public_prefixes(List[dict[str, Any]]):
            The public IP prefixes (CIDRs) to add to the public virtual circuit.

            * cidr_block (str):
                An individual public IP prefix (CIDR) to add to the public virtual circuit.
                All prefix sizes are allowed.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"public_prefixes": "publicPrefixes"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/virtualCircuits/{virtualCircuitId}/actions/bulkAddPublicPrefixes".format(
            **{"virtualCircuitId": virtual_circuit_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def bulk_delete_virtual_circuit_public_prefixes(
    hub,
    ctx,
    virtual_circuit_id: str,
    public_prefixes: List[make_dataclass("public_prefixes", [("cidr_block", str)])],
) -> Dict[str, Any]:
    r"""

    BulkDeleteVirtualCircuitPublicPrefixes
        Removes one or more customer public IP prefixes from the specified public virtual circuit.
    Use this operation (and not [UpdateVirtualCircuit](#/en/iaas/latest/VirtualCircuit/UpdateVirtualCircuit))
    to remove prefixes from the virtual circuit. When the virtual circuit's state switches
    back to PROVISIONED, Oracle stops advertising the specified prefixes across the connection.

    Args:
        virtual_circuit_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the virtual circuit.

        public_prefixes(List[dict[str, Any]]):
            The public IP prefixes (CIDRs) to remove from the public virtual circuit.


            * cidr_block (str):
                An individual public IP prefix (CIDR) to remove from the public virtual circuit.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"public_prefixes": "publicPrefixes"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/virtualCircuits/{virtualCircuitId}/actions/bulkDeletePublicPrefixes".format(
            **{"virtualCircuitId": virtual_circuit_id}
        ),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_virtual_circuit_compartment(
    hub,
    ctx,
    virtual_circuit_id: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeVirtualCircuitCompartment
        Moves a virtual circuit into a different compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        virtual_circuit_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the virtual circuit.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
            virtual circuit to.


        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/virtualCircuits/{virtualCircuitId}/actions/changeCompartment".format(
            **{"virtualCircuitId": virtual_circuit_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id, "opc-retry-token": opc_retry_token},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_virtual_circuit_associated_tunnels(
    hub, ctx, virtual_circuit_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

    ListVirtualCircuitAssociatedTunnels
        Gets the specified virtual circuit's associatedTunnelsInfo.

    Args:
        virtual_circuit_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the virtual circuit.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/virtualCircuits/{virtualCircuitId}/associatedTunnels".format(
            **{"virtualCircuitId": virtual_circuit_id}
        ),
        query_params={"limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_cross_connect_mappings(
    hub, ctx, virtual_circuit_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    ListCrossConnectMappings
        Lists the Cross Connect mapping Details for the specified
    virtual circuit.

    Args:
        virtual_circuit_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the virtual circuit.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/virtualCircuits/{virtualCircuitId}/crossConnectMappings".format(
            **{"virtualCircuitId": virtual_circuit_id}
        ),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict({"items": "items"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_virtual_circuit_public_prefixes(
    hub, ctx, virtual_circuit_id: str, verification_state: str = None
) -> Dict[str, Any]:
    r"""

    ListVirtualCircuitPublicPrefixes
        Lists the public IP prefixes and their details for the specified
    public virtual circuit.

    Args:
        virtual_circuit_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the virtual circuit.

        verification_state(str, Optional):
            A filter to only return resources that match the given verification
            state.

            The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/virtualCircuits/{virtualCircuitId}/publicPrefixes".format(
            **{"virtualCircuitId": virtual_circuit_id}
        ),
        query_params={"verificationState": verification_state},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def list_vlans(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    opc_request_id: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListVlans
        Lists the VLANs in the specified VCN and the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to only return resources that match the given lifecycle
            state. The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vlans".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "vcnId": vcn_id,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_vlan(
    hub,
    ctx,
    availability_domain: str,
    cidr_block: str,
    compartment_id: str,
    vcn_id: str,
    opc_retry_token: str = None,
    opc_request_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    nsg_ids: List[str] = None,
    route_table_id: str = None,
    vlan_tag: int = None,
) -> Dict[str, Any]:
    r"""

    CreateVlan
        Creates a VLAN in the specified VCN and the specified compartment.

    Args:
        availability_domain(str):
            The availability domain of the VLAN.

            Example: `Uocm:PHX-AD-1`


        cidr_block(str):
            The range of IPv4 addresses that will be used for layer 3 communication with
            hosts outside the VLAN. The CIDR must maintain the following rules -

            1. The CIDR block is valid and correctly formatted.
            2. The new range is within one of the parent VCN ranges.

            Example: `192.0.2.0/24`


        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the VLAN.

        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN to contain the VLAN.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        nsg_ids(List[str], Optional):
            A list of the OCIDs of the network security groups (NSGs) to add all VNICs in the VLAN to. For more
            information about NSGs, see
            [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/).
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the VLAN will use. If you don't provide a value,
            the VLAN uses the VCN's default route table.
            Defaults to None.

        vlan_tag(int, Optional):
            The IEEE 802.1Q VLAN tag for this VLAN. The value must be unique across all
            VLANs in the VCN. If you don't provide a value, Oracle assigns one.
            You cannot change the value later. VLAN tag 0 is reserved for use by Oracle.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "availability_domain": "availabilityDomain",
        "cidr_block": "cidrBlock",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "nsg_ids": "nsgIds",
        "route_table_id": "routeTableId",
        "vcn_id": "vcnId",
        "vlan_tag": "vlanTag",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vlans".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "cidrBlock": "cidr_block",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "nsgIds": "nsg_ids",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
            "vlanTag": "vlan_tag",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_vlan(
    hub, ctx, vlan_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetVlan
        Gets the specified VLAN's information.

    Args:
        vlan_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vlans/{vlanId}".format(**{"vlanId": vlan_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "cidrBlock": "cidr_block",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "nsgIds": "nsg_ids",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
            "vlanTag": "vlan_tag",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_vlan(
    hub,
    ctx,
    vlan_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    nsg_ids: List[str] = None,
    route_table_id: str = None,
) -> Dict[str, Any]:
    r"""

    UpdateVlan
        Updates the specified VLAN. Note that this operation might require changes to all
    the VNICs in the VLAN, which can take a while. The VLAN will be in the UPDATING state until the changes are complete.

    Args:
        vlan_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        nsg_ids(List[str], Optional):
            A list of the OCIDs of the network security groups (NSGs) to use with
            this VLAN. All VNICs in the VLAN will belong to these NSGs. For more
            information about NSGs, see
            [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/).
            Defaults to None.

        route_table_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the route table the VLAN will use.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "nsg_ids": "nsgIds",
        "route_table_id": "routeTableId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/vlans/{vlanId}".format(**{"vlanId": vlan_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "cidrBlock": "cidr_block",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "lifecycleState": "lifecycle_state",
            "nsgIds": "nsg_ids",
            "routeTableId": "route_table_id",
            "timeCreated": "time_created",
            "vcnId": "vcn_id",
            "vlanTag": "vlan_tag",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_vlan(
    hub, ctx, vlan_id: str, if_match: str = None, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    DeleteVlan
        Deletes the specified VLAN, but only if there are no VNICs in the VLAN.

    Args:
        vlan_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/vlans/{vlanId}".format(**{"vlanId": vlan_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_vlan_compartment(
    hub,
    ctx,
    vlan_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeVlanCompartment
        Moves a VLAN into a different compartment within the same tenancy.
    For information about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        vlan_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the VLAN to.


        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vlans/{vlanId}/actions/changeCompartment".format(**{"vlanId": vlan_id}),
        query_params={},
        data=payload,
        headers={
            "if-match": if_match,
            "opc-request-id": opc_request_id,
            "opc-retry-token": opc_retry_token,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_vnic(hub, ctx, vnic_id: str) -> Dict[str, Any]:
    r"""

    GetVnic
        Gets the information for the specified virtual network interface card (VNIC).
    You can get the VNIC [OCID](/iaas/Content/General/Concepts/identifiers.htm) from the
    [ListVnicAttachments](#/en/iaas/latest/VnicAttachment/ListVnicAttachments)
    operation.

    Args:
        vnic_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VNIC.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vnics/{vnicId}".format(**{"vnicId": vnic_id}),
        query_params={},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "hostnameLabel": "hostname_label",
            "id": "id",
            "ipv6Addresses": "ipv6_addresses",
            "isPrimary": "is_primary",
            "lifecycleState": "lifecycle_state",
            "macAddress": "mac_address",
            "nsgIds": "nsg_ids",
            "privateIp": "private_ip",
            "publicIp": "public_ip",
            "skipSourceDestCheck": "skip_source_dest_check",
            "subnetId": "subnet_id",
            "timeCreated": "time_created",
            "vlanId": "vlan_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_vnic(
    hub,
    ctx,
    vnic_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    hostname_label: str = None,
    nsg_ids: List[str] = None,
    skip_source_dest_check: bool = None,
) -> Dict[str, Any]:
    r"""

    UpdateVnic
        Updates the specified VNIC.

    Args:
        vnic_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VNIC.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        hostname_label(str, Optional):
            The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
            portion of the primary private IP's fully qualified domain name (FQDN)
            (for example, `bminstance1` in FQDN `bminstance1.subnet123.vcn1.oraclevcn.com`).
            Must be unique across all VNICs in the subnet and comply with
            [RFC 952](https://tools.ietf.org/html/rfc952) and
            [RFC 1123](https://tools.ietf.org/html/rfc1123).
            The value appears in the [Vnic](#/en/iaas/latest/Vnic/) object and also the
            [PrivateIp](#/en/iaas/latest/PrivateIp/) object returned by
            [ListPrivateIps](#/en/iaas/latest/PrivateIp/ListPrivateIps) and
            [GetPrivateIp](#/en/iaas/latest/PrivateIp/GetPrivateIp).

            For more information, see
            [DNS in Your Virtual Cloud Network](/iaas/Content/Network/Concepts/dns.htm).
            Defaults to None.

        nsg_ids(List[str], Optional):
            A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. Setting this as
            an empty array removes the VNIC from all network security groups.

            If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
            belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the
            VNIC belongs to the NSGs that are associated with the VLAN itself. See [Vlan](#/en/iaas/latest/Vlan).

            For more information about NSGs, see
            [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/).
            Defaults to None.

        skip_source_dest_check(bool, Optional):
            Whether the source/destination check is disabled on the VNIC.
            Defaults to `false`, which means the check is performed. For information about why you would
            skip the source/destination check, see
            [Using a Private IP as a Route Target](/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).

            If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
            belonging to a subnet), the value of the `skipSourceDestCheck` attribute is ignored.
            This is because the source/destination check is always disabled for VNICs in a VLAN.
            Example: `true`
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "hostname_label": "hostnameLabel",
        "nsg_ids": "nsgIds",
        "skip_source_dest_check": "skipSourceDestCheck",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/vnics/{vnicId}".format(**{"vnicId": vnic_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "hostnameLabel": "hostname_label",
            "id": "id",
            "ipv6Addresses": "ipv6_addresses",
            "isPrimary": "is_primary",
            "lifecycleState": "lifecycle_state",
            "macAddress": "mac_address",
            "nsgIds": "nsg_ids",
            "privateIp": "private_ip",
            "publicIp": "public_ip",
            "skipSourceDestCheck": "skip_source_dest_check",
            "subnetId": "subnet_id",
            "timeCreated": "time_created",
            "vlanId": "vlan_id",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_vtaps(
    hub,
    ctx,
    compartment_id: str,
    vcn_id: str = None,
    source: str = None,
    target_id: str = None,
    target_ip: str = None,
    is_vtap_enabled: bool = None,
    limit: int = None,
    page: str = None,
    opc_request_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
    display_name: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListVtaps
        Lists the virtual test access points (VTAPs) in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        vcn_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN. Defaults to None.

        source(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VTAP source. Defaults to None.

        target_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VTAP target. Defaults to None.

        target_ip(str, Optional):
            The IP address of the VTAP target. Defaults to None.

        is_vtap_enabled(bool, Optional):
            Indicates whether to list all VTAPs or only running VTAPs.

            * When `FALSE`, lists ALL running and stopped VTAPs.
            * When `TRUE`, lists only running VTAPs (VTAPs where isVtapEnabled = `TRUE`).
            Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated
            "List" call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

            Example: `50`
            Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List"
            call. For important details about how pagination works, see
            [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some "List" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these "List" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.
            Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.
            Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
            Defaults to None.

        lifecycle_state(str, Optional):
            A filter to return only resources that match the given VTAP administrative lifecycle state.
            The state value is case-insensitive.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vtaps".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "source": source,
            "targetId": target_id,
            "targetIp": target_ip,
            "isVtapEnabled": is_vtap_enabled,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "displayName": display_name,
            "lifecycleState": lifecycle_state,
        },
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_vtap(
    hub,
    ctx,
    capture_filter_id: str,
    compartment_id: str,
    source_id: str,
    vcn_id: str,
    opc_retry_token: str = None,
    opc_request_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    encapsulation_protocol: str = None,
    freeform_tags: Dict = None,
    is_vtap_enabled: bool = None,
    max_packet_size: int = None,
    source_private_endpoint_ip: str = None,
    source_private_endpoint_subnet_id: str = None,
    source_type: str = None,
    target_id: str = None,
    target_ip: str = None,
    target_type: str = None,
    traffic_mode: str = None,
    vxlan_network_identifier: int = None,
) -> Dict[str, Any]:
    r"""

    CreateVtap
        Creates a virtual test access point (VTAP) in the specified compartment.

    For the purposes of access control, you must provide the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the VTAP.
    For more information about compartments and access control, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).
    For information about OCIDs, see [Resource Identifiers](/iaas/Content/General/Concepts/identifiers.htm).

    You may optionally specify a *display name* for the VTAP, otherwise a default is provided.
    It does not have to be unique, and you can change it.

    Args:
        capture_filter_id(str):
            The capture filter's Oracle ID ([OCID](/iaas/Content/General/Concepts/identifiers.htm)).


        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the `Vtap` resource.

        source_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the source point where packets are captured.


        vcn_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VCN containing the `Vtap` resource.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        encapsulation_protocol(str, Optional):
            Defines an encapsulation header type for the VTAP's mirrored traffic.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        is_vtap_enabled(bool, Optional):
            Used to start or stop a `Vtap` resource.

            * `TRUE` directs the VTAP to start mirroring traffic.
            * `FALSE` (Default) directs the VTAP to stop mirroring traffic.
            Defaults to None.

        max_packet_size(int, Optional):
            The maximum size of the packets to be included in the filter. Defaults to None.

        source_private_endpoint_ip(str, Optional):
            The IP Address of the source private endpoint.
            Defaults to None.

        source_private_endpoint_subnet_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet that source private endpoint belongs to.
            Defaults to None.

        source_type(str, Optional):
            The source type for the VTAP.
            Defaults to None.

        target_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the destination resource where mirrored packets are sent.
            Defaults to None.

        target_ip(str, Optional):
            The IP address of the destination resource where mirrored packets are sent.
            Defaults to None.

        target_type(str, Optional):
            The target type for the VTAP.
            Defaults to None.

        traffic_mode(str, Optional):
            Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT. Defaults to None.

        vxlan_network_identifier(int, Optional):
            The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "capture_filter_id": "captureFilterId",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "encapsulation_protocol": "encapsulationProtocol",
        "freeform_tags": "freeformTags",
        "is_vtap_enabled": "isVtapEnabled",
        "max_packet_size": "maxPacketSize",
        "source_id": "sourceId",
        "source_private_endpoint_ip": "sourcePrivateEndpointIp",
        "source_private_endpoint_subnet_id": "sourcePrivateEndpointSubnetId",
        "source_type": "sourceType",
        "target_id": "targetId",
        "target_ip": "targetIp",
        "target_type": "targetType",
        "traffic_mode": "trafficMode",
        "vcn_id": "vcnId",
        "vxlan_network_identifier": "vxlanNetworkIdentifier",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vtaps".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "captureFilterId": "capture_filter_id",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "encapsulationProtocol": "encapsulation_protocol",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isVtapEnabled": "is_vtap_enabled",
            "lifecycleState": "lifecycle_state",
            "lifecycleStateDetails": "lifecycle_state_details",
            "maxPacketSize": "max_packet_size",
            "sourceId": "source_id",
            "sourcePrivateEndpointIp": "source_private_endpoint_ip",
            "sourcePrivateEndpointSubnetId": "source_private_endpoint_subnet_id",
            "sourceType": "source_type",
            "targetId": "target_id",
            "targetIp": "target_ip",
            "targetType": "target_type",
            "timeCreated": "time_created",
            "trafficMode": "traffic_mode",
            "vcnId": "vcn_id",
            "vxlanNetworkIdentifier": "vxlan_network_identifier",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_vtap(
    hub, ctx, vtap_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    GetVtap
        Gets the specified `Vtap` resource.

    Args:
        vtap_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VTAP.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vtaps/{vtapId}".format(**{"vtapId": vtap_id}),
        query_params={},
        data=payload,
        headers={"opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "captureFilterId": "capture_filter_id",
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "encapsulationProtocol": "encapsulation_protocol",
            "freeformTags": "freeform_tags",
            "id": "id",
            "isVtapEnabled": "is_vtap_enabled",
            "lifecycleState": "lifecycle_state",
            "lifecycleStateDetails": "lifecycle_state_details",
            "maxPacketSize": "max_packet_size",
            "sourceId": "source_id",
            "sourcePrivateEndpointIp": "source_private_endpoint_ip",
            "sourcePrivateEndpointSubnetId": "source_private_endpoint_subnet_id",
            "sourceType": "source_type",
            "targetId": "target_id",
            "targetIp": "target_ip",
            "targetType": "target_type",
            "timeCreated": "time_created",
            "trafficMode": "traffic_mode",
            "vcnId": "vcn_id",
            "vxlanNetworkIdentifier": "vxlan_network_identifier",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_vtap(
    hub,
    ctx,
    vtap_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    capture_filter_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    encapsulation_protocol: str = None,
    freeform_tags: Dict = None,
    is_vtap_enabled: bool = None,
    max_packet_size: int = None,
    source_id: str = None,
    source_private_endpoint_ip: str = None,
    source_private_endpoint_subnet_id: str = None,
    source_type: str = None,
    target_id: str = None,
    target_ip: str = None,
    target_type: str = None,
    traffic_mode: str = None,
    vxlan_network_identifier: int = None,
) -> Dict[str, Any]:
    r"""

    UpdateVtap
        Updates the specified VTAP's display name or tags.

    Args:
        vtap_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VTAP.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        capture_filter_id(str, Optional):
            The capture filter's Oracle ID ([OCID](/iaas/Content/General/Concepts/identifiers.htm)).
            Defaults to None.

        defined_tags(Dict, Optional):
            Defined tags for this resource. Each key is predefined and scoped to a
            namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Operations": {"CostCenter": "42"}}`
            Defaults to None.

        display_name(str, Optional):
            A user-friendly name. Does not have to be unique, and it's changeable.
            Avoid entering confidential information.
            Defaults to None.

        encapsulation_protocol(str, Optional):
            Defines an encapsulation header type for the VTAP's mirrored traffic.
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        is_vtap_enabled(bool, Optional):
            Used to start or stop a `Vtap` resource.

            * `TRUE` directs the VTAP to start mirroring traffic.
            * `FALSE` (Default) directs the VTAP to stop mirroring traffic.
            Defaults to None.

        max_packet_size(int, Optional):
            The maximum size of the packets to be included in the filter. Defaults to None.

        source_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the source point where packets are captured.
            Defaults to None.

        source_private_endpoint_ip(str, Optional):
            The IP Address of the source private endpoint.
            Defaults to None.

        source_private_endpoint_subnet_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet that source private endpoint belongs to.
            Defaults to None.

        source_type(str, Optional):
            The source type for the VTAP.
            Defaults to None.

        target_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the destination resource where mirrored packets are sent.
            Defaults to None.

        target_ip(str, Optional):
            The IP address of the destination resource where mirrored packets are sent.
            Defaults to None.

        target_type(str, Optional):
            The target type for the VTAP.
            Defaults to None.

        traffic_mode(str, Optional):
            Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT. Defaults to None.

        vxlan_network_identifier(int, Optional):
            The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "capture_filter_id": "captureFilterId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "encapsulation_protocol": "encapsulationProtocol",
        "freeform_tags": "freeformTags",
        "is_vtap_enabled": "isVtapEnabled",
        "max_packet_size": "maxPacketSize",
        "source_id": "sourceId",
        "source_private_endpoint_ip": "sourcePrivateEndpointIp",
        "source_private_endpoint_subnet_id": "sourcePrivateEndpointSubnetId",
        "source_type": "sourceType",
        "target_id": "targetId",
        "target_ip": "targetIp",
        "target_type": "targetType",
        "traffic_mode": "trafficMode",
        "vxlan_network_identifier": "vxlanNetworkIdentifier",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/vtaps/{vtapId}".format(**{"vtapId": vtap_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def delete_vtap(
    hub, ctx, vtap_id: str, if_match: str = None, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

    DeleteVtap
        Deletes the specified VTAP. This is an asynchronous operation. The VTAP's `lifecycleState` will change to
    TERMINATING temporarily until the VTAP is completely removed.

    Args:
        vtap_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VTAP.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/vtaps/{vtapId}".format(**{"vtapId": vtap_id}),
        query_params={},
        data=payload,
        headers={"if-match": if_match, "opc-request-id": opc_request_id},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_vtap_compartment(
    hub,
    ctx,
    vtap_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeVtapCompartment
        Moves a VTAP to a new compartment within the same tenancy. For information
    about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    Args:
        vtap_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VTAP.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the destination compartment for the VTAP move.


        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        opc_request_id(str, Optional):
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.
            Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vtaps/{vtapId}/actions/changeCompartment".format(**{"vtapId": vtap_id}),
        query_params={},
        data=payload,
        headers={
            "if-match": if_match,
            "opc-request-id": opc_request_id,
            "opc-retry-token": opc_retry_token,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result
