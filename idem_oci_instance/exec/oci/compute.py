"""Exec module for managing Computes. """
from collections import OrderedDict
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import Dict
from typing import List

__contracts__ = ["soft_fail"]

__func_alias__ = {"list_": "list"}


async def get(hub, ctx, resource_id: str, name: str = None) -> Dict[str, Any]:
    r"""
    Gets information about the specified instance.

    **Note:** To retrieve public and private IP addresses for an instance, use the [ListVnicAttachments](#/en/iaas/latest/VnicAttachment/ListVnicAttachments)
    operation to get the VNIC ID for the instance, and then call [GetVnic](#/en/iaas/latest/Vnic/GetVnic) with the VNIC ID.

    Args:
        resource_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

    Returns:
        Dict[str, Any]
    """

    result = dict(comment=[], ret=None, result=True)

    get = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instances/{instanceId}".format(**{"instanceId": resource_id}),
        query_params={},
        data={},
        headers={},
    )

    if not get["result"]:
        result["comment"].append(get["comment"])
        result["result"] = False
        return result

    # Convert raw response into present format
    raw_resource = get["ret"]

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
    get["ret"]["resource_id"] = resource_id

    return result


async def list_(
    hub,
    ctx,
    compartment_id: str = None,
    availability_domain: str = None,
    capacity_reservation_id: str = None,
    compute_cluster_id: str = None,
    display_name: str = None,
    limit: int = None,
    page: str = None,
    sort_by: str = None,
    sort_order: str = None,
    lifecycle_state: str = None,
) -> Dict[str, Any]:
    r"""
    Lists the instances in the specified compartment and the specified availability domain.
    You can filter the results by specifying an instance name (the list will include all the identically-named
    instances in the compartment).

    **Note:** To retrieve public and private IP addresses for an instance, use the [ListVnicAttachments](#/en/iaas/latest/VnicAttachment/ListVnicAttachments)
    operation to get the VNIC ID for the instance, and then call [GetVnic](#/en/iaas/latest/Vnic/GetVnic) with the VNIC ID.

    Args:
        compartment_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

        availability_domain(str, Optional):
            The name of the availability domain.Example: `Uocm:PHX-AD-1`. Defaults to None.

        capacity_reservation_id(str, Optional):
            The OCID of the compute capacity reservation. Defaults to None.

        compute_cluster_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the compute cluster.
            A [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) is a remote direct memory
            access (RDMA) network group. Defaults to None.

        display_name(str, Optional):
            A filter to return only resources that match the given display name exactly. Defaults to None.

        limit(int, Optional):
            For list pagination. The maximum number of results per page, or items to return in a paginated "List" call. For important details about how pagination works, see [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50` . Defaults to None.

        page(str, Optional):
            For list pagination. The value of the `opc-next-page` response header from the previous "List" call. For important details about how pagination works, see [List Pagination](/iaas/Content/API/Concepts/usingapi.htm#nine). Defaults to None.

        sort_by(str, Optional):
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

        **Note:** In general, some "List" operations (for example, `ListInstances`) let you
        optionally filter by availability domain if the scope of the resource type is within a
        single availability domain. If you call one of these "List" operations without specifying
        an availability domain, the resources are grouped by availability domain, then sorted. . Defaults to None.

        sort_order(str, Optional):
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive. Defaults to None.

        lifecycle_state(str, Optional):
            A filter to only return resources that match the given lifecycle state. The state value is case-insensitive. Defaults to None.

    Returns:
            Dict[str, Any]

    """

    result = dict(comment=[], ret=[], result=True)

    list = await hub.tool.oci.session.request(
        ctx,
        method="get",
        path="/instances/",
        query_params={
            "availabilityDomain": availability_domain,
            "capacityReservationId": capacity_reservation_id,
            "computeClusterId": compute_cluster_id,
            "compartmentId": compartment_id or ctx.acct.compartment_id,
            "displayName": display_name,
            "limit": limit,
            "page": page,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "lifecycleState": lifecycle_state,
        },
        data={},
        headers={},
    )

    if not list["result"]:
        result["comment"].append(list["comment"])
        result["result"] = False
        return result

    for raw_resource in list["ret"]:
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

        resource_in_present_format["resource_id"] = raw_resource.get("id")
        result["ret"].append(resource_in_present_format)

    return result


