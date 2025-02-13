from flask_restx import Resource, Namespace
from flask import request
from src.main.usecases.save.save_use_case import save_list_to_csv
from src.main.usecases.plataform.plataform_use_case import get_ad_on_platform
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

@ns_analytics.route('/get_ad_on_platform')
class GetAdOnPlatform(Resource):
    @ns_analytics.param('platform', '', type='string', required=True)
    def get(self):
        """
        Recupera os anúncios disponíveis para uma plataforma específica.

        Parâmetros:
        - platform (str): Nome da plataforma de anúncios (ex: 'meta_ads', 'google_ads').

        Retorna:
        - Resposta contendo os anúncios disponíveis na plataforma solicitada.
        """
        platform_name = request.args.get('platform')

        response = get_ad_on_platform(platform_name)
        save_list_to_csv(response, "get_ad_on_platform.csv")

        return response