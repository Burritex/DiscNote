"""Testes para controllers/bot_controller.py"""
import pytest
from unittest.mock import patch
from controllers.bot_controller import BotController


class TestBotControllerRunConsoleToDiscord:
    def test_prints_success_message_on_success(self, note_yellow, capsys):
        with patch("controllers.bot_controller.NoteService.from_console", return_value=note_yellow), \
             patch("controllers.bot_controller.WebhookDispatcher.send", return_value=(True, None)):
            BotController.run_console_to_discord()
        assert "sucesso" in capsys.readouterr().out.lower()

    def test_prints_failure_message_on_failure(self, note_yellow, capsys):
        with patch("controllers.bot_controller.NoteService.from_console", return_value=note_yellow), \
             patch("controllers.bot_controller.WebhookDispatcher.send", return_value=(False, 400)):
            BotController.run_console_to_discord()
        assert "falha" in capsys.readouterr().out.lower()

    def test_failure_message_includes_status_code(self, note_yellow, capsys):
        with patch("controllers.bot_controller.NoteService.from_console", return_value=note_yellow), \
             patch("controllers.bot_controller.WebhookDispatcher.send", return_value=(False, 403)):
            BotController.run_console_to_discord()
        assert "403" in capsys.readouterr().out

    def test_calls_note_service(self, note_yellow):
        with patch("controllers.bot_controller.NoteService.from_console",
                   return_value=note_yellow) as mock_service, \
             patch("controllers.bot_controller.WebhookDispatcher.send", return_value=(True, None)):
            BotController.run_console_to_discord()
        mock_service.assert_called_once()

    def test_calls_webhook_dispatcher_with_note(self, note_yellow):
        with patch("controllers.bot_controller.NoteService.from_console", return_value=note_yellow), \
             patch("controllers.bot_controller.WebhookDispatcher.send",
                   return_value=(True, None)) as mock_send:
            BotController.run_console_to_discord()
        mock_send.assert_called_once_with(note_yellow)


class TestBotControllerRunFileToDiscord:
    def test_raises_not_implemented(self):
        with pytest.raises(NotImplementedError):
            BotController.run_file_to_discord()
