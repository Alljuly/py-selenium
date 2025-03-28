from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SMGPAT.login import login_patrimonio
from SMGPAT.settings import URL_MODULES, URL_INCORPORATION
from SMGPAT.queries import query_item
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
main()