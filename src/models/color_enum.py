from enum import Enum


class ColorEnum(Enum):
    YELLOW = (16776960, "💡 Nova Ideia")
    RED = (16711680, "🚨 Pendência Urgente")
    BLUE = (255, "📘 Referência/Link")

    def __init__(self, hex_color, title):
        self.hex_color = hex_color
        self.title = title
