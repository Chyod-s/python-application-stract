from src.main.usecases.plataform.requests.plataform_request import get_platform
from src.main.usecases.plataform.plataform_use_case import get_ad_on_platform

def get_ad_on_platform_resume(platform):
    """
    Gera um resumo consolidado dos anúncios de uma plataforma.

    Parâmetros:
    - platform (str): Nome da plataforma para buscar os dados.

    Retorno:
    - dict: Um dicionário contendo a soma dos valores numéricos e o último valor de campos não numéricos.
    """
    colapse_insights = {}

    name_platform_list = get_platform()
    name_platform = name_platform_list["platforms"]
    for i in name_platform:
        if i["value"] == platform:
            name_platform = i["text"]
            break
        
    colapse_insights['platform'] = name_platform	

    insights = get_ad_on_platform(platform)

    for entry in insights:
        if isinstance(entry, str):
            continue

        for insight in entry.get('insights', []):
            for key, value in insight.items():
                if type(value) == str or key == 'id':
                    continue

                if key not in colapse_insights:
                    colapse_insights[key] = value
                else:
                    if isinstance(value, (int, float)):
                        colapse_insights[key] += value
                    else:
                        colapse_insights[key] = value 

    return colapse_insights
