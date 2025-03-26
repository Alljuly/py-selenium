from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login.login_automacao import navigator
from datetime import datetime
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

URL_MODULES = os.getenv('URL_MODULES')
URL_INCORPORATION = os.getenv('URL_INCORPORATION')

CSV_PATH = 'SMGPAT/csv_query_test.csv'

PLAQUETA_INIT_ID = 'vPATPLAQUETAINI'
PLAQUETA_FINAL_ID = 'vPATPLAQUETAFIN'
BUTTON_QUERY = 'BTNCONSULTAR'

TABLE_RESULT_ID = 'GriddetalhesContainerTbl'
BUTTON_VIZUALIZER_NAME = 'vVISUALIZAR_0'

def generate_query_csv():
    query_table = navigator.find_element(By.ID, TABLE_RESULT_ID)
    query_rows = []
    for rows in query_table:
        query_rows.append(rows)
    
    list_items = []
    if len(query_rows) > 1:
         for i, row in enumerate(query_rows[1:]):
            id_name_element = f'{BUTTON_VIZUALIZER_NAME}{i+1:03}'
            button_vizualizer = navigator.find_element(By.NAME, id_name_element)
            button_vizualizer.click()
            
            item_description = {
                    "patplaqueta": navigator.find_element(By.ID, 'PATPLAQUETA'),
                    "status": navigator.find_element(By.ID, 'span_PATSITUACAO'),
                    "organograma_name": navigator.find_element(By.ID, 'span_PATORGNADMNOME'),
                    "material_id": navigator.find_element(By.ID, 'span_vMATGRUPOCODIGO'),
                    "material_name": navigator.find_element(By.ID, 'span_MATERIALNOME'),
                    "nota_fiscal": navigator.find_element(By.ID, 'span_PATNOTAFISCALNMR'),
                    "serie_nota_fiscal": navigator.find_element(By.ID, 'span_PATNOTAFISCALSERIE'),
                    "numero_empenho": navigator.find_element(By.ID, 'span_W0378CTLPATRIMONIOLIQEMPENHONMR_0001'),
                    "ano_empenho": navigator.find_element(By.ID, 'span_W0378CTLPATRIMONIOLIQEMPENHOANO_0001'),
                    "incluido_por": navigator.find_element(By.ID, 'span_PATINCLUIDOPORNOME'),
                    "incluido_em": navigator.find_element(By.ID, 'span_PATINCLUIDOEM'),
                    "modificado_por": navigator.find_element(by.ID, 'span_PATALTERADOPORNOME'),
                    "ultima_modificacao": navigator.find_element(By.ID, 'span_PATINCLUIDOEM')
                    }
            list_items.append(item_description)
    
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    result_csv = f'resultado_consulta_{current_time}.csv' 
    header = list(item_description.keys())
    with open(result_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for item in list_items:
            writer.writerow(item)


def load_plaquetas(csv_path: str):
    df = pd.read_csv(csv_path, usecols=['plaqueta_inicial', 'plaqueta_final'])
    plaqueta_init_value = df['plaqueta_inicial'].iloc[0]
    plaqueta_final_value = df['plaqueta_final'].iloc[0] 

    return plaqueta_init_value, plaqueta_final_value

def query_item(csv_path: str):
    plaqueta_init_fieldset = navigator.find_element(By.ID, PLAQUETA_INIT_ID)
    plaqueta_final_fieldset = navigator.find_element(By.ID, PLAQUETA_FINAL_ID)

    plaquetas = load_plaquetas(csv_path)
    plaqueta_init_fieldset.send_keys(plaquetas[0])
    plaqueta_final_fieldset.send_keys(plaquetas[0])

    button_query = navigator.find_element(By.NAME, BUTTON_QUERY)
    button_query.click()

    generate_query_csv()

def query_items():
    plaqueta_init_fieldset = navigator.find_element(By.ID, PLAQUETA_INIT_ID)
    plaqueta_final_fieldset = navigator.find_element(By.ID, PLAQUETA_FINAL_ID)

    plaquetas = load_plaquetas(csv_path)
    plaqueta_init_fieldset.send_keys(plaquetas[0])
    plaqueta_final_fieldset.send_keys(plaquetas[1])

    button_query = navigator.find_element(By.NAME, BUTTON_QUERY)
    button_query.click()

    generate_query_csv()

# navegação no sistema
if navigator.current_url == URL_MODULES:

    BUTTON_NAV_INCORPORATION_ID = 'ext-gen23'
    BUTTON_NAV_ITEM_ID = 'ext-gen151'

    button_incorporation_item = navigator.find_element(By.ID, BUTTON_NAV_INCORPORATION_ID)
    button_incorporation_item.click()
    button_incorporation_item = navigator.find_element(By.ID, BUTTON_NAV_ITEM_ID)
    button_incorporation_item.click()
    
    query_item(CSV_PATH)

if navigator.current_url == URL_INCORPORATION:
    query_item(CSV_PATH)
