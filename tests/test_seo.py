import time

from pages.demoqa import DemoQa
import pytest
from pages.alerts import Alerts

def test_seo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title == demo_qa_page.pageData['title']

page_demo = DemoQa
@pytest.mark.parametrize('pages', [DemoQa, Alerts])
def test_check_title_all_pages(browser, pages):
    page_demo = pages(browser)

    page_demo.visit()
    time.sleep(2)
    assert browser.title == page_demo.pageData['title']