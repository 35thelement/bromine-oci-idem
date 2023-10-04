"""Utility functions for Computes. """
from collections import OrderedDict
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import Dict
from typing import List


async def list_app_catalog_listings(
    hub,
    ctx,
    limit: int = None,
    page: str = None,
    sort_order: str = None,
    publisher_name: str = None,
    publisher_type: str = None,
    display_name: str = None,
) -> Dict[str, Any]:
    r"""

        ListAppCatalogListings
            Lists the published listings.

        Args:
            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

            publisher_name(str, Optional):
                A filter to return only the publisher that matches the given publisher name exactly.
    . Defaults to None.

            publisher_type(str, Optional):
                A filter to return only publishers that match the given publisher type exactly. Valid types are OCI, ORACLE, TRUSTED, STANDARD.
    . Defaults to None.

            display_name(str, Optional):
                A filter to return only resources that match the given display name exactly.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/appCatalogListings".format(**{}),
        query_params={
            "limit": limit,
            "page": page,
            "sortOrder": sort_order,
            "publisherName": publisher_name,
            "publisherType": publisher_type,
            "displayName": display_name,
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


async def get_app_catalog_listing(hub, ctx, listing_id: str) -> Dict[str, Any]:
    r"""

    GetAppCatalogListing
        Gets the specified listing.

    Args:
        listing_id(str):
            The OCID of the listing.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/appCatalogListings/{listingId}".format(**{"listingId": listing_id}),
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
            "contact_url": "contactUrl",
            "description": "description",
            "display_name": "displayName",
            "listing_id": "listingId",
            "publisher_logo_url": "publisherLogoUrl",
            "publisher_name": "publisherName",
            "summary": "summary",
            "time_published": "timePublished",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_app_catalog_listing_resource_versions(
    hub,
    ctx,
    listing_id: str,
    limit: int = None,
    page: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListAppCatalogListingResourceVersions
            Gets all resource versions for a particular listing.

        Args:
            listing_id(str):
                The OCID of the listing.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/appCatalogListings/{listingId}/resourceVersions".format(
            **{"listingId": listing_id}
        ),
        query_params={"limit": limit, "page": page, "sortOrder": sort_order},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def get_app_catalog_listing_resource_version(
    hub, ctx, listing_id: str, resource_version: str
) -> Dict[str, Any]:
    r"""

    GetAppCatalogListingResourceVersion
        Gets the specified listing resource version.

    Args:
        listing_id(str):
            The OCID of the listing.

        resource_version(str):
            Listing Resource Version.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/appCatalogListings/{listingId}/resourceVersions/{resourceVersion}".format(
            **{"listingId": listing_id, "resourceVersion": resource_version}
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
            "accessible_ports": "accessiblePorts",
            "allowed_actions": "allowedActions",
            "available_regions": "availableRegions",
            "compatible_shapes": "compatibleShapes",
            "listing_id": "listingId",
            "listing_resource_id": "listingResourceId",
            "listing_resource_version": "listingResourceVersion",
            "time_published": "timePublished",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_app_catalog_listing_agreements(
    hub, ctx, listing_id: str, resource_version: str
) -> Dict[str, Any]:
    r"""

    GetAppCatalogListingAgreements
        Retrieves the agreements for a particular resource version of a listing.

    Args:
        listing_id(str):
            The OCID of the listing.

        resource_version(str):
            Listing Resource Version.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/appCatalogListings/{listingId}/resourceVersions/{resourceVersion}/agreements".format(
            **{"listingId": listing_id, "resourceVersion": resource_version}
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
            "eula_link": "eulaLink",
            "listing_id": "listingId",
            "listing_resource_version": "listingResourceVersion",
            "oracle_terms_of_use_link": "oracleTermsOfUseLink",
            "signature": "signature",
            "time_retrieved": "timeRetrieved",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_app_catalog_subscriptions(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
    listing_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListAppCatalogSubscriptions
            Lists subscriptions for a compartment.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

            listing_id(str, Optional):
                A filter to return only the listings that matches the given listing id.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/appCatalogSubscriptions".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "listingId": listing_id,
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


async def create_app_catalog_subscription(
    hub,
    ctx,
    compartment_id: str,
    listing_id: str,
    listing_resource_version: str,
    oracle_terms_of_use_link: str,
    signature: str,
    time_retrieved: str,
    opc_retry_token: str = None,
    eula_link: str = None,
) -> Dict[str, Any]:
    r"""

        CreateAppCatalogSubscription
            Create a subscription for listing resource version for a compartment. It will take some time to propagate to all regions.

        Args:
            compartment_id(str):
                The compartmentID for the subscription.

            listing_id(str):
                The OCID of the listing.

            listing_resource_version(str):
                Listing resource version.

            oracle_terms_of_use_link(str):
                Oracle TOU link.

            signature(str):
                A generated signature for this listing resource version retrieved the agreements API.

            time_retrieved(str):
                Date and time the agreements were retrieved, in [RFC3339](https://tools.ietf.org/html/rfc3339) format.
    Example: `2018-03-20T12:32:53.532Z`
    .

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            eula_link(str, Optional):
                EULA link. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "eula_link": "eulaLink",
        "listing_id": "listingId",
        "listing_resource_version": "listingResourceVersion",
        "oracle_terms_of_use_link": "oracleTermsOfUseLink",
        "signature": "signature",
        "time_retrieved": "timeRetrieved",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/appCatalogSubscriptions".format(**{}),
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
            "compartment_id": "compartmentId",
            "display_name": "displayName",
            "listing_id": "listingId",
            "listing_resource_id": "listingResourceId",
            "listing_resource_version": "listingResourceVersion",
            "publisher_name": "publisherName",
            "summary": "summary",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_app_catalog_subscription(
    hub, ctx, listing_id: str, compartment_id: str, resource_version: str
) -> Dict[str, Any]:
    r"""

    DeleteAppCatalogSubscription
        Delete a subscription for a listing resource version for a compartment.

    Args:
        listing_id(str):
            The OCID of the listing.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        resource_version(str):
            Listing Resource Version.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/appCatalogSubscriptions".format(**{}),
        query_params={
            "listingId": listing_id,
            "compartmentId": compartment_id,
            "resourceVersion": resource_version,
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


async def list_boot_volume_attachments(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    instance_id: str = None,
    boot_volume_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListBootVolumeAttachments
            Lists the boot volume attachments in the specified compartment. You can filter the
        list by specifying an instance OCID, boot volume OCID, or both.

        Args:
            availability_domain(str):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    .

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            instance_id(str, Optional):
                The OCID of the instance. Defaults to None.

            boot_volume_id(str, Optional):
                The OCID of the boot volume. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/bootVolumeAttachments/".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "instanceId": instance_id,
            "bootVolumeId": boot_volume_id,
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


async def attach_boot_volume(
    hub,
    ctx,
    boot_volume_id: str,
    instance_id: str,
    opc_retry_token: str = None,
    display_name: str = None,
    encryption_in_transit_type: str = None,
) -> Dict[str, Any]:
    r"""

        AttachBootVolume
            Attaches the specified boot volume to the specified instance.

        Args:
            boot_volume_id(str):
                The OCID of the  boot volume.

            instance_id(str):
                The OCID of the instance.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            encryption_in_transit_type(str, Optional):
                Refer the top-level definition of encryptionInTransitType.
    The default value is NONE.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "boot_volume_id": "bootVolumeId",
        "display_name": "displayName",
        "encryption_in_transit_type": "encryptionInTransitType",
        "instance_id": "instanceId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/bootVolumeAttachments/".format(**{}),
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
            "availability_domain": "availabilityDomain",
            "boot_volume_id": "bootVolumeId",
            "compartment_id": "compartmentId",
            "display_name": "displayName",
            "encryption_in_transit_type": "encryptionInTransitType",
            "id": "id",
            "instance_id": "instanceId",
            "is_pv_encryption_in_transit_enabled": "isPvEncryptionInTransitEnabled",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_boot_volume_attachment(
    hub, ctx, boot_volume_attachment_id: str
) -> Dict[str, Any]:
    r"""

    GetBootVolumeAttachment
        Gets information about the specified boot volume attachment.

    Args:
        boot_volume_attachment_id(str):
            The OCID of the boot volume attachment.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/bootVolumeAttachments/{bootVolumeAttachmentId}".format(
            **{"bootVolumeAttachmentId": boot_volume_attachment_id}
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
            "availability_domain": "availabilityDomain",
            "boot_volume_id": "bootVolumeId",
            "compartment_id": "compartmentId",
            "display_name": "displayName",
            "encryption_in_transit_type": "encryptionInTransitType",
            "id": "id",
            "instance_id": "instanceId",
            "is_pv_encryption_in_transit_enabled": "isPvEncryptionInTransitEnabled",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def detach_boot_volume(
    hub, ctx, boot_volume_attachment_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DetachBootVolume
            Detaches a boot volume from an instance. You must specify the OCID of the boot volume attachment.

        This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily
        until the attachment is completely removed.

        Args:
            boot_volume_attachment_id(str):
                The OCID of the boot volume attachment.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/bootVolumeAttachments/{bootVolumeAttachmentId}".format(
            **{"bootVolumeAttachmentId": boot_volume_attachment_id}
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


async def create_compute_capacity_report(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    shape_availabilities: List[
        make_dataclass(
            "shape_availabilities",
            [
                ("instance_shape", str),
                ("fault_domain", str, field(default=None)),
                (
                    "instance_shape_config",
                    make_dataclass(
                        "instance_shape_config",
                        [
                            ("memory_in_g_bs", float, field(default=None)),
                            ("nvmes", int, field(default=None)),
                            ("ocpus", float, field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ],
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

        CreateComputeCapacityReport
            Generates a report of the host capacity within an availability domain that is available for you
        to create compute instances. Host capacity is the physical infrastructure that resources such as compute
        instances run on.

        Use the capacity report to determine whether sufficient capacity is available for a shape before
        you create an instance or change the shape of an instance.

        Args:
            availability_domain(str):
                The availability domain for the capacity report.

    Example: `Uocm:PHX-AD-1`
    .

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the compartment. This should always be the root
    compartment.
    .

            shape_availabilities(List[dict[str, Any]]):
                Information about the shapes in the capacity report.
    .

                * fault_domain (str, Optional):
                    The fault domain for the capacity report.

    If you do not specify a fault domain, the capacity report includes information about all fault domains.


                * instance_shape (str):
                    The shape that you want to request a capacity report for. You can enumerate all available shapes by calling
    [ListShapes](#/en/iaas/latest/Shape/ListShapes).


                * instance_shape_config (dict[str, Any], Optional):
                    instanceShapeConfig

                    * memory_in_g_bs (float, Optional):
                        The total amount of memory available to the instance, in gigabytes.


                    * nvmes (int, Optional):
                        The number of NVMe drives to be used for storage.


                    * ocpus (float, Optional):
                        The total number of OCPUs available to the instance.


            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "availability_domain": "availabilityDomain",
        "compartment_id": "compartmentId",
        "shape_availabilities": "shapeAvailabilities",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/computeCapacityReports".format(**{}),
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "shape_availabilities": "shapeAvailabilities",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_compute_capacity_reservation_instance_shapes(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    opc_request_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListComputeCapacityReservationInstanceShapes
            Lists the shapes that can be reserved within the specified compartment.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            display_name(str, Optional):
                A filter to return only resources that match the given display name exactly.
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeCapacityReservationInstanceShapes".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
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


async def list_compute_capacity_reservations(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    lifecycle_state: str = None,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    opc_request_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListComputeCapacityReservations
            Lists the compute capacity reservations that match the specified criteria and compartment.

        You can limit the list by specifying a compute capacity reservation display name
        (the list will include all the identically-named compute capacity reservations in the compartment).

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            lifecycle_state(str, Optional):
                A filter to only return resources that match the given lifecycle state. Defaults to None.

            display_name(str, Optional):
                A filter to return only resources that match the given display name exactly.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeCapacityReservations".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "lifecycleState": lifecycle_state,
            "displayName": display_name,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
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


async def create_compute_capacity_reservation(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    instance_reservation_configs: List[
        make_dataclass(
            "instance_reservation_configs",
            [
                ("instance_shape", str),
                ("reserved_count", int),
                (
                    "cluster_config",
                    make_dataclass(
                        "cluster_config",
                        [
                            ("hpc_island_id", str),
                            ("network_block_ids", List[str], field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
                ("fault_domain", str, field(default=None)),
                (
                    "instance_shape_config",
                    make_dataclass(
                        "instance_shape_config",
                        [
                            ("memory_in_g_bs", float, field(default=None)),
                            ("ocpus", float, field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ] = None,
    is_default_reservation: bool = None,
) -> Dict[str, Any]:
    r"""

        CreateComputeCapacityReservation
            Creates a new compute capacity reservation in the specified compartment and availability domain.
        Compute capacity reservations let you reserve instances in a compartment.
        When you launch an instance using this reservation, you are assured that you have enough space for your instance,
        and you won't get out of capacity errors.
        For more information, see [Reserved Capacity](/iaas/Content/Compute/Tasks/reserve-capacity.htm).

        Args:
            availability_domain(str):
                The availability domain of this compute capacity reservation.

    Example: `Uocm:PHX-AD-1`
    .

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the capacity reservation.
    .

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

            instance_reservation_configs(List[dict[str, Any]], Optional):
                The capacity configurations for the capacity reservation.

    To use the reservation for the desired shape, specify the shape, count, and
    optionally the fault domain where you want this configuration.
    . Defaults to None.

                * cluster_config (dict[str, Any], Optional):
                    clusterConfig

                    * hpc_island_id (str):
                        The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the HPC island.


                    * network_block_ids (List[str], Optional):
                        The list of OCIDs of the network blocks.

                * fault_domain (str, Optional):
                    The fault domain to use for instances created using this capacity configuration.
    For more information, see [Fault Domains](/iaas/Content/General/Concepts/regions.htm#fault).
    If you do not specify the fault domain, the capacity is available for an instance
    that does not specify a fault domain. To change the fault domain for a reservation,
    delete the reservation and create a new one in the preferred fault domain.

    To retrieve a list of fault domains, use the `ListFaultDomains` operation in
    the [Identity and Access Management Service API](/iaas/api/#/en/identity/20160918/).

    Example: `FAULT-DOMAIN-1`


                * instance_shape (str):
                    The shape requested when launching instances using reserved capacity.
    The shape determines the number of CPUs, amount of memory,
    and other resources allocated to the instance.
    You can list all available shapes by calling [ListComputeCapacityReservationInstanceShapes](#/en/iaas/computeCapacityReservationInstanceShapes/ListComputeCapacityReservationInstanceShapes).


                * instance_shape_config (dict[str, Any], Optional):
                    instanceShapeConfig

                    * memory_in_g_bs (float, Optional):
                        The total amount of memory available to the instance, in gigabytes.


                    * ocpus (float, Optional):
                        The total number of OCPUs available to the instance.


                * reserved_count (int):
                    The total number of instances that can be launched from the capacity configuration.

            is_default_reservation(bool, Optional):
                Whether this capacity reservation is the default.
    For more information, see [Capacity Reservations](/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "availability_domain": "availabilityDomain",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "instance_reservation_configs": "instanceReservationConfigs",
        "is_default_reservation": "isDefaultReservation",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/computeCapacityReservations".format(**{}),
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


async def get_compute_capacity_reservation(
    hub, ctx, capacity_reservation_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        GetComputeCapacityReservation
            Gets information about the specified compute capacity reservation.

        Args:
            capacity_reservation_id(str):
                The OCID of the compute capacity reservation.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeCapacityReservations/{capacityReservationId}".format(
            **{"capacityReservationId": capacity_reservation_id}
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "instance_reservation_configs": "instanceReservationConfigs",
            "is_default_reservation": "isDefaultReservation",
            "lifecycle_state": "lifecycleState",
            "reserved_instance_count": "reservedInstanceCount",
            "time_created": "timeCreated",
            "time_updated": "timeUpdated",
            "used_instance_count": "usedInstanceCount",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_compute_capacity_reservation(
    hub,
    ctx,
    capacity_reservation_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    instance_reservation_configs: List[
        make_dataclass(
            "instance_reservation_configs",
            [
                ("instance_shape", str),
                ("reserved_count", int),
                (
                    "cluster_config",
                    make_dataclass(
                        "cluster_config",
                        [
                            ("hpc_island_id", str),
                            ("network_block_ids", List[str], field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
                ("fault_domain", str, field(default=None)),
                (
                    "instance_shape_config",
                    make_dataclass(
                        "instance_shape_config",
                        [
                            ("memory_in_g_bs", float, field(default=None)),
                            ("ocpus", float, field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
            ],
        )
    ] = None,
    is_default_reservation: bool = None,
) -> Dict[str, Any]:
    r"""

        UpdateComputeCapacityReservation
            Updates the specified capacity reservation and its associated capacity configurations.
        Fields that are not provided in the request will not be updated. Capacity configurations that are not included will be deleted.
        Avoid entering confidential information.

        Args:
            capacity_reservation_id(str):
                The OCID of the compute capacity reservation.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

            instance_reservation_configs(List[dict[str, Any]], Optional):
                The capacity configurations for the capacity reservation.

    To use the reservation for the desired shape, specify the shape, count, and
    optionally the fault domain where you want this configuration.
    . Defaults to None.

                * cluster_config (dict[str, Any], Optional):
                    clusterConfig

                    * hpc_island_id (str):
                        The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the HPC island.


                    * network_block_ids (List[str], Optional):
                        The list of OCIDs of the network blocks.

                * fault_domain (str, Optional):
                    The fault domain to use for instances created using this capacity configuration.
    For more information, see [Fault Domains](/iaas/Content/General/Concepts/regions.htm#fault).
    If you do not specify the fault domain, the capacity is available for an instance
    that does not specify a fault domain. To change the fault domain for a reservation,
    delete the reservation and create a new one in the preferred fault domain.

    To retrieve a list of fault domains, use the `ListFaultDomains` operation in
    the [Identity and Access Management Service API](/iaas/api/#/en/identity/20160918/).

    Example: `FAULT-DOMAIN-1`


                * instance_shape (str):
                    The shape requested when launching instances using reserved capacity.
    The shape determines the number of CPUs, amount of memory,
    and other resources allocated to the instance.
    You can list all available shapes by calling [ListComputeCapacityReservationInstanceShapes](#/en/iaas/computeCapacityReservationInstanceShapes/ListComputeCapacityReservationInstanceShapes).


                * instance_shape_config (dict[str, Any], Optional):
                    instanceShapeConfig

                    * memory_in_g_bs (float, Optional):
                        The total amount of memory available to the instance, in gigabytes.


                    * ocpus (float, Optional):
                        The total number of OCPUs available to the instance.


                * reserved_count (int):
                    The total number of instances that can be launched from the capacity configuration.

            is_default_reservation(bool, Optional):
                Whether this capacity reservation is the default.
    For more information, see [Capacity Reservations](/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "instance_reservation_configs": "instanceReservationConfigs",
        "is_default_reservation": "isDefaultReservation",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/computeCapacityReservations/{capacityReservationId}".format(
            **{"capacityReservationId": capacity_reservation_id}
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


async def delete_compute_capacity_reservation(
    hub,
    ctx,
    capacity_reservation_id: str,
    opc_request_id: str = None,
    if_match: str = None,
) -> Dict[str, Any]:
    r"""

        DeleteComputeCapacityReservation
            Deletes the specified compute capacity reservation.

        Args:
            capacity_reservation_id(str):
                The OCID of the compute capacity reservation.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/computeCapacityReservations/{capacityReservationId}".format(
            **{"capacityReservationId": capacity_reservation_id}
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


async def change_compute_capacity_reservation_compartment(
    hub,
    ctx,
    capacity_reservation_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

        ChangeComputeCapacityReservationCompartment
            Moves a compute capacity reservation into a different compartment. For information about
        moving resources between compartments, see
        [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            capacity_reservation_id(str):
                The OCID of the compute capacity reservation.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment
    to move the compute capacity reservation to.
    .

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/computeCapacityReservations/{capacityReservationId}/actions/changeCompartment".format(
            **{"capacityReservationId": capacity_reservation_id}
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


async def list_compute_capacity_reservation_instances(
    hub,
    ctx,
    capacity_reservation_id: str,
    availability_domain: str = None,
    compartment_id: str = None,
    opc_request_id: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListComputeCapacityReservationInstances
            Lists the instances launched under a capacity reservation. You can filter results by specifying criteria.

        Args:
            capacity_reservation_id(str):
                The OCID of the compute capacity reservation.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            compartment_id(str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment. Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeCapacityReservations/{capacityReservationId}/instances".format(
            **{"capacityReservationId": capacity_reservation_id}
        ),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
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


async def list_compute_clusters(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
    opc_request_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListComputeCluster
            Lists the compute clusters in the specified compartment.
        A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) is a remote direct memory access (RDMA) network group.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            display_name(str, Optional):
                A filter to return only resources that match the given display name exactly.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeClusters".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "displayName": display_name,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
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


async def create_compute_cluster(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    opc_retry_token: str = None,
    opc_request_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        CreateComputeCluster
            Creates an empty [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm). A compute cluster
        is a remote direct memory access (RDMA) network group.

        After the compute cluster is created, you can use the compute cluster's OCID with the
        [LaunchInstance](#/en/iaas/latest/Instance/LaunchInstance) operation to create instances in the compute cluster.
        The instances must be created in the same compartment and availability domain as the cluster.

        Use compute clusters when you want to manage instances in the cluster individually, or when you want
        to use different types of instances in the RDMA network group.

        If you want predictable capacity for a specific number of identical instances that are managed as a group,
        create a cluster network that uses instance pools by using the
        [CreateClusterNetwork](#/en/iaas/latest/ClusterNetwork/CreateClusterNetwork) operation.

        Args:
            availability_domain(str):
                The availability domain to place the compute cluster in.

    Example: `Uocm:PHX-AD-1`
    .

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "availability_domain": "availabilityDomain",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/computeClusters".format(**{}),
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_compute_cluster(
    hub, ctx, compute_cluster_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        GetComputeCluster
            Gets information about a compute cluster. A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm)
        is a remote direct memory access (RDMA) network group.

        Args:
            compute_cluster_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compute cluster.
    A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) is a remote direct memory
    access (RDMA) network group.
    .

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeClusters/{computeClusterId}".format(
            **{"computeClusterId": compute_cluster_id}
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_compute_cluster(
    hub,
    ctx,
    compute_cluster_id: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        UpdateComputeCluster
            Updates a compute cluster. A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) is a
        remote direct memory access (RDMA) network group.

        To create instances within a compute cluster, use the [LaunchInstance](#/en/iaas/latest/Instance/LaunchInstance)
        operation.

        To delete instances from a compute cluster, use the [TerminateInstance](#/en/iaas/latest/Instance/TerminateInstance)
        operation.

        Args:
            compute_cluster_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compute cluster.
    A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) is a remote direct memory
    access (RDMA) network group.
    .

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

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
        path="/computeClusters/{computeClusterId}".format(
            **{"computeClusterId": compute_cluster_id}
        ),
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

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_compute_cluster(
    hub, ctx, compute_cluster_id: str, opc_request_id: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteComputeCluster
            Deletes a compute cluster. A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) is a
        remote direct memory access (RDMA) network group.

        Before you delete a compute cluster, first delete all instances in the cluster by using
        the [TerminateInstance](#/en/iaas/latest/Instance/TerminateInstance) operation.

        Args:
            compute_cluster_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compute cluster.
    A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) is a remote direct memory
    access (RDMA) network group.
    .

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/computeClusters/{computeClusterId}".format(
            **{"computeClusterId": compute_cluster_id}
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


async def change_compute_cluster_compartment(
    hub,
    ctx,
    compute_cluster_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

        MoveComputeCluster
            Moves a compute cluster into a different compartment within the same tenancy.
        A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) is a remote direct memory access (RDMA) network group.

        For information about moving resources between compartments, see
        [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            compute_cluster_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compute cluster.
    A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) is a remote direct memory
    access (RDMA) network group.
    .

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the compute cluster to.
    .

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/computeClusters/{computeClusterId}/actions/changeCompartment".format(
            **{"computeClusterId": compute_cluster_id}
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


async def list_compute_global_image_capability_schemas(
    hub,
    ctx,
    compartment_id: str = None,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListComputeGlobalImageCapabilitySchemas
            Lists Compute Global Image Capability Schema in the specified compartment.

        Args:
            compartment_id(str, Optional):
                A filter to return only resources that match the given compartment OCID exactly.
    . Defaults to None.

            display_name(str, Optional):
                A filter to return only resources that match the given display name exactly.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeGlobalImageCapabilitySchemas".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "displayName": display_name,
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


async def get_compute_global_image_capability_schema(
    hub, ctx, compute_global_image_capability_schema_id: str
) -> Dict[str, Any]:
    r"""

    GetComputeGlobalImageCapabilitySchema
        Gets the specified Compute Global Image Capability Schema

    Args:
        compute_global_image_capability_schema_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compute global image capability schema.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeGlobalImageCapabilitySchemas/{computeGlobalImageCapabilitySchemaId}".format(
            **{
                "computeGlobalImageCapabilitySchemaId": compute_global_image_capability_schema_id
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
            "compartment_id": "compartmentId",
            "current_version_name": "currentVersionName",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_compute_global_image_capability_schema_versions(
    hub,
    ctx,
    compute_global_image_capability_schema_id: str,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListComputeGlobalImageCapabilitySchemaVersions
            Lists Compute Global Image Capability Schema versions in the specified compartment.

        Args:
            compute_global_image_capability_schema_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compute global image capability schema.

            display_name(str, Optional):
                A filter to return only resources that match the given display name exactly.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeGlobalImageCapabilitySchemas/{computeGlobalImageCapabilitySchemaId}/versions".format(
            **{
                "computeGlobalImageCapabilitySchemaId": compute_global_image_capability_schema_id
            }
        ),
        query_params={
            "displayName": display_name,
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


async def get_compute_global_image_capability_schema_version(
    hub,
    ctx,
    compute_global_image_capability_schema_id: str,
    compute_global_image_capability_schema_version_name: str,
) -> Dict[str, Any]:
    r"""

    GetComputeGlobalImageCapabilitySchemaVersion
        Gets the specified Compute Global Image Capability Schema Version

    Args:
        compute_global_image_capability_schema_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compute global image capability schema.

        compute_global_image_capability_schema_version_name(str):
            The name of the compute global image capability schema version.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeGlobalImageCapabilitySchemas/{computeGlobalImageCapabilitySchemaId}/versions/{computeGlobalImageCapabilitySchemaVersionName}".format(
            **{
                "computeGlobalImageCapabilitySchemaId": compute_global_image_capability_schema_id,
                "computeGlobalImageCapabilitySchemaVersionName": compute_global_image_capability_schema_version_name,
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
            "compute_global_image_capability_schema_id": "computeGlobalImageCapabilitySchemaId",
            "display_name": "displayName",
            "name": "name",
            "schema_data": "schemaData",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_compute_image_capability_schemas(
    hub,
    ctx,
    compartment_id: str = None,
    image_id: str = None,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListComputeImageCapabilitySchemas
            Lists Compute Image Capability Schema in the specified compartment. You can also query by a specific imageId.

        Args:
            compartment_id(str, Optional):
                A filter to return only resources that match the given compartment OCID exactly.
    . Defaults to None.

            image_id(str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of an image. Defaults to None.

            display_name(str, Optional):
                A filter to return only resources that match the given display name exactly.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeImageCapabilitySchemas".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "imageId": image_id,
            "displayName": display_name,
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


async def create_compute_image_capability_schema(
    hub,
    ctx,
    compartment_id: str,
    compute_global_image_capability_schema_version_name: str,
    image_id: str,
    schema_data: Dict,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        CreateComputeImageCapabilitySchema
            Creates compute image capability schema.

        Args:
            compartment_id(str):
                The OCID of the compartment that contains the resource.

            compute_global_image_capability_schema_version_name(str):
                The name of the compute global image capability schema version
    .

            image_id(str):
                The ocid of the image
    .

            schema_data(Dict):
                The map of each capability name to its ImageCapabilitySchemaDescriptor.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "compute_global_image_capability_schema_version_name": "computeGlobalImageCapabilitySchemaVersionName",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "image_id": "imageId",
        "schema_data": "schemaData",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/computeImageCapabilitySchemas".format(**{}),
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
            "compartment_id": "compartmentId",
            "compute_global_image_capability_schema_id": "computeGlobalImageCapabilitySchemaId",
            "compute_global_image_capability_schema_version_name": "computeGlobalImageCapabilitySchemaVersionName",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "schema_data": "schemaData",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_compute_image_capability_schema(
    hub, ctx, compute_image_capability_schema_id: str, is_merge_enabled: bool = None
) -> Dict[str, Any]:
    r"""

        GetComputeImageCapabilitySchema
            Gets the specified Compute Image Capability Schema

        Args:
            compute_image_capability_schema_id(str):
                The id of the compute image capability schema or the image ocid.

            is_merge_enabled(bool, Optional):
                Merge the image capability schema with the global image capability schema
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/computeImageCapabilitySchemas/{computeImageCapabilitySchemaId}".format(
            **{"computeImageCapabilitySchemaId": compute_image_capability_schema_id}
        ),
        query_params={"isMergeEnabled": is_merge_enabled},
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
            "compartment_id": "compartmentId",
            "compute_global_image_capability_schema_id": "computeGlobalImageCapabilitySchemaId",
            "compute_global_image_capability_schema_version_name": "computeGlobalImageCapabilitySchemaVersionName",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "schema_data": "schemaData",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_compute_image_capability_schema(
    hub,
    ctx,
    compute_image_capability_schema_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    schema_data: Dict = None,
) -> Dict[str, Any]:
    r"""

        UpdateComputeImageCapabilitySchema
            Updates the specified Compute Image Capability Schema

        Args:
            compute_image_capability_schema_id(str):
                The id of the compute image capability schema or the image ocid.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

            schema_data(Dict, Optional):
                The map of each capability name to its ImageCapabilitySchemaDescriptor. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "schema_data": "schemaData",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/computeImageCapabilitySchemas/{computeImageCapabilitySchemaId}".format(
            **{"computeImageCapabilitySchemaId": compute_image_capability_schema_id}
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
            "compartment_id": "compartmentId",
            "compute_global_image_capability_schema_id": "computeGlobalImageCapabilitySchemaId",
            "compute_global_image_capability_schema_version_name": "computeGlobalImageCapabilitySchemaVersionName",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "schema_data": "schemaData",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_compute_image_capability_schema(
    hub, ctx, compute_image_capability_schema_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteComputeImageCapabilitySchema
            Deletes the specified Compute Image Capability Schema

        Args:
            compute_image_capability_schema_id(str):
                The id of the compute image capability schema or the image ocid.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/computeImageCapabilitySchemas/{computeImageCapabilitySchemaId}".format(
            **{"computeImageCapabilitySchemaId": compute_image_capability_schema_id}
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


async def change_compute_image_capability_schema_compartment(
    hub,
    ctx,
    compute_image_capability_schema_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

        ChangeComputeImageCapabilitySchemaCompartment
            Moves a compute image capability schema into a different compartment within the same tenancy.
        For information about moving resources between compartments, see
                [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            compute_image_capability_schema_id(str):
                The id of the compute image capability schema or the image ocid.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to
    move the instance configuration to.
    .

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/computeImageCapabilitySchemas/{computeImageCapabilitySchemaId}/actions/changeCompartment".format(
            **{"computeImageCapabilitySchemaId": compute_image_capability_schema_id}
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


async def list_dedicated_vm_host_instance_shapes(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    dedicated_vm_host_shape: str = None,
    limit: int = None,
    page: str = None,
    opc_request_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListDedicatedVmHostInstanceShapes
            Lists the shapes that can be used to launch a virtual machine instance on a dedicated virtual machine host within the specified compartment.
        You can filter the list by compatibility with a specific dedicated virtual machine host shape.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            dedicated_vm_host_shape(str, Optional):
                Dedicated VM host shape name
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/dedicatedVmHostInstanceShapes".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "dedicatedVmHostShape": dedicated_vm_host_shape,
            "limit": limit,
            "page": page,
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


async def list_dedicated_vm_host_shapes(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    instance_shape_name: str = None,
    limit: int = None,
    page: str = None,
    opc_request_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListDedicatedVmHostShapes
            Lists the shapes that can be used to launch a dedicated virtual machine host within the specified compartment.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            instance_shape_name(str, Optional):
                The name for the instance's shape.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/dedicatedVmHostShapes".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "instanceShapeName": instance_shape_name,
            "limit": limit,
            "page": page,
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


async def list_dedicated_vm_hosts(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    lifecycle_state: str = None,
    display_name: str = None,
    instance_shape_name: str = None,
    limit: int = None,
    page: str = None,
    opc_request_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
    remaining_memory_in_g_bs_greater_than_or_equal_to: float = None,
    remaining_ocpus_greater_than_or_equal_to: float = None,
) -> Dict[str, Any]:
    r"""

        ListDedicatedVmHosts
            Returns the list of dedicated virtual machine hosts that match the specified criteria in the specified compartment.

        You can limit the list by specifying a dedicated virtual machine host display name. The list will include all the identically-named
        dedicated virtual machine hosts in the compartment.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            lifecycle_state(str, Optional):
                A filter to only return resources that match the given lifecycle state. Defaults to None.

            display_name(str, Optional):
                A filter to return only resources that match the given display name exactly.
    . Defaults to None.

            instance_shape_name(str, Optional):
                The name for the instance's shape.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

            remaining_memory_in_g_bs_greater_than_or_equal_to(float, Optional):
                The remaining memory of the dedicated VM host, in GBs. Defaults to None.

            remaining_ocpus_greater_than_or_equal_to(float, Optional):
                The available OCPUs of the dedicated VM host. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/dedicatedVmHosts".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "lifecycleState": lifecycle_state,
            "displayName": display_name,
            "instanceShapeName": instance_shape_name,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "remainingMemoryInGBsGreaterThanOrEqualTo": remaining_memory_in_g_bs_greater_than_or_equal_to,
            "remainingOcpusGreaterThanOrEqualTo": remaining_ocpus_greater_than_or_equal_to,
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


async def create_dedicated_vm_host(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    dedicated_vm_host_shape: str,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    fault_domain: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        CreateDedicatedVmHost
            Creates a new dedicated virtual machine host in the specified compartment and the specified availability domain.
        Dedicated virtual machine hosts enable you to run your Compute virtual machine (VM) instances on dedicated servers
        that are a single tenant and not shared with other customers.
        For more information, see [Dedicated Virtual Machine Hosts](/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm).

        Args:
            availability_domain(str):
                The availability domain of the dedicated virtual machine host.

    Example: `Uocm:PHX-AD-1`
    .

            compartment_id(str):
                The OCID of the compartment.

            dedicated_vm_host_shape(str):
                The dedicated virtual machine host shape. The shape determines the number of CPUs and
    other resources available for VM instances launched on the dedicated virtual machine host.
    .

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            fault_domain(str, Optional):
                The fault domain for the dedicated virtual machine host's assigned instances.
    For more information, see [Fault Domains](/iaas/Content/General/Concepts/regions.htm#fault).
    If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host,
    delete it and create a new dedicated virtual machine host in the preferred fault domain.

    To get a list of fault domains, use the `ListFaultDomains` operation in
    the [Identity and Access Management Service API](/iaas/api/#/en/identity/20160918/).

    Example: `FAULT-DOMAIN-1`
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "availability_domain": "availabilityDomain",
        "compartment_id": "compartmentId",
        "dedicated_vm_host_shape": "dedicatedVmHostShape",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "fault_domain": "faultDomain",
        "freeform_tags": "freeformTags",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/dedicatedVmHosts".format(**{}),
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "dedicated_vm_host_shape": "dedicatedVmHostShape",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "fault_domain": "faultDomain",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "remaining_memory_in_g_bs": "remainingMemoryInGBs",
            "remaining_ocpus": "remainingOcpus",
            "time_created": "timeCreated",
            "total_memory_in_g_bs": "totalMemoryInGBs",
            "total_ocpus": "totalOcpus",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_dedicated_vm_host(
    hub, ctx, dedicated_vm_host_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        GetDedicatedVmHost
            Gets information about the specified dedicated virtual machine host.

        Args:
            dedicated_vm_host_id(str):
                The OCID of the dedicated VM host.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/dedicatedVmHosts/{dedicatedVmHostId}".format(
            **{"dedicatedVmHostId": dedicated_vm_host_id}
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "dedicated_vm_host_shape": "dedicatedVmHostShape",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "fault_domain": "faultDomain",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "remaining_memory_in_g_bs": "remainingMemoryInGBs",
            "remaining_ocpus": "remainingOcpus",
            "time_created": "timeCreated",
            "total_memory_in_g_bs": "totalMemoryInGBs",
            "total_ocpus": "totalOcpus",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_dedicated_vm_host(
    hub,
    ctx,
    dedicated_vm_host_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        UpdateDedicatedVmHost
            Updates the displayName, freeformTags, and definedTags attributes for the specified dedicated virtual machine host.
        If an attribute value is not included, it will not be updated.

        Args:
            dedicated_vm_host_id(str):
                The OCID of the dedicated VM host.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

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
        path="/dedicatedVmHosts/{dedicatedVmHostId}".format(
            **{"dedicatedVmHostId": dedicated_vm_host_id}
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

    # Convert raw response into present format
    raw_resource = ret["ret"]

    resource_in_present_format = {}
    resource_parameters = OrderedDict(
        {
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "dedicated_vm_host_shape": "dedicatedVmHostShape",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "fault_domain": "faultDomain",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "remaining_memory_in_g_bs": "remainingMemoryInGBs",
            "remaining_ocpus": "remainingOcpus",
            "time_created": "timeCreated",
            "total_memory_in_g_bs": "totalMemoryInGBs",
            "total_ocpus": "totalOcpus",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_dedicated_vm_host(
    hub, ctx, dedicated_vm_host_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        DeleteDedicatedVmHost
            Deletes the specified dedicated virtual machine host.

        If any VM instances are assigned to the dedicated virtual machine host,
        the delete operation will fail and the service will return a 409 response code.

        Args:
            dedicated_vm_host_id(str):
                The OCID of the dedicated VM host.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/dedicatedVmHosts/{dedicatedVmHostId}".format(
            **{"dedicatedVmHostId": dedicated_vm_host_id}
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


async def change_dedicated_vm_host_compartment(
    hub,
    ctx,
    dedicated_vm_host_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

        ChangeDedicatedVmHostCompartment
            Moves a dedicated virtual machine host from one compartment to another.

        Args:
            dedicated_vm_host_id(str):
                The OCID of the dedicated VM host.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment
    to move the dedicated virtual machine host to.
    .

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/dedicatedVmHosts/{dedicatedVmHostId}/actions/changeCompartment".format(
            **{"dedicatedVmHostId": dedicated_vm_host_id}
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


async def list_dedicated_vm_host_instances(
    hub,
    ctx,
    compartment_id: str,
    dedicated_vm_host_id: str,
    availability_domain: str = None,
    limit: int = None,
    page: str = None,
    opc_request_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListDedicatedVmHostInstances
            Returns the list of instances on the dedicated virtual machine hosts that match the specified criteria.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            dedicated_vm_host_id(str):
                The OCID of the dedicated VM host.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/dedicatedVmHosts/{dedicatedVmHostId}/instances".format(
            **{"dedicatedVmHostId": dedicated_vm_host_id}
        ),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
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


async def list_images(
    hub,
    ctx,
    compartment_id: str,
    display_name: str = None,
    operating_system: str = None,
    operating_system_version: str = None,
    shape: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

        ListImages
            Lists a subset of images available in the specified compartment, including
        [platform images](/iaas/Content/Compute/References/images.htm) and
        [custom images](/iaas/Content/Compute/Tasks/managingcustomimages.htm).
        The list of platform images includes the three most recently published versions
        of each major distribution. The list does not support filtering based on image tags.

        The list of images returned is ordered to first show the recent platform images,
        then all of the custom images.

        **Caution:** Platform images are refreshed regularly. When new images are released, older versions are replaced.
        The image OCIDs remain available, but when the platform image is replaced, the image OCIDs are no longer returned as part of the platform image list.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            display_name(str, Optional):
                A filter to return only resources that match the given display name exactly.
    . Defaults to None.

            operating_system(str, Optional):
                The image's operating system.

    Example: `Oracle Linux`
    . Defaults to None.

            operating_system_version(str, Optional):
                The image's operating system version.

    Example: `7.2`
    . Defaults to None.

            shape(str, Optional):
                Shape name. Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

            lifecycle_state(str, Optional):
                A filter to only return resources that match the given lifecycle state. The state
    value is case-insensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/images".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "displayName": display_name,
            "operatingSystem": operating_system,
            "operatingSystemVersion": operating_system_version,
            "shape": shape,
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


async def create_image(
    hub,
    ctx,
    compartment_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    image_source_details: make_dataclass(
        "image_source_details",
        [
            ("source_type", str),
            ("operating_system", str, field(default=None)),
            ("operating_system_version", str, field(default=None)),
            ("source_image_type", str, field(default=None)),
        ],
    ) = None,
    instance_id: str = None,
    launch_mode: str = None,
    launch_options: make_dataclass(
        "launch_options",
        [
            ("boot_volume_type", str, field(default=None)),
            ("firmware", str, field(default=None)),
            ("is_consistent_volume_naming_enabled", bool, field(default=None)),
            ("is_pv_encryption_in_transit_enabled", bool, field(default=None)),
            ("network_type", str, field(default=None)),
            ("remote_data_volume_type", str, field(default=None)),
        ],
    ) = None,
) -> Dict[str, Any]:
    r"""

        CreateImage
            Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service.

        When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and
        the OCID of the compartment containing that instance. For more information about images,
        see [Managing Custom Images](/iaas/Content/Compute/Tasks/managingcustomimages.htm).

        When importing an exported image from Object Storage, you specify the source information
        in [ImageSourceDetails](#/en/iaas/latest/requests/ImageSourceDetails).

        When importing an image based on the namespace, bucket name, and object name,
        use [ImageSourceViaObjectStorageTupleDetails](#/en/iaas/latest/requests/ImageSourceViaObjectStorageTupleDetails).

        When importing an image based on the Object Storage URL, use
        [ImageSourceViaObjectStorageUriDetails](#/en/iaas/latest/requests/ImageSourceViaObjectStorageUriDetails).
        See [Object Storage URLs](/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs) and [Using Pre-Authenticated Requests](/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
        for constructing URLs for image import/export.

        For more information about importing exported images, see
        [Image Import/Export](/iaas/Content/Compute/Tasks/imageimportexport.htm).

        You may optionally specify a *display name* for the image, which is simply a friendly name or description.
        It does not have to be unique, and you can change it. See [UpdateImage](#/en/iaas/latest/Image/UpdateImage).
        Avoid entering confidential information.

        Args:
            compartment_id(str):
                The OCID of the compartment you want the image to be created in.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name for the image. It does not have to be unique, and it's changeable.
    Avoid entering confidential information.

    You cannot use a platform image name as a custom image name.

    Example: `My Oracle Linux image`
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

            image_source_details(dict[str, Any], Optional):
                imageSourceDetails. Defaults to None.

                * operating_system (str, Optional):
                    operatingSystem

                * operating_system_version (str, Optional):
                    operatingSystemVersion

                * source_image_type (str, Optional):
                    The format of the image to be imported. Only monolithic
    images are supported. This attribute is not used for exported Oracle images with the OCI image format.


                * source_type (str):
                    The source type for the image. Use `objectStorageTuple` when specifying the namespace,
    bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.


            instance_id(str, Optional):
                The OCID of the instance you want to use as the basis for the image.
    . Defaults to None.

            launch_mode(str, Optional):
                Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
    * `NATIVE` - VM instances launch with paravirtualized boot and VFIO devices. The default value for platform images.
    * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
    * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
    * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.
    . Defaults to None.

            launch_options(dict[str, Any], Optional):
                launchOptions. Defaults to None.

                * boot_volume_type (str, Optional):
                    Emulation type for the boot volume.
    * `ISCSI` - ISCSI attached block storage device.
    * `SCSI` - Emulated SCSI disk.
    * `IDE` - Emulated IDE disk.
    * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
    volumes on platform images.
    * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
    storage volumes on platform images.


                * firmware (str, Optional):
                    Firmware used to boot VM. Select the option that matches your operating system.
    * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
    systems that boot using MBR style bootloaders.
    * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
    default for platform images.


                * is_consistent_volume_naming_enabled (bool, Optional):
                    Whether to enable consistent volume naming feature. Defaults to false.

                * is_pv_encryption_in_transit_enabled (bool, Optional):
                    Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
    [LaunchInstanceDetails](#/en/iaas/latest/datatypes/LaunchInstanceDetails).


                * network_type (str, Optional):
                    Emulation type for the physical network interface card (NIC).
    * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
    * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
    when you launch an instance using hardware-assisted (SR-IOV) networking.
    * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.


                * remote_data_volume_type (str, Optional):
                    Emulation type for volume.
    * `ISCSI` - ISCSI attached block storage device.
    * `SCSI` - Emulated SCSI disk.
    * `IDE` - Emulated IDE disk.
    * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
    volumes on platform images.
    * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
    storage volumes on platform images.

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
        "image_source_details": "imageSourceDetails",
        "instance_id": "instanceId",
        "launch_mode": "launchMode",
        "launch_options": "launchOptions",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/images".format(**{}),
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
            "agent_features": "agentFeatures",
            "base_image_id": "baseImageId",
            "billable_size_in_g_bs": "billableSizeInGBs",
            "compartment_id": "compartmentId",
            "create_image_allowed": "createImageAllowed",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "launch_mode": "launchMode",
            "launch_options": "launchOptions",
            "lifecycle_state": "lifecycleState",
            "operating_system": "operatingSystem",
            "operating_system_version": "operatingSystemVersion",
            "size_in_m_bs": "sizeInMBs",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_image(hub, ctx, image_id: str) -> Dict[str, Any]:
    r"""

    GetImage
        Gets the specified image.

    Args:
        image_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the image.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/images/{imageId}".format(**{"imageId": image_id}),
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
            "agent_features": "agentFeatures",
            "base_image_id": "baseImageId",
            "billable_size_in_g_bs": "billableSizeInGBs",
            "compartment_id": "compartmentId",
            "create_image_allowed": "createImageAllowed",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "launch_mode": "launchMode",
            "launch_options": "launchOptions",
            "lifecycle_state": "lifecycleState",
            "operating_system": "operatingSystem",
            "operating_system_version": "operatingSystemVersion",
            "size_in_m_bs": "sizeInMBs",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_image(
    hub,
    ctx,
    image_id: str,
    opc_retry_token: str = None,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    operating_system: str = None,
    operating_system_version: str = None,
) -> Dict[str, Any]:
    r"""

        UpdateImage
            Updates the display name of the image. Avoid entering confidential information.

        Args:
            image_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the image.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

            operating_system(str, Optional):
                Operating system

    Example: `Oracle Linux`
    . Defaults to None.

            operating_system_version(str, Optional):
                Operating system version

    Example: `7.4`
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "operating_system": "operatingSystem",
        "operating_system_version": "operatingSystemVersion",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/images/{imageId}".format(**{"imageId": image_id}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token, "if-match": if_match},
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
            "agent_features": "agentFeatures",
            "base_image_id": "baseImageId",
            "billable_size_in_g_bs": "billableSizeInGBs",
            "compartment_id": "compartmentId",
            "create_image_allowed": "createImageAllowed",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "launch_mode": "launchMode",
            "launch_options": "launchOptions",
            "lifecycle_state": "lifecycleState",
            "operating_system": "operatingSystem",
            "operating_system_version": "operatingSystemVersion",
            "size_in_m_bs": "sizeInMBs",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_image(hub, ctx, image_id: str, if_match: str = None) -> Dict[str, Any]:
    r"""

        DeleteImage
            Deletes an image.

        Args:
            image_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the image.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/images/{imageId}".format(**{"imageId": image_id}),
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


async def change_image_compartment(
    hub,
    ctx,
    image_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

        ChangeImageCompartment
            Moves an image into a different compartment within the same tenancy. For information about moving
        resources between compartments, see
        [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            image_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the image.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the image to.
    .

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/images/{imageId}/actions/changeCompartment".format(
            **{"imageId": image_id}
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


async def export_image(
    hub,
    ctx,
    image_id: str,
    destination_type: str,
    opc_retry_token: str = None,
    if_match: str = None,
    export_format: str = None,
) -> Dict[str, Any]:
    r"""

        ExportImage
            Exports the specified image to the Oracle Cloud Infrastructure Object Storage service. You can use the Object Storage URL,
        or the namespace, bucket name, and object name when specifying the location to export to.

        For more information about exporting images, see [Image Import/Export](/iaas/Content/Compute/Tasks/imageimportexport.htm).

        To perform an image export, you need write access to the Object Storage bucket for the image,
        see [Let Users Write Objects to Object Storage Buckets](/iaas/Content/Identity/Concepts/commonpolicies.htm#Let4).

        See [Object Storage URLs](/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs) and [Using Pre-Authenticated Requests](/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
        for constructing URLs for image import/export.

        Args:
            image_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the image.

            destination_type(str):
                The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name.
    Use `objectStorageUri` when specifying the Object Storage URL.
    .

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            export_format(str, Optional):
                The format to export the image to. The default value is `OCI`.

    The following image formats are available:

    - `OCI` - Oracle Cloud Infrastructure file with a QCOW2 image and Oracle Cloud Infrastructure metadata (.oci).
    Use this format to export a custom image that you want to import into other tenancies or regions.
    - `QCOW2` - QEMU Copy On Write (.qcow2)
    - `VDI` - Virtual Disk Image (.vdi) for Oracle VM VirtualBox
    - `VHD` - Virtual Hard Disk (.vhd) for Hyper-V
    - `VMDK` - Virtual Machine Disk (.vmdk)
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"destination_type": "destinationType", "export_format": "exportFormat"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/images/{imageId}/actions/export".format(**{"imageId": image_id}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token, "if-match": if_match},
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
            "agent_features": "agentFeatures",
            "base_image_id": "baseImageId",
            "billable_size_in_g_bs": "billableSizeInGBs",
            "compartment_id": "compartmentId",
            "create_image_allowed": "createImageAllowed",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "launch_mode": "launchMode",
            "launch_options": "launchOptions",
            "lifecycle_state": "lifecycleState",
            "operating_system": "operatingSystem",
            "operating_system_version": "operatingSystemVersion",
            "size_in_m_bs": "sizeInMBs",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_image_shape_compatibility_entries(
    hub,
    ctx,
    image_id: str,
    limit: int = None,
    page: str = None,
    opc_request_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListImageShapeCompatibilityEntries
            Lists the compatible shapes for the specified image.

        Args:
            image_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the image.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/images/{imageId}/shapes".format(**{"imageId": image_id}),
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


async def get_image_shape_compatibility_entry(
    hub, ctx, image_id: str, shape_name: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        GetImageShapeCompatibilityEntry
            Retrieves an image shape compatibility entry.

        Args:
            image_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the image.

            shape_name(str):
                Shape name.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/images/{imageId}/shapes/{shapeName}".format(
            **{"imageId": image_id, "shapeName": shape_name}
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
            "image_id": "imageId",
            "memory_constraints": "memoryConstraints",
            "ocpu_constraints": "ocpuConstraints",
            "shape": "shape",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def add_image_shape_compatibility_entry(
    hub,
    ctx,
    image_id: str,
    shape_name: str,
    memory_constraints: make_dataclass(
        "memory_constraints",
        [
            ("max_in_g_bs", int, field(default=None)),
            ("min_in_g_bs", int, field(default=None)),
        ],
    ) = None,
    ocpu_constraints: make_dataclass(
        "ocpu_constraints",
        [("max", int, field(default=None)), ("min", int, field(default=None))],
    ) = None,
) -> Dict[str, Any]:
    r"""

    AddImageShapeCompatibilityEntry
        Adds a shape to the compatible shapes list for the image.

    Args:
        image_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the image.

        shape_name(str):
            Shape name.

        memory_constraints(dict[str, Any], Optional):
            memoryConstraints. Defaults to None.

            * max_in_g_bs (int, Optional):
                The maximum amount of memory, in gigabytes.

            * min_in_g_bs (int, Optional):
                The minimum amount of memory, in gigabytes.

        ocpu_constraints(dict[str, Any], Optional):
            ocpuConstraints. Defaults to None.

            * max (int, Optional):
                The maximum number of OCPUs supported for this image and shape.

            * min (int, Optional):
                The minimum number of OCPUs supported for this image and shape.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "memory_constraints": "memoryConstraints",
        "ocpu_constraints": "ocpuConstraints",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/images/{imageId}/shapes/{shapeName}".format(
            **{"imageId": image_id, "shapeName": shape_name}
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
            "image_id": "imageId",
            "memory_constraints": "memoryConstraints",
            "ocpu_constraints": "ocpuConstraints",
            "shape": "shape",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def remove_image_shape_compatibility_entry(
    hub, ctx, image_id: str, shape_name: str
) -> Dict[str, Any]:
    r"""

    RemoveImageShapeCompatibilityEntry
        Removes a shape from the compatible shapes list for the image.

    Args:
        image_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the image.

        shape_name(str):
            Shape name.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/images/{imageId}/shapes/{shapeName}".format(
            **{"imageId": image_id, "shapeName": shape_name}
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


async def list_instance_console_connections(
    hub,
    ctx,
    compartment_id: str,
    instance_id: str = None,
    limit: int = None,
    page: str = None,
) -> Dict[str, Any]:
    r"""

        ListInstanceConsoleConnections
            Lists the console connections for the specified compartment or instance.

        For more information about instance console connections, see [Troubleshooting Instances Using Instance Console Connections](/iaas/Content/Compute/References/serialconsole.htm).

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            instance_id(str, Optional):
                The OCID of the instance. Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instanceConsoleConnections".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "instanceId": instance_id,
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


async def create_instance_console_connection(
    hub,
    ctx,
    instance_id: str,
    public_key: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        CreateInstanceConsoleConnection
            Creates a new console connection to the specified instance.
        After the console connection has been created and is available,
        you connect to the console using SSH.

        For more information about instance console connections, see [Troubleshooting Instances Using Instance Console Connections](/iaas/Content/Compute/References/serialconsole.htm).

        Args:
            instance_id(str):
                The OCID of the instance to create the console connection to.

            public_key(str):
                The SSH public key used to authenticate the console connection.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "freeform_tags": "freeformTags",
        "instance_id": "instanceId",
        "public_key": "publicKey",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instanceConsoleConnections".format(**{}),
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
            "compartment_id": "compartmentId",
            "connection_string": "connectionString",
            "defined_tags": "definedTags",
            "fingerprint": "fingerprint",
            "freeform_tags": "freeformTags",
            "id": "id",
            "instance_id": "instanceId",
            "lifecycle_state": "lifecycleState",
            "service_host_key_fingerprint": "serviceHostKeyFingerprint",
            "vnc_connection_string": "vncConnectionString",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_instance_console_connection(
    hub, ctx, instance_console_connection_id: str
) -> Dict[str, Any]:
    r"""

    GetInstanceConsoleConnection
        Gets the specified instance console connection's information.

    Args:
        instance_console_connection_id(str):
            The OCID of the instance console connection.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instanceConsoleConnections/{instanceConsoleConnectionId}".format(
            **{"instanceConsoleConnectionId": instance_console_connection_id}
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
            "compartment_id": "compartmentId",
            "connection_string": "connectionString",
            "defined_tags": "definedTags",
            "fingerprint": "fingerprint",
            "freeform_tags": "freeformTags",
            "id": "id",
            "instance_id": "instanceId",
            "lifecycle_state": "lifecycleState",
            "service_host_key_fingerprint": "serviceHostKeyFingerprint",
            "vnc_connection_string": "vncConnectionString",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_instance_console_connection(
    hub,
    ctx,
    instance_console_connection_id: str,
    opc_request_id: str = None,
    if_match: str = None,
    defined_tags: Dict = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        UpdateInstanceConsoleConnection
            Updates the defined tags and free-form tags for the specified instance console connection.

        Args:
            instance_console_connection_id(str):
                The OCID of the instance console connection.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"defined_tags": "definedTags", "freeform_tags": "freeformTags"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/instanceConsoleConnections/{instanceConsoleConnectionId}".format(
            **{"instanceConsoleConnectionId": instance_console_connection_id}
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
            "compartment_id": "compartmentId",
            "connection_string": "connectionString",
            "defined_tags": "definedTags",
            "fingerprint": "fingerprint",
            "freeform_tags": "freeformTags",
            "id": "id",
            "instance_id": "instanceId",
            "lifecycle_state": "lifecycleState",
            "service_host_key_fingerprint": "serviceHostKeyFingerprint",
            "vnc_connection_string": "vncConnectionString",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_instance_console_connection(
    hub, ctx, instance_console_connection_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteInstanceConsoleConnection
            Deletes the specified instance console connection.

        Args:
            instance_console_connection_id(str):
                The OCID of the instance console connection.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/instanceConsoleConnections/{instanceConsoleConnectionId}".format(
            **{"instanceConsoleConnectionId": instance_console_connection_id}
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


async def list_console_histories(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    limit: int = None,
    page: str = None,
    instance_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

        ListConsoleHistories
            Lists the console history metadata for the specified compartment or instance.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            instance_id(str, Optional):
                The OCID of the instance. Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

            lifecycle_state(str, Optional):
                A filter to only return resources that match the given lifecycle state. The state
    value is case-insensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instanceConsoleHistories/".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "instanceId": instance_id,
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


async def capture_console_history(
    hub,
    ctx,
    instance_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        CaptureConsoleHistory
            Captures the most recent serial console data (up to a megabyte) for the
        specified instance.

        The `CaptureConsoleHistory` operation works with the other console history operations
        as described below.

        1. Use `CaptureConsoleHistory` to request the capture of up to a megabyte of the
        most recent console history. This call returns a `ConsoleHistory`
        object. The object will have a state of REQUESTED.
        2. Wait for the capture operation to succeed by polling `GetConsoleHistory` with
        the identifier of the console history metadata. The state of the
        `ConsoleHistory` object will go from REQUESTED to GETTING-HISTORY and
        then SUCCEEDED (or FAILED).
        3. Use `GetConsoleHistoryContent` to get the actual console history data (not the
        metadata).
        4. Optionally, use `DeleteConsoleHistory` to delete the console history metadata
        and the console history data.

        Args:
            instance_id(str):
                The OCID of the instance to get the console history from.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "instance_id": "instanceId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instanceConsoleHistories/".format(**{}),
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "instance_id": "instanceId",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_console_history(
    hub, ctx, instance_console_history_id: str
) -> Dict[str, Any]:
    r"""

    GetConsoleHistory
        Shows the metadata for the specified console history.
    See [CaptureConsoleHistory](#/en/iaas/latest/ConsoleHistory/CaptureConsoleHistory)
    for details about using the console history operations.

    Args:
        instance_console_history_id(str):
            The OCID of the console history.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instanceConsoleHistories/{instanceConsoleHistoryId}".format(
            **{"instanceConsoleHistoryId": instance_console_history_id}
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "instance_id": "instanceId",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_console_history(
    hub,
    ctx,
    instance_console_history_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        UpdateConsoleHistory
            Updates the specified console history metadata.

        Args:
            instance_console_history_id(str):
                The OCID of the console history.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            defined_tags(Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            freeform_tags(Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`
    . Defaults to None.

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
        path="/instanceConsoleHistories/{instanceConsoleHistoryId}".format(
            **{"instanceConsoleHistoryId": instance_console_history_id}
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "instance_id": "instanceId",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_console_history(
    hub, ctx, instance_console_history_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteConsoleHistory
            Deletes the specified console history metadata and the console history data.

        Args:
            instance_console_history_id(str):
                The OCID of the console history.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/instanceConsoleHistories/{instanceConsoleHistoryId}".format(
            **{"instanceConsoleHistoryId": instance_console_history_id}
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


async def get_console_history_content(
    hub, ctx, instance_console_history_id: str, offset: int = None, length: int = None
) -> Dict[str, Any]:
    r"""

    GetConsoleHistoryContent
        Gets the actual console history data (not the metadata).
    See [CaptureConsoleHistory](#/en/iaas/latest/ConsoleHistory/CaptureConsoleHistory)
    for details about using the console history operations.

    Args:
        instance_console_history_id(str):
            The OCID of the console history.

        offset(int, Optional):
            Offset of the snapshot data to retrieve. Defaults to None.

        length(int, Optional):
            Length of the snapshot data to retrieve. Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instanceConsoleHistories/{instanceConsoleHistoryId}/data".format(
            **{"instanceConsoleHistoryId": instance_console_history_id}
        ),
        query_params={"offset": offset, "length": length},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]
    return result


async def instance_action(
    hub,
    ctx,
    instance_id: str,
    action: str,
    action_type: str,
    opc_retry_token: str = None,
    if_match: str = None,
) -> Dict[str, Any]:
    r"""

        InstanceAction
            Performs one of the following power actions on the specified instance:

        - **START** - Powers on the instance.

        - **STOP** - Powers off the instance.

        - **RESET** - Powers off the instance and then powers it back on.

        - **SOFTSTOP** - Gracefully shuts down the instance by sending a shutdown command to the operating system.
        After waiting 15 minutes for the OS to shut down, the instance is powered off.
        If the applications that run on the instance take more than 15 minutes to shut down, they could be improperly stopped, resulting
        in data corruption. To avoid this, manually shut down the instance using the commands available in the OS before you softstop the
        instance.

        - **SOFTRESET** - Gracefully reboots the instance by sending a shutdown command to the operating system.
        After waiting 15 minutes for the OS to shut down, the instance is powered off and
        then powered back on.


        - **SENDDIAGNOSTICINTERRUPT** - For advanced users. **Caution: Sending a diagnostic interrupt to a live system can
        cause data corruption or system failure.** Sends a diagnostic interrupt that causes the instance's
        OS to crash and then reboot. Before you send a diagnostic interrupt, you must configure the instance to generate a
        crash dump file when it crashes. The crash dump captures information about the state of the OS at the time of
        the crash. After the OS restarts, you can analyze the crash dump to diagnose the issue. For more information, see
        [Sending a Diagnostic Interrupt](/iaas/Content/Compute/Tasks/sendingdiagnosticinterrupt.htm).



        - **DIAGNOSTICREBOOT** - Powers off the instance, rebuilds it, and then powers it back on.
        Before you send a diagnostic reboot, restart the instance's OS, confirm that the instance and networking settings are configured
        correctly, and try other [troubleshooting steps](/iaas/Content/Compute/References/troubleshooting-compute-instances.htm).
        Use diagnostic reboot as a final attempt to troubleshoot an unreachable instance. For virtual machine (VM) instances only.
        For more information, see [Performing a Diagnostic Reboot](/iaas/Content/Compute/Tasks/diagnostic-reboot.htm).


        - **REBOOTMIGRATE** - Powers off the instance, moves it to new hardware, and then powers it back on. For more information, see
        [Infrastructure Maintenance](/iaas/Content/Compute/References/infrastructure-maintenance.htm).


        For more information about managing instance lifecycle states, see
        [Stopping and Starting an Instance](/iaas/Content/Compute/Tasks/restartinginstance.htm).

        Args:
            instance_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

            action(str):
                The action to perform on the instance.

            action_type(str):
                The type of power action to perform.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"action_type": "actionType"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instances/{instanceId}".format(**{"instanceId": instance_id}),
        query_params={"action": action},
        data=payload,
        headers={"opc-retry-token": opc_retry_token, "if-match": if_match},
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
            "agent_config": "agentConfig",
            "availability_config": "availabilityConfig",
            "availability_domain": "availabilityDomain",
            "capacity_reservation_id": "capacityReservationId",
            "compartment_id": "compartmentId",
            "dedicated_vm_host_id": "dedicatedVmHostId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "extended_metadata": "extendedMetadata",
            "fault_domain": "faultDomain",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "instance_options": "instanceOptions",
            "ipxe_script": "ipxeScript",
            "launch_mode": "launchMode",
            "launch_options": "launchOptions",
            "lifecycle_state": "lifecycleState",
            "metadata": "metadata",
            "platform_config": "platformConfig",
            "preemptible_instance_config": "preemptibleInstanceConfig",
            "region": "region",
            "shape": "shape",
            "shape_config": "shapeConfig",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "time_maintenance_reboot_due": "timeMaintenanceRebootDue",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format
    return result


async def accept_shielded_integrity_policy(
    hub,
    ctx,
    instance_id: str,
    opc_request_id: str = None,
    if_match: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

        AcceptShieldedIntegrityPolicy
            Accept the changes to the PCR values in the measured boot report.

        Args:
            instance_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instances/{instanceId}/actions/acceptShieldedIntegrityPolicy".format(
            **{"instanceId": instance_id}
        ),
        query_params={},
        data=payload,
        headers={
            "opc-request-id": opc_request_id,
            "if-match": if_match,
            "opc-retry-token": opc_retry_token,
        },
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def change_instance_compartment(
    hub,
    ctx,
    instance_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

        ChangeInstanceCompartment
            Moves an instance into a different compartment within the same tenancy. For information about
        moving resources between compartments, see
        [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        When you move an instance to a different compartment, associated resources such as boot volumes and VNICs
        are not moved.

        Args:
            instance_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the instance to.
    .

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"compartment_id": "compartmentId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instances/{instanceId}/actions/changeCompartment".format(
            **{"instanceId": instance_id}
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


async def get_instance_default_credentials(
    hub, ctx, instance_id: str
) -> Dict[str, Any]:
    r"""

    GetInstanceDefaultCredentials
        Gets the generated credentials for the instance. Only works for instances that require a password to log in, such as Windows.
    For certain operating systems, users will be forced to change the initial credentials.

    Args:
        instance_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instances/{instanceId}/defaultCredentials".format(
            **{"instanceId": instance_id}
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
    resource_parameters = OrderedDict({"password": "password", "username": "username"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_instance_devices(
    hub,
    ctx,
    instance_id: str,
    is_available: bool = None,
    limit: int = None,
    page: str = None,
    opc_request_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListInstanceDevices
            Gets a list of all the devices for given instance. You can optionally filter results by device availability.

        Args:
            instance_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

            is_available(bool, Optional):
                A filter to return only available devices or only used devices.
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            sort_by(str, Optional):
                The field to sort by. You can provide one sort order (`sortOrder`). Default order for
    TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
    sort order is case sensitive.

    **Note:** In general, some "List" operations (for example, `ListInstances`) let you
    optionally filter by availability domain if the scope of the resource type is within a
    single availability domain. If you call one of these "List" operations without specifying
    an availability domain, the resources are grouped by availability domain, then sorted.
    . Defaults to None.

            sort_order(str, Optional):
                The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
    is case sensitive.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instances/{instanceId}/devices".format(**{"instanceId": instance_id}),
        query_params={
            "isAvailable": is_available,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
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


async def get_windows_instance_initial_credentials(
    hub, ctx, instance_id: str
) -> Dict[str, Any]:
    r"""

    GetWindowsInstanceInitialCredentials
        Deprecated. Use [GetInstanceDefaultCredentials](#/en/iaas/latest/InstanceCredentials/GetInstanceDefaultCredentials) instead.

    Gets the generated credentials for the instance. Only works for instances that require a password to log in, such as Windows.
    For certain operating systems, users will be forced to change the initial credentials.

    DEPRECATED

    Args:
        instance_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instances/{instanceId}/initialCredentials".format(
            **{"instanceId": instance_id}
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
    resource_parameters = OrderedDict({"password": "password", "username": "username"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_instance_maintenance_reboot(
    hub, ctx, instance_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        GetInstanceMaintenanceReboot
            Gets the maximum possible date that a maintenance reboot can be extended. For more information, see
        [Infrastructure Maintenance](/iaas/Content/Compute/References/infrastructure-maintenance.htm).

        Args:
            instance_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instances/{instanceId}/maintenanceReboot".format(
            **{"instanceId": instance_id}
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
        {"time_maintenance_reboot_due_max": "timeMaintenanceRebootDueMax"}
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_measured_boot_report(
    hub, ctx, instance_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        GetMeasuredBootReport
            Gets the measured boot report for this shielded instance.

        Args:
            instance_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instances/{instanceId}/measuredBootReport".format(
            **{"instanceId": instance_id}
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
            "is_policy_verification_successful": "isPolicyVerificationSuccessful",
            "measurements": "measurements",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_shapes(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    limit: int = None,
    page: str = None,
    image_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListShapes
            Lists the shapes that can be used to launch an instance within the specified compartment. You can
        filter the list by compatibility with a specific image.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            image_id(str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of an image. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/shapes".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "imageId": image_id,
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


async def list_vnic_attachments(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    instance_id: str = None,
    limit: int = None,
    page: str = None,
    vnic_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListVnicAttachments
            Lists the VNIC attachments in the specified compartment. A VNIC attachment
        resides in the same compartment as the attached instance. The list can be
        filtered by instance, VNIC, or availability domain.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            instance_id(str, Optional):
                The OCID of the instance. Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            vnic_id(str, Optional):
                The OCID of the VNIC. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vnicAttachments/".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "instanceId": instance_id,
            "limit": limit,
            "page": page,
            "vnicId": vnic_id,
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


async def attach_vnic(
    hub,
    ctx,
    create_vnic_details: make_dataclass(
        "create_vnic_details",
        [
            ("assign_ipv6_ip", bool, field(default=None)),
            ("assign_private_dns_record", bool, field(default=None)),
            ("assign_public_ip", bool, field(default=None)),
            ("defined_tags", Dict, field(default=None)),
            ("display_name", str, field(default=None)),
            ("freeform_tags", Dict, field(default=None)),
            ("hostname_label", str, field(default=None)),
            (
                "ipv6_address_ipv6_subnet_cidr_pair_details",
                List[
                    make_dataclass(
                        "ipv6_address_ipv6_subnet_cidr_pair_details",
                        [
                            ("ipv6_address", str, field(default=None)),
                            ("ipv6_subnet_cidr", str, field(default=None)),
                        ],
                    )
                ],
                field(default=None),
            ),
            ("nsg_ids", List[str], field(default=None)),
            ("private_ip", str, field(default=None)),
            ("skip_source_dest_check", bool, field(default=None)),
            ("subnet_id", str, field(default=None)),
            ("vlan_id", str, field(default=None)),
        ],
    ),
    instance_id: str,
    opc_retry_token: str = None,
    display_name: str = None,
    nic_index: int = None,
) -> Dict[str, Any]:
    r"""

        AttachVnic
            Creates a secondary VNIC and attaches it to the specified instance.
        For more information about secondary VNICs, see
        [Virtual Network Interface Cards (VNICs)](/iaas/Content/Network/Tasks/managingVNICs.htm).

        Args:
            create_vnic_details(dict[str, Any]):
                createVnicDetails.

                * assign_ipv6_ip (bool, Optional):
                    Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled
    subnet. Default: False. When provided you may optionally provide an IPv6 prefix
    (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr`
    is not provided then an IPv6 prefix is chosen
    for you.


                * assign_private_dns_record (bool, Optional):
                    Whether the VNIC should be assigned a DNS record. If set to false, there will be no DNS record
    registration for the VNIC. If set to true, the DNS record will be registered. The default
    value is true.

    If you specify a `hostnameLabel`, then `assignPrivateDnsRecord` must be set to true.


                * assign_public_ip (bool, Optional):
                    Whether the VNIC should be assigned a public IP address. Defaults to whether
    the subnet is public or private. If not set and the VNIC is being created
    in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the
    [Subnet](#/en/iaas/latest/Subnet/)), then no public IP address is assigned.
    If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then
    a public IP address is assigned. If set to true and
    `prohibitPublicIpOnVnic` = true, an error is returned.

    **Note:** This public IP address is associated with the primary private IP
    on the VNIC. For more information, see
    [IP Addresses](/iaas/Content/Network/Tasks/managingIPaddresses.htm).

    **Note:** There's a limit to the number of [public IPs](#/en/iaas/latest/PublicIp/)
    a VNIC or instance can have. If you try to create a secondary VNIC
    with an assigned public IP for an instance that has already
    reached its public IP limit, an error is returned. For information
    about the public IP limits, see
    [Public IP Addresses](/iaas/Content/Network/Tasks/managingpublicIPs.htm).

    Example: `false`

    If you specify a `vlanId`, then `assignPublicIp` must be set to false. See
    [Vlan](#/en/iaas/latest/Vlan).


                * defined_tags (Dict, Optional):
                    Defined tags for this resource. Each key is predefined and scoped to a
    namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Operations": {"CostCenter": "42"}}`


                * display_name (str, Optional):
                    A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.


                * freeform_tags (Dict, Optional):
                    Free-form tags for this resource. Each tag is a simple key-value pair with no
    predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

    Example: `{"Department": "Finance"}`


                * hostname_label (str, Optional):
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

    When launching an instance, use this `hostnameLabel` instead
    of the deprecated `hostnameLabel` in
    [LaunchInstanceDetails](#/en/iaas/latest/requests/LaunchInstanceDetails).
    If you provide both, the values must match.

    Example: `bminstance1`

    If you specify a `vlanId`, the `hostnameLabel` cannot be specified. VNICs on a VLAN
    can not be assigned a hostname. See [Vlan](#/en/iaas/latest/Vlan).


                * ipv6_address_ipv6_subnet_cidr_pair_details (List[dict[str, Any]], Optional):
                    A list of IPv6 prefix ranges from which the VNIC is assigned an IPv6 address.
    You can provide only the prefix ranges from which OCI selects an available
    address from the range. You can optionally choose to leave the prefix range empty
    and instead provide the specific IPv6 address within that range to use.


                    * ipv6_address (str, Optional):
                        An IPv6 address of your choice. Must be an available IPv6 address within the subnet's prefix.
    If an IPv6 address is not provided:
    - Oracle will automatically assign an IPv6 address from the subnet's IPv6 prefix if and only if there is only one IPv6 prefix on the subnet.
    - Oracle will automatically assign an IPv6 address from the subnet's IPv6 Oracle GUA prefix if it exists on the subnet.


                    * ipv6_subnet_cidr (str, Optional):
                        The IPv6 prefix allocated to the subnet.


                * nsg_ids (List[str], Optional):
                    A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
    information about NSGs, see
    [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/).

    If a `vlanId` is specified, the `nsgIds` cannot be specified. The `vlanId`
    indicates that the VNIC will belong to a VLAN instead of a subnet. With VLANs,
    all VNICs in the VLAN belong to the NSGs that are associated with the VLAN.
    See [Vlan](#/en/iaas/latest/Vlan).


                * private_ip (str, Optional):
                    A private IP address of your choice to assign to the VNIC. Must be an
    available IP address within the subnet's CIDR. If you don't specify a
    value, Oracle automatically assigns a private IP address from the subnet.
    This is the VNIC's *primary* private IP address. The value appears in
    the [Vnic](#/en/iaas/latest/Vnic/) object and also the
    [PrivateIp](#/en/iaas/latest/PrivateIp/) object returned by
    [ListPrivateIps](#/en/iaas/latest/PrivateIp/ListPrivateIps) and
    [GetPrivateIp](#/en/iaas/latest/PrivateIp/GetPrivateIp).


    If you specify a `vlanId`, the `privateIp` cannot be specified.
    See [Vlan](#/en/iaas/latest/Vlan).

    Example: `10.0.3.3`


                * skip_source_dest_check (bool, Optional):
                    Whether the source/destination check is disabled on the VNIC.
    Defaults to `false`, which means the check is performed. For information
    about why you would skip the source/destination check, see
    [Using a Private IP as a Route Target](/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).


    If you specify a `vlanId`, the `skipSourceDestCheck` cannot be specified because the
    source/destination check is always disabled for VNICs in a VLAN. See
    [Vlan](#/en/iaas/latest/Vlan).

    Example: `true`


                * subnet_id (str, Optional):
                    The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create the VNIC in. When launching an instance,
    use this `subnetId` instead of the deprecated `subnetId` in
    [LaunchInstanceDetails](#/en/iaas/latest/requests/LaunchInstanceDetails).
    At least one of them is required; if you provide both, the values must match.

    If you are an Oracle Cloud VMware Solution customer and creating a secondary
    VNIC in a VLAN instead of a subnet, provide a `vlanId` instead of a `subnetId`.
    If you provide both a `vlanId` and `subnetId`, the request fails.


                * vlan_id (str, Optional):
                    Provide this attribute only if you are an Oracle Cloud VMware Solution
    customer and creating a secondary VNIC in a VLAN. The value is the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
    See [Vlan](#/en/iaas/latest/Vlan).

    Provide a `vlanId` instead of a `subnetId`. If you provide both a
    `vlanId` and `subnetId`, the request fails.


            instance_id(str):
                The OCID of the instance.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            nic_index(int, Optional):
                Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
    Certain bare metal instance shapes have two active physical NICs (0 and 1). If
    you add a secondary VNIC to one of these instances, you can specify which NIC
    the VNIC will use. For more information, see
    [Virtual Network Interface Cards (VNICs)](/iaas/Content/Network/Tasks/managingVNICs.htm).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "create_vnic_details": "createVnicDetails",
        "display_name": "displayName",
        "instance_id": "instanceId",
        "nic_index": "nicIndex",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/vnicAttachments/".format(**{}),
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "display_name": "displayName",
            "id": "id",
            "instance_id": "instanceId",
            "lifecycle_state": "lifecycleState",
            "nic_index": "nicIndex",
            "subnet_id": "subnetId",
            "time_created": "timeCreated",
            "vlan_id": "vlanId",
            "vlan_tag": "vlanTag",
            "vnic_id": "vnicId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_vnic_attachment(hub, ctx, vnic_attachment_id: str) -> Dict[str, Any]:
    r"""

    GetVnicAttachment
        Gets the information for the specified VNIC attachment.

    Args:
        vnic_attachment_id(str):
            The OCID of the VNIC attachment.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/vnicAttachments/{vnicAttachmentId}".format(
            **{"vnicAttachmentId": vnic_attachment_id}
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
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "display_name": "displayName",
            "id": "id",
            "instance_id": "instanceId",
            "lifecycle_state": "lifecycleState",
            "nic_index": "nicIndex",
            "subnet_id": "subnetId",
            "time_created": "timeCreated",
            "vlan_id": "vlanId",
            "vlan_tag": "vlanTag",
            "vnic_id": "vnicId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def detach_vnic(
    hub, ctx, vnic_attachment_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DetachVnic
            Detaches and deletes the specified secondary VNIC.
        This operation cannot be used on the instance's primary VNIC.
        When you terminate an instance, all attached VNICs (primary
        and secondary) are automatically detached and deleted.

        **Important:** If the VNIC has a
        [private IP](#/en/iaas/latest/PrivateIp/) that is the
        [target of a route rule](/iaas/Content/Network/Tasks/managingroutetables.htm#privateip),
        deleting the VNIC causes that route rule to blackhole and the traffic
        will be dropped.

        Args:
            vnic_attachment_id(str):
                The OCID of the VNIC attachment.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/vnicAttachments/{vnicAttachmentId}".format(
            **{"vnicAttachmentId": vnic_attachment_id}
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


async def list_volume_attachments(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    limit: int = None,
    page: str = None,
    instance_id: str = None,
    volume_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListVolumeAttachments
            Lists the volume attachments in the specified compartment. You can filter the
        list by specifying an instance OCID, volume OCID, or both.

        Currently, the only supported volume attachment type are [IScsiVolumeAttachment](#/en/iaas/latest/IScsiVolumeAttachment/) and
        [ParavirtualizedVolumeAttachment](#/en/iaas/latest/ParavirtualizedVolumeAttachment/).

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            availability_domain(str, Optional):
                The name of the availability domain.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            limit(int, Optional):
                For list pagination. The maximum number of results per page, or items to return in a paginated
    "List" call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).

    Example: `50`
    . Defaults to None.

            page(str, Optional):
                For list pagination. The value of the `opc-next-page` response header from the previous "List"
    call. For important details about how pagination works, see
    [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine).
    . Defaults to None.

            instance_id(str, Optional):
                The OCID of the instance. Defaults to None.

            volume_id(str, Optional):
                The OCID of the volume. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/volumeAttachments/".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "instanceId": instance_id,
            "volumeId": volume_id,
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


async def attach_volume(
    hub,
    ctx,
    instance_id: str,
    type_: str,
    volume_id: str,
    opc_retry_token: str = None,
    device: str = None,
    display_name: str = None,
    is_read_only: bool = None,
    is_shareable: bool = None,
) -> Dict[str, Any]:
    r"""

        AttachVolume
            Attaches the specified storage volume to the specified instance.

        Args:
            instance_id(str):
                The OCID of the instance.

            type_(str):
                The type of volume. The only supported values are "iscsi" and "paravirtualized".
    .

            volume_id(str):
                The OCID of the volume.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            device(str, Optional):
                The device name. To retrieve a list of devices for a given instance, see [ListInstanceDevices](#/en/iaas/latest/Device/ListInstanceDevices). Defaults to None.

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            is_read_only(bool, Optional):
                Whether the attachment was created in read-only mode. Defaults to None.

            is_shareable(bool, Optional):
                Whether the attachment should be created in shareable mode. If an attachment
    is created in shareable mode, then other instances can attach the same volume, provided
    that they also create their attachments in shareable mode. Only certain volume types can
    be attached in shareable mode. Defaults to false if not specified.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "device": "device",
        "display_name": "displayName",
        "instance_id": "instanceId",
        "is_read_only": "isReadOnly",
        "is_shareable": "isShareable",
        "type": "type",
        "volume_id": "volumeId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/volumeAttachments/".format(**{}),
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
            "attachment_type": "attachmentType",
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "device": "device",
            "display_name": "displayName",
            "id": "id",
            "instance_id": "instanceId",
            "is_multipath": "isMultipath",
            "is_pv_encryption_in_transit_enabled": "isPvEncryptionInTransitEnabled",
            "is_read_only": "isReadOnly",
            "is_shareable": "isShareable",
            "iscsi_login_state": "iscsiLoginState",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
            "volume_id": "volumeId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_volume_attachment(hub, ctx, volume_attachment_id: str) -> Dict[str, Any]:
    r"""

    GetVolumeAttachment
        Gets information about the specified volume attachment.

    Args:
        volume_attachment_id(str):
            The OCID of the volume attachment.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/volumeAttachments/{volumeAttachmentId}".format(
            **{"volumeAttachmentId": volume_attachment_id}
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
            "attachment_type": "attachmentType",
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "device": "device",
            "display_name": "displayName",
            "id": "id",
            "instance_id": "instanceId",
            "is_multipath": "isMultipath",
            "is_pv_encryption_in_transit_enabled": "isPvEncryptionInTransitEnabled",
            "is_read_only": "isReadOnly",
            "is_shareable": "isShareable",
            "iscsi_login_state": "iscsiLoginState",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
            "volume_id": "volumeId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_volume_attachment(
    hub,
    ctx,
    volume_attachment_id: str,
    opc_request_id: str = None,
    if_match: str = None,
    iscsi_login_state: str = None,
) -> Dict[str, Any]:
    r"""

        UpdateVolumeAttachment
            Updates information about the specified volume attachment.

        Args:
            volume_attachment_id(str):
                The OCID of the volume attachment.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
    . Defaults to None.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            iscsi_login_state(str, Optional):
                The iscsi login state of the volume attachment. For a multipath volume attachment,
    all iscsi sessions need to be all logged-in or logged-out to be in logged-in or logged-out state.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"iscsi_login_state": "iscsiLoginState"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/volumeAttachments/{volumeAttachmentId}".format(
            **{"volumeAttachmentId": volume_attachment_id}
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
            "attachment_type": "attachmentType",
            "availability_domain": "availabilityDomain",
            "compartment_id": "compartmentId",
            "device": "device",
            "display_name": "displayName",
            "id": "id",
            "instance_id": "instanceId",
            "is_multipath": "isMultipath",
            "is_pv_encryption_in_transit_enabled": "isPvEncryptionInTransitEnabled",
            "is_read_only": "isReadOnly",
            "is_shareable": "isShareable",
            "iscsi_login_state": "iscsiLoginState",
            "lifecycle_state": "lifecycleState",
            "time_created": "timeCreated",
            "volume_id": "volumeId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def detach_volume(
    hub, ctx, volume_attachment_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DetachVolume
            Detaches a storage volume from an instance. You must specify the OCID of the volume attachment.

        This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily
        until the attachment is completely removed.

        Args:
            volume_attachment_id(str):
                The OCID of the volume attachment.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/volumeAttachments/{volumeAttachmentId}".format(
            **{"volumeAttachmentId": volume_attachment_id}
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
