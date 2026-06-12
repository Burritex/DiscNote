"""
    color_enum.py
    -------------
    Define os tipos de nota disponíveis no DiscNote através de um Enum.
    
    Cada membro do Enum representa uma categoria visual de nota, carregando
    o código de cor decimal (compatível com a API do Discord) e o título
    que será exibido no embed.
    
    Exemplos de uso:
        >>> from models.color_enum import ColorEnum
        >>> cor = ColorEnum.YELLOW
        >>> cor.hex_color
        16776960
        >>> cor.title
        '💡 Nova Ideia'
"""

from enum import Enum


class ColorEnum(Enum):
    """
        Enum de categorias de nota para embeds do Discord.
    
        Membros:
            YELLOW: Nota de ideia geral (amarelo).
            RED:    Pendência urgente (vermelho).
            BLUE:   Referência ou link (azul).
    
        Atributos de cada membro:
            hex_color (int): Cor decimal usada no campo ``color`` do embed do Discord.
            title     (str): Título exibido no topo do embed, incluindo emoji.
    """
    YELLOW = (16776960, "💡 Nova Ideia")
    RED = (16711680, "🚨 Pendência Urgente")
    BLUE = (255, "📘 Referência/Link")

    def __init__(self, hex_color, title):
        self.hex_color = hex_color
        self.title = title
