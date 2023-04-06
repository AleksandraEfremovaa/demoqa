from pages.droppable import Droppable
from selenium.webdriver import ActionChains
import time


def test_drop(browser):
    action_chains = ActionChains(browser)
    drop_page = Droppable(browser)

    drop_page.visit()
    # assert not drop_page.drag.check_css('backgroundColor', '')
    action_chains.drag_and_drop(drop_page.drag.find_element(), drop_page.drop.find_element()).perform()
    time.sleep(1)
    assert drop_page.drag.check_css('backgroundColor', 'steelblue')
    # action_chains.drag_and_drop(drop_page.drag.find_element(),drop_page.window.find_element()).perform()
    action_chains.drag_and_drop_by_offset(drop_page.drag.find_element(), 100, 100).perform()
    time.sleep(2)
    assert drop_page.drag.check_css('backgroundColor', 'steelblue')


