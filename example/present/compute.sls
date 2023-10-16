idem_test_compute_is_present:
  oci.compute.present:
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
