from selenium.webdriver.common.by import By

from src.utils import PLAQUETA_INIT_ID, PLAQUETA_FINAL_ID, BUTTON_QUERY, GROUP_SIZE
from src.tools import generate_query_csv, load_plaquetas
from src.tools import clear_and_send
from src.tools.webdriver_wait import wait_and_click

from .query_item_by_ID import query_random_item


def query_sequential_list_items(navigator, csv_path: str):
    plaquetas_df = load_plaquetas(csv_path)
    plaquetas_sorted = plaquetas_df.sort_values(by="patplaqueta") 
    plaquetas = plaquetas_sorted["patplaqueta"].tolist()
   
    count_plaquetas = len(plaquetas)

    grouped = []
    if count_plaquetas > GROUP_SIZE:
        grouped = [plaquetas[i:i + GROUP_SIZE] for i in range(0, len(plaquetas), GROUP_SIZE)]
    else:
        grouped = [plaquetas]

    key = str(plaquetas_sorted["patplaqueta"].iloc[0])
    clear_and_send(navigator, By.ID, PLAQUETA_INIT_ID, key)

    key = str(plaquetas_sorted["patplaqueta"].iloc[-1])
    clear_and_send(navigator, By.ID, PLAQUETA_FINAL_ID, key)

    wait_and_click(navigator, By.NAME, BUTTON_QUERY)

    return generate_query_csv(navigator, grouped)

def query_random_list_items(navigator, csv_path: str):
    plaquetas_df = load_plaquetas(csv_path)
    plaquetas_sorted = plaquetas_df.sort_values(by="patplaqueta") 
    plaquetas = plaquetas_sorted["patplaqueta"].tolist()

    items = []

    for i, _ in enumerate(plaquetas):
        item_description = query_random_item(navigator, plaquetas[i])
        if item_description:
            items.append(item_description)
    
    if items:
        generate_query_csv(navigator, items=items)
        
    return items
