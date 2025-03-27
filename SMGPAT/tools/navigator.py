from selenium import webdriver
from SMGPAT.settings import URL_NAV

def get_navigator():
    options = webdriver.ChromeOptions()
    options.add_argument("-remote-debugging-port=9222")
    options.add_argument("--user-data-dir=C:\\selenium_profile")
    navigator = webdriver.Chrome(options=options)
    navigator.maximize_window()
    navigator.get(URL_NAV)
    return navigator
