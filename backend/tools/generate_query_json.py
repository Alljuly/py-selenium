import csv
from selenium.webdriver.common.by import By
from backend.utils import *
from backend.tools.webdriver_wait import wait_presence_get_text, wait_and_click


def get_item_description(navigator):
    item_description = {
            "patplaqueta": wait_presence_get_text(navigator, By.ID, PATPLAQUETA_ID),
            "status": wait_presence_get_text(navigator, By.ID, STATUS_ID),
            "organograma_name": wait_presence_get_text(navigator, By.ID, ORGANOGRAMA_NAME_ID),
            "material_id": wait_presence_get_text(navigator, By.ID, MATERIAL_ID),
            "material_name": wait_presence_get_text(navigator, By.ID, MATERIAL_NAME_ID),
            "nota_fiscal": wait_presence_get_text(navigator, By.ID, NOTA_FISCAL_ID),
            "serie_nota_fiscal": wait_presence_get_text(navigator, By.ID, SERIE_NOTA_FISCAL_ID),
            "incluido_por": wait_presence_get_text(navigator, By.ID, INCLUIDO_POR_ID),
            "incluido_em": wait_presence_get_text(navigator, By.ID, INCLUIDO_EM_ID),
            "modificado_por": wait_presence_get_text(navigator, By.ID, MODIFICADO_POR_ID),
            "ultima_modificacao": wait_presence_get_text(navigator, By.ID, ULTIMA_MODIFICACAO_ID),  
           }
    
    wait_and_click(navigator, By.NAME, RETURN_FORM_NAME)        
    
    return item_description

def organize_items_pagination(navigator, query_rows):
    items = []
    for _, row in enumerate(query_rows):
        if not isinstance(row, (list, tuple)):  
            row = [row]
        for _, _ in enumerate(row):
            item_description = get_item_description(navigator)
            items.append(item_description) 
    
    return items

def generate_query_json(navigator, query_rows=None, items=None):
    list_items = []

    if not items:
        list_items = organize_items_pagination(navigator, query_rows)
    else:
        list_items = items

    if list_items:
        return list_items 
    else:
        print("Nenhum item encontrado para retornar.")
        return []