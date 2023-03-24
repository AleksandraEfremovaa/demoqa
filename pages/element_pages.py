from pages.base_page import BasePage
from components.components import WedElement
class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.info_text_element = WedElement(driver, '.col-md-6')
        self.elements = WedElement(driver, 'div.pattern-backgound.playgound-header > div')





