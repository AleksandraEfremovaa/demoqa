from pages.progress_bar_page import ProgressBar
import time


def test_progress_bar_page(browser):
    progress_bar = ProgressBar(browser)

    progress_bar.visit()
    time.sleep(2)
    progress_bar.start_n_stop.click()
    if progress_bar.progress_line.get_dom_attribute('aria-valuenow') == '51':
        progress_bar.start_n_stop.click()

    time.sleep(7)