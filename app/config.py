import os

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str
    log_level: str


def get_settings() -> Settings:
    app_name = os.getenv("SERVICEOPS_APP_NAME", "ServiceOps")
    log_level = os.getenv("SERVICEOPS_LOG_LEVEL", "INFO").upper()

    allowed_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

    if log_level not in allowed_levels:
        raise ValueError(f"Invalid log level: {log_level}")

    return Settings(
        app_name=app_name,
        log_level=log_level,
    )
