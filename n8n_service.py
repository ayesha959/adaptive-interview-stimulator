import requests

from config.settings import N8N_WEBHOOK_URL


def send_to_n8n(data):

    response = requests.post(
        N8N_WEBHOOK_URL,
        json=data
    )

    return response.json()