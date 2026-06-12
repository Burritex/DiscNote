from dotenv import load_dotenv
import os


load_dotenv()

class ConfigManager:
    @staticmethod
    def get_webhook_url() -> str:
        url = os.getenv("DISCORD_WEBHOOK_URL")
        if not url:
            raise ValueError("A variável DISCORD_WEBHOOK_URL não foi encontrada no .env!")
        return url
