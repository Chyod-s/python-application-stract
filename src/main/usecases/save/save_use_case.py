import csv
import os

def save_list_to_csv(data, filename="ads_data.csv"):
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
