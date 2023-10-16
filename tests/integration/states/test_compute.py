"""Tests for validating Computes. """
import pytest


PARAMETRIZE = {
    "argnames": "__test",
    "argvalues": [True, False],
    "ids": ["--test", "run"],
}

PARAMETER = {"name": "idem-test-resource- + TODO: Add unique identifier generator"}


@pytest.mark.asyncio
async def test_describe(hub, ctx):
    r"""
    **Test function**
    """

    global PARAMETER
    assert PARAMETER.get(
        "resource_id", None
    ), "The resource might not have been created"
    # TODO: replace call param values as necessary
    ret = await hub.states.oci.compute.describe(
        ctx,
    )
    resource_id = PARAMETER["resource_id"]
    assert resource_id in ret
    assert "oci.compute.present" in ret[resource_id]
    described_resource = ret[resource_id].get("oci.compute.present")
    # TODO: Add manual verification as necessary


@pytest.mark.asyncio
@pytest.mark.parametrize(**PARAMETRIZE)
async def test_present(hub, ctx, __test):
    r"""
    **Test function**
    """

    global PARAMETER
    ctx["test"] = __test
    # Create the resource
    # TODO: replace call param values as necessary
    ret = await hub.states.oci.compute.present(
        ctx,
        name=PARAMETER["name"],
    )
    assert ret["result"], ret["comment"]
    resource = ret["new_state"]
    if __test:
        assert f"Would create oci.compute: {PARAMETER['name']}" in ret["comment"]
    else:
        assert f"Created oci.compute: {PARAMETER['name']}" in ret["comment"]

    PARAMETER["resource_id"] = resource["resource_id"]
    assert not ret["old_state"] and ret["new_state"]
    assert PARAMETER["name"] == resource.get("name")

    # Now get the resource with exec
    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.compute.get(
        ctx,
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],
    )
    assert ret
    assert ret["result"], ret["comment"]
    assert ret["ret"]
    resource = ret["ret"]
    assert PARAMETER["name"] == resource.get("name")
    # TODO: Add manual verification as necessary

    # Now Update the resource
    # TODO: update resource attributes
    # TODO: replace call param values as necessary
    ret = await hub.states.oci.compute.present(
        ctx,
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],
    )

    if __test:
        assert f"Would update oci.compute: {PARAMETER['name']}" in ret["comment"]
    else:
        assert f"Updated oci.compute: {PARAMETER['name']}" in ret["comment"]
        assert ret["result"], ret["comment"]

    assert ret.get("old_state") and ret.get("new_state")
    resource = ret["new_state"]
    # TODO: Add manual verification as necessary

    # Now get the resource with exec again
    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.compute.get(
        ctx,
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],
    )
    assert ret
    assert ret["result"]
    assert ret["ret"]
    resource = ret["ret"]
    assert PARAMETER["name"] == resource.get("name")
    # TODO: Add manual verification as necessary


@pytest.mark.asyncio
@pytest.mark.parametrize(**PARAMETRIZE)
async def test_absent(hub, ctx, __test):
    r"""
    **Test function**
    """

    global PARAMETER
    assert PARAMETER.get(
        "resource_id", None
    ), "The resource might not have been created"
    ctx["test"] = __test
    # Delete the resource
    # TODO: replace call param values as necessary
    ret = await hub.states.oci.compute.absent(
        ctx,
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],
    )

    if __test:
        assert f"Would delete oci.compute: {PARAMETER['name']}" in ret["comment"]
    else:
        assert f"Deleted oci.compute: {PARAMETER['name']}" in ret["comment"]

    assert ret["result"], ret["comment"]
    assert ret.get("old_state") and not ret.get("new_state")
    ret.get("old_state")

    # Now get the resource with exec - Should not exist
    # TODO: replace call param values as necessary
    ret = await hub.exec.oci.compute.get(
        ctx,
        name=PARAMETER["name"],
        resource_id=PARAMETER["resource_id"],
    )
    assert ret
    assert ret["result"], ret["comment"]
    assert ret["ret"] is None
    assert "result is empty" in str(ret["comment"])

    # Try deleting the resource again
    # TODO: replace call param values as necessary
    ret = await hub.states.oci.compute.absent(
        ctx,
        name=PARAMETER["name"],
    )

    assert f"oci.compute: {PARAMETER['name']} already absent" in ret["comment"]
    assert ret["result"], ret["comment"]
    assert (not ret["old_state"]) and (not ret["new_state"])
    if not __test:
        PARAMETER.pop("resource_id")
