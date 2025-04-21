from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from backend.settings import URL_NAV, URL_MODULES

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def get_webdriver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    try:
        driver = webdriver.Firefox(options=options)
    except Exception as e:
        print(f"Error initializing the Firefox WebDriver: {e}")
        raise
    return driver


def open_navigator():
    driver = get_webdriver()
    driver.get(URL_NAV)
    return driver

def open_navigator_with_cookies(cookies):
    driver = get_webdriver()
    driver.get(URL_NAV)

    print("\n===== ADICIONANDO COOKIES NA NOVA SESSÃO =====")
    for cookie in cookies:
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"[ERRO] Cookie {cookie['name']} não pode ser adicionado: {e}")
    print("==============================================\n")

    driver.get(URL_MODULES)
    return driver
