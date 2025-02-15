from src.main.usecases.plataform.geral_plataform_use_case import get_general_ad_data

def get_general_ad_data_resume():
    list_colapse = []  
    dict_colapse = {}  

    general_data = get_general_ad_data()

    for value in general_data:
        platform_name = value['plataform']

        if dict_colapse and dict_colapse.get('plataform') != platform_name:
            list_colapse.append(dict_colapse.copy())
            dict_colapse.clear()

        dict_colapse['plataform'] = platform_name

        for key, val in value.items():
            if key != 'plataform':  
                if isinstance(val, (int, float)):  
                    dict_colapse[key] = dict_colapse.get(key, 0) + val

    if dict_colapse:
        list_colapse.append(dict_colapse)

    return list_colapse
