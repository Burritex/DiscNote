"""
conftest.py
-----------
Fixtures compartilhadas entre todas as suítes de teste do DiscNote.

Este arquivo é carregado automaticamente pelo pytest antes de qualquer teste.
Fixtures definidas aqui ficam disponíveis em tests/models/, tests/services/
e tests/controllers/ sem necessidade de importação explícita.
"""

import sys
import os
import pytest

# Garante que o diretório src/ esteja no path em todos os testes,
# independente de onde o pytest é invocado.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.note_model import Note
from models.color_enum import ColorEnum


# ---------------------------------------------------------------------------
# Fixtures de Note
# ---------------------------------------------------------------------------

@pytest.fixture
def note_yellow():
    """Note padrão com categoria YELLOW (💡 Nova Ideia)."""
    return Note("Estudar webhooks do Discord", ColorEnum.YELLOW)


@pytest.fixture
def note_red():
    """Note com categoria RED (🚨 Pendência Urgente)."""
    return Note("Corrigir bug crítico em produção", ColorEnum.RED)


@pytest.fixture
def note_blue():
    """Note com categoria BLUE (📘 Referência/Link)."""
    return Note("https://discord.com/developers/docs", ColorEnum.BLUE)


@pytest.fixture
def note_empty():
    """Note com valores padrão (conteúdo vazio, cor YELLOW)."""
    return Note()


# ---------------------------------------------------------------------------
# Fixtures de ambiente
# ---------------------------------------------------------------------------

@pytest.fixture
def fake_webhook_url():
    """URL de webhook falsa para testes que precisam de uma URL válida."""
    return "https://discord.com/api/webhooks/000000000/fake-token"


@pytest.fixture
def env_with_webhook(fake_webhook_url, monkeypatch):
    """
    Injeta DISCORD_WEBHOOK_URL no ambiente para testes do ConfigManager
    e WebhookDispatcher sem precisar de um arquivo .env real.
    """
    monkeypatch.setenv("DISCORD_WEBHOOK_URL", fake_webhook_url)


@pytest.fixture
def env_without_webhook(monkeypatch):
    """Remove DISCORD_WEBHOOK_URL do ambiente para testar ausência da variável."""
    monkeypatch.delenv("DISCORD_WEBHOOK_URL", raising=False)
