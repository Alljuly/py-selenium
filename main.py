from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SMGPAT.login import login_patrimonio
from SMGPAT.settings import URL_MODULES, URL_INCORPORATION, URL_TRANSFERENCE_MODULE
from SMGPAT.queries import query_item, query_random_list_items, query_sequential_list_items
from SMGPAT.utils import CSV_PATH
from SMGPAT.moviment import create, update

from dotenv import load_dotenv

load_dotenv()

def main():
    navigator = login_patrimonio()
    wait = WebDriverWait(navigator, 30)
    
    wait.until(EC.url_matches(URL_MODULES))
    event = 3
    match event:
        case 1: 
            navigator.get(URL_INCORPORATION)
            wait.until(EC.url_matches(URL_INCORPORATION))
        
            query_item(navigator, CSV_PATH)

        case 2:
            navigator.get(URL_INCORPORATION)
            wait.until(EC.url_matches(URL_INCORPORATION))
        
            query_random_list_items(navigator, CSV_PATH)
            query_sequential_list_items(navigator, CSV_PATH)

        case 3:
            navigator.get(URL_TRANSFERENCE_MODULE)
            #transf = create(navigator,'5214', reference_plaq='83130')
            #print(transf)

            update(navigator, '711', ['83130', '71744', '172804'])

            

    input("enter para fechar \n")

main()