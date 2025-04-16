from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from backend.utils.automation_constants import BUTTON_NOT_CLICABLE, ELEMENT_STALE

import time

def move_and_click(navigator, selector, identifier):
    wait = WebDriverWait(navigator, 10)
    for i in range(3):
        try:
            element = wait.until(EC.element_to_be_clickable((selector, identifier)))
            navigator.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(2) 
            element.click()     
            return 
        except StaleElementReferenceException:
            print(ELEMENT_STALE)
        except ElementNotInteractableException:
            print("O elemento não está interativo. Tentando novamente...")
        except Exception as e:
            print(f"Erro desconhecido: {e}")
    
    raise Exception(BUTTON_NOT_CLICABLE)

