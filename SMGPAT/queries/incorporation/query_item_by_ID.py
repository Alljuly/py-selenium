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

# Constantes para a descricao do item pesquisado
PATPLAQUETA_ID = 'PATPLAQUETA'
STATUS_ID = 'span_PATSITUACAO'
ORGANOGRAMA_NAME_ID = 'span_PATORGNADMNOME'
MATERIAL_ID = 'span_vMATGRUPOCODIGO'
MATERIAL_NAME_ID = 'span_MATERIALNOME'
NOTA_FISCAL_ID = 'span_PATNOTAFISCALNMR'
SERIE_NOTA_FISCAL_ID = 'span_PATNOTAFISCALSERIE'
NUMERO_EMPENHO_ID = 'span_W0378CTLPATRIMONIOLIQEMPENHONMR_0001'
ANO_EMPENHO_ID = 'span_W0378CTLPATRIMONIOLIQEMPENHOANO_0001'
INCLUIDO_POR_ID = 'span_PATINCLUIDOPORNOME'
INCLUIDO_EM_ID = 'span_PATINCLUIDOEM'
MODIFICADO_POR_ID = 'span_PATALTERADOPORNOME'
ULTIMA_MODIFICACAO_ID = 'span_PATINCLUIDOEM'

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
