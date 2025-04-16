from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from backend.scripts import *
from backend.settings import URL_MODULES

from backend.tools import open_navigator, clear_and_send, wait_and_click
from backend.utils import LOGIN_FIELDSET_ID,PASSWORD_FIELDSET_ID, BUTTOM_FORM_MODULE_ID, BUTTOM_FORM_LOGIN_NAME


import traceback

def login_and_get_cookies(username, password):

    try:
        navigator = open_navigator()

        clear_and_send(navigator, By.ID, LOGIN_FIELDSET_ID, username)

        clear_and_send(navigator, By.ID, PASSWORD_FIELDSET_ID, password)

        wait_and_click(navigator, By.NAME, BUTTOM_FORM_LOGIN_NAME)

        wait_and_click(navigator, By.ID, BUTTOM_FORM_MODULE_ID)

        wait = WebDriverWait(navigator, 30)
        wait.until(EC.url_matches(URL_MODULES))
        if(EC.url_matches(URL_MODULES)):
            cookies = navigator.get_cookies()
        
            navigator.quit()
            return cookies
        
        return None

    except Exception as e:
        print("[ERRO NO LOGIN]", e)
        traceback.print_exc()
        return None


