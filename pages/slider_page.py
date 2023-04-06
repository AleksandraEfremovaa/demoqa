from pages.base_page import BasePage
from components.components import WedElement


class SliderPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'
        }

        self.slider_btn_25 = WedElement(driver, '#sliderContainer > div.col-9 > span > input')
        self.text_field_25 = WedElement(driver, '#sliderValue')
        self.slider_btn_50 = WedElement(driver, '#sliderContainer > div.col-9 > span > input')