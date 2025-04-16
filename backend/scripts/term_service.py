from backend.tools import *
from backend.utils import *

TERMO_RESP_INPUT_ID = 'vTRMRESPID'
TERMO_FIRST_ROW_ID = 'span_CTLTRMRESPID_0001'
BUTTON_QUERY_TERM_NAME = 'BUTTON1'

def update_term(navigator, list_items, term):
    if list_items and term is not None:
        try:
            clear_and_send(navigator, By.ID, TERMO_RESP_INPUT_ID, term)
            wait_and_click(navigator, By.NAME, BUTTON_QUERY_TERM_NAME)

            wait_presence(navigator, By.ID, TERMO_FIRST_ROW_ID)

            wait_and_click(navigator, By.ID, UPDATE_TERMO_BTN_NAME)
            wait_and_click(navigator, By.ID, INCLUDE_ITEMS_FORM_ID)
            wait_and_click(navigator, By.XPATH, INPUT_RADIO_TERMO_FORM_XPATH)

            print(f"list items: {list_items}")

            for item in list_items:
                print(f'item: {item}')
                plaqueta = item['patplaqueta']
                clear_and_send(navigator, By.ID, INPUT_PATPLAQUETA_ID, plaqueta)
                wait_and_click(navigator, By.NAME, ADD_BUTTON_FORM_NAME)
            wait_and_click(navigator, By.NAME, RETURN_FORM_NAME)
        except Exception as e:
            print(f"[insert_items] Falha ao clicar no botão ou obter descrição: {e}")
            return None
    
    return None
