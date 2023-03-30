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
        self.user_number = WedElement(driver, '#userNumber')
        self.modal_dialog = WedElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WedElement(driver, '#closeLargeModal')
        self.user_email = WedElement(driver, '#userEmail')
        self.btn_submit = WedElement(driver, '#submit')
        self.user_form = WedElement(driver, '#userForm')
        self.btn_state_a_city = WedElement(driver, '#state > div > div.css-1wy0on6 > div > svg')


