"""Utility functions for Compute Managements. """
from collections import OrderedDict
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import Dict
from typing import List


async def list_cluster_networks(
    hub,
    ctx,
    compartment_id: str,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListClusterNetworks
        Lists the [cluster networks with instance pools](/iaas/Content/Compute/Tasks/managingclusternetworks.htm)
    in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
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
        path="/clusterNetworks".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "displayName": display_name,
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


async def create_cluster_network(
    hub,
    ctx,
    compartment_id: str,
    instance_pools: List[
        make_dataclass(
            "instance_pools",
            [
                ("instance_configuration_id", str),
                ("size", int),
                ("defined_tags", Dict, field(default=None)),
                ("display_name", str, field(default=None)),
                ("freeform_tags", Dict, field(default=None)),
            ],
        )
    ],
    placement_configuration: make_dataclass(
        "placement_configuration",
        [
            ("availability_domain", str),
            ("primary_subnet_id", str, field(default=None)),
            (
                "primary_vnic_subnets",
                make_dataclass(
                    "primary_vnic_subnets",
                    [
                        ("subnet_id", str),
                        (
                            "ipv6_address_ipv6_subnet_cidr_pair_details",
                            List[
                                make_dataclass(
                                    "ipv6_address_ipv6_subnet_cidr_pair_details",
                                    [("ipv6_subnet_cidr", str, field(default=None))],
                                )
                            ],
                            field(default=None),
                        ),
                        ("is_assign_ipv6_ip", bool, field(default=None)),
                    ],
                ),
                field(default=None),
            ),
            (
                "secondary_vnic_subnets",
                List[
                    make_dataclass(
                        "secondary_vnic_subnets",
                        [
                            ("subnet_id", str),
                            ("display_name", str, field(default=None)),
                            (
                                "ipv6_address_ipv6_subnet_cidr_pair_details",
                                List[
                                    make_dataclass(
                                        "ipv6_address_ipv6_subnet_cidr_pair_details",
                                        [
                                            (
                                                "ipv6_subnet_cidr",
                                                str,
                                                field(default=None),
                                            )
                                        ],
                                    )
                                ],
                                field(default=None),
                            ),
                            ("is_assign_ipv6_ip", bool, field(default=None)),
                        ],
                    )
                ],
                field(default=None),
            ),
        ],
    ),
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    CreateClusterNetwork
        Creates a [cluster network with instance pools](/iaas/Content/Compute/Tasks/managingclusternetworks.htm).
    A cluster network is a group of high performance computing (HPC), GPU, or optimized bare metal
    instances that are connected with an ultra low-latency remote direct memory access (RDMA) network.
    Cluster networks with instance pools use instance pools to manage groups of identical instances.

    Use cluster networks with instance pools when you want predictable capacity for a specific number of identical
    instances that are managed as a group.

    If you want to manage instances in the RDMA network independently of each other or use different types of instances
    in the network group, create a compute cluster by using the [CreateComputeCluster](#/en/iaas/latest/ComputeCluster/CreateComputeCluster)
    operation.

    To determine whether capacity is available for a specific shape before you create a cluster network,
    use the [CreateComputeCapacityReport](#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)
    operation.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment
            containing the cluster network.


        instance_pools(List[dict[str, Any]]):
            The data to create the instance pools in the cluster network.

            Each cluster network can have one instance pool.


            * defined_tags (Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
                namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

                Example: `{"Operations": {"CostCenter": "42"}}`
                Defaults to None.

            * display_name (str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
                Avoid entering confidential information.
                Defaults to None.

            * freeform_tags (Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
                predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

                Example: `{"Department": "Finance"}`
                Defaults to None.

            * instance_configuration_id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration
                associated with the instance pool.


            * size (int):
                The number of instances that should be in the instance pool.


        placement_configuration(dict[str, Any]):
            placementConfiguration.

            * availability_domain (str):
                The availability domain to place instances.

                Example: `Uocm:PHX-AD-1`


            * primary_subnet_id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the primary subnet to place instances. This field is deprecated.
                Use `primaryVnicSubnets` instead to set VNIC data for instances in the pool.
                Defaults to None.

            * primary_vnic_subnets (dict[str, Any], Optional):
                primaryVnicSubnets. Defaults to None.

                * ipv6_address_ipv6_subnet_cidr_pair_details (List[dict[str, Any]], Optional):
                    A list of IPv6 prefix ranges from which the VNIC should be assigned an IPv6 address.
                    You can provide only the prefix ranges and OCI will select an available
                    address from the range. You can optionally choose to leave the prefix range empty
                    and instead provide the specific IPv6 address that should be used from within that range.
                    Defaults to None.

                    * ipv6_subnet_cidr (str, Optional):
                        Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.
                        Defaults to None.

                * is_assign_ipv6_ip (bool, Optional):
                    Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled
                    subnet. Default: False. When provided you may optionally provide an IPv6 prefix
                    (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr`
                    is not provided then an IPv6 prefix is chosen
                    for you.
                    Defaults to None.

                * subnet_id (str):
                    The subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.

            * secondary_vnic_subnets (List[dict[str, Any]], Optional):
                The set of secondary VNIC data for instances in the pool. Defaults to None.

                * display_name (str, Optional):
                    The display name of the VNIC. This is also used to match against the instance configuration defined
                    secondary VNIC.
                    Defaults to None.

                * ipv6_address_ipv6_subnet_cidr_pair_details (List[dict[str, Any]], Optional):
                    A list of IPv6 prefix ranges from which the VNIC should be assigned an IPv6 address.
                    You can provide only the prefix ranges and OCI will select an available
                    address from the range. You can optionally choose to leave the prefix range empty
                    and instead provide the specific IPv6 address that should be used from within that range.
                    Defaults to None.

                    * ipv6_subnet_cidr (str, Optional):
                        Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.
                        Defaults to None.

                * is_assign_ipv6_ip (bool, Optional):
                    Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled
                    subnet. Default: False. When provided you may optionally provide an IPv6 prefix
                    (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr`
                    is not provided then an IPv6 prefix is chosen
                    for you.
                    Defaults to None.

                * subnet_id (str):
                    The subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.

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
        "instance_pools": "instancePools",
        "placement_configuration": "placementConfiguration",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/clusterNetworks".format(**{}),
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
            "hpcIslandId": "hpc_island_id",
            "id": "id",
            "instancePools": "instance_pools",
            "lifecycleState": "lifecycle_state",
            "networkBlockIds": "network_block_ids",
            "placementConfiguration": "placement_configuration",
            "timeCreated": "time_created",
            "timeUpdated": "time_updated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def get_cluster_network(hub, ctx, cluster_network_id: str) -> Dict[str, Any]:
    r"""

    GetClusterNetwork
        Gets information about a [cluster network with instance pools](/iaas/Content/Compute/Tasks/managingclusternetworks.htm).

    Args:
        cluster_network_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/clusterNetworks/{clusterNetworkId}".format(
            **{"clusterNetworkId": cluster_network_id}
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
            "hpcIslandId": "hpc_island_id",
            "id": "id",
            "instancePools": "instance_pools",
            "lifecycleState": "lifecycle_state",
            "networkBlockIds": "network_block_ids",
            "placementConfiguration": "placement_configuration",
            "timeCreated": "time_created",
            "timeUpdated": "time_updated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def update_cluster_network(
    hub,
    ctx,
    cluster_network_id: str,
    opc_retry_token: str = None,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    instance_pools: List[
        make_dataclass(
            "instance_pools",
            [
                ("id", str),
                ("defined_tags", Dict, field(default=None)),
                ("display_name", str, field(default=None)),
                ("freeform_tags", Dict, field(default=None)),
                ("instance_configuration_id", str, field(default=None)),
                ("size", int, field(default=None)),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    UpdateClusterNetwork
        Updates a [cluster network with instance pools](/iaas/Content/Compute/Tasks/managingclusternetworks.htm).
    The OCID of the cluster network remains the same.

    Args:
        cluster_network_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.

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

        instance_pools(List[dict[str, Any]], Optional):
            The instance pools in the cluster network to update.
            Defaults to None.

            * defined_tags (Dict, Optional):
                Defined tags for this resource. Each key is predefined and scoped to a
                namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

                Example: `{"Operations": {"CostCenter": "42"}}`
                Defaults to None.

            * display_name (str, Optional):
                A user-friendly name. Does not have to be unique, and it's changeable.
                Avoid entering confidential information.
                Defaults to None.

            * freeform_tags (Dict, Optional):
                Free-form tags for this resource. Each tag is a simple key-value pair with no
                predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

                Example: `{"Department": "Finance"}`
                Defaults to None.

            * id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

            * instance_configuration_id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration associated with the instance pool.
                Defaults to None.

            * size (int, Optional):
                The number of instances that should be in the instance pool.

                To determine whether capacity is available for a specific shape before you resize an instance pool,
                use the [CreateComputeCapacityReport](#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)
                operation.
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
        "instance_pools": "instancePools",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/clusterNetworks/{clusterNetworkId}".format(
            **{"clusterNetworkId": cluster_network_id}
        ),
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
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "hpcIslandId": "hpc_island_id",
            "id": "id",
            "instancePools": "instance_pools",
            "lifecycleState": "lifecycle_state",
            "networkBlockIds": "network_block_ids",
            "placementConfiguration": "placement_configuration",
            "timeCreated": "time_created",
            "timeUpdated": "time_updated",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def terminate_cluster_network(
    hub, ctx, cluster_network_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    TerminateClusterNetwork
        Deletes (terminates) a [cluster network with instance pools](/iaas/Content/Compute/Tasks/managingclusternetworks.htm).

    When you delete a cluster network, all of its resources are permanently deleted,
    including associated instances and instance pools.

    Args:
        cluster_network_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.

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
        path="/clusterNetworks/{clusterNetworkId}".format(
            **{"clusterNetworkId": cluster_network_id}
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


async def change_cluster_network_compartment(
    hub,
    ctx,
    cluster_network_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeClusterNetworkCompartment
        Moves a [cluster network with instance pools](/iaas/Content/Compute/Tasks/managingclusternetworks.htm)
    into a different compartment within the same tenancy. For
    information about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    When you move a cluster network to a different compartment, associated resources such as the instances
    in the cluster network, boot volumes, and VNICs are not moved.

    Args:
        cluster_network_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment
            into which the resource should be moved.


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
        path="/clusterNetworks/{clusterNetworkId}/actions/changeCompartment".format(
            **{"clusterNetworkId": cluster_network_id}
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


async def list_cluster_network_instances(
    hub,
    ctx,
    compartment_id: str,
    cluster_network_id: str,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

    ListClusterNetworkInstances
        Lists the instances in a [cluster network with instance pools](/iaas/Content/Compute/Tasks/managingclusternetworks.htm).

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        cluster_network_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
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
        path="/clusterNetworks/{clusterNetworkId}/instances".format(
            **{"clusterNetworkId": cluster_network_id}
        ),
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


async def list_instance_configurations(
    hub,
    ctx,
    compartment_id: str,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

    ListInstanceConfigurations
        Lists the instance configurations in the specified compartment.

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
        path="/instanceConfigurations".format(**{}),
        query_params={
            "compartmentId": compartment_id,
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


async def create_instance_configuration(
    hub,
    ctx,
    compartment_id: str,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    source: str = None,
) -> Dict[str, Any]:
    r"""

    CreateInstanceConfiguration
        Creates an instance configuration. An instance configuration is a template that defines the
    settings to use when creating Compute instances.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment
            containing the instance configuration.


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

        source(str, Optional):
            The source of the instance configuration. An instance configuration defines the
            settings to use when creating Compute instances, including details
            such as the base image, shape, and metadata. You can also specify the associated resources for the
            instance, such as block volume attachments and network configuration.

            When you create an instance configuration using an existing instance as a template, the instance
            configuration does not include any information from the source instance's boot volume, such as installed
            applications, binaries, and files on the instance. It also does not include the contents of
            any block volumes that are attached to the instance.

            To create an instance configuration that includes the custom setup from an instance's boot volume, you
            must first create a custom image from the instance (see [CreateImage](#/en/iaas/latest/Image/CreateImage)).
            Then, use the custom image to launch a new instance
            (see [LaunchInstance](#/en/iaas/latest/Instance/LaunchInstance)). Finally, create the instance
            configuration based on the instance that you created from the custom image.

            To include block volume contents with an instance configuration, first create a backup of the attached block volumes
            (see [CreateVolumeBackup](#/en/iaas/latest/VolumeBackup/CreateVolumeBackup)). Then, create the instance
            configuration by specifying the list of settings, using
            [InstanceConfigurationVolumeSourceFromVolumeBackupDetails](#/en/iaas/latest/datatypes/InstanceConfigurationVolumeSourceFromVolumeBackupDetails)
            to include the block volume backups in the list of settings.

            The following values are supported:

            * `NONE`: Creates an instance configuration using the list of settings that you specify.
            * `INSTANCE`: Creates an instance configuration using an existing instance as a template.
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
        "source": "source",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instanceConfigurations".format(**{}),
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
            "deferredFields": "deferred_fields",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceDetails": "instance_details",
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


async def get_instance_configuration(
    hub, ctx, instance_configuration_id: str
) -> Dict[str, Any]:
    r"""

    GetInstanceConfiguration
        Gets the specified instance configuration

    Args:
        instance_configuration_id(str):
            The OCID of the instance configuration.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instanceConfigurations/{instanceConfigurationId}".format(
            **{"instanceConfigurationId": instance_configuration_id}
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
            "deferredFields": "deferred_fields",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceDetails": "instance_details",
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


async def update_instance_configuration(
    hub,
    ctx,
    instance_configuration_id: str,
    opc_retry_token: str = None,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
) -> Dict[str, Any]:
    r"""

    UpdateInstanceConfiguration
        Updates the free-form tags, defined tags, and display name of an instance configuration.

    Args:
        instance_configuration_id(str):
            The OCID of the instance configuration.

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
        path="/instanceConfigurations/{instanceConfigurationId}".format(
            **{"instanceConfigurationId": instance_configuration_id}
        ),
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
            "compartmentId": "compartment_id",
            "deferredFields": "deferred_fields",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceDetails": "instance_details",
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


async def delete_instance_configuration(
    hub, ctx, instance_configuration_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    DeleteInstanceConfiguration
        Deletes an instance configuration.

    Args:
        instance_configuration_id(str):
            The OCID of the instance configuration.

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
        path="/instanceConfigurations/{instanceConfigurationId}".format(
            **{"instanceConfigurationId": instance_configuration_id}
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


async def change_instance_configuration_compartment(
    hub,
    ctx,
    instance_configuration_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeInstanceConfigurationCompartment
        Moves an instance configuration into a different compartment within the same tenancy.
    For information about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    When you move an instance configuration to a different compartment, associated resources such as
    instance pools are not moved.

    **Important:** Most of the properties for an existing instance configuration, including the compartment,
    cannot be modified after you create the instance configuration. Although you can move an instance configuration
    to a different compartment, you will not be able to use the instance configuration to manage instance pools
    in the new compartment. If you want to update an instance configuration to point to a different compartment,
    you should instead create a new instance configuration in the target compartment using
    [CreateInstanceConfiguration](/iaas/api/#/en/iaas/20160918/InstanceConfiguration/CreateInstanceConfiguration).

    Args:
        instance_configuration_id(str):
            The OCID of the instance configuration.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to
            move the instance configuration to.


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
        path="/instanceConfigurations/{instanceConfigurationId}/actions/changeCompartment".format(
            **{"instanceConfigurationId": instance_configuration_id}
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


async def launch_instance_configuration(
    hub,
    ctx,
    instance_configuration_id: str,
    instance_type: str,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    LaunchInstanceConfiguration
        Creates an instance from an instance configuration.

    If the instance configuration does not include all of the parameters that are
    required to create an instance, such as the availability domain and subnet ID, you must
    provide these parameters when you create an instance from the instance configuration.
    For more information, see the [InstanceConfiguration](#/en/iaas/latest/InstanceConfiguration/)
    resource.

    To determine whether capacity is available for a specific shape before you create an instance,
    use the [CreateComputeCapacityReport](#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)
    operation.

    Args:
        instance_configuration_id(str):
            The OCID of the instance configuration.

        instance_type(str):
            The type of instance details. Supported instanceType is compute


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
    payload = {"instance_type": "instanceType"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instanceConfigurations/{instanceConfigurationId}/actions/launch".format(
            **{"instanceConfigurationId": instance_configuration_id}
        ),
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
            "agentConfig": "agent_config",
            "availabilityConfig": "availability_config",
            "availabilityDomain": "availability_domain",
            "capacityReservationId": "capacity_reservation_id",
            "compartmentId": "compartment_id",
            "dedicatedVmHostId": "dedicated_vm_host_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "extendedMetadata": "extended_metadata",
            "faultDomain": "fault_domain",
            "freeformTags": "freeform_tags",
            "id": "id",
            "imageId": "image_id",
            "instanceOptions": "instance_options",
            "ipxeScript": "ipxe_script",
            "launchMode": "launch_mode",
            "launchOptions": "launch_options",
            "lifecycleState": "lifecycle_state",
            "metadata": "metadata",
            "platformConfig": "platform_config",
            "preemptibleInstanceConfig": "preemptible_instance_config",
            "region": "region",
            "shape": "shape",
            "shapeConfig": "shape_config",
            "sourceDetails": "source_details",
            "timeCreated": "time_created",
            "timeMaintenanceRebootDue": "time_maintenance_reboot_due",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result


async def list_instance_pools(
    hub,
    ctx,
    compartment_id: str,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""

    ListInstancePools
        Lists the instance pools in the specified compartment.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
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
            A filter to only return resources that match the given lifecycle state. The state
            value is case-insensitive.
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
        path="/instancePools".format(**{}),
        query_params={
            "compartmentId": compartment_id,
            "displayName": display_name,
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


async def create_instance_pool(
    hub,
    ctx,
    compartment_id: str,
    instance_configuration_id: str,
    placement_configurations: List[
        make_dataclass(
            "placement_configurations",
            [
                ("availability_domain", str),
                ("fault_domains", List[str], field(default=None)),
                ("primary_subnet_id", str, field(default=None)),
                (
                    "primary_vnic_subnets",
                    make_dataclass(
                        "primary_vnic_subnets",
                        [
                            ("subnet_id", str),
                            (
                                "ipv6_address_ipv6_subnet_cidr_pair_details",
                                List[
                                    make_dataclass(
                                        "ipv6_address_ipv6_subnet_cidr_pair_details",
                                        [
                                            (
                                                "ipv6_subnet_cidr",
                                                str,
                                                field(default=None),
                                            )
                                        ],
                                    )
                                ],
                                field(default=None),
                            ),
                            ("is_assign_ipv6_ip", bool, field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "secondary_vnic_subnets",
                    List[
                        make_dataclass(
                            "secondary_vnic_subnets",
                            [
                                ("subnet_id", str),
                                ("display_name", str, field(default=None)),
                                (
                                    "ipv6_address_ipv6_subnet_cidr_pair_details",
                                    List[
                                        make_dataclass(
                                            "ipv6_address_ipv6_subnet_cidr_pair_details",
                                            [
                                                (
                                                    "ipv6_subnet_cidr",
                                                    str,
                                                    field(default=None),
                                                )
                                            ],
                                        )
                                    ],
                                    field(default=None),
                                ),
                                ("is_assign_ipv6_ip", bool, field(default=None)),
                            ],
                        )
                    ],
                    field(default=None),
                ),
            ],
        )
    ],
    size: int,
    opc_retry_token: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    instance_display_name_formatter: str = None,
    instance_hostname_formatter: str = None,
    load_balancers: List[
        make_dataclass(
            "load_balancers",
            [
                ("backend_set_name", str),
                ("load_balancer_id", str),
                ("port", int),
                ("vnic_selection", str),
            ],
        )
    ] = None,
) -> Dict[str, Any]:
    r"""

    CreateInstancePool
        Creates an instance pool.

    To determine whether capacity is available for a specific shape before you create an instance pool,
    use the [CreateComputeCapacityReport](#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)
    operation.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the instance pool.


        instance_configuration_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration associated
            with the instance pool.


        placement_configurations(List[dict[str, Any]]):
            The placement configurations for the instance pool. Provide one placement configuration for
            each availability domain.

            To use the instance pool with a regional subnet, provide a placement configuration for
            each availability domain, and include the regional subnet in each placement
            configuration.


            * availability_domain (str):
                The availability domain to place instances.

                Example: `Uocm:PHX-AD-1`


            * fault_domains (List[str], Optional):
                The fault domains to place instances.

                If you don't provide any values, the system makes a best effort to distribute
                instances across all fault domains based on capacity.

                To distribute the instances evenly across selected fault domains, provide a
                set of fault domains. For example, you might want instances to be evenly
                distributed if your applications require high availability.

                To get a list of fault domains, use the
                [ListFaultDomains](#/en/identity/20160918/FaultDomain/ListFaultDomains) operation
                in the Identity and Access Management Service API.

                Example: `[FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3]`
                Defaults to None.

            * primary_subnet_id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the primary subnet in which to place instances. This field is deprecated.
                Use `primaryVnicSubnets` instead to set VNIC data for instances in the pool.
                Defaults to None.

            * primary_vnic_subnets (dict[str, Any], Optional):
                primaryVnicSubnets. Defaults to None.

                * ipv6_address_ipv6_subnet_cidr_pair_details (List[dict[str, Any]], Optional):
                    A list of IPv6 prefix ranges from which the VNIC should be assigned an IPv6 address.
                    You can provide only the prefix ranges and OCI will select an available
                    address from the range. You can optionally choose to leave the prefix range empty
                    and instead provide the specific IPv6 address that should be used from within that range.
                    Defaults to None.

                    * ipv6_subnet_cidr (str, Optional):
                        Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.
                        Defaults to None.

                * is_assign_ipv6_ip (bool, Optional):
                    Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled
                    subnet. Default: False. When provided you may optionally provide an IPv6 prefix
                    (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr`
                    is not provided then an IPv6 prefix is chosen
                    for you.
                    Defaults to None.

                * subnet_id (str):
                    The subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.

            * secondary_vnic_subnets (List[dict[str, Any]], Optional):
                The set of secondary VNIC data for instances in the pool. Defaults to None.

                * display_name (str, Optional):
                    The display name of the VNIC. This is also used to match against the instance configuration defined
                    secondary VNIC.
                    Defaults to None.

                * ipv6_address_ipv6_subnet_cidr_pair_details (List[dict[str, Any]], Optional):
                    A list of IPv6 prefix ranges from which the VNIC should be assigned an IPv6 address.
                    You can provide only the prefix ranges and OCI will select an available
                    address from the range. You can optionally choose to leave the prefix range empty
                    and instead provide the specific IPv6 address that should be used from within that range.
                    Defaults to None.

                    * ipv6_subnet_cidr (str, Optional):
                        Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.
                        Defaults to None.

                * is_assign_ipv6_ip (bool, Optional):
                    Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled
                    subnet. Default: False. When provided you may optionally provide an IPv6 prefix
                    (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr`
                    is not provided then an IPv6 prefix is chosen
                    for you.
                    Defaults to None.

                * subnet_id (str):
                    The subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.

        size(int):
            The number of instances that should be in the instance pool.

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

        instance_display_name_formatter(str, Optional):
            A user-friendly formatter for the instance pool's instances. Instance displaynames follow the format.
            The formatter does not retroactively change instance's displaynames, only instance displaynames in the future follow the format
            Defaults to None.

        instance_hostname_formatter(str, Optional):
            A user-friendly formatter for the instance pool's instances. Instance hostnames follow the format.
            The formatter does not retroactively change instance's hostnames, only instance hostnames in the future follow the format
            Defaults to None.

        load_balancers(List[dict[str, Any]], Optional):
            The load balancers to attach to the instance pool.
            Defaults to None.

            * backend_set_name (str):
                The name of the backend set on the load balancer to add instances to.

            * load_balancer_id (str):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the load balancer to attach to the instance pool.


            * port (int):
                The port value to use when creating the backend set.

            * vnic_selection (str):
                Indicates which VNIC on each instance in the pool should be used to associate with the load balancer.
                Possible values are "PrimaryVnic" or the displayName of one of the secondary VNICs on the instance configuration
                that is associated with the instance pool.

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
        "instance_configuration_id": "instanceConfigurationId",
        "instance_display_name_formatter": "instanceDisplayNameFormatter",
        "instance_hostname_formatter": "instanceHostnameFormatter",
        "load_balancers": "loadBalancers",
        "placement_configurations": "placementConfigurations",
        "size": "size",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools".format(**{}),
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
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def get_instance_pool(hub, ctx, instance_pool_id: str) -> Dict[str, Any]:
    r"""

    GetInstancePool
        Gets the specified instance pool

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instancePools/{instancePoolId}".format(
            **{"instancePoolId": instance_pool_id}
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
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def update_instance_pool(
    hub,
    ctx,
    instance_pool_id: str,
    opc_retry_token: str = None,
    if_match: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    freeform_tags: Dict = None,
    instance_configuration_id: str = None,
    instance_display_name_formatter: str = None,
    instance_hostname_formatter: str = None,
    placement_configurations: List[
        make_dataclass(
            "placement_configurations",
            [
                ("availability_domain", str),
                ("fault_domains", List[str], field(default=None)),
                ("primary_subnet_id", str, field(default=None)),
                (
                    "primary_vnic_subnets",
                    make_dataclass(
                        "primary_vnic_subnets",
                        [
                            ("subnet_id", str),
                            (
                                "ipv6_address_ipv6_subnet_cidr_pair_details",
                                List[
                                    make_dataclass(
                                        "ipv6_address_ipv6_subnet_cidr_pair_details",
                                        [
                                            (
                                                "ipv6_subnet_cidr",
                                                str,
                                                field(default=None),
                                            )
                                        ],
                                    )
                                ],
                                field(default=None),
                            ),
                            ("is_assign_ipv6_ip", bool, field(default=None)),
                        ],
                    ),
                    field(default=None),
                ),
                (
                    "secondary_vnic_subnets",
                    List[
                        make_dataclass(
                            "secondary_vnic_subnets",
                            [
                                ("subnet_id", str),
                                ("display_name", str, field(default=None)),
                                (
                                    "ipv6_address_ipv6_subnet_cidr_pair_details",
                                    List[
                                        make_dataclass(
                                            "ipv6_address_ipv6_subnet_cidr_pair_details",
                                            [
                                                (
                                                    "ipv6_subnet_cidr",
                                                    str,
                                                    field(default=None),
                                                )
                                            ],
                                        )
                                    ],
                                    field(default=None),
                                ),
                                ("is_assign_ipv6_ip", bool, field(default=None)),
                            ],
                        )
                    ],
                    field(default=None),
                ),
            ],
        )
    ] = None,
    size: int = None,
) -> Dict[str, Any]:
    r"""

    UpdateInstancePool
        Update the specified instance pool.

    The OCID of the instance pool remains the same.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

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

        instance_configuration_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration associated with the
            instance pool.
            Defaults to None.

        instance_display_name_formatter(str, Optional):
            A user-friendly formatter for the instance pool's instances. Instance displaynames follow the format.
            The formatter does not retroactively change instance's displaynames, only instance displaynames in the future follow the format
            Defaults to None.

        instance_hostname_formatter(str, Optional):
            A user-friendly formatter for the instance pool's instances. Instance hostnames follow the format.
            The formatter does not retroactively change instance's hostnames, only instance hostnames in the future follow the format
            Defaults to None.

        placement_configurations(List[dict[str, Any]], Optional):
            The placement configurations for the instance pool. Provide one placement configuration for
            each availability domain.

            To use the instance pool with a regional subnet, provide a placement configuration for
            each availability domain, and include the regional subnet in each placement
            configuration.
            Defaults to None.

            * availability_domain (str):
                The availability domain to place instances.

                Example: `Uocm:PHX-AD-1`


            * fault_domains (List[str], Optional):
                The fault domains to place instances.

                If you don't provide any values, the system makes a best effort to distribute
                instances across all fault domains based on capacity.

                To distribute the instances evenly across selected fault domains, provide a
                set of fault domains. For example, you might want instances to be evenly
                distributed if your applications require high availability.

                To get a list of fault domains, use the
                [ListFaultDomains](#/en/identity/20160918/FaultDomain/ListFaultDomains) operation
                in the Identity and Access Management Service API.

                Example: `[FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3]`
                Defaults to None.

            * primary_subnet_id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the primary subnet in which to place instances. This field is deprecated.
                Use `primaryVnicSubnets` instead to set VNIC data for instances in the pool.
                Defaults to None.

            * primary_vnic_subnets (dict[str, Any], Optional):
                primaryVnicSubnets. Defaults to None.

                * ipv6_address_ipv6_subnet_cidr_pair_details (List[dict[str, Any]], Optional):
                    A list of IPv6 prefix ranges from which the VNIC should be assigned an IPv6 address.
                    You can provide only the prefix ranges and OCI will select an available
                    address from the range. You can optionally choose to leave the prefix range empty
                    and instead provide the specific IPv6 address that should be used from within that range.
                    Defaults to None.

                    * ipv6_subnet_cidr (str, Optional):
                        Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.
                        Defaults to None.

                * is_assign_ipv6_ip (bool, Optional):
                    Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled
                    subnet. Default: False. When provided you may optionally provide an IPv6 prefix
                    (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr`
                    is not provided then an IPv6 prefix is chosen
                    for you.
                    Defaults to None.

                * subnet_id (str):
                    The subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.

            * secondary_vnic_subnets (List[dict[str, Any]], Optional):
                The set of secondary VNIC data for instances in the pool. Defaults to None.

                * display_name (str, Optional):
                    The display name of the VNIC. This is also used to match against the instance configuration defined
                    secondary VNIC.
                    Defaults to None.

                * ipv6_address_ipv6_subnet_cidr_pair_details (List[dict[str, Any]], Optional):
                    A list of IPv6 prefix ranges from which the VNIC should be assigned an IPv6 address.
                    You can provide only the prefix ranges and OCI will select an available
                    address from the range. You can optionally choose to leave the prefix range empty
                    and instead provide the specific IPv6 address that should be used from within that range.
                    Defaults to None.

                    * ipv6_subnet_cidr (str, Optional):
                        Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.
                        Defaults to None.

                * is_assign_ipv6_ip (bool, Optional):
                    Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled
                    subnet. Default: False. When provided you may optionally provide an IPv6 prefix
                    (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr`
                    is not provided then an IPv6 prefix is chosen
                    for you.
                    Defaults to None.

                * subnet_id (str):
                    The subnet [OCID](/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.

        size(int, Optional):
            The number of instances that should be in the instance pool.

            To determine whether capacity is available for a specific shape before you resize an instance pool,
            use the [CreateComputeCapacityReport](#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)
            operation.
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
        "instance_configuration_id": "instanceConfigurationId",
        "instance_display_name_formatter": "instanceDisplayNameFormatter",
        "instance_hostname_formatter": "instanceHostnameFormatter",
        "placement_configurations": "placementConfigurations",
        "size": "size",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="put",
        path="/instancePools/{instancePoolId}".format(
            **{"instancePoolId": instance_pool_id}
        ),
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
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def terminate_instance_pool(
    hub, ctx, instance_pool_id: str, if_match: str = None
) -> Dict[str, Any]:
    r"""

    TerminateInstancePool
        Terminate the specified instance pool.

    **Warning:** When you delete an instance pool, the resources that were created by the pool are permanently
    deleted, including associated instances, attached boot volumes, and block volumes.

    If an autoscaling configuration applies to the instance pool, the autoscaling configuration will be deleted
    asynchronously after the pool is deleted. You can also manually delete the autoscaling configuration using
    the `DeleteAutoScalingConfiguration` operation in the Autoscaling API.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

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
        path="/instancePools/{instancePoolId}".format(
            **{"instancePoolId": instance_pool_id}
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


async def attach_load_balancer(
    hub,
    ctx,
    instance_pool_id: str,
    backend_set_name: str,
    load_balancer_id: str,
    port: int,
    vnic_selection: str,
    opc_retry_token: str = None,
    if_match: str = None,
) -> Dict[str, Any]:
    r"""

    AttachLoadBalancer
        Attach a load balancer to the instance pool.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

        backend_set_name(str):
            The name of the backend set on the load balancer to add instances to.

        load_balancer_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the load balancer to attach to the instance pool.


        port(int):
            The port value to use when creating the backend set.

        vnic_selection(str):
            Indicates which VNIC on each instance in the pool should be used to associate with the load balancer.
            Possible values are "PrimaryVnic" or the displayName of one of the secondary VNICs on the instance configuration
            that is associated with the instance pool.


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
        "backend_set_name": "backendSetName",
        "load_balancer_id": "loadBalancerId",
        "port": "port",
        "vnic_selection": "vnicSelection",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools/{instancePoolId}/actions/attachLoadBalancer".format(
            **{"instancePoolId": instance_pool_id}
        ),
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
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def change_instance_pool_compartment(
    hub,
    ctx,
    instance_pool_id: str,
    compartment_id: str,
    if_match: str = None,
    opc_request_id: str = None,
    opc_retry_token: str = None,
) -> Dict[str, Any]:
    r"""

    ChangeInstancePoolCompartment
        Moves an instance pool into a different compartment within the same tenancy. For
    information about moving resources between compartments, see
    [Moving Resources to a Different Compartment](/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

    When you move an instance pool to a different compartment, associated resources such as the instances in
    the pool, boot volumes, VNICs, and autoscaling configurations are not moved.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment to
            move the instance pool to.


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
        path="/instancePools/{instancePoolId}/actions/changeCompartment".format(
            **{"instancePoolId": instance_pool_id}
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


async def detach_instance_pool_instance(
    hub,
    ctx,
    instance_pool_id: str,
    instance_id: str,
    opc_retry_token: str = None,
    is_auto_terminate: bool = None,
    is_decrement_size: bool = None,
) -> Dict[str, Any]:
    r"""

    DetachInstancePoolInstance
        Detaches an instance from an instance pool.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

        instance_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        is_auto_terminate(bool, Optional):
            Whether to permanently terminate (delete) the instance and its attached boot volume
            when detaching it from the instance pool. Default is `false`.
            Defaults to None.

        is_decrement_size(bool, Optional):
            Whether to decrease the size of the instance pool when the instance is detached. If `true`, the
            pool size is decreased. If `false`, the pool will provision a new, replacement instance
            using the pool's instance configuration as a template. Default is `true`.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {
        "instance_id": "instanceId",
        "is_auto_terminate": "isAutoTerminate",
        "is_decrement_size": "isDecrementSize",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools/{instancePoolId}/actions/detachInstance".format(
            **{"instancePoolId": instance_pool_id}
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


async def detach_load_balancer(
    hub,
    ctx,
    instance_pool_id: str,
    backend_set_name: str,
    load_balancer_id: str,
    opc_retry_token: str = None,
    if_match: str = None,
) -> Dict[str, Any]:
    r"""

    DetachLoadBalancer
        Detach a load balancer from the instance pool.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

        backend_set_name(str):
            The name of the backend set on the load balancer to detach from the instance pool.

        load_balancer_id(str):
            The OCID of the load balancer to detach from the instance pool.

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
        "backend_set_name": "backendSetName",
        "load_balancer_id": "loadBalancerId",
    }

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools/{instancePoolId}/actions/detachLoadBalancer".format(
            **{"instancePoolId": instance_pool_id}
        ),
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
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def reset_instance_pool(
    hub, ctx, instance_pool_id: str, opc_retry_token: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

    ResetInstancePool
        Performs the reset (immediate power off and power on) action on the specified instance pool,
    which performs the action on all the instances in the pool.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

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
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools/{instancePoolId}/actions/reset".format(
            **{"instancePoolId": instance_pool_id}
        ),
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
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def softreset_instance_pool(
    hub, ctx, instance_pool_id: str, opc_retry_token: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

    SoftresetInstancePool
        Performs the softreset (ACPI shutdown and power on) action on the specified instance pool,
    which performs the action on all the instances in the pool.

    Softreset gracefully reboots the instances by sending a shutdown command to the operating systems.
    After waiting 15 minutes for the OS to shut down, the instances are powered off and then powered back on.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

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
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools/{instancePoolId}/actions/softreset".format(
            **{"instancePoolId": instance_pool_id}
        ),
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
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def softstop_instance_pool(
    hub, ctx, instance_pool_id: str, opc_retry_token: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

    SoftstopInstancePool
        Performs the softstop (ACPI shutdown and power on) action on the specified instance pool,
    which performs the action on all the instances in the pool.

    Softstop gracefully reboots the instances by sending a shutdown command to the operating systems.
    After waiting 15 minutes for the OS to shutdown, the instances are powered off and then powered back on.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

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
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools/{instancePoolId}/actions/softstop".format(
            **{"instancePoolId": instance_pool_id}
        ),
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
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def start_instance_pool(
    hub, ctx, instance_pool_id: str, opc_retry_token: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

    StartInstancePool
        Performs the start (power on) action on the specified instance pool,
    which performs the action on all the instances in the pool.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

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
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools/{instancePoolId}/actions/start".format(
            **{"instancePoolId": instance_pool_id}
        ),
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
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def stop_instance_pool(
    hub, ctx, instance_pool_id: str, opc_retry_token: str = None, if_match: str = None
) -> Dict[str, Any]:
    r"""

    StopInstancePool
        Performs the stop (immediate power off) action on the specified instance pool,
    which performs the action on all the instances in the pool.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

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
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools/{instancePoolId}/actions/stop".format(
            **{"instancePoolId": instance_pool_id}
        ),
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
            "compartmentId": "compartment_id",
            "definedTags": "defined_tags",
            "displayName": "display_name",
            "freeformTags": "freeform_tags",
            "id": "id",
            "instanceConfigurationId": "instance_configuration_id",
            "instanceDisplayNameFormatter": "instance_display_name_formatter",
            "instanceHostnameFormatter": "instance_hostname_formatter",
            "lifecycleState": "lifecycle_state",
            "loadBalancers": "load_balancers",
            "placementConfigurations": "placement_configurations",
            "size": "size",
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


async def list_instance_pool_instances(
    hub,
    ctx,
    compartment_id: str,
    instance_pool_id: str,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
) -> Dict[str, Any]:
    r"""

    ListInstancePoolInstances
        List the instances in the specified instance pool.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly.
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
        path="/instancePools/{instancePoolId}/instances".format(
            **{"instancePoolId": instance_pool_id}
        ),
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


async def attach_instance_pool_instance(
    hub, ctx, instance_pool_id: str, instance_id: str, opc_retry_token: str = None
) -> Dict[str, Any]:
    r"""

    AttachInstancePoolInstance
        Attaches an instance to an instance pool. For information about the prerequisites
    that an instance must meet before you can attach it to a pool, see
    [Attaching an Instance to an Instance Pool](/iaas/Content/Compute/Tasks/updatinginstancepool.htm#attach-instance).

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

        instance_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

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
    payload = {"instance_id": "instanceId"}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instancePools/{instancePoolId}/instances".format(
            **{"instancePoolId": instance_pool_id}
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


async def get_instance_pool_instance(
    hub, ctx, instance_pool_id: str, instance_id: str
) -> Dict[str, Any]:
    r"""

    GetInstancePoolInstance
        Gets information about an instance that belongs to an instance pool.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

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
        path="/instancePools/{instancePoolId}/instances/{instanceId}".format(
            **{"instancePoolId": instance_pool_id, "instanceId": instance_id}
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
            "availabilityDomain": "availability_domain",
            "compartmentId": "compartment_id",
            "displayName": "display_name",
            "faultDomain": "fault_domain",
            "id": "id",
            "instanceConfigurationId": "instance_configuration_id",
            "instancePoolId": "instance_pool_id",
            "lifecycleState": "lifecycle_state",
            "loadBalancerBackends": "load_balancer_backends",
            "region": "region",
            "shape": "shape",
            "state": "state",
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


async def get_instance_pool_load_balancer_attachment(
    hub, ctx, instance_pool_id: str, instance_pool_load_balancer_attachment_id: str
) -> Dict[str, Any]:
    r"""

    GetLoadBalancerAttachment
        Gets information about a load balancer that is attached to the specified instance pool.

    Args:
        instance_pool_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

        instance_pool_load_balancer_attachment_id(str):
            The OCID of the load balancer attachment.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change request param mapping as necessary
    payload = {}

    ret = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instancePools/{instancePoolId}/loadBalancerAttachments/{instancePoolLoadBalancerAttachmentId}".format(
            **{
                "instancePoolId": instance_pool_id,
                "instancePoolLoadBalancerAttachmentId": instance_pool_load_balancer_attachment_id,
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
            "backendSetName": "backend_set_name",
            "id": "id",
            "instancePoolId": "instance_pool_id",
            "lifecycleState": "lifecycle_state",
            "loadBalancerId": "load_balancer_id",
            "port": "port",
            "vnicSelection": "vnic_selection",
        }
    )

    for parameter_raw, parameter_present in resource_parameters.items():
        if parameter_raw in raw_resource and raw_resource.get(parameter_raw):
            resource_in_present_format[parameter_present] = raw_resource.get(
                parameter_raw
            )

    result["ret"] = resource_in_present_format

    return result
