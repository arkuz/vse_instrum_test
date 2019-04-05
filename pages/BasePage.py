from selenium import webdriver


class BasePage(object):
    driver: webdriver
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self):
        self.driver.click()

    def send_keys(self, value):
        self.driver.send_keys(value)

    def clear(self):
        self.driver.clear()

    def get_delivery_cities_list(self):
        cities = [
            'Балашиха',
            'Батайск',
            'Белгород',
            'Брянск',
            'Великий Новгород',
            'Владимир',
            'Волгоград',
            'Волжский',
            'Воскресенск',
            'Дзержинск',
            'Дмитров',
            'Домодедово',
            'Дубна',
            'Железнодорожный',
            'Жуковский',
            'Зеленоград',
            'Ивантеевка',
            'Калуга',
            'Клин',
            'Коломна',
            'Королев',
            'Липецк',
            'Люберцы',
            'Миасс',
            'Мытищи',
            'Наро-Фоминск',
            'Новомосковск',
            'Новочеркасск',
            'Ногинск',
            'Одинцово',
            'Озерск',
            'Орехово-Зуево',
            'Подольск',
            'Пушкино',
            'Раменское',
            'Реутов',
            'Ростов-на-Дону',
            'Рязань',
            'Саратов',
            'Свердловский',
            'Сергиев Посад',
            'Серпухов',
            'Собинка',
            'Ступино',
            'Тверь',
            'Троицк',
            'Тула',
            'Тюмень',
            'Уфа',
            'Фрязино',
            'Химки',
            'Чехов',
            'Щелково',
            'Электросталь'
        ]
        return cities