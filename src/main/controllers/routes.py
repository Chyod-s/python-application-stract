from src.main.swagger.analytics_doc import ns_analytics
from src.main.usecases.instructions.instructions import get_instructions
from flask import jsonify
from src.main.swagger.config import api

def register_routes(app):
    @app.route('/', methods=['GET'])
    def get_data():
        response = get_instructions()

        if response.status_code == 200:
            content = response.content.decode('utf-8')
            return jsonify(content)
        else:
            return jsonify({"error": "Erro ao buscar dados"}), response.status_code

    api.add_namespace(ns_analytics)
