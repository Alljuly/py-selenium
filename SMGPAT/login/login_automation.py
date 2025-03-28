from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SMGPAT.tools import get_navigator
from SMGPAT.utils import LOGIN_FIELDSET_ID,PASSWORD_FIELDSET_ID,BUTTOM_FORM_LOGIN_NAME,BUTTOM_FORM_MODULE_ID
from SMGPAT.settings import *



def login_patrimonio():
    navigator = get_navigator()

    wait = WebDriverWait(navigator, 30)

    login_fieldset = wait.until(EC.element_to_be_clickable((By.ID, LOGIN_FIELDSET_ID)))
    password_fieldset = wait.until(EC.element_to_be_clickable((By.ID, PASSWORD_FIELDSET_ID)))

    login_fieldset.send_keys(USER_LOGIN)
    password_fieldset.send_keys(PASSWORD_LOGIN)

    login_form = wait.until(EC.element_to_be_clickable((By.NAME, BUTTOM_FORM_LOGIN_NAME)))
    login_form.click()

    module_form = wait.until(EC.element_to_be_clickable((By.ID, BUTTOM_FORM_MODULE_ID)))
    module_form.click()

    return navigator