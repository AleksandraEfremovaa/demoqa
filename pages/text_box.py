from pages.base_page import BasePage
from components.components import WedElement


class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'

        }
        self.full_name = WedElement(driver, '#userName')
        self.user_email = WedElement(driver, '#userEmail')
        self.current_address = WedElement(driver, '#currentAddress')
        self.submit_btn = WedElement(driver, '#submit')
        self.name = WedElement(driver, '#name')
        self.address = WedElement(driver, '#output > div > p#currentAddress ')