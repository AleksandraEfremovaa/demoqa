from pages.base_page import BasePage
from components.components import WedElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'

        }

        self.answer_accordion = WedElement(driver, '#section1Content > p')
        self.question_accord_first = WedElement(driver, '#section1Heading')
        self.section = WedElement(driver, '#section2Content > p:nth-child(1)')
        self.section_two = WedElement(driver, '#section2Content > p:nth-child(2)')
        self.section_three = WedElement(driver, '#section3Content > p')



