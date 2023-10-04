"""Tests for validating Computes. """
import pytest


@pytest.mark.asyncio
async def test_list_app_catalog_listings(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_app_catalog_listings(
        ctx,
        limit=value,
        page=value,
        sort_order=value,
        publisher_name=value,
        publisher_type=value,
        display_name=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_app_catalog_listing(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_app_catalog_listing(ctx, listing_id=value)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_app_catalog_listing_resource_versions(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_app_catalog_listing_resource_versions(
        ctx, listing_id=value, limit=value, page=value, sort_order=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_app_catalog_listing_resource_version(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_app_catalog_listing_resource_version(
        ctx, listing_id=value, resource_version=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_app_catalog_listing_agreements(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_app_catalog_listing_agreements(
        ctx, listing_id=value, resource_version=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_app_catalog_subscriptions(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_app_catalog_subscriptions(
        ctx,
        compartment_id=value,
        limit=value,
        page=value,
        sort_by=value,
        sort_order=value,
        listing_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_create_app_catalog_subscription(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.create_app_catalog_subscription(
        ctx,
        opc_retry_token=value,
        compartment_id=value,
        eula_link=value,
        listing_id=value,
        listing_resource_version=value,
        oracle_terms_of_use_link=value,
        signature=value,
        time_retrieved=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_delete_app_catalog_subscription(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.delete_app_catalog_subscription(
        ctx, listing_id=value, compartment_id=value, resource_version=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_boot_volume_attachments(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_boot_volume_attachments(
        ctx,
        availability_domain=value,
        compartment_id=value,
        limit=value,
        page=value,
        instance_id=value,
        boot_volume_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_attach_boot_volume(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.attach_boot_volume(
        ctx,
        opc_retry_token=value,
        boot_volume_id=value,
        display_name=value,
        encryption_in_transit_type=value,
        instance_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_boot_volume_attachment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_boot_volume_attachment(
        ctx, boot_volume_attachment_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_detach_boot_volume(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.detach_boot_volume(
        ctx, boot_volume_attachment_id=value, if_match=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_create_compute_capacity_report(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.create_compute_capacity_report(
        ctx,
        opc_request_id=value,
        opc_retry_token=value,
        availability_domain=value,
        compartment_id=value,
        shape_availabilities=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_compute_capacity_reservation_instance_shapes(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_compute_capacity_reservation_instance_shapes(
        ctx,
        availability_domain=value,
        compartment_id=value,
        opc_request_id=value,
        limit=value,
        page=value,
        display_name=value,
        sort_by=value,
        sort_order=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_compute_capacity_reservations(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_compute_capacity_reservations(
        ctx,
        availability_domain=value,
        compartment_id=value,
        lifecycle_state=value,
        display_name=value,
        limit=value,
        page=value,
        opc_request_id=value,
        sort_by=value,
        sort_order=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_create_compute_capacity_reservation(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.create_compute_capacity_reservation(
        ctx,
        opc_request_id=value,
        opc_retry_token=value,
        availability_domain=value,
        compartment_id=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
        instance_reservation_configs=value,
        is_default_reservation=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_compute_capacity_reservation(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_compute_capacity_reservation(
        ctx, capacity_reservation_id=value, opc_request_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_update_compute_capacity_reservation(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.update_compute_capacity_reservation(
        ctx,
        capacity_reservation_id=value,
        if_match=value,
        opc_request_id=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
        instance_reservation_configs=value,
        is_default_reservation=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_delete_compute_capacity_reservation(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.delete_compute_capacity_reservation(
        ctx, capacity_reservation_id=value, opc_request_id=value, if_match=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_change_compute_capacity_reservation_compartment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.change_compute_capacity_reservation_compartment(
        ctx,
        capacity_reservation_id=value,
        if_match=value,
        opc_request_id=value,
        opc_retry_token=value,
        compartment_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_compute_capacity_reservation_instances(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_compute_capacity_reservation_instances(
        ctx,
        capacity_reservation_id=value,
        availability_domain=value,
        compartment_id=value,
        opc_request_id=value,
        limit=value,
        page=value,
        sort_by=value,
        sort_order=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_compute_clusters(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_compute_clusters(
        ctx,
        availability_domain=value,
        compartment_id=value,
        display_name=value,
        limit=value,
        page=value,
        sort_by=value,
        sort_order=value,
        opc_request_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_create_compute_cluster(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.create_compute_cluster(
        ctx,
        opc_retry_token=value,
        opc_request_id=value,
        availability_domain=value,
        compartment_id=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_compute_cluster(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_compute_cluster(
        ctx, compute_cluster_id=value, opc_request_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_update_compute_cluster(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.update_compute_cluster(
        ctx,
        compute_cluster_id=value,
        opc_request_id=value,
        opc_retry_token=value,
        if_match=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_delete_compute_cluster(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.delete_compute_cluster(
        ctx, compute_cluster_id=value, opc_request_id=value, if_match=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_change_compute_cluster_compartment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.change_compute_cluster_compartment(
        ctx,
        compute_cluster_id=value,
        if_match=value,
        opc_request_id=value,
        opc_retry_token=value,
        compartment_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_compute_global_image_capability_schemas(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_compute_global_image_capability_schemas(
        ctx,
        compartment_id=value,
        display_name=value,
        limit=value,
        page=value,
        sort_by=value,
        sort_order=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_compute_global_image_capability_schema(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_compute_global_image_capability_schema(
        ctx, compute_global_image_capability_schema_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_compute_global_image_capability_schema_versions(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = (
        await hub.tool.oci.compute.list_compute_global_image_capability_schema_versions(
            ctx,
            compute_global_image_capability_schema_id=value,
            display_name=value,
            limit=value,
            page=value,
            sort_by=value,
            sort_order=value,
        )
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_compute_global_image_capability_schema_version(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_compute_global_image_capability_schema_version(
        ctx,
        compute_global_image_capability_schema_id=value,
        compute_global_image_capability_schema_version_name=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_compute_image_capability_schemas(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_compute_image_capability_schemas(
        ctx,
        compartment_id=value,
        image_id=value,
        display_name=value,
        limit=value,
        page=value,
        sort_by=value,
        sort_order=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_create_compute_image_capability_schema(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.create_compute_image_capability_schema(
        ctx,
        opc_retry_token=value,
        compartment_id=value,
        compute_global_image_capability_schema_version_name=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
        image_id=value,
        schema_data=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_compute_image_capability_schema(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_compute_image_capability_schema(
        ctx, compute_image_capability_schema_id=value, is_merge_enabled=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_update_compute_image_capability_schema(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.update_compute_image_capability_schema(
        ctx,
        compute_image_capability_schema_id=value,
        if_match=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
        schema_data=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_delete_compute_image_capability_schema(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.delete_compute_image_capability_schema(
        ctx, compute_image_capability_schema_id=value, if_match=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_change_compute_image_capability_schema_compartment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.change_compute_image_capability_schema_compartment(
        ctx,
        compute_image_capability_schema_id=value,
        if_match=value,
        opc_request_id=value,
        opc_retry_token=value,
        compartment_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_dedicated_vm_host_instance_shapes(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_dedicated_vm_host_instance_shapes(
        ctx,
        availability_domain=value,
        compartment_id=value,
        dedicated_vm_host_shape=value,
        limit=value,
        page=value,
        opc_request_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_dedicated_vm_host_shapes(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_dedicated_vm_host_shapes(
        ctx,
        availability_domain=value,
        compartment_id=value,
        instance_shape_name=value,
        limit=value,
        page=value,
        opc_request_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_dedicated_vm_hosts(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_dedicated_vm_hosts(
        ctx,
        availability_domain=value,
        compartment_id=value,
        lifecycle_state=value,
        display_name=value,
        instance_shape_name=value,
        limit=value,
        page=value,
        opc_request_id=value,
        sort_by=value,
        sort_order=value,
        remaining_memory_in_g_bs_greater_than_or_equal_to=value,
        remaining_ocpus_greater_than_or_equal_to=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_create_dedicated_vm_host(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.create_dedicated_vm_host(
        ctx,
        opc_request_id=value,
        opc_retry_token=value,
        availability_domain=value,
        compartment_id=value,
        dedicated_vm_host_shape=value,
        defined_tags=value,
        display_name=value,
        fault_domain=value,
        freeform_tags=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_dedicated_vm_host(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_dedicated_vm_host(
        ctx, dedicated_vm_host_id=value, opc_request_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_update_dedicated_vm_host(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.update_dedicated_vm_host(
        ctx,
        dedicated_vm_host_id=value,
        if_match=value,
        opc_request_id=value,
        opc_retry_token=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_delete_dedicated_vm_host(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.delete_dedicated_vm_host(
        ctx, dedicated_vm_host_id=value, opc_request_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_change_dedicated_vm_host_compartment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.change_dedicated_vm_host_compartment(
        ctx,
        dedicated_vm_host_id=value,
        if_match=value,
        opc_request_id=value,
        opc_retry_token=value,
        compartment_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_dedicated_vm_host_instances(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_dedicated_vm_host_instances(
        ctx,
        availability_domain=value,
        compartment_id=value,
        dedicated_vm_host_id=value,
        limit=value,
        page=value,
        opc_request_id=value,
        sort_by=value,
        sort_order=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_images(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_images(
        ctx,
        compartment_id=value,
        display_name=value,
        operating_system=value,
        operating_system_version=value,
        shape=value,
        limit=value,
        page=value,
        sort_by=value,
        sort_order=value,
        lifecycle_state=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_create_image(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.create_image(
        ctx,
        opc_retry_token=value,
        compartment_id=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
        image_source_details=value,
        instance_id=value,
        launch_mode=value,
        launch_options=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_image(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_image(ctx, image_id=value)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_update_image(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.update_image(
        ctx,
        image_id=value,
        opc_retry_token=value,
        if_match=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
        operating_system=value,
        operating_system_version=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_delete_image(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.delete_image(ctx, image_id=value, if_match=value)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_change_image_compartment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.change_image_compartment(
        ctx,
        image_id=value,
        if_match=value,
        opc_request_id=value,
        opc_retry_token=value,
        compartment_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_export_image(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.export_image(
        ctx,
        image_id=value,
        opc_retry_token=value,
        if_match=value,
        destination_type=value,
        export_format=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_image_shape_compatibility_entries(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_image_shape_compatibility_entries(
        ctx, image_id=value, limit=value, page=value, opc_request_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_image_shape_compatibility_entry(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_image_shape_compatibility_entry(
        ctx, image_id=value, shape_name=value, opc_request_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_add_image_shape_compatibility_entry(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.add_image_shape_compatibility_entry(
        ctx,
        image_id=value,
        shape_name=value,
        memory_constraints=value,
        ocpu_constraints=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_remove_image_shape_compatibility_entry(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.remove_image_shape_compatibility_entry(
        ctx, image_id=value, shape_name=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_instance_console_connections(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_instance_console_connections(
        ctx, compartment_id=value, instance_id=value, limit=value, page=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_create_instance_console_connection(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.create_instance_console_connection(
        ctx,
        opc_retry_token=value,
        defined_tags=value,
        freeform_tags=value,
        instance_id=value,
        public_key=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_instance_console_connection(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_instance_console_connection(
        ctx, instance_console_connection_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_update_instance_console_connection(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.update_instance_console_connection(
        ctx,
        instance_console_connection_id=value,
        opc_request_id=value,
        if_match=value,
        defined_tags=value,
        freeform_tags=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_delete_instance_console_connection(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.delete_instance_console_connection(
        ctx, instance_console_connection_id=value, if_match=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_console_histories(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_console_histories(
        ctx,
        availability_domain=value,
        compartment_id=value,
        limit=value,
        page=value,
        instance_id=value,
        sort_by=value,
        sort_order=value,
        lifecycle_state=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_capture_console_history(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.capture_console_history(
        ctx,
        opc_retry_token=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
        instance_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_console_history(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_console_history(
        ctx, instance_console_history_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_update_console_history(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.update_console_history(
        ctx,
        if_match=value,
        instance_console_history_id=value,
        defined_tags=value,
        display_name=value,
        freeform_tags=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_delete_console_history(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.delete_console_history(
        ctx, instance_console_history_id=value, if_match=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_console_history_content(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_console_history_content(
        ctx, instance_console_history_id=value, offset=value, length=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_instances(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_instances(
        ctx,
        availability_domain=value,
        capacity_reservation_id=value,
        compute_cluster_id=value,
        compartment_id=value,
        display_name=value,
        limit=value,
        page=value,
        sort_by=value,
        sort_order=value,
        lifecycle_state=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_launch_instance(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.launch_instance(
        ctx,
        opc_retry_token=value,
        agent_config=value,
        availability_config=value,
        availability_domain=value,
        capacity_reservation_id=value,
        compartment_id=value,
        compute_cluster_id=value,
        create_vnic_details=value,
        dedicated_vm_host_id=value,
        defined_tags=value,
        display_name=value,
        extended_metadata=value,
        fault_domain=value,
        freeform_tags=value,
        hostname_label=value,
        image_id=value,
        instance_options=value,
        ipxe_script=value,
        is_pv_encryption_in_transit_enabled=value,
        launch_mode=value,
        launch_options=value,
        metadata=value,
        platform_config=value,
        preemptible_instance_config=value,
        shape=value,
        shape_config=value,
        source_details=value,
        subnet_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_instance(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_instance(ctx, instance_id=value)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_update_instance(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.update_instance(
        ctx,
        instance_id=value,
        opc_retry_token=value,
        if_match=value,
        agent_config=value,
        availability_config=value,
        capacity_reservation_id=value,
        defined_tags=value,
        display_name=value,
        extended_metadata=value,
        fault_domain=value,
        freeform_tags=value,
        instance_options=value,
        launch_options=value,
        metadata=value,
        shape=value,
        shape_config=value,
        time_maintenance_reboot_due=value,
        update_operation_constraint=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_instance_action(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.instance_action(
        ctx,
        instance_id=value,
        action=value,
        opc_retry_token=value,
        if_match=value,
        action_type=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_terminate_instance(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.terminate_instance(
        ctx, instance_id=value, if_match=value, preserve_boot_volume=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_accept_shielded_integrity_policy(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.accept_shielded_integrity_policy(
        ctx,
        instance_id=value,
        opc_request_id=value,
        if_match=value,
        opc_retry_token=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_change_instance_compartment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.change_instance_compartment(
        ctx,
        if_match=value,
        instance_id=value,
        opc_request_id=value,
        opc_retry_token=value,
        compartment_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_instance_default_credentials(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_instance_default_credentials(
        ctx, instance_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_instance_devices(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_instance_devices(
        ctx,
        is_available=value,
        instance_id=value,
        limit=value,
        page=value,
        opc_request_id=value,
        sort_by=value,
        sort_order=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_windows_instance_initial_credentials(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_windows_instance_initial_credentials(
        ctx, instance_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_instance_maintenance_reboot(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_instance_maintenance_reboot(
        ctx, instance_id=value, opc_request_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_measured_boot_report(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_measured_boot_report(
        ctx, instance_id=value, opc_request_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_shapes(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_shapes(
        ctx,
        availability_domain=value,
        compartment_id=value,
        limit=value,
        page=value,
        image_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_vnic_attachments(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_vnic_attachments(
        ctx,
        availability_domain=value,
        compartment_id=value,
        instance_id=value,
        limit=value,
        page=value,
        vnic_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_attach_vnic(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.attach_vnic(
        ctx,
        opc_retry_token=value,
        create_vnic_details=value,
        display_name=value,
        instance_id=value,
        nic_index=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_vnic_attachment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_vnic_attachment(ctx, vnic_attachment_id=value)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_detach_vnic(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.detach_vnic(
        ctx, vnic_attachment_id=value, if_match=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_list_volume_attachments(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.list_volume_attachments(
        ctx,
        availability_domain=value,
        compartment_id=value,
        limit=value,
        page=value,
        instance_id=value,
        volume_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_attach_volume(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.attach_volume(
        ctx,
        opc_retry_token=value,
        device=value,
        display_name=value,
        instance_id=value,
        is_read_only=value,
        is_shareable=value,
        type_=value,
        volume_id=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_get_volume_attachment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.get_volume_attachment(
        ctx, volume_attachment_id=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_update_volume_attachment(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.update_volume_attachment(
        ctx,
        volume_attachment_id=value,
        opc_request_id=value,
        if_match=value,
        iscsi_login_state=value,
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations


@pytest.mark.asyncio
async def test_detach_volume(hub, ctx):
    r"""
    **Test function**
    """

    # TODO: replace call param values as necessary
    ret = await hub.tool.oci.compute.detach_volume(
        ctx, volume_attachment_id=value, if_match=value
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    ret["ret"]
    # TODO: Add manual validations
