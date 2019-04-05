from selenium.webdriver.common.by import By


class MainPageLocators(object):
    REGION_LINK = (By.XPATH, "//div[@class='region']//a")
    TEXT_WITH_REGION = (By.XPATH, "//a[contains(text(), 'Адреса магазинов')]")
    REGION_MODAL_FORM = (By.CSS_SELECTOR, "div.form-with-rounded-border")
    REGION_MODAL_FORM_HEADER = (By.CSS_SELECTOR, "td.form-head-name")


    CARD_MODAL_FORM = (By.XPATH, "//div[@id='popUpWindow1']")
    CARD_MODAL_FORM_HEADER = (By.CSS_SELECTOR, "td.form-head-name")








