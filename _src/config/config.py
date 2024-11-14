# ====================================================================
# Загрузка конфигурации приложения
# --------------------------------------------------------------------
#  project/config/config.py
# ====================================================================

__all__ = []

import json
import sys
from typing import Any

from project.config import APP_NAME

from project.logger import  * 
from project.logger.logger_config import get_logger, get_logger_config
from project.logger.logger_dict_config import LOG_CONFIG
from project.logger.formatter_const import LOG_FORMAT, LOG_LEVEL_FORMAT, FORMAT_STYLE
from project.logger.formatter import get_now_str

from pydantic import HttpUrl, ValidationError
from uuid import UUID
from project.config import set_var
from project.config.model_base import BaseConfig
from project.config.model_pam import PamConfig, AAPMToken, Account

from project.tools.files import load_file, write_file

logger =  get_logger_config()


# ====================================================================

# --------------------------------------------------------------------
# -=    Общая конфигурация приложения    =-

try:
    logger.debug("=== Получение конфигурации приложения ===")

    config_model = BaseConfig()
    set_var(config_model.model_dump())
except ValidationError as ex:
    msg = "Ошибка общей конфигурации приложения"
    logger.error(f"{msg}: {ex}")
    raise ValueError(f"{msg}")

        
# -= END общей конфигурации =-
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# -=    Конфигурация PAM    =-
try:
    logger.debug("Получение конфигурации PAM - сервиса ...")
    pam_model = PamConfig()
    set_var(pam_model.model_dump())
except ValidationError as ex:
    msg = "Ошибка конфигурации сервиса PAM"
    logger.error(f"{msg}: {ex}")
    raise ValueError(f"{msg}")


base_url: HttpUrl = pam_model.pam_url.base_url

aapm_password: str = pam_model.pam_url.aapm_password
aapm_password_url: HttpUrl = pam_model.pam_url.aapm_password_url
aapm_list: str = pam_model.pam_url.aapm_list
aapm_list_url: HttpUrl = pam_model.pam_url.aapm_list_url

accounts: dict[str, Account] = pam_model.accounts.accounts
cmdb_rest: Account = pam_model.accounts.accounts['cmdb_rest']
cmdb_rest_post: Account = pam_model.accounts.accounts['cmdb_rest_post']
san_rest: Account = pam_model.accounts.accounts['san_rest']

token: UUID = pam_model.token.token

# <DEBUG...
mod = sys.modules[__name__]
# print(mod.__dict__)
# ...DEBUG>

# -=  END Конфигурации PAM  =-
# --------------------------------------------------------------------

logger.debug("=== Конфигурация приложения получена ===")


