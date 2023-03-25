from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    widgets = Accordion(browser)

    widgets.visit()
    assert widgets.answer_accordion.visible()
    widgets.question_accord_first.click()
    time.sleep(2)
    assert not widgets.answer_accordion.visible()


def test_visible_accordion_default(browser):
    page_menu = Accordion(browser)

    page_menu.visit()
    assert not page_menu.section.visible()
    assert not page_menu.section_two.visible()
    assert not page_menu.section_three.visible()


