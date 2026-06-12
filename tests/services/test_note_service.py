"""Testes para services/note_service.py"""

import pytest
from unittest.mock import patch
from services.note_service import NoteService
from models.note_model import Note


class TestNoteServiceFromConsole:
    def test_returns_note_instance(self):
        with patch("builtins.input", return_value="Minha nota válida"):
            result = NoteService.from_console()
        assert isinstance(result, Note)

    def test_content_is_capitalized(self):
        with patch("builtins.input", return_value="minha nota"):
            result = NoteService.from_console()
        assert result.content == "Minha nota"

    def test_content_is_stripped(self):
        with patch("builtins.input", return_value="  nota com espaços  "):
            result = NoteService.from_console()
        assert result.content == result.content.strip()

    def test_retries_when_input_too_short(self):
        # Primeira entrada inválida, segunda válida
        inputs = iter(["ab", "nota válida agora"])
        with patch("builtins.input", side_effect=lambda _: next(inputs)):
            result = NoteService.from_console()
        assert len(result.content) >= 3

    def test_retries_when_input_is_empty(self):
        inputs = iter(["", "nota ok"])
        with patch("builtins.input", side_effect=lambda _: next(inputs)):
            result = NoteService.from_console()
        assert result.content != ""

    def test_minimum_length_accepted(self):
        with patch("builtins.input", return_value="abc"):
            result = NoteService.from_console()
        assert len(result.content) >= 3


class TestNoteServiceFromFile:
    def test_raises_not_implemented(self):
        with pytest.raises(NotImplementedError):
            NoteService.from_file("qualquer/caminho.txt")
