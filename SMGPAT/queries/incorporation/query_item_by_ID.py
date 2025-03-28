from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC


from SMGPAT.utils import PLAQUETA_INIT_ID, BUTTON_QUERY, ROW_QUERY_ID, BUTTON_VIZUALIZER_NAME
from SMGPAT.tools import *
from time import sleep

load_dotenv()

def query_item(navigator, csv_path: str):

    plaqueta_init_fieldset = navigator.find_element(By.ID, PLAQUETA_INIT_ID)

    plaquetas = load_plaquetas(csv_path)
    plaqueta_init_fieldset.send_keys(str(plaquetas[0]))

    button_query = navigator.find_element(By.NAME, BUTTON_QUERY)
    button_query.click()

    first_row =  f'{ROW_QUERY_ID}0001'
    a = wait_visibility(navigator, By.ID, first_row)

    query_rows = []
    identifier =  f'{BUTTON_VIZUALIZER_NAME}{1:04}'
    row = ''
    row = wait_visibility(navigator, By.ID, identifier)
    if EC.presence_of_element_located(row):
        query_rows.append(row)
        generate_query_csv(navigator, query_rows)

# navegação no sistema

