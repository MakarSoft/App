# ==============================================================================
# Модель базовой конфигурации
# ------------------------------------------------------------------------------
# _src/config/model_base.py
# ==============================================================================

from pydantic import (
    BaseModel,
    Field
)

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)

# Для дефолтовых значений модели...
from . import *
# (
#     WORK_DIR,
#     BASE_DIR,

#     CONF_DIRNAME,
#     CONF_TYPE,
#     CONF_FILENAME,
#     CONF_DIR,
#     BASE_CONF_FILE,

#     LOG_DIRNAME,
#     LOG_FILENAME,
#     LOG_TYPE,
#     LOG_DIR,
#     LOG_FILE,
#     DATA_DIRNAME
# )


# --------------------------------------------------------------------
# --------------------------------------------------------------------
class BaseConfig(BaseSettings):

    model_config = SettingsConfigDict(
        env_file = '.env',
        env_file_encoding = 'utf-8',
        case_sensitive=False,
        extra='ignore',
    )

    app_name: str = Field(..., env='APP_NAME')
    app_ver: str = Field(..., env='APP_VER')
    app_debug: bool = Field(..., env='APP_DEBUG')

    conf_dirname: str = Field(
        default=CONF_DIRNAME,
        env='CONF_DIRNAME'
    )

    conf_filename: str = Field(
        default=CONF_FILENAME,
        env='CONF_FILENAME'
    )

    conf_filename_suffix: str = Field(
        default=CONF_TYPE,
        env='CONF_TYPE'
    )

    log_dirname: str = Field(
        default=LOG_DIRNAME,
        env='LOG_DIRNAME'
    )

    log_filename: str = Field(
        default=LOG_FILENAME,
        env='LOG_FILENAME'
    )

    log_filename_suffix: str = Field(
        default=LOG_TYPE,
        env='LOG_TYPE'
    )

    data_dirname: str = Field(
        default=DATA_DIRNAME,
        env='LOG_DIRNAME'
    )
