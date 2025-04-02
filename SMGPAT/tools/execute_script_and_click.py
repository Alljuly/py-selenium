from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

def execute_scritp_and_click(navigator, js_selector):
    WebDriverWait(navigator, 30)
    
    for i in range(3):
        try:
            # Executa querySelector via JavaScript
            element = navigator.execute_script(f"return document.querySelector('{js_selector}');")
            if element:
                element.click()
                return
        except StaleElementReferenceException:
            print("Elemento ficou stale. Tentando novamente...")

    raise Exception("Não foi possível clicar no botão após várias tentativas")

