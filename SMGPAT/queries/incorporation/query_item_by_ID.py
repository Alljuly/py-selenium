from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC


from SMGPAT.utils import PLAQUETA_INIT_ID, BUTTON_QUERY, ROW_QUERY_ID, BUTTON_VIZUALIZER_NAME
from SMGPAT.tools import *
# from SMGPAT.tools.webdriver_wait import wait_and_click

load_dotenv()

def query_item(navigator, csv_path: str):

    plaquetas = load_plaquetas(csv_path)
    keys = str(plaquetas["numero_plaqueta"].iloc[0])
    print(keys)
    clear_and_send(navigator, By.ID, PLAQUETA_INIT_ID, keys)
    button_query = wait_presence(navigator, By.NAME, BUTTON_QUERY)
    button_query.click()

    first_row_identifier =  f'{ROW_QUERY_ID}0001'
    first_row = wait_visibility(navigator, By.ID, first_row_identifier)

    if first_row:
        query_rows = []
        identifier =  f'{BUTTON_VIZUALIZER_NAME}{1:04}'
        show_row_button = wait_visibility(navigator, By.ID, identifier)
        if show_row_button:
            query_rows.append(show_row_button)
            generate_query_csv(navigator, query_rows)

# navegação no sistema

