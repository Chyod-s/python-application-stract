from flask_restx import Resource, Namespace
from src.main.usecases.instructions.instructions import get_instructions

ns_analytics = Namespace('technical challenge analytics', description='API for fetching and aggregating analytics data from the Stract platform.')

@ns_analytics.route('/')
class UsersResource(Resource):
    @ns_analytics.doc('get_instructions')
    def get(self):
        response = get_instructions()

        """Obtém as instruções para concluir o desafio técnico"""
        return {
        "status_code":200,
        "msg": "Sucesso",
        "data": response
    }
