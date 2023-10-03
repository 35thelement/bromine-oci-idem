
"""Tests for validating Blockstorages. """

import pytest






@pytest.mark.asyncio

async def test_list_block_volume_replicas(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_block_volume_replicas(
        ctx,
        availability_domain=value, compartment_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_block_volume_replica(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_block_volume_replica(
        ctx,
        block_volume_replica_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_boot_volume_backups(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_boot_volume_backups(
        ctx,
        compartment_id=value, boot_volume_id=value, limit=value, page=value, display_name=value, source_boot_volume_backup_id=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_boot_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.create_boot_volume_backup(
        ctx,
        opc_retry_token=value, boot_volume_id=value, defined_tags=value, display_name=value, freeform_tags=value, kms_key_id=value, type_=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_boot_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_boot_volume_backup(
        ctx,
        boot_volume_backup_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_boot_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.update_boot_volume_backup(
        ctx,
        boot_volume_backup_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, kms_key_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_boot_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_boot_volume_backup(
        ctx,
        boot_volume_backup_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_boot_volume_backup_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.change_boot_volume_backup_compartment(
        ctx,
        boot_volume_backup_id=value, opc_request_id=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_copy_boot_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.copy_boot_volume_backup(
        ctx,
        boot_volume_backup_id=value, opc_retry_token=value, opc_request_id=value, destination_region=value, display_name=value, kms_key_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_boot_volume_replicas(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_boot_volume_replicas(
        ctx,
        availability_domain=value, compartment_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_boot_volume_replica(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_boot_volume_replica(
        ctx,
        boot_volume_replica_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_boot_volumes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_boot_volumes(
        ctx,
        availability_domain=value, compartment_id=value, limit=value, page=value, volume_group_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_boot_volume(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.create_boot_volume(
        ctx,
        opc_retry_token=value, autotune_policies=value, availability_domain=value, boot_volume_replicas=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, is_auto_tune_enabled=value, kms_key_id=value, size_in_g_bs=value, source_details=value, vpus_per_gb=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_boot_volume(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_boot_volume(
        ctx,
        boot_volume_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_boot_volume(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.update_boot_volume(
        ctx,
        boot_volume_id=value, if_match=value, autotune_policies=value, boot_volume_replicas=value, defined_tags=value, display_name=value, freeform_tags=value, is_auto_tune_enabled=value, size_in_g_bs=value, vpus_per_gb=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_boot_volume(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_boot_volume(
        ctx,
        boot_volume_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_boot_volume_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.change_boot_volume_compartment(
        ctx,
        boot_volume_id=value, opc_request_id=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_boot_volume_kms_key(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_boot_volume_kms_key(
        ctx,
        boot_volume_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_boot_volume_kms_key(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.update_boot_volume_kms_key(
        ctx,
        boot_volume_id=value, if_match=value, kms_key_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_boot_volume_kms_key(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_boot_volume_kms_key(
        ctx,
        boot_volume_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_volume_backup_policies(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_volume_backup_policies(
        ctx,
        limit=value, page=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_volume_backup_policy(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.create_volume_backup_policy(
        ctx,
        opc_retry_token=value, opc_request_id=value, compartment_id=value, defined_tags=value, destination_region=value, display_name=value, freeform_tags=value, schedules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_volume_backup_policy(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_volume_backup_policy(
        ctx,
        policy_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_volume_backup_policy(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.update_volume_backup_policy(
        ctx,
        policy_id=value, if_match=value, opc_request_id=value, opc_retry_token=value, defined_tags=value, destination_region=value, display_name=value, freeform_tags=value, schedules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_volume_backup_policy(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_volume_backup_policy(
        ctx,
        policy_id=value, opc_request_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_volume_backup_policy_asset_assignment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_volume_backup_policy_asset_assignment(
        ctx,
        asset_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_volume_backup_policy_assignment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.create_volume_backup_policy_assignment(
        ctx,
        asset_id=value, policy_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_volume_backup_policy_assignment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_volume_backup_policy_assignment(
        ctx,
        policy_assignment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_volume_backup_policy_assignment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_volume_backup_policy_assignment(
        ctx,
        policy_assignment_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_volume_backups(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_volume_backups(
        ctx,
        compartment_id=value, volume_id=value, limit=value, page=value, display_name=value, source_volume_backup_id=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.create_volume_backup(
        ctx,
        opc_retry_token=value, defined_tags=value, display_name=value, freeform_tags=value, kms_key_id=value, type_=value, volume_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_volume_backup(
        ctx,
        volume_backup_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.update_volume_backup(
        ctx,
        volume_backup_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, kms_key_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_volume_backup(
        ctx,
        volume_backup_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_volume_backup_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.change_volume_backup_compartment(
        ctx,
        volume_backup_id=value, opc_request_id=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_copy_volume_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.copy_volume_backup(
        ctx,
        volume_backup_id=value, opc_retry_token=value, opc_request_id=value, destination_region=value, display_name=value, kms_key_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_volume_group_backups(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_volume_group_backups(
        ctx,
        compartment_id=value, volume_group_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_volume_group_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.create_volume_group_backup(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, type_=value, volume_group_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_volume_group_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_volume_group_backup(
        ctx,
        volume_group_backup_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_volume_group_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.update_volume_group_backup(
        ctx,
        volume_group_backup_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_volume_group_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_volume_group_backup(
        ctx,
        volume_group_backup_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_volume_group_backup_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.change_volume_group_backup_compartment(
        ctx,
        volume_group_backup_id=value, opc_request_id=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_copy_volume_group_backup(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.copy_volume_group_backup(
        ctx,
        volume_group_backup_id=value, opc_retry_token=value, opc_request_id=value, destination_region=value, display_name=value, kms_key_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_volume_group_replicas(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_volume_group_replicas(
        ctx,
        availability_domain=value, compartment_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_volume_group_replica(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_volume_group_replica(
        ctx,
        volume_group_replica_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_volume_groups(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_volume_groups(
        ctx,
        availability_domain=value, compartment_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_volume_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.create_volume_group(
        ctx,
        opc_retry_token=value, availability_domain=value, backup_policy_id=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, source_details=value, volume_group_replicas=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_volume_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_volume_group(
        ctx,
        volume_group_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_volume_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.update_volume_group(
        ctx,
        volume_group_id=value, if_match=value, preserve_volume_replica=value, defined_tags=value, display_name=value, freeform_tags=value, volume_group_replicas=value, volume_ids=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_volume_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_volume_group(
        ctx,
        volume_group_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_volume_group_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.change_volume_group_compartment(
        ctx,
        volume_group_id=value, opc_request_id=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_volumes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.list_volumes(
        ctx,
        availability_domain=value, compartment_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, volume_group_id=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_volume(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.create_volume(
        ctx,
        opc_retry_token=value, autotune_policies=value, availability_domain=value, backup_policy_id=value, block_volume_replicas=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, is_auto_tune_enabled=value, kms_key_id=value, size_in_g_bs=value, size_in_m_bs=value, source_details=value, volume_backup_id=value, vpus_per_gb=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_volume(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_volume(
        ctx,
        volume_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_volume(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.update_volume(
        ctx,
        volume_id=value, if_match=value, autotune_policies=value, block_volume_replicas=value, defined_tags=value, display_name=value, freeform_tags=value, is_auto_tune_enabled=value, size_in_g_bs=value, vpus_per_gb=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_volume(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_volume(
        ctx,
        volume_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_volume_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.change_volume_compartment(
        ctx,
        volume_id=value, opc_request_id=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_volume_kms_key(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.get_volume_kms_key(
        ctx,
        volume_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_volume_kms_key(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.update_volume_kms_key(
        ctx,
        volume_id=value, if_match=value, kms_key_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_volume_kms_key(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.blockstorage.delete_volume_kms_key(
        ctx,
        volume_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations


