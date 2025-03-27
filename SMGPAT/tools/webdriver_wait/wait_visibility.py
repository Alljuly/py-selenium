from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_visibility(navigator, selector, identifier):
    print("chegou em vizibility")
    wait = WebDriverWait(navigator, 30)
    return wait.until(EC.visibility_of_element_located((selector, identifier)))