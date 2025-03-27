from selenium.webdriver.common.by import By
from dotenv import load_dotenv

from SMGPAT.utils import PLAQUETA_FINAL_ID, PLAQUETA_INIT_ID, BUTTON_QUERY
from SMGPAT.tools import *
from time import sleep

load_dotenv()

def query_item(navigator, csv_path: str):
    sleep(1)
    plaqueta_init_fieldset = navigator.find_element(By.ID, PLAQUETA_INIT_ID)
    plaqueta_final_fieldset = navigator.find_element(By.ID, PLAQUETA_FINAL_ID)

    sleep(1)
    plaquetas = load_plaquetas(csv_path)
    plaqueta_init_fieldset.send_keys(plaquetas[0])
    plaqueta_final_fieldset.send_keys(plaquetas[0])
    sleep(1)

    button_query = navigator.find_element(By.NAME, BUTTON_QUERY)
    button_query.click()
    sleep(1)

    generate_query_csv()

# navegação no sistema

