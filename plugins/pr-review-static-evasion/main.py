"""Static-analysis evasion fixture. This function is never invoked."""

import importlib


def dynamically_resolve_guarded_apis():
    module_name = "sub" + "process"
    member_name = "r" + "un"
    load_module = getattr(importlib, "import_module")
    loaded_module = load_module(module_name)
    getattr(loaded_module, member_name)(["true"])

    builtin_module = __import__("built" + "ins")
    guarded_open = getattr(builtin_module, "o" + "pen")
    return guarded_open
