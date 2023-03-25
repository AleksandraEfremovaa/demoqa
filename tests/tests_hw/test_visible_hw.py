from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    widgets = Accordion(browser)
    widgets.visit()

    assert widgets.answer_accordion.visible()
    widgets.question_accord_first.click()
    time.sleep(2)
    assert not widgets.answer_accordion.visible()


