import csv
from selenium.webdriver.common.by import By

from SMGPAT.utils import *

from datetime import datetime

def generate_query_csv(navigator):
    query_table = navigator.find_element(By.ID, TABLE_RESULT_ID)
    query_rows = []
    for rows in query_table:
        query_rows.append(rows)
    
    list_items = []
    if len(query_rows) > 1:
        for i in enumerate(query_rows[1:]):
            id_name_element = f'{BUTTON_VIZUALIZER_NAME}{i+1:03}'
            button_vizualizer = navigator.find_element(By.NAME, id_name_element)
            button_vizualizer.click()
            
            item_description = {
                    "patplaqueta": navigator.find_element(By.ID, PATPLAQUETA_ID).text,
                    "status": navigator.find_element(By.ID, STATUS_ID).text,
                    "organograma_name": navigator.find_element(By.ID, ORGANOGRAMA_NAME_ID).text,
                    "material_id": navigator.find_element(By.ID, MATERIAL_ID).text,
                    "material_name": navigator.find_element(By.ID, MATERIAL_NAME_ID).text,
                    "nota_fiscal": navigator.find_element(By.ID, NOTA_FISCAL_ID).text,
                    "serie_nota_fiscal": navigator.find_element(By.ID, SERIE_NOTA_FISCAL_ID).text,
                    "numero_empenho": navigator.find_element(By.ID, NUMERO_EMPENHO_ID).text,
                    "ano_empenho": navigator.find_element(By.ID, ANO_EMPENHO_ID).text,
                    "incluido_por": navigator.find_element(By.ID, INCLUIDO_POR_ID).text,
                    "incluido_em": navigator.find_element(By.ID, INCLUIDO_EM_ID).text,
                    "modificado_por": navigator.find_element(By.ID, MODIFICADO_POR_ID).text,
                    "ultima_modificacao": navigator.find_element(By.ID, ULTIMA_MODIFICACAO_ID).text
                    }
            list_items.append(item_description)

            button_return = navigator.find_element(By.NAME, RETURN_FORM_NAME)
            button_return.click()
    
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_csv = f'resultado_consulta_{current_time}.csv' 
        header = list(item_description.keys())
        with open(result_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for item in list_items:
                writer.writerow(item)
