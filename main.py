from _src.config import *

import _src.config.mod_attributes

from _src.config.mod_attributes import set_vars

import _src.config.mod_attributes.test as t

from _src.config.mod_attributes.test import (
    test_get_caller_module,
    test_log_function_call,
    test_log_call_stack_info,
    test_decorator,
)

import sys


# ====================================================================

mod = test_get_caller_module()
print(mod.__name__ if mod else "None")

mod = test_get_caller_module("_src.config.mod_attributes.test")
print(mod.__name__ if mod else "None")

mod = sys.modules["_src.config.mod_attributes.test"]
print(mod.__name__ if mod else "None")

test_log_function_call()
test_decorator()
test_log_call_stack_info()

attrs_dict = {
    "d": {
        "qqq": "1111",
        "www": "2222",
        "eee": "3333",
    },
    "l": [1, 2, 3, 4, 5],
    "x": 11,
    "y": 22,
    "z": 33,
}

set_vars(attrs_dict, "_src.config.mod_attributes.test")

print(
    t.x,
    t.y,
    t.z,
    t.d,
    t.l,
    sep="\n",
)
