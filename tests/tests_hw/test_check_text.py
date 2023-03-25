from pages.demoqa import DemoQa
from pages.element_pages import ElementsPage


def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_info(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_element_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_element.click()
    assert demo_qa_element_page.info_text_element.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.test_page_elements.get_text() == 'Elements'
    assert elements_page.icon_elements.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()



