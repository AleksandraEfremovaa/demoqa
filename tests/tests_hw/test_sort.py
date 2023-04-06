from pages.webtables_page import Webtables
import time


def test_sort(browser):
    check_sort = Webtables(browser)

    check_sort.visit()
    check_sort.sort_first_name.click()
    time.sleep(2)
    assert check_sort.sort_first_name.get_dom_attribute('class') == 'div.rt-th.rt-resizable-header.-sort-desc.-cursor-pointer'
    check_sort.sort_first_name.click()
    time.sleep(3)
