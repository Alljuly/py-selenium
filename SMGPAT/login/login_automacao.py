from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os


load_dotenv()

URL = os.getenv("URL_LOGIN_EJADE")

navigator = webdriver.Chrome()
navigator.maximize_window()
navigator.get(URL)

def login():
    LOGIN_FIELDSET_ID = "CTLUSULOGIN"
    PASSWORD_FIELDSET_ID = "CTLUSUSENHA"
    BUTTOM_FORM_LOGIN_NAME = "BUTTON1"
    BUTTOM_FORM_MODULE_ID = 'IMAGEMODULO_0002'

    login_fieldset = navigator.find_element(By.ID, LOGIN_FIELDSET_ID)
    password_fieldset = navigator.find_element(By.ID, PASSWORD_FIELDSET_ID)

    USER_LOGIN = os.getenv('USER_LOGIN_EJADE')
    PASSWORD_LOGIN = os.getenv('PASSWORD_LOGIN_EJADE')

    login_fieldset.send_keys(USER_LOGIN)
    password_fieldset.send_keys('PASSWORD_LOGIN_EJADE')

    button_form = navigator.find_element(By.NAME, BUTTOM_FORM_NAME)

    button_form.click()

    button_form = navigator.find_element(By.ID, BUTTOM_FORM_MODULE_ID)

return navigator


