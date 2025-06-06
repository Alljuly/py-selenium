from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_presence(navigator, selector, identifier):
    wait = WebDriverWait(navigator, 30)
    try: 
        return wait.until(EC.presence_of_element_located((selector, identifier)))
    except:
        return None