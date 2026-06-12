"""Testes para services/webhook_client.py"""
import pytest
import requests as req
from unittest.mock import patch, MagicMock
from services.webhook_client import WebhookDispatcher


class TestWebhookDispatcherSend:
    def test_returns_true_on_204(self, note_yellow, fake_webhook_url):
        mock_response = MagicMock(status_code=204)
        with patch("services.webhook_client.requests.post", return_value=mock_response), \
             patch("services.webhook_client.ConfigManager.get_webhook_url", return_value=fake_webhook_url):
            success, code = WebhookDispatcher.send(note_yellow)
        assert success is True
        assert code is None

    def test_returns_false_on_error_status(self, note_yellow, fake_webhook_url):
        mock_response = MagicMock(status_code=400)
        with patch("services.webhook_client.requests.post", return_value=mock_response), \
             patch("services.webhook_client.ConfigManager.get_webhook_url", return_value=fake_webhook_url):
            success, code = WebhookDispatcher.send(note_yellow)
        assert success is False
        assert code == 400

    def test_returns_correct_status_code_on_failure(self, note_red, fake_webhook_url):
        mock_response = MagicMock(status_code=401)
        with patch("services.webhook_client.requests.post", return_value=mock_response), \
             patch("services.webhook_client.ConfigManager.get_webhook_url", return_value=fake_webhook_url):
            _, code = WebhookDispatcher.send(note_red)
        assert code == 401

    def test_calls_post_with_correct_url(self, note_yellow, fake_webhook_url):
        mock_response = MagicMock(status_code=204)
        with patch("services.webhook_client.requests.post", return_value=mock_response) as mock_post, \
             patch("services.webhook_client.ConfigManager.get_webhook_url", return_value=fake_webhook_url):
            WebhookDispatcher.send(note_yellow)
        mock_post.assert_called_once_with(fake_webhook_url, json=note_yellow.config_json())

    def test_raises_value_error_when_url_missing(self, note_yellow):
        with patch("services.webhook_client.ConfigManager.get_webhook_url",
                   side_effect=ValueError("DISCORD_WEBHOOK_URL não encontrada")):
            with pytest.raises(ValueError):
                WebhookDispatcher.send(note_yellow)

    def test_raises_on_network_error(self, note_blue, fake_webhook_url):
        with patch("services.webhook_client.requests.post",
                   side_effect=req.exceptions.ConnectionError("sem conexão")), \
             patch("services.webhook_client.ConfigManager.get_webhook_url", return_value=fake_webhook_url):
            with pytest.raises(req.exceptions.ConnectionError):
                WebhookDispatcher.send(note_blue)
