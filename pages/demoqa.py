from pages.base_page import BasePage
from components.components import WedElement


class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'

        }

        self.icon = WedElement(driver, '#app > header > a')
        self.btn_element = WedElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WedElement(driver, '#app > footer > span')



