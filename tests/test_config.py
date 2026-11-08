import pytest

from app.config import get_settings


def test_default_settings(monkeypatch):
    monkeypatch.delenv("SERVICEOPS_APP_NAME", raising=False)
    monkeypatch.delenv("SERVICEOPS_LOG_LEVEL", raising=False)

    settings = get_settings()

    assert settings.app_name == "ServiceOps"
    assert settings.log_level == "INFO"


def test_environment_settings(monkeypatch):
    monkeypatch.setenv("SERVICEOPS_APP_NAME", "ServiceOps-Dev")
    monkeypatch.setenv("SERVICEOPS_LOG_LEVEL", "debug")

    settings = get_settings()

    assert settings.app_name == "ServiceOps-Dev"
    assert settings.log_level == "DEBUG"


def test_invalid_log_level(monkeypatch):
    monkeypatch.setenv("SERVICEOPS_LOG_LEVEL", "INVALID")

    with pytest.raises(ValueError, match="Invalid log level"):
        get_settings()