async def create(
    hub,
    ctx,
    availability_domain: str,
    shape: str,
    opc_retry_token: str = None,
    compartment_id: str = None,
    agent_config: make_dataclass(
        "agent_config",
        [
            ("are_all_plugins_disabled", bool, field(default=None)),
            ("is_management_disabled", bool, field(default=None)),
            ("is_monitoring_disabled", bool, field(default=None)),
            (
                "plugins_config",
                List[
                    make_dataclass(
                        "plugins_config", [("desired_state", str), ("name", str)]
                    )
                ],
                field(default=None),
            ),
        ],
    ) = None,
    availability_config: make_dataclass(
        "availability_config",
        [
            ("is_live_migration_preferred", bool, field(default=None)),
            ("recovery_action", str, field(default=None)),
        ],
    ) = None,
    capacity_reservation_id: str = None,
    compute_cluster_id: str = None,
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
    ) = None,
    dedicated_vm_host_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    extended_metadata: Dict = None,
    fault_domain: str = None,
    freeform_tags: Dict = None,
    hostname_label: str = None,
    image_id: str = None,
    instance_options: make_dataclass(
        "instance_options",
        [("are_legacy_imds_endpoints_disabled", bool, field(default=None))],
    ) = None,
    ipxe_script: str = None,
    is_pv_encryption_in_transit_enabled: bool = None,
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
    metadata: Dict = None,
    platform_config: make_dataclass(
        "platform_config",
        [
            ("type", str),
            ("is_measured_boot_enabled", bool, field(default=None)),
            ("is_secure_boot_enabled", bool, field(default=None)),
            ("is_trusted_platform_module_enabled", bool, field(default=None)),
        ],
    ) = None,
    preemptible_instance_config: make_dataclass(
        "preemptible_instance_config",
        [("preemption_action", make_dataclass("preemption_action", [("type", str)]))],
    ) = None,
    shape_config: make_dataclass(
        "shape_config",
        [
            ("baseline_ocpu_utilization", str, field(default=None)),
            ("memory_in_g_bs", float, field(default=None)),
            ("nvmes", int, field(default=None)),
            ("ocpus", float, field(default=None)),
        ],
    ) = None,
    source_details: make_dataclass("source_details", [("source_type", str)]) = None,
    subnet_id: str = None,
    name: str = None,
) -> Dict[str, Any]:
    """
    Creates a new instance in the specified compartment and the specified availability domain.
    For general information about instances, see
    [Overview of the Compute Service](/iaas/Content/Compute/Concepts/computeoverview.htm).

    For information about access control and compartments, see
    [Overview of the IAM Service](/iaas/Content/Identity/Concepts/overview.htm).

    For information about availability domains, see
    [Regions and Availability Domains](/iaas/Content/General/Concepts/regions.htm).
    To get a list of availability domains, use the `ListAvailabilityDomains` operation
    in the Identity and Access Management Service API.

    All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned,
    unique ID called an Oracle Cloud Identifier (OCID).
    When you create a resource, you can find its OCID in the response. You can
    also retrieve a resource's OCID by using a List API operation
    on that resource type, or by viewing the resource in the Console.

    To launch an instance using an image or a boot volume use the `sourceDetails` parameter in [LaunchInstanceDetails](#/en/iaas/latest/LaunchInstanceDetails).

    When you launch an instance, it is automatically attached to a virtual
    network interface card (VNIC), called the *primary VNIC*. The VNIC
    has a private IP address from the subnet's CIDR. You can either assign a
    private IP address of your choice or let Oracle automatically assign one.
    You can choose whether the instance has a public IP address. To retrieve the
    addresses, use the [ListVnicAttachments](#/en/iaas/latest/VnicAttachment/ListVnicAttachments)
    operation to get the VNIC ID for the instance, and then call
    [GetVnic](#/en/iaas/latest/Vnic/GetVnic) with the VNIC ID.

    You can later add secondary VNICs to an instance. For more information, see
    [Virtual Network Interface Cards (VNICs)](/iaas/Content/Network/Tasks/managingVNICs.htm).

    To launch an instance from a Marketplace image listing, you must provide the image ID of the
    listing resource version that you want, but you also must subscribe to the listing before you try
    to launch the instance. To subscribe to the listing, use the [GetAppCatalogListingAgreements](#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements)
    operation to get the signature for the terms of use agreement for the desired listing resource version.
    Then, call [CreateAppCatalogSubscription](#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription)
    with the signature. To get the image ID for the LaunchInstance operation, call
    [GetAppCatalogListingResourceVersion](#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion).

    To determine whether capacity is available for a specific shape before you create an instance,
    use the [CreateComputeCapacityReport](#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)
    operation.

    Args:
        availability_domain(str):
            The availability domain of the instance. Example: `Uocm:PHX-AD-1` .

        compartment_id(str):
            The OCID of the compartment.

        shape(str):
            The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.
            You can enumerate all available shapes by calling [ListShapes](#/en/iaas/latest/Shape/ListShapes).

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            . Defaults to None.

        agent_config(dict[str, Any], Optional):
            agentConfig. Defaults to None.

            * are_all_plugins_disabled (bool, Optional):
                Whether Oracle Cloud Agent can run all the available plugins.
                This includes the management and monitoring plugins.

                To get a list of available plugins, use the
                [ListInstanceagentAvailablePlugins](#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                [Managing Plugins with Oracle Cloud Agent](/iaas/Content/Compute/Tasks/manage-plugins.htm).


            * is_management_disabled (bool, Optional):
                Whether Oracle Cloud Agent can run all the available management plugins.
                Default value is false (management plugins are enabled).

                These are the management plugins: OS Management Service Agent and Compute Instance
                Run Command.

                The management plugins are controlled by this parameter and by the per-plugin
                configuration in the `pluginsConfig` object.

                - If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of
                the per-plugin configuration.
                - If `isManagementDisabled` is false, all of the management plugins are enabled. You
                can optionally disable individual management plugins by providing a value in the `pluginsConfig`
                object.


            * is_monitoring_disabled (bool, Optional):
                Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
                monitoring plugins. Default value is false (monitoring plugins are enabled).

                These are the monitoring plugins: Compute Instance Monitoring
                and Custom Logs Monitoring.

                The monitoring plugins are controlled by this parameter and by the per-plugin
                configuration in the `pluginsConfig` object.

                - If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of
                the per-plugin configuration.
                - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You
                can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                object.


            * plugins_config (List[dict[str, Any]], Optional):
                The configuration of plugins associated with this instance.

                * desired_state (str):
                    Whether the plugin should be enabled or disabled.

                    To enable the monitoring and management plugins, the `isMonitoringDisabled` and
                    `isManagementDisabled` attributes must also be set to false.


                * name (str):
                    The plugin name. To get a list of available plugins, use the
                    [ListInstanceagentAvailablePlugins](#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                    operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                    [Managing Plugins with Oracle Cloud Agent](/iaas/Content/Compute/Tasks/manage-plugins.htm).


        availability_config(dict[str, Any], Optional):
            availabilityConfig. Defaults to None.

            * is_live_migration_preferred (bool, Optional):
                Whether to live migrate supported VM instances to a healthy physical VM host without
                disrupting running instances during infrastructure maintenance events. If null, Oracle
                chooses the best option for migrating the VM during infrastructure maintenance events.


            * recovery_action (str, Optional):
                The lifecycle state for an instance when it is recovered after infrastructure maintenance.
                * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event.
                If the instance was running, it is automatically rebooted. This is the default action when a value is not set.
                * `STOP_INSTANCE` - The instance is recovered in the stopped state.


        capacity_reservation_id(str, Optional):
            The OCID of the compute capacity reservation this instance is launched under.
            You can opt out of all default reservations by specifying an empty string as input for this field.
            For more information, see [Capacity Reservations](/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
            . Defaults to None.

        compute_cluster_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the
            [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) that the instance will be created in.
            . Defaults to None.

        create_vnic_details(dict[str, Any], Optional):
            createVnicDetails. Defaults to None.

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


        dedicated_vm_host_id(str, Optional):
            The OCID of the dedicated virtual machine host to place the instance on.
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

        extended_metadata(Dict, Optional):
            Additional metadata key/value pairs that you provide. They serve the same purpose and
            functionality as fields in the `metadata` object.

            They are distinguished from `metadata` fields in that these can be nested JSON objects
            (whereas `metadata` fields are string/string maps only).

            The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
            32,000 bytes.
            . Defaults to None.

        fault_domain(str, Optional):
            A fault domain is a grouping of hardware and infrastructure within an availability domain.
            Each availability domain contains three fault domains. Fault domains let you distribute your
            instances so that they are not on the same physical hardware within a single availability domain.
            A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
            instances in other fault domains.

            If you do not specify the fault domain, the system selects one for you.


            To get a list of fault domains, use the
            [ListFaultDomains](#/en/identity/20160918/FaultDomain/ListFaultDomains) operation in the
            Identity and Access Management Service API.

            Example: `FAULT-DOMAIN-1`
            . Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            . Defaults to None.

                    hostname_label(str, Optional):
                        Deprecated. Instead use `hostnameLabel` in
            [CreateVnicDetails](#/en/iaas/latest/CreateVnicDetails/).
            If you provide both, the values must match.
            . Defaults to None.

        image_id(str, Optional):
            Deprecated. Use `sourceDetails` with [InstanceSourceViaImageDetails](#/en/iaas/latest/requests/InstanceSourceViaImageDetails)
            source type instead. If you specify values for both, the values must match.
            . Defaults to None.

                    instance_options(dict[str, Any], Optional):
                        instanceOptions. Defaults to None.

                        * are_legacy_imds_endpoints_disabled (bool, Optional):
                            Whether to disable the legacy (/v1) instance metadata service endpoints.
            Customers who have migrated to /v2 should set this to true for added security.
            Default is false.


        ipxe_script(str, Optional):
            This is an advanced option.

            When a bare metal or virtual machine
            instance boots, the iPXE firmware that runs on the instance is
            configured to run an iPXE script to continue the boot process.

            If you want more control over the boot process, you can provide
            your own custom iPXE script that will run when the instance boots.
            Be aware that the same iPXE script will run
            every time an instance boots, not only after the initial
            LaunchInstance call.

            The default iPXE script connects to the instance's local boot
            volume over iSCSI and performs a network boot. If you use a custom iPXE
            script and want to network-boot from the instance's local boot volume
            over iSCSI the same way as the default iPXE script, use the
            following iSCSI IP address: 169.254.0.2, and boot volume IQN:
            iqn.2015-02.oracle.boot.

            If your instance boot volume attachment type is paravirtualized,
            the boot volume is attached to the instance through virtio-scsi and no iPXE script is used.
            If your instance boot volume attachment type is paravirtualized
            and you use custom iPXE to network boot into your instance,
            the primary boot volume is attached as a data volume through virtio-scsi drive.

            For more information about the Bring Your Own Image feature of
            Oracle Cloud Infrastructure, see
            [Bring Your Own Image](/iaas/Content/Compute/References/bringyourownimage.htm).

            For more information about iPXE, see http://ipxe.org.
            . Defaults to None.

        is_pv_encryption_in_transit_enabled(bool, Optional):
            Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false. Defaults to None.

        launch_mode(str, Optional):
            Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
            * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
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


        metadata(Dict, Optional):
            Custom metadata key/value pairs that you provide, such as the SSH public key
            required to connect to the instance.

            A metadata service runs on every launched instance. The service is an HTTP
            endpoint listening on 169.254.169.254. You can use the service to:

            * Provide information to [Cloud-Init](https://cloudinit.readthedocs.org/en/latest/)
              to be used for various system initialization tasks.

            * Get information about the instance, including the custom metadata that you
              provide when you launch the instance.

             **Providing Cloud-Init Metadata**

             You can use the following metadata key names to provide information to
             Cloud-Init:

             **"ssh_authorized_keys"** - Provide one or more public SSH keys to be
             included in the `~/.ssh/authorized_keys` file for the default user on the
             instance. Use a newline character to separate multiple keys. The SSH
             keys must be in the format necessary for the `authorized_keys` file, as shown
             in the example below.

             **"user_data"** - Provide your own base64-encoded data to be used by
             Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
             information about how to take advantage of user data, see the
             [Cloud-Init Documentation](http://cloudinit.readthedocs.org/en/latest/topics/format.html).

             **Metadata Example**

                  "metadata" : {
                     "quake_bot_level" : "Severe",
                     "ssh_authorized_keys" : "ssh-rsa <your_public_SSH_key>== rsa-key-20160227",
                     "user_data" : "<your_public_SSH_key>=="
                  }
             **Getting Metadata on the Instance**

             To get information about your instance, connect to the instance using SSH and issue any of the
             following GET requests:

                 curl -H "Authorization: Bearer Oracle" http://169.254.169.254/opc/v2/instance/
                 curl -H "Authorization: Bearer Oracle" http://169.254.169.254/opc/v2/instance/metadata/
                 curl -H "Authorization: Bearer Oracle" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>

             You'll get back a response that includes all the instance information; only the metadata information; or
             the metadata information for the specified key name, respectively.

             The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.
            . Defaults to None.

        platform_config(dict[str, Any], Optional):
            platformConfig. Defaults to None.

            * is_measured_boot_enabled (bool, Optional):
                Whether the Measured Boot feature is enabled on the instance.


            * is_secure_boot_enabled (bool, Optional):
                Whether Secure Boot is enabled on the instance.


            * is_trusted_platform_module_enabled (bool, Optional):
                Whether the Trusted Platform Module (TPM) is enabled on the instance.


            * type (str):
                The type of platform being configured.


        preemptible_instance_config(dict[str, Any], Optional):
            preemptibleInstanceConfig. Defaults to None.

            * preemption_action (dict[str, Any]):
                preemptionAction

                * type (str):
                    The type of action to run when the instance is interrupted for eviction.

        shape_config(dict[str, Any], Optional):
            shapeConfig. Defaults to None.

            * baseline_ocpu_utilization (str, Optional):
                The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
                non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.

                The following values are supported:
                - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
                - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
                - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.


            * memory_in_g_bs (float, Optional):
                The total amount of memory available to the instance, in gigabytes.


            * nvmes (int, Optional):
                The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.


            * ocpus (float, Optional):
                The total number of OCPUs available to the instance.


        source_details(dict[str, Any], Optional):
            sourceDetails. Defaults to None.

            * source_type (str):
                The source type for the instance.
                Use `image` when specifying the image OCID. Use `bootVolume` when specifying
                the boot volume OCID.


        subnet_id(str, Optional):
            Deprecated. Instead use `subnetId` in
            [CreateVnicDetails](#/en/iaas/latest/CreateVnicDetails/).
            At least one of them is required; if you provide both, the values must match.
            . Defaults to None.

    Returns:
        Dict[str, Any]
    """

    result = dict(comment=[], ret=[], result=True)

    desired_state = {
        k: v
        for k, v in locals().items()
        if k not in ("hub", "ctx", "result") and v is not None
    }

    resource_to_raw_input_mapping = {
        "agent_config": "agentConfig",
        "availability_config": "availabilityConfig",
        "availability_domain": "availabilityDomain",
        "capacity_reservation_id": "capacityReservationId",
        "compartment_id": "compartmentId",
        "compute_cluster_id": "computeClusterId",
        "create_vnic_details": "createVnicDetails",
        "dedicated_vm_host_id": "dedicatedVmHostId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "extended_metadata": "extendedMetadata",
        "fault_domain": "faultDomain",
        "freeform_tags": "freeformTags",
        "hostname_label": "hostnameLabel",
        "image_id": "imageId",
        "instance_options": "instanceOptions",
        "ipxe_script": "ipxeScript",
        "is_pv_encryption_in_transit_enabled": "isPvEncryptionInTransitEnabled",
        "launch_mode": "launchMode",
        "launch_options": "launchOptions",
        "metadata": "metadata",
        "platform_config": "platformConfig",
        "preemptible_instance_config": "preemptibleInstanceConfig",
        "shape": "shape",
        "shape_config": "shapeConfig",
        "source_details": "sourceDetails",
        "subnet_id": "subnetId",
    }

    payload = {}
    for key, value in desired_state.items():
        if key in resource_to_raw_input_mapping.keys() and value is not None:
            payload[resource_to_raw_input_mapping[key]] = value

    if "compartmentId" not in payload:
        payload["compartmentId"] = ctx.acct.compartment_id

    create = await hub.tool.oci.session.request(
        ctx,
        method="post",
        path="/instances/".format(**{}),
        query_params={},
        data=payload,
        headers={"opc-retry-token": opc_retry_token},
    )

    if not create["result"]:
        result["comment"].append(create["comment"])
        result["result"] = False
        return result

    result["comment"].append(
        f"Created oci.compute '{name}'",
    )

    result["ret"] = {"name": name, "resource_id": create["ret"]["id"]}
    return result


