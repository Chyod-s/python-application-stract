import requests
import os

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def get_instructions():
    url = 'https://sidebar.stract.to/api'
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf-8')

    return desealize_content(content)

def desealize_content(response):

    response = response.split('\n')

    response = [x for x in response if x != '']

    return response
