# ====================================================================
# attributes.py
# ====================================================================

import inspect
import logging
import sys
import types

from collections import namedtuple
from typing import Any, Optional, Generator


NameValue = namedtuple("NameValue", ("name", "value"))


# --------------------------------------------------------------------
class SetAttrError(Exception):
    """Исключение, возникающее при ошибке установки атрибута."""

    pass


# --------------------------------------------------------------------
def _get_caller_module(
    mod_name: Optional[str] = None, depth: int = 2
) -> Optional[types.ModuleType]:
    """Получает модуль вызывающего контекста."""

    if not mod_name:
        frame = inspect.currentframe()
        for _ in range(depth):
            if frame is None:
                return None  # Фрейм не доступен
            frame = frame.f_back
        return inspect.getmodule(frame)
    elif isinstance(mod_name, str) and mod_name in sys.modules:
        return sys.modules[mod_name]
    return None


# --------------------------------------------------------------------
def iterate_module_attributes(
    mod: Optional[types.ModuleType] = None,
) -> Generator[NameValue, None, None]:
    """Итерирует атрибуты модуля, возвращая их имена и значения."""

    if mod is None:
        mod = sys.modules[__name__]
    for name in dir(mod):
        if name.startswith("_"):
            continue
        value = getattr(mod, name)
        if inspect.ismodule(value) or callable(value):
            continue
        yield NameValue(name, value)


# --------------------------------------------------------------------
def set_attribute(
    mod: types.ModuleType, attr_name: str, attr_value: Any
) -> str:
    """Устанавливает атрибут модуля и возвращает его имя."""

    # INFO:
    # ----------------------------------------------------------------
    # Установка и добавление атрибутов в модуль с помощью функции setattr
    # обычно будет успешным, за исключением некоторых случаев, связанных с
    # именами специальных атрибутов или ограничениями, установленными для
    # модуля.
    # В контексте данного проекта исключение SetAttrError скорее всего
    # не возникнет.

    try:
        setattr(mod, attr_name, attr_value)
        return attr_name

    except AttributeError as exception:
        raise SetAttrError(
            f"setattr error: {attr_name}, {attr_value}, {mod.__name__}"
        ) from exception


# --------------------------------------------------------------------
def try_set_attribute(
    mod: types.ModuleType, attr_name: str, attr_value: Any
) -> Optional[str]:

    try:
        attr_name = set_attribute(mod, attr_name, attr_value)
    except SetAttrError as exception:
        logging.error(exception)
        return None

    return attr_name


# --------------------------------------------------------------------
def set_mod_vars(d: dict[str, Any], mod: Optional[types.ModuleType]) -> None:
    """Устанавливает переменные модуля из словаря."""

    if isinstance(mod, types.ModuleType):
        attr_list: list[Optional[str]] = [
            try_set_attribute(mod, k, v) for k, v in d.items()
        ]
        if hasattr(mod, "__all__"):
            mod.__all__.extend(filter(None, attr_list))


# --------------------------------------------------------------------
def set_vars(d: dict[str, Any], mod_name: Optional[str]) -> None:
    """Устанавливает переменные в модуле по имени."""

    mod = _get_caller_module(mod_name)
    set_mod_vars(d, mod)


# --------------------------------------------------------------------
