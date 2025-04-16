from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from .webdriver_wait import wait_and_click, wait_presence

def clear_and_send(navigator, selector, identifier, keys):
    wait_and_click(navigator, selector, identifier)
    element = wait_presence(navigator, selector, identifier)
    element.clear()
    element.send_keys(keys)

