"""Utility functions for Blockstorages. """
from collections import OrderedDict
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import Dict
from typing import List


async def list_block_volume_replicas(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

        ListBlockVolumeReplicas
            Lists the block volume replicas in the specified compartment and availability domain.

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

            lifecycle_state(str, Optional):
                A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
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
        path="/blockVolumeReplicas".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
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


async def get_block_volume_replica(
    hub, ctx, block_volume_replica_id: str
) -> Dict[str, Any]:
    r"""

    GetBlockVolumeReplica
        Gets information for the specified block volume replica.

    Args:
        block_volume_replica_id(str):
            The OCID of the block volume replica.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/blockVolumeReplicas/{blockVolumeReplicaId}".format(
            **{"blockVolumeReplicaId": block_volume_replica_id}
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
            "block_volume_id": "blockVolumeId",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "time_created": "timeCreated",
            "time_last_synced": "timeLastSynced",
            "total_data_transferred_in_g_bs": "totalDataTransferredInGBs",
            "volume_group_replica_id": "volumeGroupReplicaId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_boot_volume_backups(
    hub,
    ctx,
    compartment_id: str,
    boot_volume_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    source_boot_volume_backup_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

        ListBootVolumeBackups
            Lists the boot volume backups in the specified compartment. You can filter the results by boot volume.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            boot_volume_id(str, Optional):
                The OCID of the boot volume. Defaults to None.

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

            source_boot_volume_backup_id(str, Optional):
                A filter to return only resources that originated from the given source boot volume backup.
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
                A filter to only return resources that match the given lifecycle state. The state value is
    case-insensitive.
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
        path="/bootVolumeBackups".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "bootVolumeId": boot_volume_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sourceBootVolumeBackupId": source_boot_volume_backup_id,
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


async def create_boot_volume_backup(
    hub,
    ctx,
    boot_volume_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    kms_key_id: str = None,
    type_: str = None,
) -> Dict[str, Any]:
    r"""

        CreateBootVolumeBackup
            Creates a new boot volume backup of the specified boot volume. For general information about boot volume backups,
        see [Overview of Boot Volume Backups](/iaas/Content/Block/Concepts/bootvolumebackups.htm)

        When the request is received, the backup object is in a REQUEST_RECEIVED state.
        When the data is imaged, it goes into a CREATING state.
        After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.

        Args:
            boot_volume_id(str):
                The OCID of the boot volume that needs to be backed up.

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

            kms_key_id(str, Optional):
                The OCID of the Vault service key which is the master encryption key for the volume backup.
    For more information about the Vault service and encryption keys, see
    [Overview of Vault service](/iaas/Content/KeyManagement/Concepts/keyoverview.htm) and
    [Using Keys](/iaas/Content/KeyManagement/Tasks/usingkeys.htm).
    . Defaults to None.

            type_(str, Optional):
                The type of backup to create. If omitted, defaults to incremental. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "boot_volume_id": "bootVolumeId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "kms_key_id": "kmsKeyId",
        "type": "type",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/bootVolumeBackups".format(**{}),
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
            "boot_volume_id": "bootVolumeId",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "source_boot_volume_backup_id": "sourceBootVolumeBackupId",
            "source_type": "sourceType",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_g_bs": "uniqueSizeInGBs",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_boot_volume_backup(
    hub, ctx, boot_volume_backup_id: str
) -> Dict[str, Any]:
    r"""

    GetBootVolumeBackup
        Gets information for the specified boot volume backup.

    Args:
        boot_volume_backup_id(str):
            The OCID of the boot volume backup.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/bootVolumeBackups/{bootVolumeBackupId}".format(
            **{"bootVolumeBackupId": boot_volume_backup_id}
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
            "boot_volume_id": "bootVolumeId",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "source_boot_volume_backup_id": "sourceBootVolumeBackupId",
            "source_type": "sourceType",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_g_bs": "uniqueSizeInGBs",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_boot_volume_backup(
    hub,
    ctx,
    boot_volume_backup_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    kms_key_id: str = None,
) -> Dict[str, Any]:
    r"""

        UpdateBootVolumeBackup
            Updates the display name for the specified boot volume backup.
        Avoid entering confidential information.

        Args:
            boot_volume_backup_id(str):
                The OCID of the boot volume backup.

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

            kms_key_id(str, Optional):
                The OCID of the Vault service key which is the master encryption key for the volume backup.
    For more information about the Vault service and encryption keys, see
    [Overview of Vault service](/iaas/Content/KeyManagement/Concepts/keyoverview.htm) and
    [Using Keys](/iaas/Content/KeyManagement/Tasks/usingkeys.htm).
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
        "kms_key_id": "kmsKeyId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/bootVolumeBackups/{bootVolumeBackupId}".format(
            **{"bootVolumeBackupId": boot_volume_backup_id}
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
            "boot_volume_id": "bootVolumeId",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "source_boot_volume_backup_id": "sourceBootVolumeBackupId",
            "source_type": "sourceType",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_g_bs": "uniqueSizeInGBs",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_boot_volume_backup(
    hub, ctx, boot_volume_backup_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteBootVolumeBackup
            Deletes a boot volume backup.

        Args:
            boot_volume_backup_id(str):
                The OCID of the boot volume backup.

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
        path="/bootVolumeBackups/{bootVolumeBackupId}".format(
            **{"bootVolumeBackupId": boot_volume_backup_id}
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


async def change_boot_volume_backup_compartment(
    hub,
    ctx,
    boot_volume_backup_id: str,
    compartment_id: str,
    opc_request_id: str = None,
) -> Dict[str, Any]:
    r"""

        ChangeBootVolumeBackupCompartment
            Moves a boot volume backup into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            boot_volume_backup_id(str):
                The OCID of the boot volume backup.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the boot volume backup to.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
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
        path="/bootVolumeBackups/{bootVolumeBackupId}/actions/changeCompartment".format(
            **{"bootVolumeBackupId": boot_volume_backup_id}
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


async def copy_boot_volume_backup(
    hub,
    ctx,
    boot_volume_backup_id: str,
    destination_region: str,
    opc_retry_token: str = None,
    opc_request_id: str = None,
    display_name: str = None,
    kms_key_id: str = None,
) -> Dict[str, Any]:
    r"""

        CreateBootVolumeBackupCopy
            Creates a boot volume backup copy in specified region. For general information about volume backups,
        see [Overview of Boot Volume Backups](/iaas/Content/Block/Concepts/bootvolumebackups.htm)

        Args:
            boot_volume_backup_id(str):
                The OCID of the boot volume backup.

            destination_region(str):
                The name of the destination region.

    Example: `us-ashburn-1`
    .

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

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            kms_key_id(str, Optional):
                The OCID of the Vault service key in the destination region which will be the master encryption key
    for the copied boot volume backup. If you do not specify this attribute the boot volume backup
    will be encrypted with the Oracle-provided encryption key when it is copied to the destination region.


    For more information about the Vault service and encryption keys, see
    [Overview of Vault service](/iaas/Content/KeyManagement/Concepts/keyoverview.htm) and
    [Using Keys](/iaas/Content/KeyManagement/Tasks/usingkeys.htm).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "destination_region": "destinationRegion",
        "display_name": "displayName",
        "kms_key_id": "kmsKeyId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/bootVolumeBackups/{bootVolumeBackupId}/actions/copy".format(
            **{"bootVolumeBackupId": boot_volume_backup_id}
        ),
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
            "boot_volume_id": "bootVolumeId",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "source_boot_volume_backup_id": "sourceBootVolumeBackupId",
            "source_type": "sourceType",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_g_bs": "uniqueSizeInGBs",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_boot_volume_replicas(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

        ListBootVolumeReplicas
            Lists the boot volume replicas in the specified compartment and availability domain.

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

            lifecycle_state(str, Optional):
                A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
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
        path="/bootVolumeReplicas".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
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


async def get_boot_volume_replica(
    hub, ctx, boot_volume_replica_id: str
) -> Dict[str, Any]:
    r"""

    GetBootVolumeReplica
        Gets information for the specified boot volume replica.

    Args:
        boot_volume_replica_id(str):
            The OCID of the boot volume replica.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/bootVolumeReplicas/{bootVolumeReplicaId}".format(
            **{"bootVolumeReplicaId": boot_volume_replica_id}
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
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "time_created": "timeCreated",
            "time_last_synced": "timeLastSynced",
            "total_data_transferred_in_g_bs": "totalDataTransferredInGBs",
            "volume_group_replica_id": "volumeGroupReplicaId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_boot_volumes(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    volume_group_id: str = None,
) -> Dict[str, Any]:
    r"""

        ListBootVolumes
            Lists the boot volumes in the specified compartment and availability domain.

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

            volume_group_id(str, Optional):
                The OCID of the volume group. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/bootVolumes".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "volumeGroupId": volume_group_id,
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


async def create_boot_volume(
    hub,
    ctx,
    compartment_id: str,
    source_details: make_dataclass("source_details", [("type", str)]),
    opc_retry_token: str = None,
    autotune_policies: List[
        make_dataclass("autotune_policies", [("autotune_type", str)])
    ] = None,
    availability_domain: str = None,
    boot_volume_replicas: List[
        make_dataclass(
            "boot_volume_replicas",
            [("availability_domain", str), ("display_name", str, field(default=None))],
        )
    ] = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    is_auto_tune_enabled: bool = None,
    kms_key_id: str = None,
    size_in_g_bs: int = None,
    vpus_per_gb: int = None,
) -> Dict[str, Any]:
    r"""

        CreateBootVolume
            Creates a new boot volume in the specified compartment from an existing boot volume or a boot volume backup.
        For general information about boot volumes, see [Boot Volumes](/iaas/Content/Block/Concepts/bootvolumes.htm).
        You may optionally specify a *display name* for the volume, which is simply a friendly name or
        description. It does not have to be unique, and you can change it. Avoid entering confidential information.

        Args:
            compartment_id(str):
                The OCID of the compartment that contains the boot volume.

            source_details(dict[str, Any]):
                sourceDetails.

                * type (str):
                    type

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            autotune_policies(List[dict[str, Any]], Optional):
                The list of autotune policies to be enabled for this volume. Defaults to None.

                * autotune_type (str):
                    This specifies the type of autotunes supported by OCI.

            availability_domain(str, Optional):
                The availability domain of the volume. Omissible for cloning a volume. The new volume will be created in the availability domain of the source volume.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            boot_volume_replicas(List[dict[str, Any]], Optional):
                The list of boot volume replicas to be enabled for this boot volume
    in the specified destination availability domains.
    . Defaults to None.

                * availability_domain (str):
                    The availability domain of the boot volume replica.

    Example: `Uocm:PHX-AD-1`


                * display_name (str, Optional):
                    A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.


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

            is_auto_tune_enabled(bool, Optional):
                Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated.
    Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.
    . Defaults to None.

            kms_key_id(str, Optional):
                The OCID of the Vault service key to assign as the master encryption key
    for the boot volume.
    . Defaults to None.

            size_in_g_bs(int, Optional):
                The size of the volume in GBs. Defaults to None.

            vpus_per_gb(int, Optional):
                The number of volume performance units (VPUs) that will be applied to this volume per GB,
    representing the Block Volume service's elastic performance options.
    See [Block Volume Performance Levels](/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.

    Allowed values:

      * `10`: Represents the Balanced option.

      * `20`: Represents the Higher Performance option.

      * `30`-`120`: Represents the Ultra High Performance option.

    For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "autotune_policies": "autotunePolicies",
        "availability_domain": "availabilityDomain",
        "boot_volume_replicas": "bootVolumeReplicas",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "is_auto_tune_enabled": "isAutoTuneEnabled",
        "kms_key_id": "kmsKeyId",
        "size_in_g_bs": "sizeInGBs",
        "source_details": "sourceDetails",
        "vpus_per_gb": "vpusPerGB",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/bootVolumes".format(**{}),
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
            "auto_tuned_vpus_per_gb": "autoTunedVpusPerGB",
            "autotune_policies": "autotunePolicies",
            "availability_domain": "availabilityDomain",
            "boot_volume_replicas": "bootVolumeReplicas",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "is_auto_tune_enabled": "isAutoTuneEnabled",
            "is_hydrated": "isHydrated",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "volume_group_id": "volumeGroupId",
            "vpus_per_gb": "vpusPerGB",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_boot_volume(hub, ctx, boot_volume_id: str) -> Dict[str, Any]:
    r"""

    GetBootVolume
        Gets information for the specified boot volume.

    Args:
        boot_volume_id(str):
            The OCID of the boot volume.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/bootVolumes/{bootVolumeId}".format(**{"bootVolumeId": boot_volume_id}),
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
            "auto_tuned_vpus_per_gb": "autoTunedVpusPerGB",
            "autotune_policies": "autotunePolicies",
            "availability_domain": "availabilityDomain",
            "boot_volume_replicas": "bootVolumeReplicas",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "is_auto_tune_enabled": "isAutoTuneEnabled",
            "is_hydrated": "isHydrated",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "volume_group_id": "volumeGroupId",
            "vpus_per_gb": "vpusPerGB",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_boot_volume(
    hub,
    ctx,
    boot_volume_id: str,
    if_match: str = None,
    autotune_policies: List[
        make_dataclass("autotune_policies", [("autotune_type", str)])
    ] = None,
    boot_volume_replicas: List[
        make_dataclass(
            "boot_volume_replicas",
            [("availability_domain", str), ("display_name", str, field(default=None))],
        )
    ] = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    is_auto_tune_enabled: bool = None,
    size_in_g_bs: int = None,
    vpus_per_gb: int = None,
) -> Dict[str, Any]:
    r"""

        UpdateBootVolume
            Updates the specified boot volume's display name, defined tags, and free-form tags.

        Args:
            boot_volume_id(str):
                The OCID of the boot volume.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            autotune_policies(List[dict[str, Any]], Optional):
                The list of autotune policies to be enabled for this volume. Defaults to None.

                * autotune_type (str):
                    This specifies the type of autotunes supported by OCI.

            boot_volume_replicas(List[dict[str, Any]], Optional):
                The list of boot volume replicas that this boot volume will be updated to have
    in the specified destination availability domains.
    . Defaults to None.

                * availability_domain (str):
                    The availability domain of the boot volume replica.

    Example: `Uocm:PHX-AD-1`


                * display_name (str, Optional):
                    A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.


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

            is_auto_tune_enabled(bool, Optional):
                Specifies whether the auto-tune performance is enabled for this boot volume. This field is deprecated.
    Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.
    . Defaults to None.

            size_in_g_bs(int, Optional):
                The size to resize the volume to in GBs. Has to be larger than the current size. Defaults to None.

            vpus_per_gb(int, Optional):
                The number of volume performance units (VPUs) that will be applied to this volume per GB,
    representing the Block Volume service's elastic performance options.
    See [Block Volume Performance Levels](/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.

    Allowed values:

      * `10`: Represents Balanced option.

      * `20`: Represents Higher Performance option.

      * `30`-`120`: Represents the Ultra High Performance option.

    For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "autotune_policies": "autotunePolicies",
        "boot_volume_replicas": "bootVolumeReplicas",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "is_auto_tune_enabled": "isAutoTuneEnabled",
        "size_in_g_bs": "sizeInGBs",
        "vpus_per_gb": "vpusPerGB",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/bootVolumes/{bootVolumeId}".format(**{"bootVolumeId": boot_volume_id}),
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
            "auto_tuned_vpus_per_gb": "autoTunedVpusPerGB",
            "autotune_policies": "autotunePolicies",
            "availability_domain": "availabilityDomain",
            "boot_volume_replicas": "bootVolumeReplicas",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "image_id": "imageId",
            "is_auto_tune_enabled": "isAutoTuneEnabled",
            "is_hydrated": "isHydrated",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "volume_group_id": "volumeGroupId",
            "vpus_per_gb": "vpusPerGB",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_boot_volume(
    hub, ctx, boot_volume_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteBootVolume
            Deletes the specified boot volume. The volume cannot have an active connection to an instance.
        To disconnect the boot volume from a connected instance, see
        [Disconnecting From a Boot Volume](/iaas/Content/Block/Tasks/deletingbootvolume.htm).
        **Warning:** All data on the boot volume will be permanently lost when the boot volume is deleted.

        Args:
            boot_volume_id(str):
                The OCID of the boot volume.

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
        path="/bootVolumes/{bootVolumeId}".format(**{"bootVolumeId": boot_volume_id}),
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


async def change_boot_volume_compartment(
    hub, ctx, boot_volume_id: str, compartment_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        ChangeBootVolumeCompartment
            Moves a boot volume into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            boot_volume_id(str):
                The OCID of the boot volume.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the boot volume to.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
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
        path="/bootVolumes/{bootVolumeId}/actions/changeCompartment".format(
            **{"bootVolumeId": boot_volume_id}
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


async def get_boot_volume_kms_key(
    hub, ctx, boot_volume_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        GetBootVolumeKmsKey
            Gets the Vault service encryption key assigned to the specified boot volume.

        Args:
            boot_volume_id(str):
                The OCID of the boot volume.

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
        method="get",
        path="/bootVolumes/{bootVolumeId}/kmsKey".format(
            **{"bootVolumeId": boot_volume_id}
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
    resource_parameters = OrderedDict({"kms_key_id": "kmsKeyId"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_boot_volume_kms_key(
    hub, ctx, boot_volume_id: str, if_match: str = None, kms_key_id: str = None
) -> Dict[str, Any]:
    r"""

        UpdateBootVolumeKmsKey
            Updates the specified volume with a new Vault service master encryption key.

        Args:
            boot_volume_id(str):
                The OCID of the boot volume.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            kms_key_id(str, Optional):
                The OCID of the new Vault service key to assign to protect the specified volume.
    This key has to be a valid Vault service key, and policies must exist to allow the user and the Block Volume service to access this key.
    If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"kms_key_id": "kmsKeyId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/bootVolumes/{bootVolumeId}/kmsKey".format(
            **{"bootVolumeId": boot_volume_id}
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
    resource_parameters = OrderedDict({"kms_key_id": "kmsKeyId"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_boot_volume_kms_key(
    hub, ctx, boot_volume_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteBootVolumeKmsKey
            Removes the specified boot volume's assigned Vault Service encryption key.

        Args:
            boot_volume_id(str):
                The OCID of the boot volume.

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
        path="/bootVolumes/{bootVolumeId}/kmsKey".format(
            **{"bootVolumeId": boot_volume_id}
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


async def list_volume_backup_policies(
    hub, ctx, limit: int = None, page: str = None, compartment_id: str = None
) -> Dict[str, Any]:
    r"""

        ListVolumeBackupPolicies
            Lists all the volume backup policies available in the specified compartment.

        For more information about Oracle defined backup policies and user defined backup policies,
        see [Policy-Based Backups](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

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

            compartment_id(str, Optional):
                The OCID of the compartment.
    If no compartment is specified, the Oracle defined backup policies are listed.
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
        path="/volumeBackupPolicies".format(**{}),
        query_params={"limit": limit, "page": page, "compartmentId": compartment_id},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_volume_backup_policy(
    hub,
    ctx,
    compartment_id: str,
    opc_retry_token: str = None,
    opc_request_id: str = None,
    defined_tags: Dict = None,
    destination_region: str = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    schedules: List[
        make_dataclass(
            "schedules",
            [
                ("backup_type", str),
                ("period", str),
                ("retention_seconds", int),
                ("day_of_month", int, field(default=None)),
                ("day_of_week", str, field(default=None)),
                ("hour_of_day", int, field(default=None)),
                ("month", str, field(default=None)),
                ("offset_seconds", int, field(default=None)),
                ("offset_type", str, field(default=None)),
                ("time_zone", str, field(default=None)),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

        CreateVolumeBackupPolicy
            Creates a new user defined backup policy.

        For more information about Oracle defined backup policies and user defined backup policies,
        see [Policy-Based Backups](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

        Args:
            compartment_id(str):
                The OCID of the compartment.

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

            destination_region(str, Optional):
                The paired destination region for copying scheduled backups to. Example: `us-ashburn-1`.
    See [Region Pairs](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#RegionPairs) for details about paired regions.
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

            schedules(List[dict[str, Any]], Optional):
                The collection of schedules for the volume backup policy. See
    see [Schedules](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#schedules) in
    [Policy-Based Backups](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm) for more information.
    . Defaults to None.

                * backup_type (str):
                    The type of volume backup to create.

                * day_of_month (int, Optional):
                    The day of the month to schedule the volume backup.

                * day_of_week (str, Optional):
                    The day of the week to schedule the volume backup.

                * hour_of_day (int, Optional):
                    The hour of the day to schedule the volume backup.

                * month (str, Optional):
                    The month of the year to schedule the volume backup.

                * offset_seconds (int, Optional):
                    The number of seconds that the volume backup start
    time should be shifted from the default interval boundaries specified by
    the period. The volume backup start time is the frequency start time plus the offset.


                * offset_type (str, Optional):
                    Indicates how the offset is defined. If value is `STRUCTURED`,
    then `hourOfDay`, `dayOfWeek`, `dayOfMonth`, and `month` fields are used
    and `offsetSeconds` will be ignored in requests and users should ignore its
    value from the responses.

    `hourOfDay` is applicable for periods `ONE_DAY`,
    `ONE_WEEK`, `ONE_MONTH` and `ONE_YEAR`.

    `dayOfWeek` is applicable for period
    `ONE_WEEK`.

    `dayOfMonth` is applicable for periods `ONE_MONTH` and `ONE_YEAR`.

    'month' is applicable for period 'ONE_YEAR'.

    They will be ignored in the requests for inapplicable periods.

    If value is `NUMERIC_SECONDS`, then `offsetSeconds`
    will be used for both requests and responses and the structured fields will be
    ignored in the requests and users should ignore their values from the responses.

    For clients using older versions of Apis and not sending `offsetType` in their
    requests, the behaviour is just like `NUMERIC_SECONDS`.


                * period (str):
                    The volume backup frequency.

                * retention_seconds (int):
                    How long, in seconds, to keep the volume backups created by this schedule.

                * time_zone (str, Optional):
                    Specifies what time zone is the schedule in

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "destination_region": "destinationRegion",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "schedules": "schedules",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/volumeBackupPolicies".format(**{}),
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
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "destination_region": "destinationRegion",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "schedules": "schedules",
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


async def get_volume_backup_policy(hub, ctx, policy_id: str) -> Dict[str, Any]:
    r"""

    GetVolumeBackupPolicy
        Gets information for the specified volume backup policy.

    Args:
        policy_id(str):
            The OCID of the volume backup policy.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/volumeBackupPolicies/{policyId}".format(**{"policyId": policy_id}),
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
            "defined_tags": "definedTags",
            "destination_region": "destinationRegion",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "schedules": "schedules",
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


async def update_volume_backup_policy(
    hub,
    ctx,
    policy_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    destination_region: str = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    schedules: List[
        make_dataclass(
            "schedules",
            [
                ("backup_type", str),
                ("period", str),
                ("retention_seconds", int),
                ("day_of_month", int, field(default=None)),
                ("day_of_week", str, field(default=None)),
                ("hour_of_day", int, field(default=None)),
                ("month", str, field(default=None)),
                ("offset_seconds", int, field(default=None)),
                ("offset_type", str, field(default=None)),
                ("time_zone", str, field(default=None)),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

        UpdateVolumeBackupPolicy
            Updates a user defined backup policy.
         For more information about user defined backup policies,
         see [Policy-Based Backups](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#UserDefinedBackupPolicies).

         Avoid entering confidential information.

        Args:
            policy_id(str):
                The OCID of the volume backup policy.

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

            destination_region(str, Optional):
                The paired destination region for copying scheduled backups to. Example: `us-ashburn-1`.
    Specify `none` to reset the `destinationRegion` parameter.
    See [Region Pairs](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#RegionPairs) for details about paired regions.
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

            schedules(List[dict[str, Any]], Optional):
                The collection of schedules for the volume backup policy. See
    see [Schedules](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#schedules) in
    [Policy-Based Backups](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm) for more information.
    . Defaults to None.

                * backup_type (str):
                    The type of volume backup to create.

                * day_of_month (int, Optional):
                    The day of the month to schedule the volume backup.

                * day_of_week (str, Optional):
                    The day of the week to schedule the volume backup.

                * hour_of_day (int, Optional):
                    The hour of the day to schedule the volume backup.

                * month (str, Optional):
                    The month of the year to schedule the volume backup.

                * offset_seconds (int, Optional):
                    The number of seconds that the volume backup start
    time should be shifted from the default interval boundaries specified by
    the period. The volume backup start time is the frequency start time plus the offset.


                * offset_type (str, Optional):
                    Indicates how the offset is defined. If value is `STRUCTURED`,
    then `hourOfDay`, `dayOfWeek`, `dayOfMonth`, and `month` fields are used
    and `offsetSeconds` will be ignored in requests and users should ignore its
    value from the responses.

    `hourOfDay` is applicable for periods `ONE_DAY`,
    `ONE_WEEK`, `ONE_MONTH` and `ONE_YEAR`.

    `dayOfWeek` is applicable for period
    `ONE_WEEK`.

    `dayOfMonth` is applicable for periods `ONE_MONTH` and `ONE_YEAR`.

    'month' is applicable for period 'ONE_YEAR'.

    They will be ignored in the requests for inapplicable periods.

    If value is `NUMERIC_SECONDS`, then `offsetSeconds`
    will be used for both requests and responses and the structured fields will be
    ignored in the requests and users should ignore their values from the responses.

    For clients using older versions of Apis and not sending `offsetType` in their
    requests, the behaviour is just like `NUMERIC_SECONDS`.


                * period (str):
                    The volume backup frequency.

                * retention_seconds (int):
                    How long, in seconds, to keep the volume backups created by this schedule.

                * time_zone (str, Optional):
                    Specifies what time zone is the schedule in

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "destination_region": "destinationRegion",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "schedules": "schedules",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/volumeBackupPolicies/{policyId}".format(**{"policyId": policy_id}),
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
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "destination_region": "destinationRegion",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "schedules": "schedules",
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


async def delete_volume_backup_policy(
    hub, ctx, policy_id: str, opc_request_id: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteVolumeBackupPolicy
            Deletes a user defined backup policy.
         For more information about user defined backup policies,
         see [Policy-Based Backups](/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#UserDefinedBackupPolicies).

         Avoid entering confidential information.

        Args:
            policy_id(str):
                The OCID of the volume backup policy.

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
        path="/volumeBackupPolicies/{policyId}".format(**{"policyId": policy_id}),
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


async def get_volume_backup_policy_asset_assignment(
    hub, ctx, asset_id: str, limit: int = None, page: str = None
) -> Dict[str, Any]:
    r"""

        GetVolumeBackupPolicyAssetAssignment
            Gets the volume backup policy assignment for the specified volume. The
        `assetId` query parameter is required, and the returned list will contain at most
        one item, since volume can only have one volume backup policy assigned at a time.

        Args:
            asset_id(str):
                The OCID of an asset (e.g. a volume).

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
        path="/volumeBackupPolicyAssignments".format(**{}),
        query_params={"assetId": asset_id, "limit": limit, "page": page},
        data=payload,
        headers={},
    )

    if not ret["result"]:
        result["comment"].append(ret["comment"])
        result["result"] = False
        return result

    result["ret"] = ret["ret"]

    return result


async def create_volume_backup_policy_assignment(
    hub, ctx, asset_id: str, policy_id: str
) -> Dict[str, Any]:
    r"""

    CreateVolumeBackupPolicyAssignment
        Assigns a volume backup policy to the specified volume. Note that a given volume can
    only have one backup policy assigned to it. If this operation is used for a volume that already
    has a different backup policy assigned, the prior backup policy will be silently unassigned.

    Args:
        asset_id(str):
            The OCID of the volume to assign the policy to.

        policy_id(str):
            The OCID of the volume backup policy to assign to the volume.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"asset_id": "assetId", "policy_id": "policyId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/volumeBackupPolicyAssignments".format(**{}),
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
            "asset_id": "assetId",
            "id": "id",
            "policy_id": "policyId",
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


async def get_volume_backup_policy_assignment(
    hub, ctx, policy_assignment_id: str
) -> Dict[str, Any]:
    r"""

    GetVolumeBackupPolicyAssignment
        Gets information for the specified volume backup policy assignment.

    Args:
        policy_assignment_id(str):
            The OCID of the volume backup policy assignment.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/volumeBackupPolicyAssignments/{policyAssignmentId}".format(
            **{"policyAssignmentId": policy_assignment_id}
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
            "asset_id": "assetId",
            "id": "id",
            "policy_id": "policyId",
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


async def delete_volume_backup_policy_assignment(
    hub, ctx, policy_assignment_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteVolumeBackupPolicyAssignment
            Deletes a volume backup policy assignment.

        Args:
            policy_assignment_id(str):
                The OCID of the volume backup policy assignment.

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
        path="/volumeBackupPolicyAssignments/{policyAssignmentId}".format(
            **{"policyAssignmentId": policy_assignment_id}
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


async def list_volume_backups(
    hub,
    ctx,
    compartment_id: str,
    volume_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    source_volume_backup_id: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

        ListVolumeBackups
            Lists the volume backups in the specified compartment. You can filter the results by volume.

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            volume_id(str, Optional):
                The OCID of the volume. Defaults to None.

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

            source_volume_backup_id(str, Optional):
                A filter to return only resources that originated from the given source volume backup.
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
        path="/volumeBackups".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "volumeId": volume_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sourceVolumeBackupId": source_volume_backup_id,
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


async def create_volume_backup(
    hub,
    ctx,
    volume_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    kms_key_id: str = None,
    type_: str = None,
) -> Dict[str, Any]:
    r"""

        CreateVolumeBackup
            Creates a new backup of the specified volume. For general information about volume backups,
        see [Overview of Block Volume Service Backups](/iaas/Content/Block/Concepts/blockvolumebackups.htm)

        When the request is received, the backup object is in a REQUEST_RECEIVED state.
        When the data is imaged, it goes into a CREATING state.
        After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.

        Args:
            volume_id(str):
                The OCID of the volume that needs to be backed up.

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

            kms_key_id(str, Optional):
                The OCID of the Vault service key which is the master encryption key for the volume backup.
    For more information about the Vault service and encryption keys, see
    [Overview of Vault service](/iaas/Content/KeyManagement/Concepts/keyoverview.htm) and
    [Using Keys](/iaas/Content/KeyManagement/Tasks/usingkeys.htm).
    . Defaults to None.

            type_(str, Optional):
                The type of backup to create. If omitted, defaults to INCREMENTAL. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "kms_key_id": "kmsKeyId",
        "type": "type",
        "volume_id": "volumeId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/volumeBackups".format(**{}),
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
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_type": "sourceType",
            "source_volume_backup_id": "sourceVolumeBackupId",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_g_bs": "uniqueSizeInGBs",
            "unique_size_in_mbs": "uniqueSizeInMbs",
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


async def get_volume_backup(hub, ctx, volume_backup_id: str) -> Dict[str, Any]:
    r"""

    GetVolumeBackup
        Gets information for the specified volume backup.

    Args:
        volume_backup_id(str):
            The OCID of the volume backup.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/volumeBackups/{volumeBackupId}".format(
            **{"volumeBackupId": volume_backup_id}
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
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_type": "sourceType",
            "source_volume_backup_id": "sourceVolumeBackupId",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_g_bs": "uniqueSizeInGBs",
            "unique_size_in_mbs": "uniqueSizeInMbs",
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


async def update_volume_backup(
    hub,
    ctx,
    volume_backup_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    kms_key_id: str = None,
) -> Dict[str, Any]:
    r"""

        UpdateVolumeBackup
            Updates the display name for the specified volume backup.
        Avoid entering confidential information.

        Args:
            volume_backup_id(str):
                The OCID of the volume backup.

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

            kms_key_id(str, Optional):
                The OCID of the Vault service key which is the master encryption key for the volume backup.
    For more information about the Vault service and encryption keys, see
    [Overview of Vault service](/iaas/Content/KeyManagement/Concepts/keyoverview.htm) and
    [Using Keys](/iaas/Content/KeyManagement/Tasks/usingkeys.htm).
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
        "kms_key_id": "kmsKeyId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/volumeBackups/{volumeBackupId}".format(
            **{"volumeBackupId": volume_backup_id}
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
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_type": "sourceType",
            "source_volume_backup_id": "sourceVolumeBackupId",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_g_bs": "uniqueSizeInGBs",
            "unique_size_in_mbs": "uniqueSizeInMbs",
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


async def delete_volume_backup(
    hub, ctx, volume_backup_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteVolumeBackup
            Deletes a volume backup.

        Args:
            volume_backup_id(str):
                The OCID of the volume backup.

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
        path="/volumeBackups/{volumeBackupId}".format(
            **{"volumeBackupId": volume_backup_id}
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


async def change_volume_backup_compartment(
    hub, ctx, volume_backup_id: str, compartment_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        ChangeVolumeBackupCompartment
            Moves a volume backup into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            volume_backup_id(str):
                The OCID of the volume backup.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the volume backup to.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
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
        path="/volumeBackups/{volumeBackupId}/actions/changeCompartment".format(
            **{"volumeBackupId": volume_backup_id}
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


async def copy_volume_backup(
    hub,
    ctx,
    volume_backup_id: str,
    destination_region: str,
    opc_retry_token: str = None,
    opc_request_id: str = None,
    display_name: str = None,
    kms_key_id: str = None,
) -> Dict[str, Any]:
    r"""

        CreateVolumeBackupCopy
            Creates a volume backup copy in specified region. For general information about volume backups,
        see [Overview of Block Volume Service Backups](/iaas/Content/Block/Concepts/blockvolumebackups.htm)

        Args:
            volume_backup_id(str):
                The OCID of the volume backup.

            destination_region(str):
                The name of the destination region.

    Example: `us-ashburn-1`
    .

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

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            kms_key_id(str, Optional):
                The OCID of the Vault service key in the destination region which will be the master encryption key
    for the copied volume backup.
    If you do not specify this attribute the volume backup will be encrypted with the Oracle-provided encryption
    key when it is copied to the destination region.


    For more information about the Vault service and encryption keys, see
    [Overview of Vault service](/iaas/Content/KeyManagement/Concepts/keyoverview.htm) and
    [Using Keys](/iaas/Content/KeyManagement/Tasks/usingkeys.htm).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "destination_region": "destinationRegion",
        "display_name": "displayName",
        "kms_key_id": "kmsKeyId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/volumeBackups/{volumeBackupId}/actions/copy".format(
            **{"volumeBackupId": volume_backup_id}
        ),
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
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_type": "sourceType",
            "source_volume_backup_id": "sourceVolumeBackupId",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_g_bs": "uniqueSizeInGBs",
            "unique_size_in_mbs": "uniqueSizeInMbs",
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


async def list_volume_group_backups(
    hub,
    ctx,
    compartment_id: str,
    volume_group_id: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

        ListVolumeGroupBackups
            Lists the volume group backups in the specified compartment. You can filter the results by volume group.
        For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

        Args:
            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

            volume_group_id(str, Optional):
                The OCID of the volume group. Defaults to None.

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
        path="/volumeGroupBackups".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "volumeGroupId": volume_group_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
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


async def create_volume_group_backup(
    hub,
    ctx,
    volume_group_id: str,
    opc_retry_token: str = None,
    compartment_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    type_: str = None,
) -> Dict[str, Any]:
    r"""

        CreateVolumeGroupBackup
            Creates a new backup volume group of the specified volume group.
        For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

        Args:
            volume_group_id(str):
                The OCID of the volume group that needs to be backed up.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            compartment_id(str, Optional):
                The OCID of the compartment that will contain the volume group
    backup. This parameter is optional, by default backup will be created in
    the same compartment and source volume group.
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

            type_(str, Optional):
                The type of backup to create. If omitted, defaults to incremental. Defaults to None.

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
        "type": "type",
        "volume_group_id": "volumeGroupId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/volumeGroupBackups".format(**{}),
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
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_type": "sourceType",
            "source_volume_group_backup_id": "sourceVolumeGroupBackupId",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_gbs": "uniqueSizeInGbs",
            "unique_size_in_mbs": "uniqueSizeInMbs",
            "volume_backup_ids": "volumeBackupIds",
            "volume_group_id": "volumeGroupId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_volume_group_backup(
    hub, ctx, volume_group_backup_id: str
) -> Dict[str, Any]:
    r"""

        GetVolumeGroupBackup
            Gets information for the specified volume group backup. For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

        Args:
            volume_group_backup_id(str):
                The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.
    .

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/volumeGroupBackups/{volumeGroupBackupId}".format(
            **{"volumeGroupBackupId": volume_group_backup_id}
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
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_type": "sourceType",
            "source_volume_group_backup_id": "sourceVolumeGroupBackupId",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_gbs": "uniqueSizeInGbs",
            "unique_size_in_mbs": "uniqueSizeInMbs",
            "volume_backup_ids": "volumeBackupIds",
            "volume_group_id": "volumeGroupId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_volume_group_backup(
    hub,
    ctx,
    volume_group_backup_id: str,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

        UpdateVolumeGroupBackup
            Updates the display name for the specified volume group backup. For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

        Args:
            volume_group_backup_id(str):
                The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.
    .

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
        path="/volumeGroupBackups/{volumeGroupBackupId}".format(
            **{"volumeGroupBackupId": volume_group_backup_id}
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
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_type": "sourceType",
            "source_volume_group_backup_id": "sourceVolumeGroupBackupId",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_gbs": "uniqueSizeInGbs",
            "unique_size_in_mbs": "uniqueSizeInMbs",
            "volume_backup_ids": "volumeBackupIds",
            "volume_group_id": "volumeGroupId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_volume_group_backup(
    hub, ctx, volume_group_backup_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteVolumeGroupBackup
            Deletes a volume group backup. This operation deletes all the backups in
        the volume group. For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

        Args:
            volume_group_backup_id(str):
                The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.
    .

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
        path="/volumeGroupBackups/{volumeGroupBackupId}".format(
            **{"volumeGroupBackupId": volume_group_backup_id}
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


async def change_volume_group_backup_compartment(
    hub,
    ctx,
    volume_group_backup_id: str,
    compartment_id: str,
    opc_request_id: str = None,
) -> Dict[str, Any]:
    r"""

        ChangeVolumeGroupBackupCompartment
            Moves a volume group backup into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            volume_group_backup_id(str):
                The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.
    .

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the volume group backup to.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
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
        path="/volumeGroupBackups/{volumeGroupBackupId}/actions/changeCompartment".format(
            **{"volumeGroupBackupId": volume_group_backup_id}
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


async def copy_volume_group_backup(
    hub,
    ctx,
    volume_group_backup_id: str,
    destination_region: str,
    opc_retry_token: str = None,
    opc_request_id: str = None,
    display_name: str = None,
    kms_key_id: str = None,
) -> Dict[str, Any]:
    r"""

        CreateVolumeGroupBackupCopy
            Creates a volume group backup copy in specified region. For general information about volume group backups,
        see [Overview of Block Volume Backups](/iaas/Content/Block/Concepts/blockvolumebackups.htm).

        Args:
            volume_group_backup_id(str):
                The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.
    .

            destination_region(str):
                The name of the destination region.

    Example: `us-ashburn-1`
    .

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

            display_name(str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.
    . Defaults to None.

            kms_key_id(str, Optional):
                The OCID of the Vault service key in the destination region which will be the master encryption key
    for the copied volume group backup.
    If you do not specify this attribute the volume group backup will be encrypted with the Oracle-provided encryption
    key when it is copied to the destination region.


    For more information about the Vault service and encryption keys, see
    [Overview of Vault service](/iaas/Content/KeyManagement/Concepts/keyoverview.htm) and
    [Using Keys](/iaas/Content/KeyManagement/Tasks/usingkeys.htm).
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "destination_region": "destinationRegion",
        "display_name": "displayName",
        "kms_key_id": "kmsKeyId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/volumeGroupBackups/{volumeGroupBackupId}/actions/copy".format(
            **{"volumeGroupBackupId": volume_group_backup_id}
        ),
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
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "expiration_time": "expirationTime",
            "freeform_tags": "freeformTags",
            "id": "id",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_type": "sourceType",
            "source_volume_group_backup_id": "sourceVolumeGroupBackupId",
            "time_created": "timeCreated",
            "time_request_received": "timeRequestReceived",
            "type": "type",
            "unique_size_in_gbs": "uniqueSizeInGbs",
            "unique_size_in_mbs": "uniqueSizeInMbs",
            "volume_backup_ids": "volumeBackupIds",
            "volume_group_id": "volumeGroupId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_volume_group_replicas(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

        Lists the volume group replicas in the specified compartment.
            Lists the volume group replicas in the specified compartment. You can filter the results by volume group.
        For more information, see [Volume Group Replication](/iaas/Content/Block/Concepts/volumegroupreplication.htm).

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

            lifecycle_state(str, Optional):
                A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
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
        path="/volumeGroupReplicas".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
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


async def get_volume_group_replica(
    hub, ctx, volume_group_replica_id: str
) -> Dict[str, Any]:
    r"""

    Gets information for the specified volume group replica.
        Gets information for the specified volume group replica.

    Args:
        volume_group_replica_id(str):
            The OCID of the volume replica group.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/volumeGroupReplicas/{volumeGroupReplicaId}".format(
            **{"volumeGroupReplicaId": volume_group_replica_id}
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
            "lifecycle_state": "lifecycleState",
            "member_replicas": "memberReplicas",
            "size_in_g_bs": "sizeInGBs",
            "time_created": "timeCreated",
            "time_last_synced": "timeLastSynced",
            "volume_group_id": "volumeGroupId",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_volume_groups(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

        ListVolumeGroups
            Lists the volume groups in the specified compartment and availability domain.
        For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

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

            lifecycle_state(str, Optional):
                A filter to only return resources that match the given lifecycle
    state. The state value is case-insensitive.
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
        path="/volumeGroups".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
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


async def create_volume_group(
    hub,
    ctx,
    availability_domain: str,
    compartment_id: str,
    source_details: make_dataclass("source_details", [("type", str)]),
    opc_retry_token: str = None,
    backup_policy_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    volume_group_replicas: List[
        make_dataclass(
            "volume_group_replicas",
            [("availability_domain", str), ("display_name", str, field(default=None))],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

        CreateVolumeGroup
            Creates a new volume group in the specified compartment.
        A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing
        volume group, or by restoring a volume group backup.
        You may optionally specify a *display name* for the volume group, which is simply a friendly name or
        description. It does not have to be unique, and you can change it. Avoid entering confidential information.

        For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

        Args:
            availability_domain(str):
                The availability domain of the volume group.

            compartment_id(str):
                The OCID of the compartment that contains the volume group.

            source_details(dict[str, Any]):
                sourceDetails.

                * type (str):
                    type

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            backup_policy_id(str, Optional):
                If provided, specifies the ID of the volume backup policy to assign to the newly
    created volume group. If omitted, no policy will be assigned.
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

            volume_group_replicas(List[dict[str, Any]], Optional):
                The list of volume group replicas that this volume group will be enabled to have
    in the specified destination availability domains.
    . Defaults to None.

                * availability_domain (str):
                    The availability domain of the volume group replica.

    Example: `Uocm:PHX-AD-1`


                * display_name (str, Optional):
                    A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "availability_domain": "availabilityDomain",
        "backup_policy_id": "backupPolicyId",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "source_details": "sourceDetails",
        "volume_group_replicas": "volumeGroupReplicas",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/volumeGroups".format(**{}),
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
            "is_hydrated": "isHydrated",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "volume_group_replicas": "volumeGroupReplicas",
            "volume_ids": "volumeIds",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_volume_group(hub, ctx, volume_group_id: str) -> Dict[str, Any]:
    r"""

    GetVolumeGroup
        Gets information for the specified volume group. For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

    Args:
        volume_group_id(str):
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/volumeGroups/{volumeGroupId}".format(
            **{"volumeGroupId": volume_group_id}
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
            "is_hydrated": "isHydrated",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "volume_group_replicas": "volumeGroupReplicas",
            "volume_ids": "volumeIds",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_volume_group(
    hub,
    ctx,
    volume_group_id: str,
    if_match: str = None,
    preserve_volume_replica: bool = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    volume_group_replicas: List[
        make_dataclass(
            "volume_group_replicas",
            [("availability_domain", str), ("display_name", str, field(default=None))],
        )
    ] = None,
    volume_ids: List[str] = None,
) -> Dict[str, Any]:
    r"""

        UpdateVolumeGroup
            Updates the set of volumes in a volume group along with the display name. Use this operation
        to add or remove volumes in a volume group. Specify the full list of volume IDs to include in the
        volume group. If the volume ID is not specified in the call, it will be removed from the volume group.
        Avoid entering confidential information.

        For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

        Args:
            volume_group_id(str):
                The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            preserve_volume_replica(bool, Optional):
                Specifies whether to disable or preserve the individual volume replication when removing a volume from the
    replication enabled volume group. When set to `true`, the individual volume replica is preserved. The default
    value is `true`.
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

            volume_group_replicas(List[dict[str, Any]], Optional):
                The list of volume group replicas that this volume group will be updated to have
    in the specified destination availability domains.
    . Defaults to None.

                * availability_domain (str):
                    The availability domain of the volume group replica.

    Example: `Uocm:PHX-AD-1`


                * display_name (str, Optional):
                    A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.


            volume_ids(List[str], Optional):
                OCIDs for the volumes in this volume group. Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "volume_group_replicas": "volumeGroupReplicas",
        "volume_ids": "volumeIds",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/volumeGroups/{volumeGroupId}".format(
            **{"volumeGroupId": volume_group_id}
        ),
        query_params={"preserveVolumeReplica": preserve_volume_replica},
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
            "is_hydrated": "isHydrated",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "volume_group_replicas": "volumeGroupReplicas",
            "volume_ids": "volumeIds",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_volume_group(
    hub, ctx, volume_group_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteVolumeGroup
            Deletes the specified volume group. Individual volumes are not deleted, only the volume group is deleted.
        For more information, see [Volume Groups](/iaas/Content/Block/Concepts/volumegroups.htm).

        Args:
            volume_group_id(str):
                The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

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
        path="/volumeGroups/{volumeGroupId}".format(
            **{"volumeGroupId": volume_group_id}
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


async def change_volume_group_compartment(
    hub, ctx, volume_group_id: str, compartment_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        ChangeVolumeGroupCompartment
            Moves a volume group into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            volume_group_id(str):
                The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the volume group to.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
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
        path="/volumeGroups/{volumeGroupId}/actions/changeCompartment".format(
            **{"volumeGroupId": volume_group_id}
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


async def list_volumes(
    hub,
    ctx,
    compartment_id: str,
    availability_domain: str = None,
    limit: int = None,
    page: str = None,
    display_name: str = None,
    sort_by: str = None,
    sort_order: str = None,
    volume_group_id: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

        ListVolumes
            Lists the volumes in the specified compartment and availability domain.

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

            volume_group_id(str, Optional):
                The OCID of the volume group. Defaults to None.

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
        path="/volumes".format(**{}),
        query_params={
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": limit,
            "page": page,
            "displayName": display_name,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "volumeGroupId": volume_group_id,
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


async def create_volume(
    hub,
    ctx,
    compartment_id: str,
    opc_retry_token: str = None,
    autotune_policies: List[
        make_dataclass("autotune_policies", [("autotune_type", str)])
    ] = None,
    availability_domain: str = None,
    backup_policy_id: str = None,
    block_volume_replicas: List[
        make_dataclass(
            "block_volume_replicas",
            [("availability_domain", str), ("display_name", str, field(default=None))],
        )
    ] = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    is_auto_tune_enabled: bool = None,
    kms_key_id: str = None,
    size_in_g_bs: int = None,
    size_in_m_bs: int = None,
    source_details: make_dataclass("source_details", [("type", str)]) = None,
    volume_backup_id: str = None,
    vpus_per_gb: int = None,
) -> Dict[str, Any]:
    r"""

        CreateVolume
            Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from
        50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB).
        For general information about block volumes, see
        [Overview of Block Volume Service](/iaas/Content/Block/Concepts/overview.htm).

        A volume and instance can be in separate compartments but must be in the same availability domain.
        For information about access control and compartments, see
        [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm). For information about
        availability domains, see [Regions and Availability Domains](/iaas/Content/General/Concepts/regions.htm).
        To get a list of availability domains, use the `ListAvailabilityDomains` operation
        in the Identity and Access Management Service API.

        You may optionally specify a *display name* for the volume, which is simply a friendly name or
        description. It does not have to be unique, and you can change it. Avoid entering confidential information.

        Args:
            compartment_id(str):
                The OCID of the compartment that contains the volume.

            opc_retry_token(str, Optional):
                A token that uniquely identifies a request so it can be retried in case of a timeout or
    server error without risk of executing that same action again. Retry tokens expire after 24
    hours, but can be invalidated before then due to conflicting operations (for example, if a resource
    has been deleted and purged from the system, then a retry of the original creation request
    may be rejected).
    . Defaults to None.

            autotune_policies(List[dict[str, Any]], Optional):
                The list of autotune policies to be enabled for this volume. Defaults to None.

                * autotune_type (str):
                    This specifies the type of autotunes supported by OCI.

            availability_domain(str, Optional):
                The availability domain of the volume. Omissible for cloning a volume. The new volume will be created in the availability domain of the source volume.

    Example: `Uocm:PHX-AD-1`
    . Defaults to None.

            backup_policy_id(str, Optional):
                If provided, specifies the ID of the volume backup policy to assign to the newly
    created volume. If omitted, no policy will be assigned.
    . Defaults to None.

            block_volume_replicas(List[dict[str, Any]], Optional):
                The list of block volume replicas to be enabled for this volume
    in the specified destination availability domains.
    . Defaults to None.

                * availability_domain (str):
                    The availability domain of the block volume replica.

    Example: `Uocm:PHX-AD-1`


                * display_name (str, Optional):
                    A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.


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

            is_auto_tune_enabled(bool, Optional):
                Specifies whether the auto-tune performance is enabled for this volume. This field is deprecated.
    Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.
    . Defaults to None.

            kms_key_id(str, Optional):
                The OCID of the Vault service key to assign as the master encryption key
    for the volume.
    . Defaults to None.

            size_in_g_bs(int, Optional):
                The size of the volume in GBs. Defaults to None.

            size_in_m_bs(int, Optional):
                The size of the volume in MBs. The value must be a multiple of 1024.
    This field is deprecated. Use sizeInGBs instead.
    . Defaults to None.

            source_details(dict[str, Any], Optional):
                sourceDetails. Defaults to None.

                * type (str):
                    type

            volume_backup_id(str, Optional):
                The OCID of the volume backup from which the data should be restored on the newly created volume.
    This field is deprecated. Use the sourceDetails field instead to specify the
    backup for the volume.
    . Defaults to None.

            vpus_per_gb(int, Optional):
                The number of volume performance units (VPUs) that will be applied to this volume per GB,
    representing the Block Volume service's elastic performance options.
    See [Block Volume Performance Levels](/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.

    Allowed values:

      * `0`: Represents Lower Cost option.

      * `10`: Represents Balanced option.

      * `20`: Represents Higher Performance option.

      * `30`-`120`: Represents the Ultra High Performance option.

    For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "autotune_policies": "autotunePolicies",
        "availability_domain": "availabilityDomain",
        "backup_policy_id": "backupPolicyId",
        "block_volume_replicas": "blockVolumeReplicas",
        "compartment_id": "compartmentId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "is_auto_tune_enabled": "isAutoTuneEnabled",
        "kms_key_id": "kmsKeyId",
        "size_in_g_bs": "sizeInGBs",
        "size_in_m_bs": "sizeInMBs",
        "source_details": "sourceDetails",
        "volume_backup_id": "volumeBackupId",
        "vpus_per_gb": "vpusPerGB",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/volumes".format(**{}),
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
            "auto_tuned_vpus_per_gb": "autoTunedVpusPerGB",
            "autotune_policies": "autotunePolicies",
            "availability_domain": "availabilityDomain",
            "block_volume_replicas": "blockVolumeReplicas",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "is_auto_tune_enabled": "isAutoTuneEnabled",
            "is_hydrated": "isHydrated",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "volume_group_id": "volumeGroupId",
            "vpus_per_gb": "vpusPerGB",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_volume(hub, ctx, volume_id: str) -> Dict[str, Any]:
    r"""

    GetVolume
        Gets information for the specified volume.

    Args:
        volume_id(str):
            The OCID of the volume.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/volumes/{volumeId}".format(**{"volumeId": volume_id}),
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
            "auto_tuned_vpus_per_gb": "autoTunedVpusPerGB",
            "autotune_policies": "autotunePolicies",
            "availability_domain": "availabilityDomain",
            "block_volume_replicas": "blockVolumeReplicas",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "is_auto_tune_enabled": "isAutoTuneEnabled",
            "is_hydrated": "isHydrated",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "volume_group_id": "volumeGroupId",
            "vpus_per_gb": "vpusPerGB",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_volume(
    hub,
    ctx,
    volume_id: str,
    if_match: str = None,
    autotune_policies: List[
        make_dataclass("autotune_policies", [("autotune_type", str)])
    ] = None,
    block_volume_replicas: List[
        make_dataclass(
            "block_volume_replicas",
            [("availability_domain", str), ("display_name", str, field(default=None))],
        )
    ] = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    is_auto_tune_enabled: bool = None,
    size_in_g_bs: int = None,
    vpus_per_gb: int = None,
) -> Dict[str, Any]:
    r"""

        UpdateVolume
            Updates the specified volume's display name.
        Avoid entering confidential information.

        Args:
            volume_id(str):
                The OCID of the volume.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            autotune_policies(List[dict[str, Any]], Optional):
                The list of autotune policies enabled for this volume. Defaults to None.

                * autotune_type (str):
                    This specifies the type of autotunes supported by OCI.

            block_volume_replicas(List[dict[str, Any]], Optional):
                The list of block volume replicas that this volume will be updated to have
    in the specified destination availability domains.
    . Defaults to None.

                * availability_domain (str):
                    The availability domain of the block volume replica.

    Example: `Uocm:PHX-AD-1`


                * display_name (str, Optional):
                    A user-friendly name. Does not have to be unique, and it's changeable.
    Avoid entering confidential information.


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

            is_auto_tune_enabled(bool, Optional):
                Specifies whether the auto-tune performance is enabled for this volume. This field is deprecated.
    Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.
    . Defaults to None.

            size_in_g_bs(int, Optional):
                The size to resize the volume to in GBs. Has to be larger than the current size. Defaults to None.

            vpus_per_gb(int, Optional):
                The number of volume performance units (VPUs) that will be applied to this volume per GB,
    representing the Block Volume service's elastic performance options.
    See [Block Volume Performance Levels](/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.

    Allowed values:

      * `0`: Represents Lower Cost option.

      * `10`: Represents Balanced option.

      * `20`: Represents Higher Performance option.

      * `30`-`120`: Represents the Ultra High Performance option.

    For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "autotune_policies": "autotunePolicies",
        "block_volume_replicas": "blockVolumeReplicas",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "freeform_tags": "freeformTags",
        "is_auto_tune_enabled": "isAutoTuneEnabled",
        "size_in_g_bs": "sizeInGBs",
        "vpus_per_gb": "vpusPerGB",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/volumes/{volumeId}".format(**{"volumeId": volume_id}),
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
            "auto_tuned_vpus_per_gb": "autoTunedVpusPerGB",
            "autotune_policies": "autotunePolicies",
            "availability_domain": "availabilityDomain",
            "block_volume_replicas": "blockVolumeReplicas",
            "compartment_id": "compartmentId",
            "defined_tags": "definedTags",
            "display_name": "displayName",
            "freeform_tags": "freeformTags",
            "id": "id",
            "is_auto_tune_enabled": "isAutoTuneEnabled",
            "is_hydrated": "isHydrated",
            "kms_key_id": "kmsKeyId",
            "lifecycle_state": "lifecycleState",
            "size_in_g_bs": "sizeInGBs",
            "size_in_m_bs": "sizeInMBs",
            "source_details": "sourceDetails",
            "time_created": "timeCreated",
            "volume_group_id": "volumeGroupId",
            "vpus_per_gb": "vpusPerGB",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_volume(
    hub, ctx, volume_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteVolume
            Deletes the specified volume. The volume cannot have an active connection to an instance.
        To disconnect the volume from a connected instance, see
        [Disconnecting From a Volume](/iaas/Content/Block/Tasks/disconnectingfromavolume.htm).
        **Warning:** All data on the volume will be permanently lost when the volume is deleted.

        Args:
            volume_id(str):
                The OCID of the volume.

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
        path="/volumes/{volumeId}".format(**{"volumeId": volume_id}),
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


async def change_volume_compartment(
    hub, ctx, volume_id: str, compartment_id: str, opc_request_id: str = None
) -> Dict[str, Any]:
    r"""

        ChangeVolumeCompartment
            Moves a volume into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

        Args:
            volume_id(str):
                The OCID of the volume.

            compartment_id(str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the volume to.

            opc_request_id(str, Optional):
                Unique identifier for the request.
    If you need to contact Oracle about a particular request, please provide the request ID.
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
        path="/volumes/{volumeId}/actions/changeCompartment".format(
            **{"volumeId": volume_id}
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


async def get_volume_kms_key(
    hub, ctx, volume_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        GetVolumeKmsKey
            Gets the Vault service encryption key assigned to the specified volume.

        Args:
            volume_id(str):
                The OCID of the volume.

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
        method="get",
        path="/volumes/{volumeId}/kmsKey".format(**{"volumeId": volume_id}),
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
    resource_parameters = OrderedDict({"kms_key_id": "kmsKeyId"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_volume_kms_key(
    hub, ctx, volume_id: str, if_match: str = None, kms_key_id: str = None
) -> Dict[str, Any]:
    r"""

        UpdateVolumeKmsKey
            Updates the specified volume with a new Key Management master encryption key.

        Args:
            volume_id(str):
                The OCID of the volume.

            if_match(str, Optional):
                For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
    parameter to the value of the etag from a previous GET or POST response for that resource. The resource
    will be updated or deleted only if the etag you provide matches the resource's current etag value.
    . Defaults to None.

            kms_key_id(str, Optional):
                The OCID of the new Vault service key to assign to protect the specified volume.
    This key has to be a valid Vault service key, and policies must exist to allow the user and the Block Volume service to access this key.
    If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.
    . Defaults to None.

        Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {"kms_key_id": "kmsKeyId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/volumes/{volumeId}/kmsKey".format(**{"volumeId": volume_id}),
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
    resource_parameters = OrderedDict({"kms_key_id": "kmsKeyId"})

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def delete_volume_kms_key(
    hub, ctx, volume_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

        DeleteVolumeKmsKey
            Removes the specified volume's assigned Vault service encryption key.

        Args:
            volume_id(str):
                The OCID of the volume.

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
        path="/volumes/{volumeId}/kmsKey".format(**{"volumeId": volume_id}),
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
