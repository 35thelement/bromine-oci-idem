
"""Tests for validating Compute Managements. """

import pytest






@pytest.mark.asyncio

async def test_list_cluster_networks(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.list_cluster_networks(
        ctx,
        compartment_id=value, display_name=value, limit=value, page=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_cluster_network(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.create_cluster_network(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, instance_pools=value, placement_configuration=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_cluster_network(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.get_cluster_network(
        ctx,
        cluster_network_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_cluster_network(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.update_cluster_network(
        ctx,
        cluster_network_id=value, opc_retry_token=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, instance_pools=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_terminate_cluster_network(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.terminate_cluster_network(
        ctx,
        cluster_network_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_cluster_network_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.change_cluster_network_compartment(
        ctx,
        cluster_network_id=value, if_match=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_cluster_network_instances(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.list_cluster_network_instances(
        ctx,
        compartment_id=value, cluster_network_id=value, display_name=value, limit=value, page=value, sort_by=value, sort_order=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_instance_configurations(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.list_instance_configurations(
        ctx,
        compartment_id=value, limit=value, page=value, sort_by=value, sort_order=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_instance_configuration(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.create_instance_configuration(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, source=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_instance_configuration(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.get_instance_configuration(
        ctx,
        instance_configuration_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_instance_configuration(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.update_instance_configuration(
        ctx,
        instance_configuration_id=value, opc_retry_token=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_instance_configuration(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.delete_instance_configuration(
        ctx,
        instance_configuration_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_instance_configuration_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.change_instance_configuration_compartment(
        ctx,
        instance_configuration_id=value, if_match=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_launch_instance_configuration(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.launch_instance_configuration(
        ctx,
        instance_configuration_id=value, opc_retry_token=value, instance_type=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_instance_pools(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.list_instance_pools(
        ctx,
        compartment_id=value, display_name=value, limit=value, page=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_instance_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.create_instance_pool(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, instance_configuration_id=value, instance_display_name_formatter=value, instance_hostname_formatter=value, load_balancers=value, placement_configurations=value, size=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_instance_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.get_instance_pool(
        ctx,
        instance_pool_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_instance_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.update_instance_pool(
        ctx,
        instance_pool_id=value, opc_retry_token=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, instance_configuration_id=value, instance_display_name_formatter=value, instance_hostname_formatter=value, placement_configurations=value, size=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_terminate_instance_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.terminate_instance_pool(
        ctx,
        instance_pool_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_attach_load_balancer(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.attach_load_balancer(
        ctx,
        instance_pool_id=value, opc_retry_token=value, if_match=value, backend_set_name=value, load_balancer_id=value, port=value, vnic_selection=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_instance_pool_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.change_instance_pool_compartment(
        ctx,
        instance_pool_id=value, if_match=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_detach_instance_pool_instance(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.detach_instance_pool_instance(
        ctx,
        instance_pool_id=value, opc_retry_token=value, instance_id=value, is_auto_terminate=value, is_decrement_size=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_detach_load_balancer(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.detach_load_balancer(
        ctx,
        instance_pool_id=value, opc_retry_token=value, if_match=value, backend_set_name=value, load_balancer_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_reset_instance_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.reset_instance_pool(
        ctx,
        instance_pool_id=value, opc_retry_token=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_softreset_instance_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.softreset_instance_pool(
        ctx,
        instance_pool_id=value, opc_retry_token=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_softstop_instance_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.softstop_instance_pool(
        ctx,
        instance_pool_id=value, opc_retry_token=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_start_instance_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.start_instance_pool(
        ctx,
        instance_pool_id=value, opc_retry_token=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_stop_instance_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.stop_instance_pool(
        ctx,
        instance_pool_id=value, opc_retry_token=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_instance_pool_instances(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.list_instance_pool_instances(
        ctx,
        compartment_id=value, instance_pool_id=value, display_name=value, limit=value, page=value, sort_by=value, sort_order=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_attach_instance_pool_instance(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.attach_instance_pool_instance(
        ctx,
        instance_pool_id=value, opc_retry_token=value, instance_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_instance_pool_instance(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.get_instance_pool_instance(
        ctx,
        instance_pool_id=value, instance_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_instance_pool_load_balancer_attachment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute_management.get_instance_pool_load_balancer_attachment(
        ctx,
        instance_pool_id=value, instance_pool_load_balancer_attachment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations


