from selenium import webdriver  
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from backend.settings import URL_NAV, URL_MODULES
import tempfile

CHROMIUM_PATH = "/usr/bin/chromium"
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

def open_navigator():
    options = Options()
    options.add_argument("--headless=new")  # Mais leve que o antigo headless
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--single-process")
    options.add_argument("--remote-debugging-port=9222")
    
    options.binary_location = CHROMIUM_PATH

    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    service = Service(executable_path=CHROMEDRIVER_PATH)
    navigator = webdriver.Chrome(service=service, options=options)

    navigator.get(URL_NAV)
    return navigator


def open_navigator_with_cookies(cookies):
    options = Options()
    options.add_argument("--headless=new") 
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--single-process")
    options.add_argument("--remote-debugging-port=9222")

    options.binary_location = CHROMIUM_PATH

    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    service = Service(executable_path=CHROMEDRIVER_PATH)
    navigator = webdriver.Chrome(service=service, options=options)

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
