from selenium.webdriver.common.by import By

from automacao.utils import PLAQUETA_INIT_ID, PLAQUETA_FINAL_ID, BUTTON_QUERY, GROUP_SIZE
from automacao.tools import generate_query_json, load_plaquetas
from automacao.tools import clear_and_send
from automacao.tools.webdriver_wait import wait_and_click

from .query_item_by_ID import query_random_item


# def query_sequential_list_items(navigator, csv_path: str):
#     plaquetas_df = load_plaquetas(csv_path)
#     plaquetas_sorted = plaquetas_df.sort_values(by="patplaqueta") 
#     plaquetas = plaquetas_sorted["patplaqueta"].tolist()
   
#     count_plaquetas = len(plaquetas)

#     grouped = []
#     if count_plaquetas > GROUP_SIZE:
#         grouped = [plaquetas[i:i + GROUP_SIZE] for i in range(0, len(plaquetas), GROUP_SIZE)]
#     else:
#         grouped = [plaquetas]

#     key = str(plaquetas_sorted["patplaqueta"].iloc[0])
#     clear_and_send(navigator, By.ID, PLAQUETA_INIT_ID, key)

#     key = str(plaquetas_sorted["patplaqueta"].iloc[-1])
#     clear_and_send(navigator, By.ID, PLAQUETA_FINAL_ID, key)

#     wait_and_click(navigator, By.NAME, BUTTON_QUERY)

#     return generate_query_csv(navigator, grouped)

def query_list_items_service(navigator, plaquetas_data):
    plaquetas_df = load_plaquetas(plaquetas_data)
    plaquetas_sorted = plaquetas_df.sort_values(by="patplaqueta") 
    print('sorted plaquetas', plaquetas_sorted)
    plaquetas = plaquetas_sorted["patplaqueta"].astype(str).tolist()
    print('plaquetas', plaquetas)

    items = []

    for plaqueta in plaquetas:
        item_description = query_random_item(navigator, plaqueta)
        print(f'item description: {item_description}')
        if item_description:
            items.append(item_description)
    
    result_json = []
    if items:
        result_json = generate_query_json(navigator, items=items)
        
    return result_json
