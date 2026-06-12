from datetime import datetime
from models import ColorEnum


class Note:
    def __init__(self, content: str = "", color_option: ColorEnum = ColorEnum.YELLOW):
        self._content = content
        self._color_option = color_option
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value: str):
        self._content = value

    @property
    def color_option(self):
        return self._color_option
    
    @color_option.setter
    def color_option(self, value: ColorEnum):
        self._color_option = value

    def _get_date(self) -> str:
        return datetime.now().strftime("%d/%m/%Y %H:%M")
    
    def config_json(self):
        return {
            "embeds": [{
                "title": self.color_option.title,  # Pega direto do Enum
                "description": self.content,
                "color": self.color_option.hex_color,
                "footer": {
                    "text": f"Data: {self._get_date()}"
                }
            }]
        }
