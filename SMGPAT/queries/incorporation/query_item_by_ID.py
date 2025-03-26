from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login.login_automacao import navigator
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

URL_MODULES = os.getenv('URL_MODULES')
URL_INCORPORATION = os.getenv('URL_INCORPORATION')

CSV_PATH = 'SMGPAT/csv_query_test.csv'

PLAQUETA_INIT_ID = 'vPATPLAQUETAINI'
PLAQUETA_FINAL_ID = 'vPATPLAQUETAFIN'
BUTTON_QUERY = 'BTNCONSULTAR'

def load_plaquetas(csv_path: str):
    plaqueta_init_value = read_csv(csv_path, usecols['plaqueta_inicial'])
    plaqueta_final_value = read_csv(csv_path, usecols['plaqueta_final'])

    return [plaqueta_init_value, plaqueta_final_value]

def query_item(csv_path: str):
    plaqueta_init_fieldset = navigator.find_element(BY.ID, PLAQUETA_INIT_ID)
    plaqueta_final_fieldset = navigator.find_element(BY.ID, PLAQUETA_FINAL_ID)

    plaquetas = load_plaquetas(csv_path)
    plaqueta_init_fieldset.send_keys(plaquetas[0])
    plaqueta_final_fieldset.send_keys(plaquetas[0])

    button_query = navigator.find_element(BY.NAME, BUTTON_QUERY)
    button_query.click()

def query_items():
    plaqueta_init_fieldset = navigator.find_element(BY.ID, PLAQUETA_INIT_ID)
    plaqueta_final_fieldset = navigator.find_element(BY.ID, PLAQUETA_FINAL_ID)

    plaquetas = load_plaquetas(csv_path)
    plaqueta_init_fieldset.send_keys(plaquetas[0])
    plaqueta_final_fieldset.send_keys(plaquetas[1])

    button_query = navigator.find_element(BY.NAME, BUTTON_QUERY)
    button_query.click()
       
# navegação no sistema
if navigator.current_url == URL_MODULES:

    BUTTON_NAV_INCORPORATION_ID = 'ext-gen23'
    BUTTON_NAV_ITEM_ID = 'ext-gen151'

    button_incorporation_item = navigator.find_element(BY.ID, BUTTON_NAV_INCORPORATION_ID)
    button_incorporation_item.click()
    button_incorporation_item = navigator.find_element(BY.ID, BUTTON_NAV_ITEM_ID)
    button_incorporation_item.click()
    
    query_item(CSV_PATH)

if navigator.current_url == URL_INCORPORATION:
    query_item(CSV_PATH)
