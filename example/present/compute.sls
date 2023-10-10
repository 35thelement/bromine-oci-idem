idem_test_compute_is_present:
  oci.compute.present:
  - agent_config:
      areAllPluginsDisabled: boolean
      isManagementDisabled: boolean
      isMonitoringDisabled: boolean
      pluginsConfig: null
  - availability_config:
      isLiveMigrationPreferred: null
      recoveryAction: RESTORE_INSTANCE
  - availability_domain: value
  - compartment_id: value
  - defined_tags:
      Compute-Tag:
        RequestedBy: value
  - display_name: value
  - fault_domain: FAULT-DOMAIN-3
  - image_id: value
  - instance_options:
      areLegacyImdsEndpointsDisabled: boolean
  - launch_mode: PARAVIRTUALIZED
  - launch_options:
      bootVolumeType: PARAVIRTUALIZED
      firmware: UEFI_64
      isConsistentVolumeNamingEnabled: false
      isEncryptionInTransitEnabled: null
      isPvEncryptionInTransitEnabled: false
      networkType: PARAVIRTUALIZED
      remoteDataVolumeType: PARAVIRTUALIZED
  - lifecycle_state: RUNNING
  - region: iad
  - shape: VM.Standard2.1
  - shape_config:
      baselineOcpuUtilization: null
      gpuDescription: null
      gpus: 0
      localDiskDescription: null
      localDisks: 0
      localDisksTotalSizeInGBs: null
      maxVnicAttachments: 2
      memoryInGBs: 15.0
      networkingBandwidthInGbps: 1.0
      ocpus: 1.0
      processorDescription: "2.0 GHz Intel\xAE Xeon\xAE Platinum 8167M (Skylake)"
      vcpus: 2
  - source_details:
      bootVolumeSizeInGBs: null
      bootVolumeVpusPerGB: null
      imageId: value
      instanceSourceImageFilterDetails: null
      kmsKeyId: null
      sourceType: image
