import unittest
import re
import random
from unittest import TestCase as asserts
from selenium import webdriver
from pages.MainPage import MainPage
from pages.ProductCardPage import ProductCardPage
from pages.ContactsPage import ContactsPage
from locators.MainPageLocators import MainPageLocators
from locators.ProductCardLocators import ProductCardLocators
from locators.BaseLocators import BaseLocators
from locators.ContactsPageLocators import ContactsPageLocators
from helpers import waiters as w


class Tests(unittest.TestCase):
    maxDiff = None

    driver: webdriver
    driver = None

    MAIN_PAGE = None
    PRODUCT_CARD_PAGE = None
    CONTACTS_PAGE = None

    url = 'https://www.vseinstrumenti.ru/'

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.MAIN_PAGE = MainPage(self.driver)
        self.PRODUCT_CARD_PAGE = ProductCardPage(self.driver)
        self.CONTACTS_PAGE = ContactsPage(self.driver)


    @classmethod
    def tearDownClass(self):
        self.driver.close()


    # test 1
    def test_title(self):
        self.MAIN_PAGE.open_url(self.url)
        elems_with_region = self.MAIN_PAGE.find_elements(BaseLocators.TEXT_WITH_REGION)
        text = elems_with_region[-1].text
        city = re.findall('(\S+)', text)[-1]
        expected_title = 'Интернет-магазин ВсеИнструменты.ру в '+ \
                          city +' - электроинструмент, садовый и ручной инструмент, оборудование и станки'
        actual_title = self.MAIN_PAGE.get_title()
        asserts().assertEqual(expected_title, actual_title, 'Error: page title is not equals')


    # test 2
    def test_region_modal_form(self):
        self.MAIN_PAGE.open_url(self.url)
        self.MAIN_PAGE.find_element(BaseLocators.REGION_LINK).click()
        w.wait_until_elem_present(self.driver, BaseLocators.REGION_MODAL_FORM)
        exp_header = 'Выберите свой город'
        act_header = self.MAIN_PAGE.find_element(BaseLocators.REGION_MODAL_FORM_HEADER).text
        asserts().assertEqual(exp_header, act_header, 'Error: region modal form is not showed')


    # test 3
    def test_button_to_cart_on_sale(self):
        self.url = self.url + 'stanki/struzhkootsosy/enkor/korvet-61/'
        self.PRODUCT_CARD_PAGE.open_url(self.url)
        self.PRODUCT_CARD_PAGE.find_element(ProductCardLocators.BUTTON_SALE_TO_CARD).click()
        exp_name = self.PRODUCT_CARD_PAGE.find_element(ProductCardLocators.PRODUCT_NAME).text
        w.wait_until_elem_present(self.driver, BaseLocators.CARD_MODAL_FORM)
        act_name = self.PRODUCT_CARD_PAGE.find_element(BaseLocators.CARD_MODAL_PRODUCT_LINK).text
        asserts().assertEqual(act_name.strip(), exp_name.strip(), 'Error: product name in card is different')


    # test 4
    def test_find_random_city_with_delivery(self):
        self.MAIN_PAGE.open_url(self.url)
        self.MAIN_PAGE.find_element(BaseLocators.REGION_LINK).click()
        w.wait_until_elem_present(self.driver, BaseLocators.REGION_MODAL_FORM)
        city_elems = self.MAIN_PAGE.find_elements(BaseLocators.CITY_WITH_DELIVERY)
        act_cities_count = len(city_elems)
        exp_city_list = self.MAIN_PAGE.get_delivery_cities_list()
        exp_cities_count = len(exp_city_list)
        random_city_num = random.randint(0, len(city_elems)-1)
        act_city_name = city_elems[random_city_num].text
        asserts().assertEqual(act_cities_count, exp_cities_count, 'Error: count of cities list is different')
        asserts().assertIn(act_city_name, exp_city_list, 'Error: city is absent in cities list')


    # test 5
    def test_button_to_cart_high_bonus(self):
        self.url = self.url + 'instrument/'
        self.MAIN_PAGE.open_url(self.url)
        products = self.MAIN_PAGE.find_elements(BaseLocators.HIGH_BONUS_PRODUCT)
        random_product_num = random.randint(0, len(products) - 1)
        product = products[random_product_num]
        exp_name = product.find_element(*BaseLocators.HIGH_BONUS_PRODUCT_LINK).get_attribute('title')
        product.find_element(*BaseLocators.BUTTON_HIGH_BONUS_TO_CARD).click()
        w.wait_until_elem_present(self.driver, BaseLocators.REGION_MODAL_FORM)
        act_name = self.PRODUCT_CARD_PAGE.find_element(BaseLocators.CARD_MODAL_PRODUCT_LINK).text
        asserts().assertEqual(act_name.strip(), exp_name.strip(), 'Error: product name in card is different')


    # test 6
    def test_claims_department_phone(self):
        self.url = self.url + 'contacts/1.html'
        self.MAIN_PAGE.open_url(self.url)
        exp_phone = '+7 (800) 550-37-70'
        act_phone = self.CONTACTS_PAGE.find_element(ContactsPageLocators.CLAIMS_PHONE).text
        asserts().assertEqual(act_phone.strip(), exp_phone.strip(), 'Error: claims department phone is different')


if __name__ == '__main__':
    unittest.main()