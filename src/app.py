from datetime import datetime
import requests
import os
from dotenv import load_dotenv


load_dotenv()

def set_nota() -> str:
    print("Digite a nota: ")
    return input("> ")


def set_json(text) -> dict:
    return {
        "embeds": [{
            "title": "💡 Nova Ideia",
            "description": f"{text}",
            "color": 16776960,
            "footer": {
            "text": f"Data: {datetime.now().strftime("%d/%m/%Y %H:%M")}"
            }
        }]
    }


def enviar_nota(nota) -> None:
    webhook = os.getenv("DISCORD_WEBHOOK_URL")
    response = requests.post(webhook, json=nota)
    if response.status_code == 204:
        print("Nota enviada com sucesso!")
    else:
        print(f"Erro ao enviar: {response.status_code}")


if __name__ == "__main__":
    nota = set_nota()
    body = set_json(nota)
    enviar_nota(body)
