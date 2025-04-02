"""
pegar o csv q eu criei
filtrar items baixados
ordenar item por centro de custo
criar transferencia
incluir items
fechar transferencia
"""
from SMGPAT.utils import INCLUDE_TRANSFERENCE_BUTTON_NAME, BACK_POPUP_TRANFERENCE_XPATH,\
TRANSFERENCE_INPUT_CODE_ID, TRANSFERENCE_BUTTON_NAME, PLAQUETA_REFERENCIA_ID,\
ORIGEN_REFERENCIA_ID


from SMGPAT.settings import URL_TRANSFERENCE, URL_TRANSFERENCE_MODULE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from SMGPAT.tools.webdriver_wait import *
from SMGPAT.tools import *

#from time import sleep

def find(navigator, transference_number):
    if not EC.url_matches(URL_TRANSFERENCE_MODULE):
        navigator.get(URL_TRANSFERENCE_MODULE)

    clear_and_send(navigator, By.ID, TRANSFERENCE_INPUT_CODE_ID, transference_number)
    move_and_click(navigator, By.NAME, BUTTON_QUERY)

    last_transference = wait_visibility_and_get_text(navigator, By.ID, LAST_TRANFERENCE_NUMBER_ID)
    if last_transference == transference_number:
        return True
    
    return False

def delete(navigator, transference_number):
    if find(navigator, transference_number):
        wait_and_click(navigator, By.ID, LAST_TRANFERENCE_NUMBER_ID)

def confirm(navigator, transference_number):
    if find(navigator, transference_number):
        wait_and_click(navigator, By.NAME, FINALIZE_TRANSFERENCE_BUTTON_NAME)

def update(navigator, transference_number, list_items):
    transference_exists = True
    if EC.url_matches(URL_TRANSFERENCE_MODULE):
        transference_exists = find(navigator, transference_number)

    if transference_exists and EC.url_contains(URL_TRANSFERENCE):
        wait_and_click(navigator, By.ID, INCLUDE_ITEMS_FORM_ID)
        wait_and_click(navigator, By.XPATH, INPUT_SEARCH_BY_PLAQUETA)
    
        for plaqueta in range(list_items):
            clear_and_send(navigator, By.ID, INPUT_PLAQUETA_ID, plaqueta)
            wait_and_click(navigator, By.NAME, INCLUDE_ITEM_BUTTON_NAME)

def create(navigator, destiny, reference_orig = None, reference_plaq = None):
    reference_id = ''
    if reference_plaq:
        reference_id = PLAQUETA_REFERENCIA_ID
    elif reference_orig:
        reference_id = ORIGEN_REFERENCIA_ID
    
    referece = reference_orig or reference_plaq
    
    wait_and_click(navigator, By.NAME, INCLUDE_TRANSFERENCE_BUTTON_NAME)

    wait_and_click(navigator, By.NAME, TRANSFERENCE_BUTTON_NAME)

    transference_description = f'Transferencia de Patrimonio'

    clear_and_send(navigator, By.ID, INPUT_TEXT_AREA_TRANSFERENCE_ID, transference_description)

    clear_and_send(navigator, By.ID, reference_id, referece)

    clear_and_send(navigator, By.ID, TRANSFERENCE_DESTINY_INPUT_ID, destiny)

    wait_and_click(navigator, By.NAME, CONFIRM_TRANSFERENCE_BUTTON_NAME)

    wait_and_click(navigator, By.ID, CLOSE_POPUP_MODULE_BTN_ID)
 
    wait_and_click(navigator, By.NAME, BACK_MODULE_BTN_NAME)

    transference_number = wait_presence_get_text(navigator, By.NAME, LAST_TRANFERENCE_NUMBER_ID)

    return transference_number
   




    


    
# seletor js document.querySelector()