from pages.base_page import BasePage
from components.components import WedElement


class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'

        }

        self.first_name = WedElement(driver, '#firstName')
        self.last_name = WedElement(driver, '#lastName')
        self.gender_male = WedElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
        self.gender_female = WedElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2)')
        self.gender_other = WedElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(3)')
        self.mobile = WedElement(driver, '#userNumber')

