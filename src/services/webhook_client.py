"""
    webhook_client.py
    -----------------
    Responsável pelo envio de objetos ``Note`` ao Discord via webhook.
    
    Responsabilidade:
        Isolar toda a comunicação HTTP com a API do Discord, evitando que
        lógica de rede se espalhe por outras camadas da aplicação.
    
    Dependências externas:
        requests: realiza a requisição HTTP POST ao endpoint do webhook.
    
    Referência da API:
        https://discord.com/developers/docs/resources/webhook
"""


from services import ConfigManager
from models import Note
import requests


class WebhookDispatcher:
    """
        Despachante de notas para o webhook do Discord.
    
        Todos os métodos são estáticos — a classe não precisa ser instanciada.
    """

    @staticmethod
    def send(note: Note):
        """
            Envia uma ``Note`` formatada como embed para o webhook do Discord.
    
            Obtém a URL do webhook via ``ConfigManager``, serializa a nota
            com ``note.config_json()`` e realiza um POST à API do Discord.
    
            Args:
                note (Note): Objeto Note a ser enviado.
    
            Returns:
                tuple[bool, int | None]:
                    - ``(True, None)``        se o envio foi bem-sucedido (HTTP 204).
                    - ``(False, status_code)`` se a API retornou um erro.
    
            Raises:
                requests.exceptions.RequestException: Em caso de falha de rede
                    (timeout, sem conexão, DNS, etc.).
                ValueError: Se a URL do webhook não estiver configurada no ``.env``
                            (propagado do ``ConfigManager``).
        """
        url = ConfigManager.get_webhook_url()
        response = requests.post(url, json=note.config_json())
        if response.status_code == 204:
            return True, None
        else:
            return False, response.status_code
