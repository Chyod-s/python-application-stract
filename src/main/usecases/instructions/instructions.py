import requests
import os

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def get_instructions():
    url = 'https://sidebar.stract.to/api'
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    return requests.get(url, headers=headers)
    