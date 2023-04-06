from pages.base_page import BasePage
from components.components import WedElement


class Webtables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'

        }

        self.add_btn = WedElement(driver, '#addNewRecordButton')
        self.submit_btn = WedElement(driver, '#submit')
        self.close_btn_form = WedElement(driver, ' div.fade.modal.show > div > div > div.modal-header > button > span:nth-child(1)')
        self.first_name = WedElement(driver, '#firstName')
        self.last_name = WedElement(driver, '#lastName')
        self.email = WedElement(driver, '#userEmail')
        self.age = WedElement(driver, '#age')
        self.salary = WedElement(driver, '#salary')
        self.department = WedElement(driver, '#department')
        self.table_add = WedElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div')
        self.pencil = WedElement(driver, '#edit-record-4 > svg > path')
        self.registration_form = WedElement(driver, 'body > div.fade.modal.show > div > div')
        self.no_rows_found = WedElement(driver, 'div.rt-noData')
        self.table = WedElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody')
        self.btn_delete_row = WedElement(driver, '[title = "Delete')
        self.first_name_table = WedElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.trashcan = WedElement(driver, '#delete-record-4 > svg > path')

        self.sort_first_name = WedElement(driver, 'div.rt-resizable-header-content')