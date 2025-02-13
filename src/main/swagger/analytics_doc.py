from flask_restx import Resource, Namespace
from flask import request
from src.main.usecases.infos.infos_use_case import get_infos
from src.main.usecases.plataform.requests.plataform_request import get_accounts_platform, get_fields_platform, get_insights_platform

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

@ns_analytics.route('/accounts_platform')
class GetAccountsPlataform(Resource):
    @ns_analytics.param('platform', '', type='string', required=True)
    @ns_analytics.param('page', '', type='int', required=False)
    def get(self):
        """
        Recupera uma lista de contas para uma plataforma específica.

        Parâmetros:
        - platform (str): Nome da plataforma (ex: 'meta_ads').
        - page (int, opcional): Número da página para paginação dos resultados.

        Retorna:
        - Resposta com a lista de contas da plataforma solicitada.
        """
        platform_name = request.args.get('platform', default='meta_ads')

        page = request.args.get('page', default=None)

        response = get_accounts_platform(platform_name, page)

        return response
        
@ns_analytics.route('/fields_platform')
class GetFieldsPlataform(Resource):
    @ns_analytics.param('platform', '', type='string', required=True)
    @ns_analytics.param('page', '', type='int', required=False)
    def get(self):
        """
        Recupera os campos disponíveis para uma plataforma específica.

        Parâmetros:
        - platform (str): Nome da plataforma (ex: 'meta_ads').
        - page (int, opcional): Número da página para paginação dos resultados.

        Retorna:
        - Resposta com os campos disponíveis da plataforma solicitada.
        """
        platform_name = request.args.get('platform', default='meta_ads')

        page = request.args.get('page', default=None)

        response = get_fields_platform(platform_name, page)

        return response

@ns_analytics.route('/insights_platform')
class GetInsightsPlatform(Resource):
    @ns_analytics.param('platform', '', type='string', required=True)
    @ns_analytics.param('account', '', type='string', required=True)
    @ns_analytics.param('token', '', type='string', required=True)
    @ns_analytics.param('fields', 'List of fields', type='array', required=True, items={'type': 'string'})
    def get(self):
        """
        Recupera os insights de uma plataforma específica para uma conta.

        Parâmetros:
        - platform (str): Nome da plataforma (ex: 'meta_ads').
        - account (str): Identificador da conta.
        - token (str): Token de autenticação.
        - fields (list): Lista de campos de dados a serem recuperados.

        Retorna:
        - Resposta com os insights da plataforma e da conta solicitadas.
        """
        platform_name = request.args.get('platform')
        account = request.args.get('account')
        token = request.args.get('token')
        fields = request.args.getlist('fields')

        response = get_insights_platform(platform_name, account, token, fields)

        return response