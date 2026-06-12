"""
    config_manager.py
    -----------------
    Gerencia a leitura de variáveis de configuração do arquivo ``.env``.
    
    Responsabilidade:
        Isolar o acesso às variáveis de ambiente do restante da aplicação,
        garantindo que configurações sensíveis (como a URL do webhook)
        sejam validadas antes de serem utilizadas.
    
    Dependências externas:
        python-dotenv: carrega automaticamente o arquivo ``.env`` na raiz do projeto.
    
    Exemplo de ``.env`` esperado:
        DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/SEU_ID/SEU_TOKEN
"""

from dotenv import load_dotenv
import os


load_dotenv()

class ConfigManager:
    """
        Provedor de configurações da aplicação via variáveis de ambiente.
    
        Todos os métodos são estáticos — a classe não precisa ser instanciada.
    """

    @staticmethod
    def get_webhook_url() -> str:
        """
            Retorna a URL do webhook do Discord definida no ``.env``.
    
            Returns:
                str: URL completa do webhook.
    
            Raises:
                ValueError: Se a variável ``DISCORD_WEBHOOK_URL`` não estiver definida
                            ou estiver vazia no arquivo ``.env``.
        """
        url = os.getenv("DISCORD_WEBHOOK_URL")
        if not url:
            raise ValueError("A variável DISCORD_WEBHOOK_URL não foi encontrada no .env!")
        return url
