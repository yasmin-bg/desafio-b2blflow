import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WhatsAppService:
    def __init__(self):
        self.instance_id = os.getenv("ZAPI_INSTANCE_ID")
        self.token = os.getenv("ZAPI_TOKEN")

        if not self.instance_id or not self.token:
            raise ValueError("Z-API não configurada corretamente")

        self.base_url = (
            f"https://api.z-api.io/instances/"
            f"{self.instance_id}/token/{self.token}/send-text"
        )

    def enviar_mensagem(self, telefone: str, mensagem: str):

        payload = {
            "phone": telefone,
            "message": mensagem
        }

        response = requests.post(self.base_url, json=payload, timeout=10)

        if response.status_code != 200:
            raise Exception(f"Erro Z-API: {response.text}")

        return response.json()