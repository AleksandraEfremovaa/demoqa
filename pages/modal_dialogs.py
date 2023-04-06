from pages.base_page import BasePage
from components.components import WedElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'

        }

        self.btns_alerts_frame = WedElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon_main_page = WedElement(driver, '#app > header > a > img')
        self.main_page = WedElement(driver, 'https://demoqa.com/')
        self.small_modal = WedElement(driver, '#showSmallModal')
        self.large_modal = WedElement(driver, '#showLargeModal')
        self.modal_window_small = WedElement(driver, 'body > div.fade.modal.show > div > div')
        self.close_small_modal = WedElement(driver, '#closeSmallModal')
        self.close_large_modal = WedElement(driver, '#closeLargeModal')
        self.modal_window_large = WedElement(driver, 'body > div.fade.modal.show > div > div')

