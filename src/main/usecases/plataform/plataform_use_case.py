from src.main.usecases.plataform.requests.plataform_request import get_accounts_platform, get_fields_platform

def get_ad_on_platform(platform):
    """ 
    Obtém os anúncios disponíveis para uma plataforma específica, 
    fazendo paginação caso necessário.

    Parâmetros:
    - platform (str): Nome da plataforma.

    Retorna:
    - list: Lista contendo os anúncios disponíveis.
    """
    people = get_fields(platform)
    

    return people
    
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

    if 'fields' in fields and fields['pagination']['total'] > 0:
        total_pages = fields['pagination']['total']
        
        page += fields['pagination']['total']

        for i in range(1, total_pages + 1):
            fields = get_fields_platform(platform, i)
            if 'fields' in fields:
                list_fields.extend(fields['fields'])

        return list_fields
    