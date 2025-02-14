from src.main.usecases.plataform.plataform_use_case import get_ad_on_platform
from src.main.usecases.plataform.requests.plataform_request import get_platform

def get_general_ad_data():
    """
    Obtém informações publicitárias de todas as plataformas disponíveis.

    Retorna:
    - list: Uma lista de dicionários contendo os dados de anúncios para cada plataforma.
    """
    general_ad_data = []

    platforms = get_platform()

    for platform_group in platforms.values():
        for platform in platform_group:
            platform_name = platform["value"]
            ad_data = get_ad_on_platform(platform_name)

            general_ad_data.extend(ad_data)  
            
    return process_general_ad_data(general_ad_data)

def process_general_ad_data(list_platforms):
    """
    Processa os dados de anúncios adicionando o nome da plataforma a cada entrada.

    Parâmetros:
    - list_platforms (list): Lista contendo os dados brutos das plataformas.

    Retorna:
    - list: Lista formatada com a chave 'plataform' adicionada.
    """
    general_ad_data = []
    platform_name = ""

    for item in list_platforms:
        if isinstance(item, str):  
            platform_name = item
            continue

        if isinstance(item, dict) and item:  
            first_key = next(iter(item), None)  

            if first_key and isinstance(item[first_key], list):  
                for ad_details in item[first_key]:
                    if isinstance(ad_details, dict): 
                        formatted_entry = {'plataform': platform_name, **ad_details}

                        if general_ad_data:
                            formatted_entry = generate_new_ad_data(formatted_entry, general_ad_data)
                   
                        general_ad_data.append(formatted_entry)

    return general_ad_data

def generate_new_ad_data(formatted_entry, general_ad_data):
    """
    Mapeia e transforma os dados de um anúncio para um formato padronizado.
    
    Parâmetros:
    - formatted_entry (dict): Dicionário contendo os dados formatados do anúncio.
    - general_ad_data (list[dict]): Lista de dicionários contendo dados gerais dos anúncios.

    Retorna:
    - dict: Dicionário com os dados do anúncio no formato padronizado.
    """
    if not general_ad_data:
        return {}

    new_dict = {}
    new_keys = set(general_ad_data[0].keys())  

    key_mapping = {
        "region": "country",
        "status": "effective_status",
        "adName": "ad_name",
        "cost": "spend"
    }

    for key, value in formatted_entry.items():
        mapped_key = key_mapping.get(key, key) 
        new_dict[mapped_key] = value
        new_keys.add(mapped_key)  

    return new_dict
