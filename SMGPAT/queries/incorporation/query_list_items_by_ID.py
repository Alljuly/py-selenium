from selenium.webdriver.common.by import By

from SMGPAT.utils import PLAQUETA_INIT_ID, ROW_QUERY_ID, BUTTON_QUERY, BUTTON_VIZUALIZER_NAME, GROUP_SIZE
from SMGPAT.tools import generate_query_csv, load_plaquetas
from SMGPAT.tools.webdriver_wait import wait_visibility, wait_presence 
from SMGPAT.tools import clear_and_send

def query_random_list_items(navigator, csv_path: str):
    plaquetas = load_plaquetas(csv_path)
    count_plaquetas = len(plaquetas)
    grouped = plaquetas.sort()
    print(plaquetas)
    if count_plaquetas > GROUP_SIZE:
        grouped = [plaquetas[i:i + GROUP_SIZE] for i in range(0, len(plaquetas), GROUP_SIZE)]

    

    