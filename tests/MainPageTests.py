import unittest
from unittest import TestCase as asserts
from selenium import webdriver
from pages.MainPage import MainPage
from pages.ProductCardPage import ProductCardPage
from locators.MainPageLocators import MainPageLocators
from locators.ProductCardLocators import ProductCardLocators
from locators.BaseLocators import BaseLocators
from helpers import waiters as w
import re
import time


class MainPageTests(unittest.TestCase):
    maxDiff = None

    driver: webdriver
    driver = None

    MAIN_PAGE = None
    PRODUCT_CARD_PAGE = None

    url = 'https://www.vseinstrumenti.ru/'

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.MAIN_PAGE = MainPage(self.driver)
        self.PRODUCT_CARD_PAGE = ProductCardPage(self.driver)
        #self.MAIN_PAGE.open_url(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.close()


    # test 1
    def test_title(self):
        self.MAIN_PAGE.open_url(self.url)
        elems_with_region = self.MAIN_PAGE.find_elements(*MainPageLocators.TEXT_WITH_REGION)
        text = elems_with_region[-1].text
        city = re.findall('(\S+)', text)[-1]
        expected_title = 'Интернет-магазин ВсеИнструменты.ру в '+ \
                          city +' - электроинструмент, садовый и ручной инструмент, оборудование и станки'
        actual_title = self.MAIN_PAGE.get_title()
        asserts().assertEqual(expected_title, actual_title, 'Error: page title is not equals')


    # test 2
    def test_region_modal_form(self):
        self.MAIN_PAGE.open_url(self.url)
        self.MAIN_PAGE.find_element(*MainPageLocators.REGION_LINK).click()
        w.wait_until_elem_present(self.driver, MainPageLocators.REGION_MODAL_FORM)
        exp_header = 'Выберите свой город'
        act_header = self.MAIN_PAGE.find_element(*MainPageLocators.REGION_MODAL_FORM_HEADER).text
        asserts().assertEqual(exp_header, act_header, 'Error: region modal form is not showed')


    # test 3 - переделать на проверку товара
    def test_button_to_cart_on_sale(self):
        self.url = self.url + 'stanki/struzhkootsosy/enkor/korvet-61/'
        self.PRODUCT_CARD_PAGE.open_url(self.url)
        self.PRODUCT_CARD_PAGE.find_element(*ProductCardLocators.BUTTON_SALE_TO_CARD).click()
        w.wait_until_elem_present(self.driver, BaseLocators.CARD_MODAL_FORM)
        exp_header = 'Товар добавлен в корзину'
        act_header = self.PRODUCT_CARD_PAGE.find_element(*BaseLocators.CARD_MODAL_FORM_HEADER).text
        asserts().assertEqual(exp_header, act_header, 'Error: card modal form is not showed')





if __name__ == '__main__':
    unittest.main()