from selenium.webdriver.common.by import By
from dotenv import load_dotenv

import time
from src.utils import PLAQUETA_INIT_ID, PLAQUETA_FINAL_ID, BUTTON_QUERY, ROW_QUERY_ID, BUTTON_VIZUALIZER_NAME
from src.tools import *

load_dotenv()


def fill_input_field(navigator, keys):
    clear_and_send(navigator, By.ID, PLAQUETA_INIT_ID, keys)
    clear_and_send(navigator, By.ID, PLAQUETA_FINAL_ID, keys)
    button_query = wait_presence(navigator, By.NAME, BUTTON_QUERY)
    button_query.click()

    
    return

def query_item(navigator, csv_path: str = None): 
    path_csv = None
    plaquetas = load_plaquetas(csv_path)
    keys = str(plaquetas["patplaqueta"].iloc[0])

    fill_input_field(navigator, keys)
    
    time.sleep(2)
    result = wait_presence(navigator, By.ID, FIRST_ROW_QUERY_ID)
    if result:
        query_rows = []
        show_row_button = wait_visibility(navigator, By.ID, FIRST_VIZUALIZER_NAME)
        if show_row_button:
            query_rows.append(show_row_button)
            path_csv = generate_query_csv(navigator, query_rows)

    return path_csv

def query_random_item(navigator, plaquetas: str):
    item = None
    keys = str(plaquetas)    
    first_row = fill_input_field(navigator, keys)

    if first_row:
        time.sleep(2)
        element = wait_presence(navigator, By.ID, FIRST_VIZUALIZER_NAME)
        if element is not None:
            item = get_item_description(navigator, 0)
       
    return item
