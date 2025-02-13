import csv

def save_list_to_csv(data, filename="ads_data.csv"):
    """ 
    Obtém os anúncios de uma plataforma e salva em um arquivo CSV.

    Parâmetros:
    - platform (str): Nome da plataforma.
    - filename (str): Nome do arquivo CSV de saída (padrão: "ads_data.csv").
    
    Retorna:
    - None
    """
    name = ''
    with open(filename, mode="w", newline="", encoding="latin1") as file:
        writer = csv.DictWriter(file, fieldnames=['plataform'] + list(data[1]['insights'][0].keys()))

        writer.writeheader()

        for entry in data:
            if type(entry) is str:
                name = entry
                continue

            insights = entry['insights']
            
            for insight in insights:
                insight = {'plataform': name, **insight}

                writer.writerow(insight)
