from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

from backend.utils.automation_constants import ELEMENT_STALE, BUTTON_NOT_CLICABLE


def execute_scritp_and_click(navigator, js_selector):
    WebDriverWait(navigator, 30)
    
    for _ in range(3):
        try:
            element = navigator.execute_script(f"return document.querySelector('{js_selector}');")
            if element:
                element.click()
                return
        except StaleElementReferenceException:
            print(ELEMENT_STALE)

    raise Exception(BUTTON_NOT_CLICABLE)

