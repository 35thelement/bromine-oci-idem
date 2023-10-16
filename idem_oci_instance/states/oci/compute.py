"""States module for managing Computes. """
from dataclasses import field
from dataclasses import make_dataclass
from typing import Any
from typing import Dict
from typing import List

import dict_tools.differ as differ

__contracts__ = ["resource"]


async def present(
    hub,
    ctx,
    name: str,
    availability_domain: str,
    compartment_id: str,
    shape: str,
    image_id: str,
    subnet_id: str,
    resource_id: str = None,
    opc_retry_token: str = None,
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
) -> Dict[str, Any]:
    """
    LaunchInstance
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
        name(str):
            Idem name of the resource.

        availability_domain(str):
            The availability domain of the instance.

            Example: `Uocm:PHX-AD-1`


        compartment_id(str):
            The OCID of the compartment.

        shape(str):
            The shape of an instance. The shape determines the number of CPUs, amount of memory,
            and other resources allocated to the instance.

            You can enumerate all available shapes by calling [ListShapes](#/en/iaas/latest/Shape/ListShapes).


        resource_id(str, Optional):
            Compute unique ID. Defaults to None.

        opc_retry_token(str, Optional):
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
            Defaults to None.

        agent_config(dict[str, Any], Optional):
            agentConfig. Defaults to None.

            * are_all_plugins_disabled (bool, Optional):
                Whether Oracle Cloud Agent can run all the available plugins.
                This includes the management and monitoring plugins.

                To get a list of available plugins, use the
                [ListInstanceagentAvailablePlugins](#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                [Managing Plugins with Oracle Cloud Agent](/iaas/Content/Compute/Tasks/manage-plugins.htm).
                Defaults to None.

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
                Defaults to None.

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
                Defaults to None.

            * plugins_config (List[dict[str, Any]], Optional):
                The configuration of plugins associated with this instance. Defaults to None.

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
                Defaults to None.

            * recovery_action (str, Optional):
                The lifecycle state for an instance when it is recovered after infrastructure maintenance.
                * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event.
                If the instance was running, it is automatically rebooted. This is the default action when a value is not set.
                * `STOP_INSTANCE` - The instance is recovered in the stopped state.
                Defaults to None.

        capacity_reservation_id(str, Optional):
            The OCID of the compute capacity reservation this instance is launched under.
            You can opt out of all default reservations by specifying an empty string as input for this field.
            For more information, see [Capacity Reservations](/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
            Defaults to None.

        compute_cluster_id(str, Optional):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the
            [compute cluster](/iaas/Content/Compute/Tasks/compute-clusters.htm) that the instance will be created in.
            Defaults to None.

        create_vnic_details(dict[str, Any], Optional):
            createVnicDetails. Defaults to None.

            * assign_ipv6_ip (bool, Optional):
                Whether to allocate an IPv6 address at instance and VNIC creation from an IPv6 enabled
                subnet. Default: False. When provided you may optionally provide an IPv6 prefix
                (`ipv6SubnetCidr`) of your choice to assign the IPv6 address from. If `ipv6SubnetCidr`
                is not provided then an IPv6 prefix is chosen
                for you.
                Defaults to None.

            * assign_private_dns_record (bool, Optional):
                Whether the VNIC should be assigned a DNS record. If set to false, there will be no DNS record
                registration for the VNIC. If set to true, the DNS record will be registered. The default
                value is true.

                If you specify a `hostnameLabel`, then `assignPrivateDnsRecord` must be set to true.
                Defaults to None.

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
                Defaults to None.

            * ipv6_address_ipv6_subnet_cidr_pair_details (List[dict[str, Any]], Optional):
                A list of IPv6 prefix ranges from which the VNIC is assigned an IPv6 address.
                You can provide only the prefix ranges from which OCI selects an available
                address from the range. You can optionally choose to leave the prefix range empty
                and instead provide the specific IPv6 address within that range to use.
                Defaults to None.

                * ipv6_address (str, Optional):
                    An IPv6 address of your choice. Must be an available IPv6 address within the subnet's prefix.
                    If an IPv6 address is not provided:
                    - Oracle will automatically assign an IPv6 address from the subnet's IPv6 prefix if and only if there is only one IPv6 prefix on the subnet.
                    - Oracle will automatically assign an IPv6 address from the subnet's IPv6 Oracle GUA prefix if it exists on the subnet.
                    Defaults to None.

                * ipv6_subnet_cidr (str, Optional):
                    The IPv6 prefix allocated to the subnet.
                    Defaults to None.

            * nsg_ids (List[str], Optional):
                A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                information about NSGs, see
                [NetworkSecurityGroup](#/en/iaas/latest/NetworkSecurityGroup/).

                If a `vlanId` is specified, the `nsgIds` cannot be specified. The `vlanId`
                indicates that the VNIC will belong to a VLAN instead of a subnet. With VLANs,
                all VNICs in the VLAN belong to the NSGs that are associated with the VLAN.
                See [Vlan](#/en/iaas/latest/Vlan).
                Defaults to None.

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
                Defaults to None.

            * skip_source_dest_check (bool, Optional):
                Whether the source/destination check is disabled on the VNIC.
                Defaults to `false`, which means the check is performed. For information
                about why you would skip the source/destination check, see
                [Using a Private IP as a Route Target](/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).


                If you specify a `vlanId`, the `skipSourceDestCheck` cannot be specified because the
                source/destination check is always disabled for VNICs in a VLAN. See
                [Vlan](#/en/iaas/latest/Vlan).

                Example: `true`
                Defaults to None.

            * subnet_id (str, Optional):
                The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create the VNIC in. When launching an instance,
                use this `subnetId` instead of the deprecated `subnetId` in
                [LaunchInstanceDetails](#/en/iaas/latest/requests/LaunchInstanceDetails).
                At least one of them is required; if you provide both, the values must match.

                If you are an Oracle Cloud VMware Solution customer and creating a secondary
                VNIC in a VLAN instead of a subnet, provide a `vlanId` instead of a `subnetId`.
                If you provide both a `vlanId` and `subnetId`, the request fails.
                Defaults to None.

            * vlan_id (str, Optional):
                Provide this attribute only if you are an Oracle Cloud VMware Solution
                customer and creating a secondary VNIC in a VLAN. The value is the [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
                See [Vlan](#/en/iaas/latest/Vlan).

                Provide a `vlanId` instead of a `subnetId`. If you provide both a
                `vlanId` and `subnetId`, the request fails.
                Defaults to None.

        dedicated_vm_host_id(str, Optional):
            The OCID of the dedicated virtual machine host to place the instance on.
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

        extended_metadata(Dict, Optional):
            Additional metadata key/value pairs that you provide. They serve the same purpose and
            functionality as fields in the `metadata` object.

            They are distinguished from `metadata` fields in that these can be nested JSON objects
            (whereas `metadata` fields are string/string maps only).

            The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
            32,000 bytes.
            Defaults to None.

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
            Defaults to None.

        freeform_tags(Dict, Optional):
            Free-form tags for this resource. Each tag is a simple key-value pair with no
            predefined name, type, or namespace. For more information, see [Resource Tags](/iaas/Content/General/Concepts/resourcetags.htm).

            Example: `{"Department": "Finance"}`
            Defaults to None.

        hostname_label(str, Optional):
            Deprecated. Instead use `hostnameLabel` in
            [CreateVnicDetails](#/en/iaas/latest/CreateVnicDetails/).
            If you provide both, the values must match.
            Defaults to None.

        image_id(str, Optional):
            Deprecated. Use `sourceDetails` with [InstanceSourceViaImageDetails](#/en/iaas/latest/requests/InstanceSourceViaImageDetails)
            source type instead. If you specify values for both, the values must match.
            Defaults to None.

        instance_options(dict[str, Any], Optional):
            instanceOptions. Defaults to None.

            * are_legacy_imds_endpoints_disabled (bool, Optional):
                Whether to disable the legacy (/v1) instance metadata service endpoints.
                Customers who have migrated to /v2 should set this to true for added security.
                Default is false.
                Defaults to None.

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
            Defaults to None.

        is_pv_encryption_in_transit_enabled(bool, Optional):
            Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false. Defaults to None.

        launch_mode(str, Optional):
            Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
            * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
            * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
            * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
            * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.
            Defaults to None.

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
                Defaults to None.

            * firmware (str, Optional):
                Firmware used to boot VM. Select the option that matches your operating system.
                * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                systems that boot using MBR style bootloaders.
                * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                default for platform images.
                Defaults to None.

            * is_consistent_volume_naming_enabled (bool, Optional):
                Whether to enable consistent volume naming feature. Defaults to false. Defaults to None.

            * is_pv_encryption_in_transit_enabled (bool, Optional):
                Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
                [LaunchInstanceDetails](#/en/iaas/latest/datatypes/LaunchInstanceDetails).
                Defaults to None.

            * network_type (str, Optional):
                Emulation type for the physical network interface card (NIC).
                * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
                * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                when you launch an instance using hardware-assisted (SR-IOV) networking.
                * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                Defaults to None.

            * remote_data_volume_type (str, Optional):
                Emulation type for volume.
                * `ISCSI` - ISCSI attached block storage device.
                * `SCSI` - Emulated SCSI disk.
                * `IDE` - Emulated IDE disk.
                * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                volumes on platform images.
                * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                storage volumes on platform images.
                Defaults to None.

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
            Defaults to None.

        platform_config(dict[str, Any], Optional):
            platformConfig. Defaults to None.

            * is_measured_boot_enabled (bool, Optional):
                Whether the Measured Boot feature is enabled on the instance.
                Defaults to None.

            * is_secure_boot_enabled (bool, Optional):
                Whether Secure Boot is enabled on the instance.
                Defaults to None.

            * is_trusted_platform_module_enabled (bool, Optional):
                Whether the Trusted Platform Module (TPM) is enabled on the instance.
                Defaults to None.

            * type (str):
                The type of platform being configured.


        preemptible_instance_config(dict[str, Any], Optional):
            preemptibleInstanceConfig. Defaults to None.

            * preemption_action (dict[str, Any]):
                preemptionAction.

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
                Defaults to None.

            * memory_in_g_bs (float, Optional):
                The total amount of memory available to the instance, in gigabytes.
                Defaults to None.

            * nvmes (int, Optional):
                The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                Defaults to None.

            * ocpus (float, Optional):
                The total number of OCPUs available to the instance.
                Defaults to None.

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
            Defaults to None.

    Returns:
        Dict[str, Any]

    Example:
        .. code-block:: sls


          idem_test_oci.compute_is_present:
              oci.oci.compute.present:
              - opc_retry_token: string
              - agent_config:
                  are_all_plugins_disabled: bool
                  is_management_disabled: bool
                  is_monitoring_disabled: bool
                  plugins_config:
                  - desired_state: string
                    name: string
              - availability_config:
                  is_live_migration_preferred: bool
                  recovery_action: string
              - availability_domain: string
              - capacity_reservation_id: string
              - compartment_id: string
              - compute_cluster_id: string
              - create_vnic_details:
                  assign_ipv6_ip: bool
                  assign_private_dns_record: bool
                  assign_public_ip: bool
                  defined_tags: Dict
                  display_name: string
                  freeform_tags: Dict
                  hostname_label: string
                  ipv6_address_ipv6_subnet_cidr_pair_details:
                  - ipv6_address: string
                    ipv6_subnet_cidr: string
                  nsg_ids:
                  - value
                  private_ip: string
                  skip_source_dest_check: bool
                  subnet_id: string
                  vlan_id: string
              - dedicated_vm_host_id: string
              - defined_tags: Dict
              - display_name: string
              - extended_metadata: Dict
              - fault_domain: string
              - freeform_tags: Dict
              - hostname_label: string
              - image_id: string
              - instance_options:
                  are_legacy_imds_endpoints_disabled: bool
              - ipxe_script: string
              - is_pv_encryption_in_transit_enabled: bool
              - launch_mode: string
              - launch_options:
                  boot_volume_type: string
                  firmware: string
                  is_consistent_volume_naming_enabled: bool
                  is_pv_encryption_in_transit_enabled: bool
                  network_type: string
                  remote_data_volume_type: string
              - metadata: Dict
              - platform_config:
                  is_measured_boot_enabled: bool
                  is_secure_boot_enabled: bool
                  is_trusted_platform_module_enabled: bool
                  type_: string
              - preemptible_instance_config:
                  preemption_action:
                    type_: string
              - shape: string
              - shape_config:
                  baseline_ocpu_utilization: string
                  memory_in_g_bs: float
                  nvmes: int
                  ocpus: float
              - source_details:
                  source_type: string
              - subnet_id: string


    """

    result = dict(
        comment=[], old_state={}, new_state={}, name=name, result=True, rerun_data=None
    )

    desired_state = {
        k: v
        for k, v in locals().items()
        if k not in ("hub", "ctx", "kwargs", "result") and v is not None
    }

    if resource_id:
        # Possible parameters: **{"resource_id": resource_id, "name": name, "agent_config": agent_config, "availability_config": availability_config, "availability_domain": availability_domain, "capacity_reservation_id": capacity_reservation_id, "compartment_id": compartment_id, "compute_cluster_id": compute_cluster_id, "create_vnic_details": create_vnic_details, "dedicated_vm_host_id": dedicated_vm_host_id, "defined_tags": defined_tags, "display_name": display_name, "extended_metadata": extended_metadata, "fault_domain": fault_domain, "freeform_tags": freeform_tags, "hostname_label": hostname_label, "image_id": image_id, "instance_options": instance_options, "ipxe_script": ipxe_script, "is_pv_encryption_in_transit_enabled": is_pv_encryption_in_transit_enabled, "launch_mode": launch_mode, "launch_options": launch_options, "metadata": metadata, "platform_config": platform_config, "preemptible_instance_config": preemptible_instance_config, "shape": shape, "shape_config": shape_config, "source_details": source_details, "subnet_id": subnet_id}
        before = await hub.exec.oci.compute.get(
            ctx,
            name=name,
            resource_id=resource_id,
        )

        if not before["result"] or not before["ret"]:
            result["result"] = False
            result["comment"] = before["comment"]
            return result

        result["old_state"] = before.ret

        result["comment"].append(f"'oci.compute: {name}' already exists")

        # If there are changes in desired state from existing state
        changes = differ.deep_diff(before.ret if before.ret else {}, desired_state)

        if bool(changes.get("new")):
            if ctx.test:
                result["new_state"] = hub.tool.oci.test_state_utils.generate_test_state(
                    enforced_state={}, desired_state=desired_state
                )
                result["comment"].append(f"Would update oci.compute: {name}")
                return result
            else:
                # Update the resource
                update_ret = await hub.exec.oci.compute.update(
                    ctx,
                    **{
                        "resource_id": resource_id,
                        "name": name,
                        "agent_config": agent_config,
                        "availability_config": availability_config,
                        "availability_domain": availability_domain,
                        "capacity_reservation_id": capacity_reservation_id,
                        "compartment_id": compartment_id,
                        "compute_cluster_id": compute_cluster_id,
                        "create_vnic_details": create_vnic_details,
                        "dedicated_vm_host_id": dedicated_vm_host_id,
                        "defined_tags": defined_tags,
                        "display_name": display_name,
                        "extended_metadata": extended_metadata,
                        "fault_domain": fault_domain,
                        "freeform_tags": freeform_tags,
                        "hostname_label": hostname_label,
                        "image_id": image_id,
                        "instance_options": instance_options,
                        "ipxe_script": ipxe_script,
                        "is_pv_encryption_in_transit_enabled": is_pv_encryption_in_transit_enabled,
                        "launch_mode": launch_mode,
                        "launch_options": launch_options,
                        "metadata": metadata,
                        "platform_config": platform_config,
                        "preemptible_instance_config": preemptible_instance_config,
                        "shape": shape,
                        "shape_config": shape_config,
                        "source_details": source_details,
                        "subnet_id": subnet_id,
                    },
                )
                result["result"] = update_ret["result"]

                if result["result"]:
                    result["comment"].append(f"Updated 'oci.compute: {name}'")
                else:
                    result["comment"].append(update_ret["comment"])
    else:
        if ctx.test:
            result["new_state"] = hub.tool.oci.test_state_utils.generate_test_state(
                enforced_state={}, desired_state=desired_state
            )
            result["comment"] = (f"Would create oci.compute: {name}",)
            return result
        else:
            create_ret = await hub.exec.oci.compute.create(
                ctx,
                **{
                    "resource_id": resource_id,
                    "name": name,
                    "agent_config": agent_config,
                    "availability_config": availability_config,
                    "availability_domain": availability_domain,
                    "capacity_reservation_id": capacity_reservation_id,
                    "compartment_id": compartment_id,
                    "compute_cluster_id": compute_cluster_id,
                    "create_vnic_details": create_vnic_details,
                    "dedicated_vm_host_id": dedicated_vm_host_id,
                    "defined_tags": defined_tags,
                    "display_name": display_name,
                    "extended_metadata": extended_metadata,
                    "fault_domain": fault_domain,
                    "freeform_tags": freeform_tags,
                    "hostname_label": hostname_label,
                    "image_id": image_id,
                    "instance_options": instance_options,
                    "ipxe_script": ipxe_script,
                    "is_pv_encryption_in_transit_enabled": is_pv_encryption_in_transit_enabled,
                    "launch_mode": launch_mode,
                    "launch_options": launch_options,
                    "metadata": metadata,
                    "platform_config": platform_config,
                    "preemptible_instance_config": preemptible_instance_config,
                    "shape": shape,
                    "shape_config": shape_config,
                    "source_details": source_details,
                    "subnet_id": subnet_id,
                },
            )
            result["result"] = create_ret["result"]

            if result["result"]:
                result["comment"].append(f"Created 'oci.compute: {name}'")
                resource_id = create_ret["ret"]["resource_id"]
                # Safeguard for any future errors so that the resource_id is saved in the ESM
                result["new_state"] = dict(name=name, resource_id=resource_id)
            else:
                result["comment"].append(create_ret["comment"])

    if not result["result"]:
        # If there is any failure in create/update, it should reconcile.
        # The type of data is less important here to use default reconciliation
        # If there are no changes for 3 runs with rerun_data, then it will come out of execution
        result["rerun_data"] = dict(name=name, resource_id=resource_id)

    # Possible parameters: **{"resource_id": resource_id, "name": name, "agent_config": agent_config, "availability_config": availability_config, "availability_domain": availability_domain, "capacity_reservation_id": capacity_reservation_id, "compartment_id": compartment_id, "compute_cluster_id": compute_cluster_id, "create_vnic_details": create_vnic_details, "dedicated_vm_host_id": dedicated_vm_host_id, "defined_tags": defined_tags, "display_name": display_name, "extended_metadata": extended_metadata, "fault_domain": fault_domain, "freeform_tags": freeform_tags, "hostname_label": hostname_label, "image_id": image_id, "instance_options": instance_options, "ipxe_script": ipxe_script, "is_pv_encryption_in_transit_enabled": is_pv_encryption_in_transit_enabled, "launch_mode": launch_mode, "launch_options": launch_options, "metadata": metadata, "platform_config": platform_config, "preemptible_instance_config": preemptible_instance_config, "shape": shape, "shape_config": shape_config, "source_details": source_details, "subnet_id": subnet_id}
    after = await hub.exec.oci.compute.get(
        ctx,
        name=name,
        resource_id=resource_id,
    )
    result["new_state"] = after.ret
    return result


