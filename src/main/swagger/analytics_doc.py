from flask_restx import Resource, Namespace
from flask import request
from src.main.usecases.save.save_use_case import save_list_to_csv
from src.main.usecases.plataform.plataform_use_case import get_ad_on_platform
from src.main.usecases.plataform.resume_plataform_use_case import get_ad_on_platform_resume
from src.main.usecases.infos.infos_use_case import get_infos

ns_analytics = Namespace('challenge_insights', description='API for fetching and aggregating analytics data.')

@ns_analytics.route('/')
class UsersResource(Resource):
    @ns_analytics.doc('get_infos')
    def get(self):
        """
        Obtém o nome, email, Github e o link para o LinkedIn.

        Retorna:
        - Um dicionário contendo os dados com o nome, email e link do LinkedIn.
        """
        response = get_infos()

        return {
        "data": response
        }

@ns_analytics.route('/<string:platform>')
class GetAdOnPlatform(Resource):
    def get(self, platform):
        """
        Recupera os anúncios disponíveis para uma plataforma específica.

        Parâmetros:
        - platform (str): Nome da plataforma de anúncios (ex: 'meta_ads', 'google_ads').

        Retorna:
        - Resposta contendo os anúncios disponíveis na plataforma solicitada.

        Os anuncios também são salvos no arquivo "get_ad_on_platform.csv" dentro da pasta de saída.
        """

        response = get_ad_on_platform(platform)
        save_list_to_csv(response, "get_ad_on_platform.csv")

        return response

@ns_analytics.route('/<string:platform>/Resume')
class GetAdOnPlatformColapse(Resource):
    def get(self, platform):
        """
        Retorna um resumo consolidado dos anúncios de uma plataforma e salva os dados em um arquivo CSV.

        Parâmetros:
        - platform (str): Nome da plataforma cujos dados de anúncios serão processados.

        Retorno:
        - dict: Um dicionário contendo o resumo dos anúncios da plataforma.
        
        O resumo também é salvo no arquivo "get_ad_on_platform_resume.csv" dentro da pasta de saída.
        """

        response = get_ad_on_platform_resume(platform)
        save_list_to_csv(response, "get_ad_on_platform_resume.csv")

        return response

@ns_analytics.route('/geral')
class UsersResource(Resource):
    @ns_analytics.doc('get_general_info')
    def get(self):
        """
   
        """

        return "lol"
    
@ns_analytics.route('/geral/resumo')
class UsersResource(Resource):
    @ns_analytics.doc('get_general_info_resume')
    def get(self):
        """
   
        """

        return "hahaha"