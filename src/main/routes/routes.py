from src.main.swagger.config import api
from src.main.swagger.analytics_doc import ns_analytics
from flask import jsonify
import requests
import os
from . import app

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

@app.route('/', methods=['GET'])
def get_data():
    url = 'https://sidebar.stract.to/api'
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content = response.content.decode('utf-8')
        return jsonify(content)
    else:
        return jsonify({"error": "Erro ao buscar dados"}), response.status_code

api.init_app(app)
api.add_namespace(ns_analytics)
