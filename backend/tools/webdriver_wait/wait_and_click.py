from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from ..move_and_click import move_and_click
from .wait_presence import wait_presence
from backend.utils.automation_constants import ELEMENT_STALE, BUTTON_NOT_CLICABLE

def wait_and_click(navigator, selector, identifier):
    WebDriverWait(navigator, 30)
    for i in range(3):
        try:
            element = wait_presence(navigator, selector, identifier)
            if element:
                move_and_click(navigator, selector, identifier)
                return
        except StaleElementReferenceException:
            print(ELEMENT_STALE)
    
    raise Exception(f"{BUTTON_NOT_CLICABLE}: {selector}, ID: {identifier}")