async def absent(
    hub,
    ctx,
    name: str,
    resource_id: str = None,
    instance_id: str = None,
    if_match: str = None,
    preserve_boot_volume: bool = None,
) -> Dict[str, Any]:
    """

    TerminateInstance
        Permanently terminates (deletes) the specified instance. Any attached VNICs and volumes are automatically detached
    when the instance terminates.

    To preserve the boot volume associated with the instance, specify `true` for `PreserveBootVolumeQueryParam`.
    To delete the boot volume when the instance is deleted, specify `false` or do not specify a value for `PreserveBootVolumeQueryParam`.

    This is an asynchronous operation. The instance's `lifecycleState` changes to TERMINATING temporarily
    until the instance is completely deleted. After the instance is deleted, the record remains visible in the list of instances
    with the state TERMINATED for at least 12 hours, but no further action is needed.

    Args:
        name(str):
            Idem name of the resource.

        instance_id(str):
            The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the instance.

        resource_id(str, Optional):
            Compute unique ID. Defaults to None.

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

    Example:
        .. code-block:: sls


            idem_test_oci.compute_is_absent:
              oci.oci.compute.absent:
              - instance_id: string
              - if_match: string
              - preserve_boot_volume: bool


    """

    result = dict(
        comment=[], old_state={}, new_state={}, name=name, result=True, rerun_data=None
    )

    if not resource_id:
        resource_id = (ctx.old_state or {}).get("resource_id")

    if not resource_id:
        result["comment"].append(f"'oci.compute: {name}' already absent")
        return result

    before = await hub.exec.oci.compute.get(
        ctx,
        name=name,
        resource_id=resource_id,
    )

    if before["ret"]:
        if ctx.test:
            result["comment"] = f"Would delete oci.compute: {name}"
            return result

        delete_ret = await hub.exec.oci.compute.delete(
            ctx,
            name=name,
            resource_id=resource_id,
        )
        result["result"] = delete_ret["result"]

        if result["result"]:
            result["comment"].append(f"Deleted oci.compute: {name}")
        else:
            # If there is any failure in delete, it should reconcile.
            # The type of data is less important here to use default reconciliation
            # If there are no changes for 3 runs with rerun_data, then it will come out of execution
            result["rerun_data"] = resource_id
            result["comment"].append(delete_ret["result"])
    else:
        result["comment"].append(f"oci.compute: {name} already absent")
        return result

    result["old_state"] = before.ret
    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    """
    Describe the resource in a way that can be recreated/managed with the corresponding "present" function



    Returns:
        Dict[str, Any]

    Example:

        .. code-block:: bash

            $ idem describe oci.compute
    """

    result = {}

    # TODO: Add other required parameters from: {}
    ret = await hub.exec.oci.compute.list(ctx)

    if not ret or not ret["result"]:
        hub.log.debug(f"Could not describe oci.compute {ret['comment']}")
        return result

    for resource in ret["ret"]:
        # TODO: Look for respective identifier in **
        resource_id = resource.get("resource_id")
        result[resource_id] = {
            "oci.compute.present": [
                {parameter_key: parameter_value}
                for parameter_key, parameter_value in resource.items()
            ]
        }
    return result
