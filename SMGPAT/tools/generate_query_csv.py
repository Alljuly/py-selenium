import csv
from selenium.webdriver.common.by import By
from SMGPAT.utils import *
from SMGPAT.tools.webdriver_wait import wait_presence_get_text, wait_visibility, wait_and_click

from datetime import datetime

def get_item_description(navigator, index):
    id_name_element = f'{BUTTON_VIZUALIZER_NAME}{index+1:04}'
    print(id_name_element)
    wait_and_click(navigator, By.ID, id_name_element)
    
    item_description = {
            "patplaqueta": wait_presence_get_text(navigator, By.ID, PATPLAQUETA_ID),
            "status": wait_presence_get_text(navigator, By.ID, STATUS_ID),
            "organograma_name": wait_presence_get_text(navigator, By.ID, ORGANOGRAMA_NAME_ID),
            "material_id": wait_presence_get_text(navigator, By.ID, MATERIAL_ID),
            "material_name": wait_presence_get_text(navigator, By.ID, MATERIAL_NAME_ID),
            "nota_fiscal": wait_presence_get_text(navigator, By.ID, NOTA_FISCAL_ID),
            "serie_nota_fiscal": wait_presence_get_text(navigator, By.ID, SERIE_NOTA_FISCAL_ID),
            "numero_empenho": '',
            "ano_empenho": '',
            "incluido_por": wait_presence_get_text(navigator, By.ID, INCLUIDO_POR_ID),
            "incluido_em": wait_presence_get_text(navigator, By.ID, INCLUIDO_EM_ID),
            "modificado_por": wait_presence_get_text(navigator, By.ID, MODIFICADO_POR_ID),
            "ultima_modificacao": wait_presence_get_text(navigator, By.ID, ULTIMA_MODIFICACAO_ID),  
           }
    
    empenho = wait_visibility(navigator, By.ID, 'W0378GriddetalhesContainerDiv')

    if empenho:
        item_description["numero_empenho"] = wait_presence_get_text(navigator, By.ID, NUMERO_EMPENHO_ID)
        item_description["ano_empenho"] = wait_presence_get_text(navigator, By.ID, ANO_EMPENHO_ID)

    wait_and_click(navigator, By.NAME, RETURN_FORM_NAME)        
    
    return item_description

def organize_items_pagination(navigator, query_rows):
    items = []
    for _, row in enumerate(query_rows):
        if not isinstance(row, (list, tuple)):  
            row = [row]
        for j, m in enumerate(row):
            item_description = get_item_description(navigator, j)
            items.append(item_description) 
    print(items)
    
    return items

def generate_query_csv(navigator, query_rows = None, items = None):
    list_items = []
    if not items:
        list_items = organize_items_pagination(navigator, query_rows)
    else:
        list_items = items

    item_description = {
            "patplaqueta": '',
            "status": '',
            "organograma_name": '',
            "material_id": '',
            "material_name": '',
            "nota_fiscal": '',
            "serie_nota_fiscal": '',
            "numero_empenho": '',
            "ano_empenho": '',
            "incluido_por": '',
            "incluido_em": '',
            "modificado_por": '',
            "ultima_modificacao": wait_presence_get_text(navigator, By.ID, ULTIMA_MODIFICACAO_ID),  

        }
    
    if list_items:
        header = item_description.keys()
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_csv = f'resultado_consulta_{current_time}.csv' 

        with open(result_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader() 

            for item in list_items:
                    writer.writerow(item)  
    else:
        print("Nenhum item encontrado para escrever no CSV.")