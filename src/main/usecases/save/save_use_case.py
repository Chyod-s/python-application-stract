import csv
import os

def save_list_to_csv(data, filename="ads_data.csv"):
    """ 
    Obtém os anúncios de uma plataforma e salva em um arquivo CSV.

    Parâmetros:
    - platform (str): Nome da plataforma.
    - filename (str): Nome do arquivo CSV de saída (padrão: "ads_data.csv").
    
    Retorna:
    - None
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
