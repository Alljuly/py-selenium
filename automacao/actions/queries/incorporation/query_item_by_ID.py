from selenium.webdriver.common.by import By
from dotenv import load_dotenv

import time
from automacao.utils import PLAQUETA_INIT_ID, PLAQUETA_FINAL_ID, BUTTON_QUERY, BUTTON_VIZUALIZER_NAME
from automacao.tools import *

load_dotenv()


def fill_input_field(navigator, keys):
    clear_and_send(navigator, By.ID, PLAQUETA_INIT_ID, keys)
    clear_and_send(navigator, By.ID, PLAQUETA_FINAL_ID, keys)
    wait_and_click(navigator, By.NAME, BUTTON_QUERY)

    return

def query_item(navigator, data_json: dict = None, plaqueta = None): 
    if plaqueta is None:
        plaquetas_df = load_plaquetas(data_json)
        plaqueta = plaquetas_df["patplaqueta"].iloc[0]

    keys = str(plaqueta)

    fill_input_field(navigator, keys)
    
    time.sleep(2)
    result = wait_presence(navigator, By.ID, FIRST_ROW_QUERY_ID)
    res_json = []

    if result:
        show_row_button = wait_visibility(navigator, By.ID, FIRST_VIZUALIZER_NAME)
        if show_row_button:
            res_json = generate_query_json(navigator, query_rows=[show_row_button])

    return res_json


def query_random_item(navigator, plaqueta):
    print(f'plaquetaaaaaaa : {plaqueta}')
    fill_input_field(navigator, plaqueta)

    time.sleep(2)
    id_name_element = f'{BUTTON_VIZUALIZER_NAME}{1:04}'  
    try:
        wait_and_click(navigator, By.ID, id_name_element)
        item = get_item_description(navigator, 0)
        return item
    except Exception as e:
        print(f"[query_random_item] Falha ao clicar no botão ou obter descrição: {e}")
        return None

       
