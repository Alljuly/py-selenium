from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.actions import *
from src.settings import URL_MODULES, URL_INCORPORATION, URL_TRANSFERENCE_MODULE
from src.utils import CSV_PATH

from dotenv import load_dotenv

load_dotenv()

def main():
    navigator = login_patrimonio()
    wait = WebDriverWait(navigator, 30)
    
    wait.until(EC.url_matches(URL_MODULES))
    event = 1

    match event:
        case 1: 
            navigator.get(URL_INCORPORATION)
            wait.until(EC.url_matches(URL_INCORPORATION))
        
            csv_res = query_random_list_items(navigator, CSV_PATH)

            print(csv_res)

        case 2:
            navigator.get(URL_INCORPORATION)
            wait.until(EC.url_matches(URL_INCORPORATION))
        
            list_items_path = query_random_list_items(navigator, CSV_PATH) 

            if list_items_path:
                navigator.get(URL_TRANSFERENCE_MODULE)
                list_items = order_items(list_items_path) 
                for item_group in list_items:
                    reference_plaq = item_group[0]['patplaqueta']
                    transf = create(navigator,destination, reference_plaq=reference_plaq) 
                    items = [item['patplaqueta'] for item in item_group]
                    update(navigator,transf, items)

    input("enter para fechar \n")

main()