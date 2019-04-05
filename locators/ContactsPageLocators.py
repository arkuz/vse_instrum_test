from selenium.webdriver.common.by import By


class ContactsPageLocators(object):
    CLAIMS_PHONE = (By.XPATH, "//td[contains(text(),'Отдел претензий')]/following-sibling::td[@class='contact_info_table_telefon']")



