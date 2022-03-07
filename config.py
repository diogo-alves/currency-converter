# from __future__ import annotations

from functools import lru_cache
from typing import List

from pydantic import BaseSettings
from pydantic.networks import AnyHttpUrl

from enums import CurrencyCode


class Settings(BaseSettings):
    EXCHANGE_RATE_API_KEY: str
    EXCHANGE_RATE_API_URL: str
    EXCHANGE_RATE_API_BASE: str = CurrencyCode.USD
    CORS_ORIGINS: List[AnyHttpUrl] = []

    class Config:
        env_file = '.env'
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
