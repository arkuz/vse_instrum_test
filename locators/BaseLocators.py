from selenium.webdriver.common.by import By


class BaseLocators(object):
    CARD_MODAL_FORM = (By.XPATH, "//div[@id='popUpWindow1']")
    CARD_MODAL_FORM_HEADER = (By.CSS_SELECTOR, "td.form-head-name")








