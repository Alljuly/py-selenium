from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def wait_presence_get_text(navigator, selector, identifier):
    try:
        wait = WebDriverWait(navigator, 30)
        element = wait.until(EC.presence_of_element_located((selector, identifier)))

        return element.text .strip() if element.text else None
    except NoSuchElementException:
        return None
