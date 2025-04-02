from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from .wait_visibility import wait_visibility


def wait_visibility_and_get_text(navigator, selector, identifier):
    try:
        element = wait_visibility(navigator, selector, identifier)
        return element.text .strip() if element.text else None
    except NoSuchElementException:
        return None
