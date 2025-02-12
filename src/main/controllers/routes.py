from flask import Flask, jsonify
from src.main.swagger.analytics_doc import ns_analytics
from src.main.usecases.instructions.instructions import get_instructions
from src.main.swagger.config import api

def register_routes(app):
    def get_data_instructions():
        response = {
            "data": get_instructions()
        }
        return jsonify(response)

    app.route('/instructions', methods=['GET'])(get_data_instructions)

    api.add_namespace(ns_analytics)
