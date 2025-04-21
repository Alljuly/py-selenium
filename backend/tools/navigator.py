from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from backend.settings import URL_NAV, URL_MODULES

def get_webdriver():
    options = Options()
    options.headless = True  # Roda o Firefox no modo headless (sem interface gráfica)
    options.add_argument("--disable-gpu")  # Desabilita GPU, embora no modo headless não seja necessário
    options.add_argument("--no-sandbox")  # Necessário para contêineres Docker ou ambiente restrito
    options.add_argument("--disable-dev-shm-usage")  # Previne problemas de memória em containers
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--single-process")

    # Inicializando o WebDriver com o Firefox
    driver = webdriver.Firefox(options=options)
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
