from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SMGPAT.login import login
from SMGPAT.tools.webdriver_wait import wait_presence, wait_visibility
from SMGPAT.utils import BUTTON_NAV_INCORPORATION_ID, BUTTON_NAV_ITEM_XPATH
from SMGPAT.settings import URL_MODULES, URL_INCORPORATION
from SMGPAT.queries import query_item

from dotenv import load_dotenv

load_dotenv()

def main():
    navigator = login()
    wait = WebDriverWait(navigator, 30)
    print("oii")
    wait.until(navigator.current_url == URL_MODULES)
    print("opa")
    button_incorporation = wait_presence(navigator, By.ID, BUTTON_NAV_INCORPORATION_ID)
    button_incorporation.click()

    wait.until(navigator.current_url == URL_INCORPORATION)
    wait.until(EC.presence_of_element_located((By.XPATH, BUTTON_NAV_ITEM_XPATH)))
    button_incorporation_item = wait_visibility(navigator, By.XPATH, BUTTON_NAV_ITEM_XPATH)
    button_incorporation_item.click()
    CSV_PATH = 'SMGPAT/csv_query_test.csv'
    print(CSV_PATH)
    #query_item(navigator, CSV_PATH)
    
    input("enter para fechar\n")
main()