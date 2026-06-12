"""Testes para services/config_manager.py"""
import pytest
from services.config_manager import ConfigManager


class TestConfigManager:
    def test_returns_url_when_set(self, env_with_webhook, fake_webhook_url):
        assert ConfigManager.get_webhook_url() == fake_webhook_url

    def test_raises_when_url_missing(self, env_without_webhook):
        with pytest.raises(ValueError, match="DISCORD_WEBHOOK_URL"):
            ConfigManager.get_webhook_url()

    def test_raises_when_url_empty_string(self, monkeypatch):
        monkeypatch.setenv("DISCORD_WEBHOOK_URL", "")
        with pytest.raises(ValueError):
            ConfigManager.get_webhook_url()

    def test_error_message_is_descriptive(self, env_without_webhook):
        with pytest.raises(ValueError) as exc_info:
            ConfigManager.get_webhook_url()
        assert "DISCORD_WEBHOOK_URL" in str(exc_info.value)
