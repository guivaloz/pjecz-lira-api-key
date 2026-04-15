"""
Settings
"""

import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings"""

    DB_HOST: str = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_NAME: str = os.getenv("DB_NAME", "pjecz_lira")
    DB_PASS: str = os.getenv("DB_PASS", "")
    DB_USER: str = os.getenv("DB_USER", "")
    FERNET_KEY: str = os.getenv("FERNET_KEY", "")
    ORIGINS: str = os.getenv("ORIGINS", "http://127.0.0.1:3000")
    SALT: str = os.getenv("SALT", "")
    TZ: str = os.getenv("TZ", "America/Mexico_City")

    class Config:
        """Load configuration"""

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            """Customise sources, first environment variables, then .env file, then google cloud secret manager"""
            return env_settings, file_secret_settings, init_settings


@lru_cache()
def get_settings() -> Settings:
    """Get Settings"""
    return Settings()
