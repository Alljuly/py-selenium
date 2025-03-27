from selenium.webdriver.common.by import By

from SMGPAT.utils import PLAQUETA_INIT_ID, PLAQUETA_FINAL_ID, BUTTON_QUERY
from SMGPAT.tools import generate_query_csv, load_plaquetas

def query_items(navigator, csv_path: str):
    plaqueta_init_fieldset = navigator.find_element(By.ID, PLAQUETA_INIT_ID)
    plaqueta_final_fieldset = navigator.find_element(By.ID, PLAQUETA_FINAL_ID)

    plaquetas = load_plaquetas(csv_path)
    plaqueta_init_fieldset.send_keys(plaquetas[0])
    plaqueta_final_fieldset.send_keys(plaquetas[1])

    button_query = navigator.find_element(By.NAME, BUTTON_QUERY)
    button_query.click()

    generate_query_csv()