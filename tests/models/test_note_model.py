"""Testes para models/note_model.py"""
import re
import pytest
from unittest.mock import patch
from models.note_model import Note
from models.color_enum import ColorEnum


class TestNoteInit:
    def test_default_content_is_empty(self, note_empty):
        assert note_empty.content == ""

    def test_default_color_is_yellow(self, note_empty):
        assert note_empty.color_option == ColorEnum.YELLOW

    def test_custom_content(self, note_yellow):
        assert note_yellow.content == "Estudar webhooks do Discord"

    def test_custom_color_red(self, note_red):
        assert note_red.color_option == ColorEnum.RED

    def test_custom_color_blue(self, note_blue):
        assert note_blue.color_option == ColorEnum.BLUE


class TestNoteProperties:
    def test_content_setter(self, note_empty):
        note_empty.content = "Novo conteúdo"
        assert note_empty.content == "Novo conteúdo"

    def test_color_setter(self, note_empty):
        note_empty.color_option = ColorEnum.BLUE
        assert note_empty.color_option == ColorEnum.BLUE


class TestNoteConfigJson:
    def test_returns_dict(self, note_yellow):
        assert isinstance(note_yellow.config_json(), dict)

    def test_embeds_key_exists(self, note_yellow):
        assert "embeds" in note_yellow.config_json()

    def test_embed_title_matches_color(self, note_red):
        payload = note_red.config_json()
        assert payload["embeds"][0]["title"] == ColorEnum.RED.title

    def test_embed_description_matches_content(self, note_blue):
        payload = note_blue.config_json()
        assert payload["embeds"][0]["description"] == note_blue.content

    def test_embed_color_matches_enum(self, note_yellow):
        payload = note_yellow.config_json()
        assert payload["embeds"][0]["color"] == ColorEnum.YELLOW.hex_color

    def test_embed_footer_contains_date(self, note_yellow):
        with patch.object(note_yellow, '_get_date', return_value="01/01/2025 12:00"):
            payload = note_yellow.config_json()
        assert "01/01/2025 12:00" in payload["embeds"][0]["footer"]["text"]

    def test_get_date_format(self, note_empty):
        assert re.match(r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}", note_empty._get_date())
