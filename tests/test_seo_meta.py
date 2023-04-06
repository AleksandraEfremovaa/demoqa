from pages.alerts import Alerts
from pages.accordion import Accordion
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab
import time
import pytest


@pytest.mark.parametrize('pages', [Alerts, Accordion, DemoQa, BrowserTab])
def test_check_head(browser, pages):
    page = pages(browser)

    page.visit()
    assert page.meta.get_dom_attribute('name') == 'viewport'
    assert page.meta.get_dom_attribute('content') == 'width=device-width,initial-scale=1'