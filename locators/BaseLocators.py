from selenium.webdriver.common.by import By


class BaseLocators(object):
    REGION_LINK = (By.XPATH, "//div[@class='region']//a")
    TEXT_WITH_REGION = (By.XPATH, "//a[contains(text(), 'Адреса магазинов')]")
    REGION_MODAL_FORM = (By.CSS_SELECTOR, "div.form-with-rounded-border")
    REGION_MODAL_FORM_HEADER = (By.CSS_SELECTOR, "td.form-head-name")
    CITY_WITH_DELIVERY = (By.XPATH, "//div[contains(@class,'deliveryCourierConteiner')]//a[contains(@class,'fst-b')=False]")


    CARD_MODAL_FORM = (By.XPATH, "//div[@id='popUpWindow1']")
    CARD_MODAL_FORM_HEADER = (By.CSS_SELECTOR, "td.form-head-name")
    CARD_MODAL_PRODUCT_LINK = (By.XPATH, "//a[@id='waddcarturl']")


    HIGH_BONUS_PRODUCT = (By.XPATH, "//div[a//span[contains(text(),'Высокие бонусы СПАСИБО')]]")
    HIGH_BONUS_PRODUCT_LINK = (By.XPATH, ".//div[contains(@class,'product-name')]/a")
    #BUTTON_HIGH_BONUS_TO_CARD = (By.XPATH, "//div[a//span[contains(text(),'Высокие бонусы СПАСИБО')]]//div[@class='buttons']/a")
    BUTTON_HIGH_BONUS_TO_CARD = (By.XPATH, ".//div[@class='buttons']/a")








