from selenium import webdriver  
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from backend.settings import URL_NAV, URL_MODULES
import tempfile


def create_options():
    options = Options()
    options.add_argument("--headless=new")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    

    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    return options

def open_navigator():
    options = create_options()
    navigator = webdriver.Chrome(options=options)

    navigator.get(URL_NAV)
    return navigator

def open_navigator_with_cookies(cookies):
    options = create_options()
    navigator = webdriver.Chrome(options=options)
    #   navigator.maximize_window()

    navigator.get(URL_NAV)

    print("\n===== ADICIONANDO COOKIES NA NOVA SESSÃO =====")
    for cookie in cookies:
        try:
            navigator.add_cookie(cookie)
        except Exception as e:
            print(f"[ERRO] Cookie {cookie['name']} não pode ser adicionado: {e}")
    print("==============================================\n")

    navigator.get(URL_MODULES)
    return navigator
