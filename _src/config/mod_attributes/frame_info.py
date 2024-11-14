# ====================================================================
# frame_info.py
# ====================================================================

import inspect
import functools
import logging

from typing import Callable, ParamSpec, TypeVar


Param = ParamSpec("Param")
RetType = TypeVar("RetType")


# --------------------------------------------------------------
def log_call_info(func: Callable[Param, RetType]) -> Callable[Param, RetType]:

    @functools.wraps(func)
    def wrapper(*args: Param.args, **kwargs: Param.kwargs) -> RetType:

        frame = inspect.currentframe()
        if frame is not None and frame.f_back is not None:
            frame_info = inspect.getframeinfo(frame.f_back)
            logging.warning(
                "Calling {} from {} in {} at line {}".format(
                    {func.__name__},
                    {frame_info.function},
                    {frame_info.filename},
                    {frame_info.lineno},
                )
            )
        else:
            logging.warning(f"Calling {func.__name__} from an unknown context")

        return func(*args, **kwargs)

    return wrapper


# --------------------------------------------------------------------
def log_call_stack_info() -> None:

    stack = inspect.stack()
    for frame_info in stack:
        info = inspect.getframeinfo(frame_info.frame)
        logging.warning(
            "Function: {}, File: {}, Line: {}".format(
                info.function, info.filename, info.lineno
            )
        )


# --------------------------------------------------------------------
def log_function_call() -> None:
    frame = inspect.currentframe()
    if frame is None:
        logging.warning("log_function_call: Unknown context")
    else:
        frame_info = inspect.getframeinfo(frame)
        logging.warning(
            "log_function_call: Function called - {}"
            " in {} at line {}".format(
                frame_info.function, frame_info.filename, frame_info.lineno
            )
        )


# --------------------------------------------------------------------
