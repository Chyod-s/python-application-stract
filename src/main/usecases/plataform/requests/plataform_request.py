import requests
import os
import json

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def get_accounts_platform(plataform, page):
    url = f'https://sidebar.stract.to/api/accounts?platform={plataform}'
    if page:
        url += f'&page={page}'

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf-8')

    return json.loads(content)

def get_fields_platform(plataform, page):
    url = f'https://sidebar.stract.to/api/fields?platform={plataform}'
    if page:
        url += f'&page={page}'

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf-8')

    return json.loads(content)

def get_insights_platform(platform, account, token, fields):
    url = f'https://sidebar.stract.to/api/insights?platform={platform}&account={account}&token={token}&fields={fields}'
    
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf-8')

    return json.loads(content)
