from flask_restx import Resource, Namespace
from src.main.usecases.plataform.resume_geral_plataform_use_case import get_general_ad_data_resume
from src.main.usecases.plataform.geral_plataform_use_case import get_general_ad_data
from src.main.usecases.save.save_use_case import save_data_to_csv
from src.main.usecases.plataform.plataform_use_case import get_ad_on_platform
from src.main.usecases.plataform.resume_plataform_use_case import get_ad_on_platform_resume
from src.main.usecases.infos.infos_use_case import get_infos

ns_analytics = Namespace('api', description='')

@ns_analytics.route('/')
class UsersResource(Resource):
    @ns_analytics.doc('get_infos')
    def get(self):
        """
        Obtém o nome, e-mail, linkedIn e o link para o github.

        Retorna:
        - Um dicionário contendo os dados com o nome, e-mail e linkedIn e o link para o github.

        O dicionario também são sera salvo no arquivo "get_infos.csv" dentro da pasta de saída.
        """
        response = get_infos()
        save_data_to_csv(response, "get_infos.csv")

        return response


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
        save_data_to_csv(response, "get_ad_on_platform.csv")

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
        save_data_to_csv(response, "get_ad_on_platform_resume.csv")

        return response

@ns_analytics.route('/geral')
class GeneralAdDataResource(Resource):
    @ns_analytics.doc('get_general_ad_data')
    def get(self):
        """
        Recupera os dados publicitários de todas as plataformas disponíveis.

        Retorna:
        - dict: Um dicionário contendo as informações agregadas de anúncios para cada plataforma.

        Os anuncios também são salvos no arquivo "get_general_ad_data.csv" dentro da pasta de saída.
        """
        response = get_general_ad_data()
        save_data_to_csv(response, "get_general_ad_data.csv")

        return response

    
@ns_analytics.route('/geral/resume')
class UsersResource(Resource):
    @ns_analytics.doc('get_general_info_resume')
    def get(self):
        """
        Recupera um resumo dos dados gerais de anúncios.

        Retorna:
        - dict: Um dicionário contendo as informações agregadas do resumo de anúncios.

        Os anuncios também são salvos no arquivo "get_general_ad_data_resume.csv" dentro da pasta de saída.
        """
        response = get_general_ad_data_resume()
        save_data_to_csv(response, "get_general_ad_data_resume.csv")

        return response
    