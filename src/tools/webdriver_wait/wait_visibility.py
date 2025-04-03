from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_visibility(navigator, selector, identifier):
    try:
        wait = WebDriverWait(navigator, 20)
        element = wait.until(EC.visibility_of_element_located((selector, identifier)))
        return element
    except: 
        None
