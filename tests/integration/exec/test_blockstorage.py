
"""Tests for validating Blockstorages. """

import pytest







PARAMETER = {'name': 'idem-test-resource- + TODO: Add unique identifier generator'}


@pytest.mark.asyncio

async def test_create(hub, ctx):
    r'''
    **Test function**
    '''


    # Test - create new resource
    global PARAMETER
    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.blockstorage.create(
        ctx,
        name=PARAMETER["name"],)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    assert resource
    PARAMETER["resource_id"] = resource.get("resource_id", None)
    assert PARAMETER["resource_id"]
    # TODO: Add manual validations

    # Now get the resource
    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.blockstorage.get(
        ctx,
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],)
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    assert resource
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_get(hub, ctx):
    r'''
    **Test function**
    '''


    # Test - Invalid/Not-Found resource lookup
    global PARAMETER
    assert PARAMETER.get("resource_id", None), "The resource might not have been created"

    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.blockstorage.get(
        ctx,
        name=PARAMETER["name"],
        resource_id="invalid_resource_id",)
    assert ret
    assert ret["result"], ret["comment"]
    assert ret["ret"] is None
    assert "result is empty" in str(ret["comment"])

    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.blockstorage.get(
        ctx,
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],)
    assert ret
    assert ret["result"], ret["comment"]
    assert ret["ret"]
    resource = ret["ret"]
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_list(hub, ctx):
    r'''
    **Test function**
    '''


    # TODO: replace call param values as necessary
    global PARAMETER
    ret = await hub.exec.oci.blockstorage.list(
        ctx,)
    assert ret
    assert ret["result"], ret["comment"]
    assert ret["ret"]
    for resource in ret["ret"]:
        assert resource
        # TODO: Add manual validations



@pytest.mark.asyncio

async def test_update(hub, ctx):
    r'''
    **Test function**
    '''


    # Test - Update existing resource
    global PARAMETER

    assert PARAMETER.get("resource_id", None), "The resource might not have been created"

    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.blockstorage.update(
        ctx,
        # TODO: replace call param values as necessary
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],)
    assert ret
    assert ret["result"], ret["comment"]
    assert ret["ret"]
    resource = ret["ret"]
    assert resource
    # TODO: Add manual validations

    # Now get the resource
    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.blockstorage.get(
        ctx,
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],)
    assert ret
    assert ret["result"], ret["comment"]
    assert ret["ret"]
    resource = ret["ret"]
    assert resource
    # TODO: Add manual validations



@pytest.mark.asyncio

async def test_delete(hub, ctx):
    r'''
    **Test function**
    '''


    # Test - Delete existing resource
    global PARAMETER
    assert PARAMETER.get("resource_id", None), "The resource might not have been created"

    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.blockstorage.delete(
        ctx,
        name="",
        resource_id=PARAMETER["resource_id"],)
    assert ret
    assert ret["result"], ret["comment"]
    assert not ret["ret"]

    # Now get the resource
    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.blockstorage.get(
        ctx,
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],)
    assert ret
    assert ret["result"], ret["comment"]
    assert ret["ret"] is None
    assert "result is empty" in str(ret["comment"])


