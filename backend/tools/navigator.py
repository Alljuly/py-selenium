from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from backend.settings import URL_NAV, URL_MODULES, BROWSERLESS_URL

def open_navigator():
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--single-process")
    
    
    capabilities = DesiredCapabilities.CHROME
    capabilities['browserName'] = 'chrome'
    capabilities['goog:chromeOptions'] = {
        "args": [
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-software-rasterizer",
            "--disable-background-networking",
            "--disable-features=VizDisplayCompositor",
            "--single-process"
        ],
        "w3c": False
    }

    driver = webdriver.Remote(
        command_executor=BROWSERLESS_URL,
        options=options,
        keep_alive=True  
    )

    driver.get(URL_NAV)
    return driver


def open_navigator_with_cookies(cookies):
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--single-process")
    
    # Configurações do WebDriver com WebSocket
    capabilities = DesiredCapabilities.CHROME
    capabilities['browserName'] = 'chrome'
    capabilities['goog:chromeOptions'] = {
        "args": [
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-software-rasterizer",
            "--disable-background-networking",
            "--disable-features=VizDisplayCompositor",
            "--single-process"
        ],
        "w3c": False
    }

    driver = webdriver.Remote(
        command_executor=BROWSERLESS_URL,
        options=options,
        keep_alive=True
    )

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
