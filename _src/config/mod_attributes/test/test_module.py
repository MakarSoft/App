import types
from typing import Optional

from .. import (
    _get_caller_module,
    log_function_call,
    log_call_info,
    log_call_stack_info,
)


def test_get_caller_module(
    mod_name: Optional[str] = None,
) -> Optional[types.ModuleType]:

    mod = _get_caller_module(mod_name)
    return mod


def test_log_function_call():
    log_function_call()


def test_log_call_stack_info():
    log_call_stack_info()


@log_call_info
def test_decorator():
    print("Inside my_function")


a = 0
b = 1
x = 100
y = 200
z = 300
