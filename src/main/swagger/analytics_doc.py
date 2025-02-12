from flask_restx import Resource, Namespace

ns_analytics = Namespace('technical challenge analytics', description='API for fetching and aggregating analytics data from the Stract platform.')

@ns_analytics.route('/')
class UsersResource(Resource):
    @ns_analytics.doc('get_instructions')
    def get(self):
        """Obtém as instruções para concluir o desafio técnico"""
        return {
        "status_code":200,
        "msg": "Sucesso",
        "data": "get_data"
    }