"""
pegar o csv q eu criei
filtrar items baixados
ordenar item por centro de custo
criar transferencia
incluir items
fechar transferencia
"""
from selenium.webdriver.common.by import By
from SMGPAT.tools.webdriver_wait import *
from SMGPAT.tools import *
from SMGPAT.utils import INCLUDE_TRANSFERENCE_BUTTON_NAME,BACK_MODULE_BTN_NAME, TRANSFERENCE_BUTTON_NAME, PLAQUETA_REFERENCIA_ID, CLOSE_TRANSFERENCE_CONFIRM_MODAL_NAME



def confirm_tranference(navigator, transference_number : str):
    clear_and_send(navigator, By.ID, 'vTRANSFPATCODIGO', transference_number)
    wait_and_click(navigator, By.NAME, BUTTON_QUERY)

    last_transference = wait_presence_get_text(navigator, By.ID, LAST_TRANFERENCE_NUMBER_ID)
    
    if last_transference == transference_number:
        wait_and_click(navigator, By.NAME, FINALIZE_TRANSFERENCE_BUTTON_NAME)

def insert_items(navigator, list_items):
    wait_and_click(navigator, By.ID, INCLUDE_ITEMS_FORM_ID)

    wait_and_click(navigator, By.XPATH, INPUT_SEARCH_BY_PLAQUETA)

    for plaqueta in range(list_items):
        clear_and_send(navigator, By.ID, INPUT_PLAQUETA_ID, plaqueta)
        wait_and_click(navigator, By.NAME, INCLUDE_ITEM_BUTTON_NAME)

def create_transference(navigator, destiny, csv_path = None, items = None):
    list_items = []
    if not items:
        df = load_plaquetas(csv_path)
        list_items = df.tolist()
    else: 
        list_items = items   

    wait_and_click(navigator, By.NAME, INCLUDE_TRANSFERENCE_BUTTON_NAME)

    wait_and_click(navigator, By.NAME, TRANSFERENCE_BUTTON_NAME)

    transference_description = f'Transferencia de Patrimonio'

    clear_and_send(navigator, By.ID, INPUT_TEXT_AREA_TRANSFERENCE_ID, transference_description)

    clear_and_send(navigator, By.ID, PLAQUETA_REFERENCIA_ID, list_items[0])

    clear_and_send(navigator, By.ID, TRANSFERENCE_DESTINY_INPUT_ID, destiny)

    wait_and_click(navigator, By.NAME, CONFIRM_TRANSFERENCE_BUTTON_NAME)

    wait_and_click(navigator, By.NAME, CLOSE_TRANSFERENCE_CONFIRM_MODAL_NAME)

    insert_items(navigator, list_items)

    wait_and_click(navigator, By.NAME, BACK_MODULE_BTN_NAME)

    transference_identifier = wait_presence_get_text(navigator, By.ID, LAST_TRANFERENCE_NUMBER_ID)
    return transference_identifier


    


    
