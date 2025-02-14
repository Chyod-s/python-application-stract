import csv
import os

def save_data_to_csv(data, filename="ads_data.csv"):
    """ 
    Salva os dados de anúncios de diferentes plataformas em um arquivo CSV.

    Parâmetros:
    - data (list): Lista de dicionários contendo dados de anúncios organizados por plataforma. 
                   Cada item pode ser uma string (nome da plataforma) ou um dicionário com a chave "insights".
    - filename (str): Nome do arquivo CSV de saída (padrão: "ads_data.csv").

    Funcionalidade:
    - Cria um diretório "files_csv" na raiz do projeto, caso não exista.
    - Remove a chave "id" dos dados antes de salvá-los.
    - Adiciona uma nova coluna "plataform" para indicar a qual plataforma os dados pertencem.
    - Escreve os dados no arquivo CSV, garantindo que os cabeçalhos correspondam às chaves dos insights.

    Retorna:
    - None (apenas salva o arquivo no diretório especificado).
    """
    name = ""

    def criar_pasta(caminho):
        if not os.path.exists(caminho):
            os.makedirs(caminho)

    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "files_csv"))

    criar_pasta(directory)
    
    save_path = os.path.join(directory, filename)

    if isinstance(data, dict):
        save_dict_data_to_csv(data, save_path)
    elif isinstance(data, list):
        for i in data:
            save_dict_data_to_csv(i, save_path, 'a')
    else:
        save_obj_data_to_csv(data, save_path)


def save_dict_data_to_csv(data, save_path, type_mode='w'):
    """
    Salva um dicionário em um arquivo CSV, garantindo que os dados sejam escritos nas colunas corretas, 
    sem alterar a ordem original das colunas.

    Parâmetros:
    - data (dict): Dicionário a ser salvo no CSV.
    - save_path (str): Caminho do arquivo CSV.
    - type_mode (str): Modo de abertura do arquivo ('w' para sobrescrever, 'a' para adicionar).
    """
    file_exists = os.path.exists(save_path)
    existing_columns = []

    if file_exists:
        with open(save_path, mode="r", newline="", encoding="latin1") as file:
            reader = csv.reader(file)
            existing_columns = next(reader, [])  

    fieldnames = existing_columns if existing_columns else list(data.keys())
    if 'id' in fieldnames:
        fieldnames.remove('id')

    with open(save_path, mode=type_mode, newline="", encoding="latin1") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists or type_mode == 'w':
            writer.writeheader()

        writer.writerow({col: data.get(col, "") for col in fieldnames})


def save_obj_data_to_csv(data, save_path):
    """
    Salva dados de uma lista de objetos em um arquivo CSV, incluindo a plataforma e removendo o campo 'id'.

    Parâmetros:
    - data (list[dict | str]): Lista contendo dicionários com insights e strings representando a plataforma.
    - save_path (str): Caminho do arquivo CSV.

    Funcionamento:
    1. Obtém as chaves dos insights e remove 'id' se presente.
    2. Cria o CSV com colunas ordenadas e adiciona 'plataform'.
    3. Itera sobre `data`, armazenando a string da plataforma e processando os insights.
    4. Escreve os insights no CSV, garantindo a ordem correta das colunas.

    Exemplo de Saída:
    ```
    plataforma,ad_name,clicks,country,cpc
    Facebook Ads,Anúncio 9,886,BR,0.335
    ```
    """
    keys = list(data[1]['insights'][0].keys())
    if 'id' in keys:
        keys.remove('id')
    
    with open(save_path, mode="w", newline="", encoding="latin1") as file:
        writer = csv.DictWriter(file, fieldnames=['plataform'] + keys)

        writer.writeheader()

        for entry in data:
            if type(entry) is str:
                name = entry
                continue

            insights = entry['insights']
            
            for insight in insights:
                insight.pop('id', None)
                insight = {'plataform': name, **insight}

                writer.writerow(insight)
