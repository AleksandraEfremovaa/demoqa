from pages.element_pages import ElementsPage
import time


def test_visible_btn_sidebar(browser):
    page_elements = ElementsPage(browser)

    page_elements.visit()
    assert page_elements.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    de_mo_qa_pages = ElementsPage(browser)

    de_mo_qa_pages.visit()
    assert de_mo_qa_pages.btn_sidebar_first_checkbox.visible()
    de_mo_qa_pages.btn_sidebar_first.click()
    time.sleep(2)
    assert not de_mo_qa_pages.btn_sidebar_first_checkbox.visible()

