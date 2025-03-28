from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SMGPAT.login import login_patrimonio
from SMGPAT.settings import URL_MODULES, URL_INCORPORATION
from SMGPAT.queries import query_item, query_random_list_items, query_sequential_list_items
from SMGPAT.utils import CSV_PATH

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
        
            query_item(navigator, CSV_PATH)

            input("enter para fechar\n")

        case 2:
            navigator.get(URL_INCORPORATION)
            wait.until(EC.url_matches(URL_INCORPORATION))
        
            #query_random_list_items(navigator, CSV_PATH)
            query_sequential_list_items(navigator, CSV_PATH)

            input("enter para fechar\n")

main()