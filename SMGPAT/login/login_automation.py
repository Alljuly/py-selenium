from selenium.webdriver.common.by import By

from SMGPAT.tools import get_navigator, clear_and_send, wait_and_click
from SMGPAT.utils import LOGIN_FIELDSET_ID,PASSWORD_FIELDSET_ID, BUTTOM_FORM_MODULE_ID, BUTTOM_FORM_LOGIN_NAME
from SMGPAT.settings import USER_LOGIN, PASSWORD_LOGIN

def login_patrimonio():
    navigator = get_navigator()

    clear_and_send(navigator, By.ID, LOGIN_FIELDSET_ID, USER_LOGIN)
    clear_and_send(navigator, By.ID, PASSWORD_FIELDSET_ID, PASSWORD_LOGIN)

    wait_and_click(navigator, By.NAME, BUTTOM_FORM_LOGIN_NAME)
    wait_and_click(navigator, By.ID, BUTTOM_FORM_MODULE_ID)
    
    return navigator