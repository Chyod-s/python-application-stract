from flask_restx import Resource, Namespace
from flask import request
from src.main.usecases.instructions.instructions_use_case import get_instructions
from src.main.usecases.infos.infos_use_case import get_infos
from main.usecases.plataform.accounts_use_case import get_plataform

ns_analytics = Namespace('challenge_insights', description='API for fetching and aggregating analytics data.')

@ns_analytics.route('/')
class UsersResource(Resource):
    @ns_analytics.doc('get_infos')
    def get(self):
        response = get_infos()

        """Obtém nome, email e o link para o seu LinkedIn"""
        return {
        "data": response
        }


@ns_analytics.route('/plataform')
class GetPlataform(Resource):
    @ns_analytics.param('platform', '', type='string', required=True)
    @ns_analytics.param('page', '', type='int', required=False)
    def get(self):
        platform_name = request.args.get('platform', default='meta_ads')

        page = request.args.get('page', default=None)

        response = get_plataform(platform_name, page)

        """ """
        return response
        
