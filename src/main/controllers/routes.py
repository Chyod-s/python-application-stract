from flask import Flask, jsonify
from src.main.swagger.analytics_doc import ns_analytics
from src.main.usecases.instructions.instructions_use_case import get_instructions
from src.main.usecases.plataform.requests.plataform_request import get_accounts_platform
from src.main.swagger.config import api

def register_routes(app):
    def get_data_instructions():
        response = {
            "data": get_instructions()
        }
        return jsonify(response)

    app.route('/instructions', methods=['GET'])(get_data_instructions)

    def get_data_plataform():
        response = get_accounts_platform()
        
        return jsonify(response)

    app.route('/plataform', methods=['GET'])(get_data_plataform)

    api.add_namespace(ns_analytics)
