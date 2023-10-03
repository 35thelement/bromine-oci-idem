
"""States module for managing Computes. """

from typing import Any
from typing import Dict
from typing import List
from collections import OrderedDict
from dataclasses import field
from dataclasses import make_dataclass
import dict_tools.differ as differ

__contracts__ = ['resource']




async def present(
    hub,
    ctx
,
) -> Dict[str, Any]:
    '''

    Returns:
        Dict[str, Any]

    Example:
        .. code-block:: sls


          idem_test_oci.compute_is_present:
              oci.oci.compute.present: []


    '''


    result = dict(
            comment=[], old_state={}, new_state={}, name=name, result=True, rerun_data=None
        )

    desired_state = {
        k: v
        for k, v in locals().items()
        if k not in ("hub", "ctx", "kwargs", "result") and v is not None
    }

    if resource_id:
        # Possible parameters: **{}
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
                    enforced_state={},
                    desired_state=desired_state
                )
                result["comment"].append(f"Would update oci.compute: {name}")
                return result
            else:
                # Update the resource
                update_ret = await hub.exec.oci.compute.update(
                    ctx,
                    **{}
                )
                result["result"] = update_ret["result"]

                if result["result"]:
                    result["comment"].append(f"Updated 'oci.compute: {name}'")
                else:
                    result["comment"].append(update_ret["comment"])
    else:
        if ctx.test:
            result["new_state"] = hub.tool.oci.test_state_utils.generate_test_state(
                enforced_state={},
                desired_state=desired_state
            )
            result["comment"] = (f"Would create oci.compute: {name}",)
            return result
        else:
            create_ret = await hub.exec.oci.compute.create(
                ctx,
                **{}
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

    # Possible parameters: **{}
    after = await hub.exec.oci.compute.get(
        ctx,
        name=name,
        resource_id=resource_id,
    )
    result["new_state"] = after.ret
    return result



async def absent(
    hub,
    ctx
,
)  -> Dict[str, Any]:
    '''
    

    Returns:
        Dict[str, Any]

    Example:
        .. code-block:: sls


            idem_test_oci.compute_is_absent:
              oci.oci.compute.absent: []


    '''


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
    '''
    Describe the resource in a way that can be recreated/managed with the corresponding "present" function

    

    Returns:
        Dict[str, Any]

    Example:

        .. code-block:: bash

            $ idem describe oci.compute
    '''


    result = {}

    # TODO: Add other required parameters from: {}
    ret = await hub.exec.oci.compute.list(
        ctx
    )

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


