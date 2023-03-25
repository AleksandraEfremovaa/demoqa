from pages.base_page import BasePage


class Accordion(BasePage):
    def __init__(self, driver):
        self.url_accordion = 'https://demoqa.com/accordian'
        super().__init__(driver, self.url_accordion)

        self.answer_accordion = '#section1Content > p'
        self.question_accord_first = '#section1Heading'

