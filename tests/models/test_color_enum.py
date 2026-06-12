"""Testes para models/color_enum.py"""

import pytest
from models.color_enum import ColorEnum


class TestColorEnum:
    def test_yellow_hex_color(self):
        assert ColorEnum.YELLOW.hex_color == 16776960

    def test_yellow_title(self):
        assert ColorEnum.YELLOW.title == "💡 Nova Ideia"

    def test_red_hex_color(self):
        assert ColorEnum.RED.hex_color == 16711680

    def test_red_title(self):
        assert ColorEnum.RED.title == "🚨 Pendência Urgente"

    def test_blue_hex_color(self):
        assert ColorEnum.BLUE.hex_color == 255

    def test_blue_title(self):
        assert ColorEnum.BLUE.title == "📘 Referência/Link"

    def test_all_members_exist(self):
        members = [e.name for e in ColorEnum]
        assert "YELLOW" in members
        assert "RED" in members
        assert "BLUE" in members

    def test_members_are_unique(self):
        colors = [e.hex_color for e in ColorEnum]
        assert len(colors) == len(set(colors))
