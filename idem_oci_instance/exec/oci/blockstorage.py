"""Exec module for managing Blockstorages. """
from typing import Any
from typing import Dict

__contracts__ = ["soft_fail"]

__func_alias__ = {"list_": "list"}


async def get(hub, ctx) -> Dict[str, Any]:
    """

    Returns:
        Dict[str, Any]

    Examples:
        Resource State:

        .. code-block:: sls

            unmanaged_resource:
              exec.run:
                - path: oci.blockstorage.get
                - kwargs:


        Exec call from the CLI:

        .. code-block:: bash

            idem exec oci.blockstorage.get
    """

    result = dict(comment=[], ret=None, result=True)

    # TODO: Change function methods params if needed
    get = await hub.tool.oci.session.request(
        ctx,
        method="TODO",
        path="TODO".format(**{}),
        query_params={},
        data={},
        headers={},
    )

    if not get["result"]:
        # Send empty result for not found
        if get["status"] == 404:
            result["comment"].append(f"Get '{name}' result is empty")
            return result

        result["comment"].append(get["comment"])
        result["result"] = False
        return result

    # Case: Empty results
    if not get["ret"]:
        result["comment"].append(f"Get '{name}' result is empty")
        return result

    # TODO: Make sure resource_id is mapped in get response
    get["ret"]["resource_id"] = resource_id
    result["ret"] = get["ret"]

    return result


async def list_(hub, ctx) -> Dict[str, Any]:
    """

    Returns:
        Dict[str, Any]

    Examples:

        Resource State:

        .. code-block:: sls

            unmanaged_resources:
              exec.run:
                - path: oci.blockstorage.list
                - kwargs:


        Exec call from the CLI:

        .. code-block:: bash

            idem exec oci.blockstorage.list

        Describe call from the CLI:

        .. code-block:: bash

            $ idem describe oci.blockstorage

    """

    result = dict(comment=[], ret=[], result=True)

    # TODO: Change function methods params if needed
    list = await hub.tool.oci.session.request(
        ctx,
        method="TODO",
        path="TODO",
        query_params={},
        data={},
        headers={},
    )

    if not list["result"]:
        result["comment"].append(list["comment"])
        result["result"] = False
        return result

    for resource in list["ret"]:

        # TODO: Map resource_id from response
        resource["resource_id"] = ""
        result["ret"].append(resource)

    return result


async def create(hub, ctx) -> Dict[str, Any]:
    """

    Returns:
        Dict[str, Any]

    Examples:
        Using in a state:

        .. code-block:: sls

            resource_is_present:
              oci.blockstorage.present:
                -

        Exec call from the CLI:

        .. code-block:: bash

            idem exec oci.blockstorage.create
    """

    result = dict(comment=[], ret=[], result=True)

    desired_state = {
        k: v
        for k, v in locals().items()
        if k not in ("hub", "ctx", "result") and v is not None
    }

    # TODO: Change request param mapping as necessary
    resource_to_raw_input_mapping = {}

    payload = {}
    for key, value in desired_state.items():
        if key in resource_to_raw_input_mapping.keys() and value is not None:
            payload[resource_to_raw_input_mapping[key]] = value

    create = await hub.tool.oci.session.request(
        ctx,
        method="TODO",
        path="TODO",
        query_params={},
        data=payload,
        headers={},
    )

    if not create["result"]:
        result["comment"].append(create["comment"])
        result["result"] = False
        return result

    result["comment"].append(
        f"Created oci.blockstorage '{name}'",
    )

    result["ret"] = create["ret"]
    # TODO: add "resource_id" to returned response by mapping to correct resource identifier
    return result


async def update(hub, ctx) -> Dict[str, Any]:
    """

    Returns:
        Dict[str, Any]

    Examples:
        Using in a state:

        .. code-block:: sls

            resource_is_present:
              oci.blockstorage.present:
                -

        Exec call from the CLI:

        .. code-block:: bash

            idem exec oci.blockstorage.update
    """

    result = dict(comment=[], ret=[], result=True)

    desired_state = {
        k: v
        for k, v in locals().items()
        if k not in ("hub", "ctx", "result") and v is not None
    }

    # TODO: Change request param mapping as necessary
    resource_to_raw_input_mapping = {}

    payload = {}
    for key, value in desired_state.items():
        if key in resource_to_raw_input_mapping.keys() and value is not None:
            payload[resource_to_raw_input_mapping[key]] = value

    if payload:
        update = await hub.tool.oci.session.request(
            ctx,
            method="TODO",
            path="TODO".format(**{}),
            query_params={},
            data=payload,
            headers={},
        )

        if not update["result"]:
            result["comment"].append(update["comment"])
            result["result"] = False
            return result

        result["ret"] = update["ret"]
        result["comment"].append(
            f"Updated oci.blockstorage '{name}'",
        )

    return result


async def delete(hub, ctx) -> Dict[str, Any]:
    """

    Returns:
        Dict[str, Any]

    Examples:
        Resource State:

        .. code-block:: sls

            resource_is_absent:
              oci.blockstorage.absent:
                -

        Exec call from the CLI:

        .. code-block:: bash

            idem exec oci.blockstorage.delete
    """

    result = dict(comment=[], ret=[], result=True)

    delete = await hub.tool.oci.session.request(
        ctx,
        method="TODO",
        path="TODO".format(**{}),
        query_params={},
        data={},
        headers={},
    )

    if not delete["result"]:
        result["comment"].append(delete["comment"])
        result["result"] = False
        return result

    result["comment"].append(f"Deleted '{name}'")
    return result
