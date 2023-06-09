from pages.base_page import BasePage
from components.components import WedElement


class Droppable(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'

        }
        self.drag = WedElement(driver, '#draggable')
        self.drop = WedElement(driver, '#droppable')
        self.window = WedElement(driver, '#simpleDropContainer')
