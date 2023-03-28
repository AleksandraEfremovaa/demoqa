from pages.modal_dialogs import ModalDialogs
import time


def test_modal_elements(browser):
    demo_qa_page = ModalDialogs(browser)

    demo_qa_page.visit()
    assert demo_qa_page.btns_alerts_frame.check_count_elements(5)


def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    browser.refresh()
    modal_dialogs.icon_main_page.click()
    time.sleep(2)
    browser.back()
    browser.set_window_size(900, 400)
    time.sleep(3)
    browser.forward()
    assert modal_dialogs.equal_url()
    assert browser.title == modal_dialogs.pageData['title']
    browser.set_window_size(1000, 1000)


