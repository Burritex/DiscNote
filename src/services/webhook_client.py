from services import ConfigManager
from models import Note
import requests


class WebhookDispatcher:
    @staticmethod
    def send(note: Note):
        url = ConfigManager.get_webhook_url()
        response = requests.post(url, json=note.config_json())
        if response.status_code == 204:
            return True, None
        else:
            return False, response.status_code
