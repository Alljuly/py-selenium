from selenium.webdriver.common.by import By
from dotenv import load_dotenv

from backend.utils import PLAQUETA_INIT_ID, PLAQUETA_FINAL_ID, BUTTON_QUERY, BUTTON_VIZUALIZER_NAME
from backend.tools import *

load_dotenv()

import time
def fill_input_field(navigator, keys):
    clear_and_send(navigator, By.ID, PLAQUETA_INIT_ID, keys)
    clear_and_send(navigator, By.ID, PLAQUETA_FINAL_ID, keys)
    wait_and_click(navigator, By.NAME, BUTTON_QUERY)

    return


def query_random_item(navigator, plaqueta):
    fill_input_field(navigator, plaqueta)

    try:
        time.sleep(2) 
        wait_and_click(navigator, By.XPATH, BUTTON_VIZUALIZER_XPATH )
        item = get_item_description(navigator)
        return item
    except Exception as e:
        print(f"[query_random_item] Falha ao clicar no botão ou obter descrição: {e}")
        return None

       
