# ==============================================================================
# Базовые константы проекта
# ------------------------------------------------------------------------------
# _src/config/const_base.py
# ==============================================================================

# Структура проекта...
# ------------------------------------------------------------------------------
#
# [<Project>]          :: Рабочий каталог проекта
#   │
#   ├── main.py
#   │   ...
#   ├── [config]       :: файлы конфигурации
#   │      ├── ...
#   │      └── ...
#   ├── [ logs ]       :: логи
#   │      ├── ...
#   │      └── ...
#   ├── [ _src ]    :: код проекта
#   │      ├── __init__.py
#  ...    ...
#   │      ├── [config] <--      :: пакет для работы с конфигурацией приложения
#   │      │   ───┬─────
#   │      │      ├── __init__.py
#   │      │      ├── const_base.py    <- this file
#   │      │      │...                 ------------
#   │      │      └── ...
#   │      ├── [logger]          :: пакет логирования
#   │      │      ├── __init__.py
#   │      │      └── ...
#   │      ├── [secur]            :: пакет работы с безопасностью
#   │      │      ├── __init__.py
#   │      │      └── ...
# #  ...    ...
# ------------------------------------------------------------------------------

__all__ = [
    "APP_NAME",
    "APP_DEBUG",
    "WORK_DIR",
    "BASE_DIR",
    "CONF_DIRNAME",
    "CONF_TYPE",
    "CONF_FILENAME",
    "CONF_DIR",
    "BASE_CONF_FILE",
    "DATA_DIRNAME",
    "LOG_DIRNAME",
    "LOG_FILENAME",
    "LOG_TYPE",
    "LOG_DIR",
    "LOG_FILE",
]

from pathlib import Path
from typing import Final, Literal


# Тип конфигурационных файлов
ConfigType = Literal["json", "yaml", "toml"]


# --------------------------------------------------------------------
# Общие параметры приложения...

APP_NAME = "MY_APP"
APP_DEBUG = True

# --------------------------------------------------------------------
# рабоий каталог
WORK_DIR = Path.cwd()
BASE_DIR = str(WORK_DIR)

# имя каталога с файлами конфигураций
CONF_DIRNAME: Final[str] = "configs"

# тип файлов конфигурации по умолчанию
CONF_TYPE: Final[ConfigType] = "json"

# имя базового файла конфигурации
CONF_FILENAME: Final[str] = "_config"

# каталог файлов конфигурации (строковое представление)
CONF_DIR: Final[str] = str(Path.joinpath(WORK_DIR, CONF_DIRNAME))

# полное имя базового файла конфигурации приложения
BASE_CONF_FILE: Final[str] = str(
    Path.joinpath(WORK_DIR, CONF_DIRNAME, CONF_FILENAME).with_suffix(
        f".{CONF_TYPE}"
    )
)

# --------------------------------------------------------------------
# имя каталога с файлами данных
DATA_DIRNAME: Final[str] = "data"

# имя каталога с файлами логов
LOG_DIRNAME: Final[str] = "logs"

# имя основного файла логов
LOG_FILENAME: Final[str] = "app"

# тип основного файла логов (log - текстовый формат- не json)
LOG_TYPE: Final[str] = "log"

# каталог файлов логов (строковое представление)
LOG_DIR: Final[str] = str(Path.joinpath(WORK_DIR, LOG_DIRNAME))

# # полное имя основного файла логов приложения
LOG_FILE: Final[str] = str(
    Path.joinpath(WORK_DIR, LOG_DIRNAME, LOG_FILENAME).with_suffix(
        f".{LOG_TYPE}"
    )
)
