from pages.base_page import BasePage
from components.components import WedElement


class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'

        }
        self.alert_btn = WedElement(driver, '#alertButton')
        self.confirm_btn = WedElement(driver, '#confirmButton')
        self.text_block = WedElement(driver, '#confirmResult')
        self.prompt_btn = WedElement(driver, '#promtButton')
        self.text_block_prompt = WedElement(driver, '#promptResult')
        self.time_alert_btn = WedElement(driver, '#timerAlertButton')