from pages.text_box import TextBox
import time


def test_clear(browser):
    text_page = TextBox(browser)

    text_page.visit()
    text_page.full_name.send_keys('hello')
    time.sleep(2)
    text_page.full_name.clear()
    time.sleep(2)
    assert text_page.full_name.get_text() == ''