from flask import Response, jsonify
from src.main.usecases.plataform.resume_geral_plataform_use_case import get_general_ad_data_resume
from src.main.usecases.plataform.geral_plataform_use_case import get_general_ad_data
from src.main.usecases.plataform.resume_plataform_use_case import get_ad_on_platform_resume
from src.main.usecases.save.save_use_case import save_data_to_csv
from src.main.usecases.plataform.plataform_use_case import get_ad_on_platform
from src.main.usecases.infos.infos_use_case import get_infos
from src.main.swagger.analytics_doc import ns_analytics
from src.main.usecases.plataform.requests.plataform_request import get_instructions
from src.main.swagger.config import api

def register_routes(app):

    @app.route('/instructions', methods=['GET'])
    def get_data_instructions_route():
        return Response(get_instructions(), mimetype="text/plain") 
    
    @app.route('/name', methods=['GET'])
    def users_information_route():
        response = get_infos()
        save_data_to_csv(response, "get_infos.csv")

        return jsonify(get_infos()) 
    
    @app.route('/<string:platform>', methods=['GET'])
    def get_ad_on_platform_route(platform):
        response = get_ad_on_platform(platform)
        save_data_to_csv(response, "get_ad_on_platform.csv")

        return jsonify(response)
    
    @app.route('/<string:platform>/resume', methods=['GET'])
    def get_ad_on_platform_resume_route(platform):
        response = get_ad_on_platform_resume(platform)
        save_data_to_csv(response, "get_ad_on_platform_resume.csv")

        return jsonify(response)
    
    @app.route('/geral', methods=['GET'])
    def get_general_ad_data_resume_route():
        response = get_general_ad_data()
        save_data_to_csv(response, "get_general_ad_data.csv")

        return jsonify(response)
    
    @app.route('/geral/resume', methods=['GET'])
    def get_general_ad_data_resume_resume_route():
        response = get_general_ad_data_resume()
        save_data_to_csv(response, "get_general_ad_data_resume.csv")

        return jsonify(response)
    
    api.add_namespace(ns_analytics)
