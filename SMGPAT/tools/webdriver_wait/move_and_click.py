from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

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
            print("Elemento stale. Tentando novamente...")
        except ElementNotInteractableException:
            print("O elemento não está interativo. Tentando novamente...")
        except Exception as e:
            print(f"Erro desconhecido: {e}")
    
    raise Exception("Não foi possível clicar no botão após várias tentativas")

