from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_until_elem_present(driver, locator, sec=10):
    el = WebDriverWait(driver, sec).until(
        EC.presence_of_element_located(locator)
    )
    return el
