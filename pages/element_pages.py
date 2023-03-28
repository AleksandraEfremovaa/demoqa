from pages.base_page import BasePage
from components.components import WedElement


class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'

        }

        self.info_text_element = WedElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.test_page_elements = WedElement(driver, 'divplaygound-header > div')
        self.icon_elements = WedElement(driver, 'header > a > img')
        self.btn_sidebar_first = WedElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WedElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first_checkbox = WedElement(driver, 'div:nth-child(1) > div > ul > #item-1 > span')
        self.btns_first_menu = WedElement(driver, 'div:nth-child(1)> div > ul > li')








