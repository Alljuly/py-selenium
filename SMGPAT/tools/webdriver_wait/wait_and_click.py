from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def scroll_to_element(navigator, selector, identifier):
    element = WebDriverWait(navigator, 10).until(EC.presence_of_element_located((selector, identifier)))
    navigator.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1) 

def wait_and_click(navigator, selector, identifier):
    wait = WebDriverWait(navigator, 30)

    for i in range(3):
        try:
            scroll_to_element(navigator, selector, identifier)
            element = wait.until(EC.element_to_be_clickable((selector, identifier)))
            element.click()
            return
        except StaleElementReferenceException:
            print("Elemento ficou stale. Tentando novamente...")
    
    raise Exception("Não foi possível clicar no botão após várias tentativas")
