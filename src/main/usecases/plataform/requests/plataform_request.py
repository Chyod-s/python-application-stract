import requests
import os
import json

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
BASE_API_URL = os.getenv("BASE_API_URL")
GET_PLATFORMS_URL = os.getenv("GET_PLATFORMS_URL")
GET_ACCOUNTS_BY_PLATFORM_URL = os.getenv("GET_ACCOUNTS_BY_PLATFORM_URL")
GET_FIELDS_BY_PLATFORM_URL = os.getenv("GET_FIELDS_BY_PLATFORM_URL")
GET_INSIGHTS_URL = os.getenv("GET_INSIGHTS_URL")

def get_instructions():
    url = BASE_API_URL
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "text/plain"
    }
    response = requests.get(url, headers=headers)
    return response.content.decode('utf-8')

def get_platform():
    url = GET_PLATFORMS_URL

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf-8')

    return json.loads(content)

def get_accounts_platform(plataform, page):
    url = GET_ACCOUNTS_BY_PLATFORM_URL + plataform
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
    url = GET_FIELDS_BY_PLATFORM_URL + plataform
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
    url = f'{GET_INSIGHTS_URL+ platform}&account={account}&token={token}&fields={fields}'
    
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf-8')

    return json.loads(content)
