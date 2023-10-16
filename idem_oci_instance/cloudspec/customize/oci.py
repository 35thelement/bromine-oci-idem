def run(hub, ctx):
    """
    Use this plugin to customize cloud spec

    ctx.cloud_spec(NamespaceDict):
        The generated cloud_spec from a source in the following format:

        {
            "project_name": "",
            "service_name": "",
            "api_version": "latest",
            "request_format": "",
            "plugins": {
                plugin_name: {
                    "imports": [],
                    "virtual_imports": [],
                    "func_alias": {},
                    "virtualname": "",
                    "doc": "docstring",
                    "functions": {
                        "function_name": {
                            "doc": "",
                            "return_type": "",
                            "hardcoded": {},
                            "params": {
                                "param_name": {
                                    "doc": "Docstring for this parameter",
                                    "param_type": "Type",
                                    "required": True|False,
                                    "default": "",
                                    "target": "",
                                    "target_type": "mapping|value|arg|kwargs"
                                    "member": {
                                        "name": "param_type_name",
                                        "params": {
                                            "nested_param1_name": CloudSpecParam,
                                            "nested_param2_name": CloudSpecParam,
                                            ...
                                        }
                                    },
                                },
                            }
                        },
                    }
                },
            }
        }
    """

    if ctx.cloud_spec.get("plugins", {}).get("compute", {}).get:
        compute_plugin_functions = ctx.cloud_spec["plugins"]["compute"]["functions"]
        if compute_plugin_functions.get("get_instance"):
            compute_plugin_functions["get"] = compute_plugin_functions["get_instance"]
        if compute_plugin_functions.get("list_instances"):
            compute_plugin_functions["list"] = compute_plugin_functions[
                "list_instances"
            ]
        if compute_plugin_functions.get("launch_instance"):
            compute_plugin_functions["create"] = compute_plugin_functions[
                "launch_instance"
            ]
            compute_plugin_functions["present"] = compute_plugin_functions[
                "launch_instance"
            ]
        if compute_plugin_functions.get("update_instance"):
            compute_plugin_functions["update"] = compute_plugin_functions[
                "update_instance"
            ]
        if compute_plugin_functions.get("terminate_instance"):
            compute_plugin_functions["delete"] = compute_plugin_functions[
                "terminate_instance"
            ]
            compute_plugin_functions["absent"] = compute_plugin_functions[
                "terminate_instance"
            ]
