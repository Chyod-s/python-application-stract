
from src.main.usecases.plataform.plataform_use_case import get_ad_on_platform
from src.main.usecases.plataform.requests.plataform_request import get_platform

def get_general_ad_data():
    """
    Obtém informações publicitárias de todas as plataformas disponíveis.

    Retorna:
    - dict: Um dicionário contendo os dados de anúncios para cada plataforma.
    """
    general_ad_data = {}

    platforms = get_platform()

    for platform_group in platforms.values():
        for platform in platform_group:
            platform_name = platform["value"]
            ad_data = get_ad_on_platform(platform_name)

            general_ad_data[platform_name] = ad_data

    return general_ad_data