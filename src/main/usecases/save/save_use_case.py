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
    # Obtendo os cabeçalhos a partir das chaves do primeiro item da lista
    headers = data[0].keys()  

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)