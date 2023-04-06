from pages.text_box import TextBox
import allure


@allure.feature('check attr')
@allure.story('Проверка атрибута placeholder')
@allure.severity(allure.severity_level.NORMAL)
def test_placeholder(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    assert text_box_page.full_name.get_dom_attribute('placeholder') =='Full Name'


def test_fail():
    assert 111 == 222

