from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from .wait_presence import wait_presence


def wait_presence_get_text(navigator, selector, identifier):
    try:
        element = wait_presence(navigator, selector, identifier)
        return element.text .strip() if element.text else None
    except NoSuchElementException:
        return None
