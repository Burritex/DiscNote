"""
    note_model.py
    -------------
    Define o modelo de domínio ``Note``, que representa uma nota a ser
    enviada ao Discord como embed.
    
    Responsabilidade:
        Armazenar o conteúdo e a categoria visual da nota, além de gerar
        o payload JSON pronto para ser enviado à API de webhooks do Discord.
    
    Exemplos de uso:
        >>> from models.note_model import Note
        >>> from models.color_enum import ColorEnum
        >>> nota = Note("Estudar sobre webhooks", ColorEnum.BLUE)
        >>> payload = nota.config_json()
        >>> payload["embeds"][0]["title"]
        '📘 Referência/Link'
"""

from datetime import datetime
from models import ColorEnum


class Note:
    """
        Representa uma nota com conteúdo textual e categoria de cor.
    
        Args:
            content      (str):       Texto da nota. Padrão: string vazia.
            color_option (ColorEnum): Categoria visual da nota. Padrão: YELLOW.
    
        Propriedades:
            content      (str):       Conteúdo da nota (getter/setter).
            color_option (ColorEnum): Categoria de cor (getter/setter).
    
        Métodos:
            config_json() -> dict: Monta o payload de embed para o webhook do Discord.
    """

    def __init__(self, content: str = "", color_option: ColorEnum = ColorEnum.YELLOW):
        self._content = content
        self._color_option = color_option
    
    @property
    def content(self):
        """Retorna o conteúdo textual da nota."""
        return self._content
    
    @content.setter
    def content(self, value: str):
        """Define o conteúdo textual da nota."""
        self._content = value

    @property
    def color_option(self):
        """Retorna a categoria de cor da nota."""
        return self._color_option
    
    @color_option.setter
    def color_option(self, value: ColorEnum):
        """Define a categoria de cor da nota."""
        self._color_option = value

    def _get_date(self) -> str:
        """
            Retorna a data e hora atuais formatadas.
    
            Returns:
                str: Data no formato ``dd/mm/AAAA HH:MM``.
        """
        return datetime.now().strftime("%d/%m/%Y %H:%M")
    
    def config_json(self):
        """
            Monta o payload JSON do embed para a API de webhooks do Discord.
    
            O payload segue a estrutura esperada pela Discord Webhook API,
            com os campos ``title``, ``description``, ``color`` e ``footer``.
    
            Returns:
                dict: Dicionário pronto para ser serializado e enviado via POST.
        """
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
