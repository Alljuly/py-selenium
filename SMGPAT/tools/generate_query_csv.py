import csv
from selenium.webdriver.common.by import By
from SMGPAT.utils import *
from SMGPAT.tools.webdriver_wait import wait_presence_get_text, wait_visibility, wait_and_click

from datetime import datetime

def get_item_description(navigator, query_row):
    id_name_element = f'{BUTTON_VIZUALIZER_NAME}{query_row:04}'
    
    wait_and_click(navigator, By.NAME, id_name_element)
    
    item_description = {
            "patplaqueta": wait_presence_get_text(navigator, By.ID, PATPLAQUETA_ID),
            "status": wait_presence_get_text(navigator, By.ID, STATUS_ID),
            "organograma_name": wait_presence_get_text(navigator, By.ID, ORGANOGRAMA_NAME_ID),
            "material_id": wait_presence_get_text(navigator, By.ID, MATERIAL_ID),
            "material_name": wait_presence_get_text(navigator, By.ID, MATERIAL_NAME_ID),
            "nota_fiscal": wait_presence_get_text(navigator, By.ID, NOTA_FISCAL_ID),
            "serie_nota_fiscal": wait_presence_get_text(navigator, By.ID, SERIE_NOTA_FISCAL_ID),
           }
    
    empenho = wait_visibility(navigator, By.ID, 'W0378GriddetalhesContainerDiv')
    if empenho:
        empenho_description = {
            "numero_empenho": wait_presence_get_text(navigator, By.ID, NUMERO_EMPENHO_ID),
            "ano_empenho": wait_presence_get_text(navigator, By.ID, ANO_EMPENHO_ID),
            "incluido_por": wait_presence_get_text(navigator, By.ID, INCLUIDO_POR_ID),
            "incluido_em": wait_presence_get_text(navigator, By.ID, INCLUIDO_EM_ID),
            "modificado_por": wait_presence_get_text(navigator, By.ID, MODIFICADO_POR_ID),
            "ultima_modificacao": wait_presence_get_text(navigator, By.ID, ULTIMA_MODIFICACAO_ID)
            
        }
    else:
        empenho_description = {
            "numero_empenho": "",
            "ano_empenho": "",
            "incluido_por": "",
            "incluido_em": "",
            "modificado_por": "",
            "ultima_modificacao": " ",   
        }
        item_description = item_description | empenho_description
    
    wait_and_click(navigator, By.NAME, RETURN_FORM_NAME)        
    return item_description

def organize_items_pagination(navigator, query_rows):
    pass

def generate_items_description(navigator, query_rows):
    list_items = [ ]
    item_description = { 
       # "patplaqueta": navigator.find_element(By.ID, PATPLAQUETA_ID),
       # "status": navigator.find_element(By.ID, STATUS_ID),
       # "organograma_name": navigator.find_element(By.ID, ORGANOGRAMA_NAME_ID),
       # "material_id": navigator.find_element(By.ID, MATERIAL_ID),
       # "material_name": navigator.find_element(By.ID, MATERIAL_NAME_ID),
       # "nota_fiscal": navigator.find_element(By.ID, NOTA_FISCAL_ID),
       # "serie_nota_fiscal": navigator.find_element(By.ID, SERIE_NOTA_FISCAL_ID),
       # "numero_empenho": navigator.find_element(By.ID, NUMERO_EMPENHO_ID),
       # "ano_empenho": navigator.find_element(By.ID, ANO_EMPENHO_ID),
       # "incluido_por": navigator.find_element(By.ID, INCLUIDO_POR_ID),
       # "incluido_em": navigator.find_element(By.ID, INCLUIDO_EM_ID),
       # "modificado_por": navigator.find_element(By.ID, MODIFICADO_POR_ID),
       # "ultima_modificacao": navigator.find_element(By.ID, ULTIMA_MODIFICACAO_ID)
    }
    if len(query_rows) == 1:
        item_description = get_item_description(navigator, 1)
        list_items.append(item_description)
        return list_items
    elif len(query_rows) > 1:
        items = organize_items_pagination(navigator, query_rows)
        return list_items.append(items)


def generate_query_csv(navigator, query_rows):
    list_items = generate_items_description(navigator, query_rows)
   
    if list_items:
        header = list(list_items[0].keys()) 
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_csv = f'resultado_consulta_{current_time}.csv' 

        with open(result_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader() 

            for item in list_items:
                    writer.writerow(item)  
    else:
        print("Nenhum item encontrado para escrever no CSV.")