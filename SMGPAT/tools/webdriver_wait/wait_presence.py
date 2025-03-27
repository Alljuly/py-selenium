from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_presence(navigator, selector, identifier):
        print("chegou em presence")
        wait = WebDriverWait(navigator, 30)
        return wait.until(EC.presence_of_element_located((selector, identifier)))