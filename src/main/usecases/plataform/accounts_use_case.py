from src.main.usecases.plataform.requests.plataform_request import get_accounts_platform
import os

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def get_plataform(plataform, page):
    return get_accounts_platform(plataform, page)

