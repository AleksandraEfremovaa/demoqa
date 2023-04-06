from pages.base_page import BasePage
from components.components import WedElement


class ProgressBar(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title':'DEMOQA'
        }

        self.start_n_stop = WedElement(driver, '#startStopButton')
        self.progress_line = WedElement(driver, '#progressBar > div')