async def update(
    hub,
    ctx,
    resource_id: str,
    name: str = None,
    opc_retry_token: str = None,
    if_match: str = None,
    agent_config: make_dataclass(
        "agent_config",
        [
            ("are_all_plugins_disabled", bool, field(default=None)),
            ("is_management_disabled", bool, field(default=None)),
            ("is_monitoring_disabled", bool, field(default=None)),
            (
                "plugins_config",
                List[
                    make_dataclass(
                        "plugins_config", [("desired_state", str), ("name", str)]
                    )
                ],
                field(default=None),
            ),
        ],
    ) = None,
    availability_config: make_dataclass(
        "availability_config",
        [
            ("is_live_migration_preferred", bool, field(default=None)),
            ("recovery_action", str, field(default=None)),
        ],
    ) = None,
    capacity_reservation_id: str = None,
    defined_tags: Dict = None,
    display_name: str = None,
    extended_metadata: Dict = None,
    fault_domain: str = None,
    freeform_tags: Dict = None,
    instance_options: make_dataclass(
        "instance_options",
        [("are_legacy_imds_endpoints_disabled", bool, field(default=None))],
    ) = None,
    launch_options: make_dataclass(
        "launch_options",
        [
            ("boot_volume_type", str, field(default=None)),
            ("is_pv_encryption_in_transit_enabled", bool, field(default=None)),
            ("network_type", str, field(default=None)),
        ],
    ) = None,
    metadata: Dict = None,
    shape: str = None,
    shape_config: make_dataclass(
        "shape_config",
        [
            ("baseline_ocpu_utilization", str, field(default=None)),
            ("memory_in_g_bs", float, field(default=None)),
            ("nvmes", int, field(default=None)),
            ("ocpus", float, field(default=None)),
        ],
    ) = None,
    time_maintenance_reboot_due: str = None,
    update_operation_constraint: str = None,
) -> Dict[str, Any]:
    """
    Updates certain fields on the specified instance. Fields that are not provided in the
    request will not be updated. Avoid entering confidential information.

    Changes to metadata fields will be reflected in the instance metadata service (this may take
    up to a minute).

    The OCID of the instance remains the same.

    Args:
        resource_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

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

        agent_config(dict[str, Any], Optional):
            agentConfig. Defaults to None.

            * are_all_plugins_disabled (bool, Optional):
                Whether Oracle Cloud Agent can run all the available plugins.
                This includes the management and monitoring plugins.

                To get a list of available plugins, use the
                [ListInstanceagentAvailablePlugins](#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                [Managing Plugins with Oracle Cloud Agent](/iaas/Content/Compute/Tasks/manage-plugins.htm).


            * is_management_disabled (bool, Optional):
                Whether Oracle Cloud Agent can run all the available management plugins.

                These are the management plugins: OS Management Service Agent and Compute Instance
                Run Command.

                The management plugins are controlled by this parameter and by the per-plugin
                configuration in the `pluginsConfig` object.

                - If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of
                the per-plugin configuration.
                - If `isManagementDisabled` is false, all of the management plugins are enabled. You
                can optionally disable individual management plugins by providing a value in the `pluginsConfig`
                object.


            * is_monitoring_disabled (bool, Optional):
                Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
                monitoring plugins.

                These are the monitoring plugins: Compute Instance Monitoring
                and Custom Logs Monitoring.

                The monitoring plugins are controlled by this parameter and by the per-plugin
                configuration in the `pluginsConfig` object.

                - If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of
                the per-plugin configuration.
                - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You
                can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                object.


            * plugins_config (List[dict[str, Any]], Optional):
                The configuration of plugins associated with this instance.

                * desired_state (str):
                    Whether the plugin should be enabled or disabled.

                    To enable the monitoring and management plugins, the `isMonitoringDisabled` and
                    `isManagementDisabled` attributes must also be set to false.


                * name (str):
                    The plugin name. To get a list of available plugins, use the
                    [ListInstanceagentAvailablePlugins](#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                    operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                    [Managing Plugins with Oracle Cloud Agent](/iaas/Content/Compute/Tasks/manage-plugins.htm).


        availability_config(dict[str, Any], Optional):
            availabilityConfig. Defaults to None.

            * is_live_migration_preferred (bool, Optional):
                Whether to live migrate supported VM instances to a healthy physical VM host without
                disrupting running instances during infrastructure maintenance events. If null, Oracle
                chooses the best option for migrating the VM during infrastructure maintenance events.


            * recovery_action (str, Optional):
                The lifecycle state for an instance when it is recovered after infrastructure maintenance.
                * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event.
                If the instance was running, it is automatically rebooted. This is the default action when a value is not set.
                * `STOP_INSTANCE` - The instance is recovered in the stopped state.


        capacity_reservation_id(str, Optional):
            The OCID of the compute capacity reservation this instance is launched under.
            You can remove the instance from a reservation by specifying an empty string as input for this field.
            For more information, see [Capacity Reservations](/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
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

        extended_metadata(Dict, Optional):
            Additional metadata key/value pairs that you provide. They serve the same purpose and
            functionality as fields in the `metadata` object.

            They are distinguished from `metadata` fields in that these can be nested JSON objects
            (whereas `metadata` fields are string/string maps only).

            The "user_data" field and the "ssh_authorized_keys" field cannot be changed after an instance
            has launched. Any request that updates, removes, or adds either of these fields will be
            rejected. You must provide the same values for "user_data" and "ssh_authorized_keys" that
            already exist on the instance.

            The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
            32,000 bytes.
            . Defaults to None.

        fault_domain(str, Optional):
            A fault domain is a grouping of hardware and infrastructure within an availability domain.
            Each availability domain contains three fault domains. Fault domains let you distribute your
            instances so that they are not on the same physical hardware within a single availability domain.
            A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
            instances in other fault domains.

            To get a list of fault domains, use the
            [ListFaultDomains](#/en/identity/20160918/FaultDomain/ListFaultDomains) operation in the
            Identity and Access Management Service API.

            Example: `FAULT-DOMAIN-1`
            . Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            . Defaults to None.

        instance_options(dict[str, Any], Optional):
            instanceOptions. Defaults to None.

            * are_legacy_imds_endpoints_disabled (bool, Optional):
                Whether to disable the legacy (/v1) instance metadata service endpoints.
                Customers who have migrated to /v2 should set this to true for added security.
                Default is false.


        launch_options(dict[str, Any], Optional):
            launchOptions. Defaults to None.

            * boot_volume_type (str, Optional):
                Emulation type for the boot volume.
                * `ISCSI` - ISCSI attached block storage device.
                * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                storage volumes on platform images.

                Before you change the boot volume attachment type, detach all block volumes and VNICs except for
                the boot volume and the primary VNIC.

                If the instance is running when you change the boot volume attachment type, it will be rebooted.

                **Note:** Some instances might not function properly if you change the boot volume attachment type. After
                the instance reboots and is running, connect to it. If the connection fails or the OS doesn't behave
                as expected, the changes are not supported. Revert the instance to the original boot volume attachment type.


            * is_pv_encryption_in_transit_enabled (bool, Optional):
                Whether to enable in-transit encryption for the volume's paravirtualized attachment.
                To enable in-transit encryption for block volumes and boot volumes, this field must be set to `true`.

                Data in transit is transferred over an internal and highly secure network. If you have specific
                compliance requirements related to the encryption of the data while it is moving between the
                instance and the boot volume or the block volume, you can enable in-transit encryption.
                In-transit encryption is not enabled by default.

                All boot volumes and block volumes are encrypted at rest.

                For more information, see [Block Volume Encryption](/iaas/Content/Block/Concepts/overview.htm#Encrypti).


            * network_type (str, Optional):
                Emulation type for the physical network interface card (NIC).
                * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                when you launch an instance using hardware-assisted (SR-IOV) networking.
                * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.

                Before you change the networking type, detach all VNICs and block volumes except for the primary
                VNIC and the boot volume.

                The image must have paravirtualized drivers installed. For more information, see
                [Editing an Instance](/iaas/Content/Compute/Tasks/resizinginstances.htm).

                If the instance is running when you change the network type, it will be rebooted.

                **Note:** Some instances might not function properly if you change the networking type. After
                the instance reboots and is running, connect to it. If the connection fails or the OS doesn't behave
                as expected, the changes are not supported. Revert the instance to the original networking type.


        metadata(Dict, Optional):
            Custom metadata key/value string pairs that you provide. Any set of key/value pairs
            provided here will completely replace the current set of key/value pairs in the `metadata`
            field on the instance.

            The "user_data" field and the "ssh_authorized_keys" field cannot be changed after an instance
            has launched. Any request that updates, removes, or adds either of these fields will be
            rejected. You must provide the same values for "user_data" and "ssh_authorized_keys" that
            already exist on the instance.

            The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
            32,000 bytes.
            . Defaults to None.

        shape(str, Optional):
            The shape of the instance. The shape determines the number of CPUs and the amount of memory
            allocated to the instance. For more information about how to change shapes, and a list of
            shapes that are supported, see
            [Editing an Instance](/iaas/Content/Compute/Tasks/resizinginstances.htm).

            For details about the CPUs, memory, and other properties of each shape, see
            [Compute Shapes](/iaas/Content/Compute/References/computeshapes.htm).

            The new shape must be compatible with the image that was used to launch the instance. You
            can enumerate all available shapes and determine image compatibility by calling
            [ListShapes](#/en/iaas/latest/Shape/ListShapes).

            To determine whether capacity is available for a specific shape before you change the shape of an instance,
            use the [CreateComputeCapacityReport](#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)
            operation.

            If the instance is running when you change the shape, the instance is rebooted.

            Example: `VM.Standard2.1`
            . Defaults to None.

        shape_config(dict[str, Any], Optional):
            shapeConfig. Defaults to None.

            * baseline_ocpu_utilization (str, Optional):
                The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
                non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.

                The following values are supported:
                - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
                - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
                - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.


            * memory_in_g_bs (float, Optional):
                The total amount of memory available to the instance, in gigabytes.


            * nvmes (int, Optional):
                The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.


            * ocpus (float, Optional):
                The total number of OCPUs available to the instance.


        time_maintenance_reboot_due(str, Optional):
            For a VM instance, resets the scheduled time that the instance will be reboot migrated for
            infrastructure maintenance, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
            If the instance hasn't been rebooted after this date, Oracle reboots the instance within 24 hours of the time
            and date that maintenance is due.

            To get the maximum possible date that a maintenance reboot can be extended,
            use [GetInstanceMaintenanceReboot](#/en/iaas/latest/InstanceMaintenanceReboot/GetInstanceMaintenanceReboot).

            Regardless of how the instance is stopped, this flag is reset to empty as soon as the instance reaches the
            Stopped state.

            To reboot migrate a bare metal instance, use the [InstanceAction](#/en/iaas/latest/Instance/InstanceAction) operation.

            For more information, see
            [Infrastructure Maintenance](/iaas/Content/Compute/References/infrastructure-maintenance.htm).

            Example: `2018-05-25T21:10:29.600Z`
            . Defaults to None.

        update_operation_constraint(str, Optional):
            The parameter acts as a fail-safe to prevent unwanted downtime when updating a running instance.
            The default is ALLOW_DOWNTIME.
            * `ALLOW_DOWNTIME` - Compute might reboot the instance while updating the instance if a reboot is required.
            * `AVOID_DOWNTIME` - If the instance is in running state, Compute tries to update the instance without rebooting
                              it. If the instance requires a reboot to be updated, an error is returned and the instance
                              is not updated. If the instance is stopped, it is updated and remains in the stopped state.
            . Defaults to None.

    Returns:
        Dict[str, Any]
    """

    result = dict(comment=[], ret=[], result=True)

    desired_state = {
        k: v
        for k, v in locals().items()
        if k not in ("hub", "ctx", "result") and v is not None
    }

    resource_to_raw_input_mapping = {
        "agent_config": "agentConfig",
        "availability_config": "availabilityConfig",
        "capacity_reservation_id": "capacityReservationId",
        "defined_tags": "definedTags",
        "display_name": "displayName",
        "extended_metadata": "extendedMetadata",
        "fault_domain": "faultDomain",
        "freeform_tags": "freeformTags",
        "instance_options": "instanceOptions",
        "launch_options": "launchOptions",
        "metadata": "metadata",
        "shape": "shape",
        "shape_config": "shapeConfig",
        "time_maintenance_reboot_due": "timeMaintenanceRebootDue",
        "update_operation_constraint": "updateOperationConstraint",
    }

    payload = {}
    for key, value in desired_state.items():
        if key in resource_to_raw_input_mapping.keys() and value is not None:
            payload[resource_to_raw_input_mapping[key]] = value

    if payload:
        update = await hub.tool.oci.session.request(
            ctx,
            method="put",
            path="/instances/{instanceId}".format(**{"instanceId": resource_id}),
            query_params={},
            data=payload,
            headers={"opc-retry-token": opc_retry_token, "if-match": if_match},
        )

        if not update["result"]:
            result["comment"].append(update["comment"])
            result["result"] = False
            return result

        result["ret"] = {"name": name, "resource_id": resource_id}
        result["comment"].append(
            f"Updated oci.compute '{name}'",
        )

    return result


