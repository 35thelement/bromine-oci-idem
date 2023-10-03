
"""Tests for validating Virtual Networks. """

import pytest






@pytest.mark.asyncio

async def test_list_allowed_peer_regions_for_remote_peering(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_allowed_peer_regions_for_remote_peering(
        ctx,)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_byoip_ranges(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_byoip_ranges(
        ctx,
        opc_request_id=value, limit=value, page=value, display_name=value, lifecycle_state=value, sort_by=value, sort_order=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_byoip_range(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_byoip_range(
        ctx,
        opc_request_id=value, opc_retry_token=value, cidr_block=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, ipv6_cidr_block=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_byoip_range(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_byoip_range(
        ctx,
        opc_request_id=value, byoip_range_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_byoip_range(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_byoip_range(
        ctx,
        opc_request_id=value, byoip_range_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_byoip_range(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_byoip_range(
        ctx,
        opc_request_id=value, byoip_range_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_advertise_byoip_range(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.advertise_byoip_range(
        ctx,
        opc_request_id=value, byoip_range_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_byoip_range_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_byoip_range_compartment(
        ctx,
        byoip_range_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_validate_byoip_range(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.validate_byoip_range(
        ctx,
        opc_request_id=value, byoip_range_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_withdraw_byoip_range(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.withdraw_byoip_range(
        ctx,
        opc_request_id=value, byoip_range_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_byoip_allocated_ranges(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_byoip_allocated_ranges(
        ctx,
        opc_request_id=value, byoip_range_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_capture_filters(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_capture_filters(
        ctx,
        compartment_id=value, limit=value, page=value, opc_request_id=value, sort_by=value, sort_order=value, display_name=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_capture_filter(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_capture_filter(
        ctx,
        opc_retry_token=value, opc_request_id=value, compartment_id=value, defined_tags=value, display_name=value, filter_type=value, freeform_tags=value, vtap_capture_filter_rules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_capture_filter(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_capture_filter(
        ctx,
        capture_filter_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_capture_filter(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_capture_filter(
        ctx,
        capture_filter_id=value, if_match=value, opc_request_id=value, defined_tags=value, display_name=value, freeform_tags=value, vtap_capture_filter_rules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_capture_filter(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_capture_filter(
        ctx,
        capture_filter_id=value, if_match=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_capture_filter_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_capture_filter_compartment(
        ctx,
        capture_filter_id=value, if_match=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_cpe_device_shapes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_cpe_device_shapes(
        ctx,
        limit=value, page=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_cpe_device_shape(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_cpe_device_shape(
        ctx,
        cpe_device_shape_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_cpes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_cpes(
        ctx,
        compartment_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_cpe(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_cpe(
        ctx,
        opc_retry_token=value, compartment_id=value, cpe_device_shape_id=value, defined_tags=value, display_name=value, freeform_tags=value, ip_address=value, is_private=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_cpe(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_cpe(
        ctx,
        cpe_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_cpe(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_cpe(
        ctx,
        cpe_id=value, if_match=value, cpe_device_shape_id=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_cpe(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_cpe(
        ctx,
        cpe_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_cpe_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_cpe_compartment(
        ctx,
        cpe_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_cpe_device_config_content(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_cpe_device_config_content(
        ctx,
        cpe_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_cross_connect_groups(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_cross_connect_groups(
        ctx,
        compartment_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_cross_connect_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_cross_connect_group(
        ctx,
        opc_retry_token=value, compartment_id=value, customer_reference_name=value, defined_tags=value, display_name=value, freeform_tags=value, macsec_properties=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_cross_connect_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_cross_connect_group(
        ctx,
        cross_connect_group_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_cross_connect_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_cross_connect_group(
        ctx,
        if_match=value, cross_connect_group_id=value, customer_reference_name=value, defined_tags=value, display_name=value, freeform_tags=value, macsec_properties=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_cross_connect_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_cross_connect_group(
        ctx,
        cross_connect_group_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_cross_connect_group_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_cross_connect_group_compartment(
        ctx,
        cross_connect_group_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_cross_connect_locations(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_cross_connect_locations(
        ctx,
        compartment_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_crossconnect_port_speed_shapes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_crossconnect_port_speed_shapes(
        ctx,
        compartment_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_cross_connects(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_cross_connects(
        ctx,
        compartment_id=value, cross_connect_group_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_cross_connect(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_cross_connect(
        ctx,
        opc_retry_token=value, compartment_id=value, cross_connect_group_id=value, customer_reference_name=value, defined_tags=value, display_name=value, far_cross_connect_or_cross_connect_group_id=value, freeform_tags=value, location_name=value, macsec_properties=value, near_cross_connect_or_cross_connect_group_id=value, port_speed_shape_name=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_cross_connect(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_cross_connect(
        ctx,
        cross_connect_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_cross_connect(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_cross_connect(
        ctx,
        cross_connect_id=value, if_match=value, customer_reference_name=value, defined_tags=value, display_name=value, freeform_tags=value, is_active=value, macsec_properties=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_cross_connect(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_cross_connect(
        ctx,
        cross_connect_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_cross_connect_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_cross_connect_compartment(
        ctx,
        cross_connect_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_cross_connect_letter_of_authority(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_cross_connect_letter_of_authority(
        ctx,
        cross_connect_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_cross_connect_status(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_cross_connect_status(
        ctx,
        cross_connect_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_dhcp_options(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_dhcp_options(
        ctx,
        compartment_id=value, vcn_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_dhcp_options(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_dhcp_options(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, options=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_dhcp_options(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_dhcp_options(
        ctx,
        dhcp_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_dhcp_options(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_dhcp_options(
        ctx,
        dhcp_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, options=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_dhcp_options(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_dhcp_options(
        ctx,
        dhcp_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_dhcp_options_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_dhcp_options_compartment(
        ctx,
        dhcp_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_drg_attachments(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_drg_attachments(
        ctx,
        compartment_id=value, vcn_id=value, drg_id=value, limit=value, page=value, network_id=value, attachment_type=value, drg_route_table_id=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_drg_attachment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_drg_attachment(
        ctx,
        opc_retry_token=value, defined_tags=value, display_name=value, drg_id=value, drg_route_table_id=value, freeform_tags=value, network_details=value, route_table_id=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_drg_attachment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_drg_attachment(
        ctx,
        drg_attachment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_drg_attachment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_drg_attachment(
        ctx,
        drg_attachment_id=value, if_match=value, defined_tags=value, display_name=value, drg_route_table_id=value, export_drg_route_distribution_id=value, freeform_tags=value, network_details=value, route_table_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_drg_attachment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_drg_attachment(
        ctx,
        drg_attachment_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_remove_export_drg_route_distribution(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.remove_export_drg_route_distribution(
        ctx,
        drg_attachment_id=value, opc_request_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_drg_route_distributions(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_drg_route_distributions(
        ctx,
        drg_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_drg_route_distribution(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_drg_route_distribution(
        ctx,
        opc_retry_token=value, defined_tags=value, display_name=value, distribution_type=value, drg_id=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_drg_route_distribution(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_drg_route_distribution(
        ctx,
        drg_route_distribution_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_drg_route_distribution(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_drg_route_distribution(
        ctx,
        if_match=value, drg_route_distribution_id=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_drg_route_distribution(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_drg_route_distribution(
        ctx,
        if_match=value, drg_route_distribution_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_add_drg_route_distribution_statements(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.add_drg_route_distribution_statements(
        ctx,
        drg_route_distribution_id=value, statements=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_remove_drg_route_distribution_statements(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.remove_drg_route_distribution_statements(
        ctx,
        drg_route_distribution_id=value, statement_ids=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_drg_route_distribution_statements(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_drg_route_distribution_statements(
        ctx,
        drg_route_distribution_id=value, statements=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_drg_route_distribution_statements(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_drg_route_distribution_statements(
        ctx,
        drg_route_distribution_id=value, limit=value, page=value, sort_by=value, sort_order=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_drg_route_tables(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_drg_route_tables(
        ctx,
        drg_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, import_drg_route_distribution_id=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_drg_route_table(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_drg_route_table(
        ctx,
        opc_retry_token=value, defined_tags=value, display_name=value, drg_id=value, freeform_tags=value, import_drg_route_distribution_id=value, is_ecmp_enabled=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_drg_route_table(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_drg_route_table(
        ctx,
        drg_route_table_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_drg_route_table(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_drg_route_table(
        ctx,
        if_match=value, drg_route_table_id=value, defined_tags=value, display_name=value, freeform_tags=value, import_drg_route_distribution_id=value, is_ecmp_enabled=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_drg_route_table(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_drg_route_table(
        ctx,
        if_match=value, drg_route_table_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_add_drg_route_rules(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.add_drg_route_rules(
        ctx,
        drg_route_table_id=value, opc_retry_token=value, route_rules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_remove_drg_route_rules(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.remove_drg_route_rules(
        ctx,
        drg_route_table_id=value, route_rule_ids=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_remove_import_drg_route_distribution(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.remove_import_drg_route_distribution(
        ctx,
        drg_route_table_id=value, opc_request_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_drg_route_rules(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_drg_route_rules(
        ctx,
        drg_route_table_id=value, route_rules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_drg_route_rules(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_drg_route_rules(
        ctx,
        drg_route_table_id=value, limit=value, page=value, route_type=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_drgs(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_drgs(
        ctx,
        compartment_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_drg(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_drg(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_drg(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_drg(
        ctx,
        drg_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_drg(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_drg(
        ctx,
        drg_id=value, if_match=value, default_drg_route_tables=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_drg(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_drg(
        ctx,
        drg_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_all_drg_attachments(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_all_drg_attachments(
        ctx,
        drg_id=value, opc_request_id=value, limit=value, page=value, attachment_type=value, is_cross_tenancy=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_upgrade_drg(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.upgrade_drg(
        ctx,
        drg_id=value, opc_request_id=value, opc_retry_token=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_upgrade_status(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_upgrade_status(
        ctx,
        drg_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_drg_redundancy_status(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_drg_redundancy_status(
        ctx,
        drg_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_fast_connect_provider_services(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_fast_connect_provider_services(
        ctx,
        compartment_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_fast_connect_provider_service(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_fast_connect_provider_service(
        ctx,
        provider_service_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_fast_connect_provider_service_key(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_fast_connect_provider_service_key(
        ctx,
        provider_service_id=value, provider_service_key_name=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
        ctx,
        limit=value, page=value, provider_service_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_internet_gateways(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_internet_gateways(
        ctx,
        compartment_id=value, vcn_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_internet_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_internet_gateway(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, is_enabled=value, route_table_id=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_internet_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_internet_gateway(
        ctx,
        ig_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_internet_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_internet_gateway(
        ctx,
        ig_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, is_enabled=value, route_table_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_internet_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_internet_gateway(
        ctx,
        ig_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_internet_gateway_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_internet_gateway_compartment(
        ctx,
        ig_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_allowed_ike_ip_sec_parameters(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_allowed_ike_ip_sec_parameters(
        ctx,
        opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_ip_sec_connections(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_ip_sec_connections(
        ctx,
        compartment_id=value, drg_id=value, cpe_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_ip_sec_connection(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_ip_sec_connection(
        ctx,
        opc_retry_token=value, compartment_id=value, cpe_id=value, cpe_local_identifier=value, cpe_local_identifier_type=value, defined_tags=value, display_name=value, drg_id=value, freeform_tags=value, static_routes=value, tunnel_configuration=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_ip_sec_connection(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_ip_sec_connection(
        ctx,
        ipsc_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_ip_sec_connection(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_ip_sec_connection(
        ctx,
        ipsc_id=value, if_match=value, cpe_local_identifier=value, cpe_local_identifier_type=value, defined_tags=value, display_name=value, freeform_tags=value, static_routes=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_ip_sec_connection(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_ip_sec_connection(
        ctx,
        ipsc_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_ip_sec_connection_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_ip_sec_connection_compartment(
        ctx,
        ipsc_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_ipsec_cpe_device_config_content(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_ipsec_cpe_device_config_content(
        ctx,
        ipsc_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_ip_sec_connection_device_config(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_ip_sec_connection_device_config(
        ctx,
        ipsc_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_ip_sec_connection_device_status(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_ip_sec_connection_device_status(
        ctx,
        ipsc_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_ip_sec_connection_tunnels(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_ip_sec_connection_tunnels(
        ctx,
        ipsc_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_ip_sec_connection_tunnel(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_ip_sec_connection_tunnel(
        ctx,
        ipsc_id=value, tunnel_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_ip_sec_connection_tunnel(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_ip_sec_connection_tunnel(
        ctx,
        ipsc_id=value, tunnel_id=value, if_match=value, opc_request_id=value, bgp_session_config=value, display_name=value, dpd_config=value, encryption_domain_config=value, nat_translation_enabled=value, oracle_initiation=value, phase_one_config=value, phase_two_config=value, routing=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_ip_sec_connection_tunnel_error(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_ip_sec_connection_tunnel_error(
        ctx,
        ipsc_id=value, tunnel_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_ip_sec_connection_tunnel_routes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_ip_sec_connection_tunnel_routes(
        ctx,
        ipsc_id=value, tunnel_id=value, limit=value, page=value, advertiser=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_ip_sec_connection_tunnel_shared_secret(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_ip_sec_connection_tunnel_shared_secret(
        ctx,
        ipsc_id=value, tunnel_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_ip_sec_connection_tunnel_shared_secret(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_ip_sec_connection_tunnel_shared_secret(
        ctx,
        ipsc_id=value, tunnel_id=value, if_match=value, shared_secret=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_tunnel_cpe_device_config(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_tunnel_cpe_device_config(
        ctx,
        ipsc_id=value, tunnel_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_tunnel_cpe_device_config(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_tunnel_cpe_device_config(
        ctx,
        ipsc_id=value, tunnel_id=value, if_match=value, opc_retry_token=value, opc_request_id=value, tunnel_cpe_device_config=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_tunnel_cpe_device_config_content(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_tunnel_cpe_device_config_content(
        ctx,
        ipsc_id=value, tunnel_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_ip_sec_connection_tunnel_security_associations(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_ip_sec_connection_tunnel_security_associations(
        ctx,
        ipsc_id=value, tunnel_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_ipv6s(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_ipv6s(
        ctx,
        limit=value, page=value, ip_address=value, subnet_id=value, vnic_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_ipv6(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_ipv6(
        ctx,
        opc_request_id=value, opc_retry_token=value, defined_tags=value, display_name=value, freeform_tags=value, ip_address=value, ipv6_subnet_cidr=value, is_internet_access_allowed=value, vnic_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_ipv6(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_ipv6(
        ctx,
        ipv6_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_ipv6(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_ipv6(
        ctx,
        ipv6_id=value, if_match=value, opc_request_id=value, defined_tags=value, display_name=value, freeform_tags=value, is_internet_access_allowed=value, vnic_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_ipv6(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_ipv6(
        ctx,
        ipv6_id=value, if_match=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_local_peering_gateways(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_local_peering_gateways(
        ctx,
        compartment_id=value, limit=value, page=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_local_peering_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_local_peering_gateway(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, route_table_id=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_local_peering_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_local_peering_gateway(
        ctx,
        local_peering_gateway_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_local_peering_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_local_peering_gateway(
        ctx,
        local_peering_gateway_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, route_table_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_local_peering_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_local_peering_gateway(
        ctx,
        local_peering_gateway_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_local_peering_gateway_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_local_peering_gateway_compartment(
        ctx,
        local_peering_gateway_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_connect_local_peering_gateways(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.connect_local_peering_gateways(
        ctx,
        local_peering_gateway_id=value, peer_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_nat_gateways(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_nat_gateways(
        ctx,
        compartment_id=value, vcn_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_nat_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_nat_gateway(
        ctx,
        opc_retry_token=value, block_traffic=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, public_ip_id=value, route_table_id=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_nat_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_nat_gateway(
        ctx,
        nat_gateway_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_nat_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_nat_gateway(
        ctx,
        if_match=value, nat_gateway_id=value, block_traffic=value, defined_tags=value, display_name=value, freeform_tags=value, route_table_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_nat_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_nat_gateway(
        ctx,
        if_match=value, nat_gateway_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_nat_gateway_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_nat_gateway_compartment(
        ctx,
        nat_gateway_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_network_security_groups(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_network_security_groups(
        ctx,
        compartment_id=value, vlan_id=value, vcn_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_network_security_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_network_security_group(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_network_security_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_network_security_group(
        ctx,
        network_security_group_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_network_security_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_network_security_group(
        ctx,
        if_match=value, network_security_group_id=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_network_security_group(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_network_security_group(
        ctx,
        if_match=value, network_security_group_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_add_network_security_group_security_rules(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.add_network_security_group_security_rules(
        ctx,
        network_security_group_id=value, security_rules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_network_security_group_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_network_security_group_compartment(
        ctx,
        network_security_group_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_remove_network_security_group_security_rules(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.remove_network_security_group_security_rules(
        ctx,
        network_security_group_id=value, security_rule_ids=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_network_security_group_security_rules(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_network_security_group_security_rules(
        ctx,
        network_security_group_id=value, security_rules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_network_security_group_security_rules(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_network_security_group_security_rules(
        ctx,
        network_security_group_id=value, direction=value, limit=value, page=value, sort_by=value, sort_order=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_network_security_group_vnics(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_network_security_group_vnics(
        ctx,
        network_security_group_id=value, limit=value, page=value, sort_by=value, sort_order=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_networking_topology(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_networking_topology(
        ctx,
        compartment_id=value, access_level=value, query_compartment_subtree=value, opc_request_id=value, if_none_match=value, cache_control=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_private_ips(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_private_ips(
        ctx,
        limit=value, page=value, ip_address=value, subnet_id=value, vnic_id=value, vlan_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_private_ip(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_private_ip(
        ctx,
        opc_retry_token=value, defined_tags=value, display_name=value, freeform_tags=value, hostname_label=value, ip_address=value, vlan_id=value, vnic_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_private_ip(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_private_ip(
        ctx,
        private_ip_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_private_ip(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_private_ip(
        ctx,
        private_ip_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, hostname_label=value, vnic_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_private_ip(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_private_ip(
        ctx,
        private_ip_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_public_ip_pools(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_public_ip_pools(
        ctx,
        opc_request_id=value, limit=value, page=value, display_name=value, byoip_range_id=value, sort_by=value, sort_order=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_public_ip_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_public_ip_pool(
        ctx,
        opc_request_id=value, opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_public_ip_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_public_ip_pool(
        ctx,
        opc_request_id=value, public_ip_pool_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_public_ip_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_public_ip_pool(
        ctx,
        opc_request_id=value, public_ip_pool_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_public_ip_pool(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_public_ip_pool(
        ctx,
        opc_request_id=value, public_ip_pool_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_add_public_ip_pool_capacity(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.add_public_ip_pool_capacity(
        ctx,
        opc_request_id=value, public_ip_pool_id=value, opc_retry_token=value, byoip_range_id=value, cidr_block=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_public_ip_pool_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_public_ip_pool_compartment(
        ctx,
        public_ip_pool_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_remove_public_ip_pool_capacity(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.remove_public_ip_pool_capacity(
        ctx,
        public_ip_pool_id=value, opc_request_id=value, opc_retry_token=value, cidr_block=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_public_ips(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_public_ips(
        ctx,
        limit=value, page=value, scope=value, availability_domain=value, lifetime=value, compartment_id=value, public_ip_pool_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_public_ip(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_public_ip(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, lifetime=value, private_ip_id=value, public_ip_pool_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_public_ip_by_ip_address(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_public_ip_by_ip_address(
        ctx,
        ip_address=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_public_ip_by_private_ip_id(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_public_ip_by_private_ip_id(
        ctx,
        private_ip_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_public_ip(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_public_ip(
        ctx,
        public_ip_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_public_ip(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_public_ip(
        ctx,
        public_ip_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, private_ip_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_public_ip(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_public_ip(
        ctx,
        public_ip_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_public_ip_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_public_ip_compartment(
        ctx,
        public_ip_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_remote_peering_connections(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_remote_peering_connections(
        ctx,
        compartment_id=value, drg_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_remote_peering_connection(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_remote_peering_connection(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, drg_id=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_remote_peering_connection(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_remote_peering_connection(
        ctx,
        remote_peering_connection_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_remote_peering_connection(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_remote_peering_connection(
        ctx,
        if_match=value, remote_peering_connection_id=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_remote_peering_connection(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_remote_peering_connection(
        ctx,
        if_match=value, remote_peering_connection_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_remote_peering_connection_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_remote_peering_connection_compartment(
        ctx,
        remote_peering_connection_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_connect_remote_peering_connections(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.connect_remote_peering_connections(
        ctx,
        remote_peering_connection_id=value, peer_id=value, peer_region_name=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_route_tables(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_route_tables(
        ctx,
        compartment_id=value, limit=value, page=value, vcn_id=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_route_table(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_route_table(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, route_rules=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_route_table(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_route_table(
        ctx,
        rt_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_route_table(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_route_table(
        ctx,
        rt_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, route_rules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_route_table(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_route_table(
        ctx,
        rt_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_route_table_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_route_table_compartment(
        ctx,
        rt_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_security_lists(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_security_lists(
        ctx,
        compartment_id=value, limit=value, page=value, vcn_id=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_security_list(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_security_list(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, egress_security_rules=value, freeform_tags=value, ingress_security_rules=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_security_list(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_security_list(
        ctx,
        security_list_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_security_list(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_security_list(
        ctx,
        security_list_id=value, if_match=value, defined_tags=value, display_name=value, egress_security_rules=value, freeform_tags=value, ingress_security_rules=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_security_list(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_security_list(
        ctx,
        security_list_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_security_list_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_security_list_compartment(
        ctx,
        security_list_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_service_gateways(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_service_gateways(
        ctx,
        compartment_id=value, vcn_id=value, limit=value, page=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_service_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_service_gateway(
        ctx,
        opc_retry_token=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, route_table_id=value, services=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_service_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_service_gateway(
        ctx,
        service_gateway_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_service_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_service_gateway(
        ctx,
        service_gateway_id=value, if_match=value, block_traffic=value, defined_tags=value, display_name=value, freeform_tags=value, route_table_id=value, services=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_service_gateway(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_service_gateway(
        ctx,
        service_gateway_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_attach_service_id(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.attach_service_id(
        ctx,
        if_match=value, service_gateway_id=value, service_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_service_gateway_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_service_gateway_compartment(
        ctx,
        service_gateway_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_detach_service_id(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.detach_service_id(
        ctx,
        if_match=value, service_gateway_id=value, service_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_services(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_services(
        ctx,
        limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_service(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_service(
        ctx,
        service_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_subnet_topology(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_subnet_topology(
        ctx,
        compartment_id=value, access_level=value, query_compartment_subtree=value, subnet_id=value, opc_request_id=value, if_none_match=value, cache_control=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_subnets(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_subnets(
        ctx,
        compartment_id=value, limit=value, page=value, vcn_id=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_subnet(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_subnet(
        ctx,
        opc_retry_token=value, availability_domain=value, cidr_block=value, compartment_id=value, defined_tags=value, dhcp_options_id=value, display_name=value, dns_label=value, freeform_tags=value, ipv6_cidr_block=value, ipv6_cidr_blocks=value, prohibit_public_ip_on_vnic=value, route_table_id=value, security_list_ids=value, vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_subnet(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_subnet(
        ctx,
        subnet_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_subnet(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_subnet(
        ctx,
        subnet_id=value, if_match=value, defined_tags=value, dhcp_options_id=value, display_name=value, freeform_tags=value, ipv6_cidr_block=value, ipv6_cidr_blocks=value, route_table_id=value, security_list_ids=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_subnet(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_subnet(
        ctx,
        subnet_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_add_ipv6_subnet_cidr(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.add_ipv6_subnet_cidr(
        ctx,
        subnet_id=value, opc_retry_token=value, if_match=value, opc_request_id=value, ipv6_cidr_block=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_subnet_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_subnet_compartment(
        ctx,
        subnet_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_remove_ipv6_subnet_cidr(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.remove_ipv6_subnet_cidr(
        ctx,
        subnet_id=value, opc_retry_token=value, if_match=value, opc_request_id=value, ipv6_cidr_block=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_vcn_topology(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_vcn_topology(
        ctx,
        compartment_id=value, access_level=value, query_compartment_subtree=value, vcn_id=value, opc_request_id=value, if_none_match=value, cache_control=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_vcns(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_vcns(
        ctx,
        compartment_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_vcn(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_vcn(
        ctx,
        opc_retry_token=value, byoipv6_cidr_details=value, cidr_block=value, cidr_blocks=value, compartment_id=value, defined_tags=value, display_name=value, dns_label=value, freeform_tags=value, ipv6_cidr_block=value, ipv6_private_cidr_blocks=value, is_ipv6_enabled=value, is_oracle_gua_allocation_enabled=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_vcn(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_vcn(
        ctx,
        vcn_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_vcn(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_vcn(
        ctx,
        vcn_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_vcn(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_vcn(
        ctx,
        vcn_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_add_vcn_cidr(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.add_vcn_cidr(
        ctx,
        vcn_id=value, opc_request_id=value, opc_retry_token=value, if_match=value, cidr_block=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_add_ipv6_vcn_cidr(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.add_ipv6_vcn_cidr(
        ctx,
        vcn_id=value, opc_request_id=value, opc_retry_token=value, if_match=value, byoipv6_cidr_detail=value, ipv6_private_cidr_block=value, is_oracle_gua_allocation_enabled=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_vcn_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_vcn_compartment(
        ctx,
        vcn_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_modify_vcn_cidr(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.modify_vcn_cidr(
        ctx,
        vcn_id=value, opc_request_id=value, opc_retry_token=value, if_match=value, new_cidr_block=value, original_cidr_block=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_remove_vcn_cidr(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.remove_vcn_cidr(
        ctx,
        vcn_id=value, opc_request_id=value, opc_retry_token=value, if_match=value, cidr_block=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_remove_ipv6_vcn_cidr(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.remove_ipv6_vcn_cidr(
        ctx,
        vcn_id=value, opc_request_id=value, opc_retry_token=value, if_match=value, ipv6_cidr_block=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_virtual_circuit_bandwidth_shapes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_virtual_circuit_bandwidth_shapes(
        ctx,
        compartment_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_virtual_circuits(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_virtual_circuits(
        ctx,
        compartment_id=value, limit=value, page=value, display_name=value, sort_by=value, sort_order=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_virtual_circuit(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_virtual_circuit(
        ctx,
        opc_retry_token=value, bandwidth_shape_name=value, bgp_admin_state=value, compartment_id=value, cross_connect_mappings=value, customer_bgp_asn=value, defined_tags=value, display_name=value, freeform_tags=value, gateway_id=value, ip_mtu=value, is_bfd_enabled=value, is_transport_mode=value, provider_name=value, provider_service_id=value, provider_service_key_name=value, provider_service_name=value, public_prefixes=value, region=value, routing_policy=value, type_=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_virtual_circuit(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_virtual_circuit(
        ctx,
        virtual_circuit_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_virtual_circuit(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_virtual_circuit(
        ctx,
        virtual_circuit_id=value, if_match=value, bandwidth_shape_name=value, bgp_admin_state=value, cross_connect_mappings=value, customer_bgp_asn=value, defined_tags=value, display_name=value, freeform_tags=value, gateway_id=value, ip_mtu=value, is_bfd_enabled=value, is_transport_mode=value, provider_service_key_name=value, provider_state=value, reference_comment=value, routing_policy=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_virtual_circuit(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_virtual_circuit(
        ctx,
        virtual_circuit_id=value, if_match=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_bulk_add_virtual_circuit_public_prefixes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.bulk_add_virtual_circuit_public_prefixes(
        ctx,
        virtual_circuit_id=value, public_prefixes=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_bulk_delete_virtual_circuit_public_prefixes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.bulk_delete_virtual_circuit_public_prefixes(
        ctx,
        virtual_circuit_id=value, public_prefixes=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_virtual_circuit_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_virtual_circuit_compartment(
        ctx,
        virtual_circuit_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_virtual_circuit_associated_tunnels(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_virtual_circuit_associated_tunnels(
        ctx,
        virtual_circuit_id=value, limit=value, page=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_cross_connect_mappings(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_cross_connect_mappings(
        ctx,
        opc_request_id=value, virtual_circuit_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_virtual_circuit_public_prefixes(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_virtual_circuit_public_prefixes(
        ctx,
        virtual_circuit_id=value, verification_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_vlans(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_vlans(
        ctx,
        compartment_id=value, limit=value, page=value, vcn_id=value, display_name=value, sort_by=value, sort_order=value, opc_request_id=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_vlan(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_vlan(
        ctx,
        opc_retry_token=value, opc_request_id=value, availability_domain=value, cidr_block=value, compartment_id=value, defined_tags=value, display_name=value, freeform_tags=value, nsg_ids=value, route_table_id=value, vcn_id=value, vlan_tag=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_vlan(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_vlan(
        ctx,
        vlan_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_vlan(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_vlan(
        ctx,
        vlan_id=value, if_match=value, opc_request_id=value, defined_tags=value, display_name=value, freeform_tags=value, nsg_ids=value, route_table_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_vlan(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_vlan(
        ctx,
        vlan_id=value, if_match=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_vlan_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_vlan_compartment(
        ctx,
        if_match=value, vlan_id=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_vnic(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_vnic(
        ctx,
        vnic_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_vnic(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_vnic(
        ctx,
        vnic_id=value, if_match=value, defined_tags=value, display_name=value, freeform_tags=value, hostname_label=value, nsg_ids=value, skip_source_dest_check=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list_vtaps(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.list_vtaps(
        ctx,
        compartment_id=value, vcn_id=value, source=value, target_id=value, target_ip=value, is_vtap_enabled=value, limit=value, page=value, opc_request_id=value, sort_by=value, sort_order=value, display_name=value, lifecycle_state=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_create_vtap(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.create_vtap(
        ctx,
        opc_retry_token=value, opc_request_id=value, capture_filter_id=value, compartment_id=value, defined_tags=value, display_name=value, encapsulation_protocol=value, freeform_tags=value, is_vtap_enabled=value, max_packet_size=value, source_id=value, source_private_endpoint_ip=value, source_private_endpoint_subnet_id=value, source_type=value, target_id=value, target_ip=value, target_type=value, traffic_mode=value, vcn_id=value, vxlan_network_identifier=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get_vtap(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.get_vtap(
        ctx,
        vtap_id=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update_vtap(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.update_vtap(
        ctx,
        vtap_id=value, if_match=value, opc_request_id=value, capture_filter_id=value, defined_tags=value, display_name=value, encapsulation_protocol=value, freeform_tags=value, is_vtap_enabled=value, max_packet_size=value, source_id=value, source_private_endpoint_ip=value, source_private_endpoint_subnet_id=value, source_type=value, target_id=value, target_ip=value, target_type=value, traffic_mode=value, vxlan_network_identifier=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete_vtap(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.delete_vtap(
        ctx,
        vtap_id=value, if_match=value, opc_request_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_change_vtap_compartment(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.virtual_network.change_vtap_compartment(
        ctx,
        vtap_id=value, if_match=value, opc_request_id=value, opc_retry_token=value, compartment_id=value
)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations


