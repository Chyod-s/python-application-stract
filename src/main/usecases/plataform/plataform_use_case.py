from src.main.usecases.plataform.requests.plataform_request import get_accounts_platform, get_fields_platform, get_insights_platform

def get_ad_on_platform(platform):
    """
    Recupera os anúncios disponíveis para uma plataforma específica, utilizando insights de contas associadas à plataforma.

    Parâmetros:
    - platform (str): Nome da plataforma da qual os anúncios serão recuperados.

    Retorna:
    - list: Lista contendo os anúncios disponíveis, extraídos dos insights das contas da plataforma.
    """
    insights = get_insights(platform)
    
    return insights

def get_insights(platform):
    """
    Recupera os insights de uma plataforma específica para todas as contas disponíveis.

    Parâmetros:
    - platform (str): Nome da plataforma da qual os insights serão obtidos.

    Retorna:
    - list: Lista contendo os insights de todas as contas associadas à plataforma.
    """
    list_insights = list()

    fields = get_fields(platform)
    list_field = ",".join(field["value"] for field in fields)
    
    people = get_people_accounts(platform)
    for i in people:
        account = i["id"]
        token = i["token"]
        insights = get_insights_platform(platform, account, token, list_field)
        list_insights.append(insights)
 
    return list_insights


def get_people_accounts(platform):
    """
    Obtém a lista de contas associadas a uma determinada plataforma, realizando paginação se necessário.

    Parâmetros:
    - platform (str): Nome da plataforma da qual as contas serão recuperadas.

    Retorna:
    - list: Uma lista contendo todas as contas associadas à plataforma.
    - Se nenhuma conta for encontrada, retorna uma lista vazia.
    """
    page = 0
    list_people = list()

    people = get_accounts_platform(platform, page)

    if 'pagination' in people and people['pagination']['total'] > 0:
        total_pages = people['pagination']['total']
        
        page += people['pagination']['total']

        for i in range(1, total_pages + 1):
            people = get_accounts_platform(platform, i)
            if 'accounts' in people:
                list_people.extend(people['accounts'])

        return list_people


def get_fields(platform):
    """
    Obtém a lista de campos disponíveis para uma determinada plataforma, realizando paginação se necessário.

    Parâmetros:
    - platform (str): Nome da plataforma da qual os campos serão recuperados.

    Retorna:
    - list: Uma lista contendo todos os campos disponíveis na plataforma.
    - Se nenhum campo for encontrado, retorna uma lista vazia.
    """
    page = 0
    list_fields = list()

    fields = get_fields_platform(platform, page)

    if len(fields) == 1:
        return fields['fields']

    total_pages = fields['pagination']['total']
    
    page += fields['pagination']['total']

    for i in range(1, total_pages + 1):
        fields = get_fields_platform(platform, i)
        if 'fields' in fields:
            list_fields.extend(fields['fields'])

    return list_fields
    