async def delete(
    hub,
    ctx,
    resource_id: str,
    if_match: str = None,
    preserve_boot_volume: bool = None,
    name: str = None,
) -> Dict[str, Any]:
    r"""
    Permanently terminates (deletes) the specified instance. Any attached VNICs and volumes are automatically detached
    when the instance terminates.

    To preserve the boot volume associated with the instance, specify `true` for `PreserveBootVolumeQueryParam`.
    To delete the boot volume when the instance is deleted, specify `false` or do not specify a value for `PreserveBootVolumeQueryParam`.

    This is an asynchronous operation. The instance's `lifecycleState` changes to TERMINATING temporarily
    until the instance is completely deleted. After the instance is deleted, the record remains visible in the list of instances
    with the state TERMINATED for at least 12 hours, but no further action is needed.

    Args:
        resource_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

        if_match(str, Optional):
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
            Defaults to None.

        preserve_boot_volume(bool, Optional):
            Specifies whether to delete or preserve the boot volume when terminating an instance.
            When set to `true`, the boot volume is preserved. The default value is `false`.
            Defaults to None.

    Returns:
        Dict[str, Any]

    """

    result = dict(comment=[], ret=[], result=True)

    delete = await hub.tool.oci.session.request(
        ctx,
        method="delete",
        path="/instances/{instanceId}".format(**{"instanceId": resource_id}),
        query_params={"preserveBootVolume": preserve_boot_volume},
        data={},
        headers={"if-match": if_match},
    )

    if not delete["result"]:
        result["comment"].append(delete["comment"])
        result["result"] = False
        return result

    result["comment"].append(f"Deleted '{name}'")
    return result
