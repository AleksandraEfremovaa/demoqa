from pages.alerts import Alerts
import time
import allure

@allure.title('проверка видимости алерта')
def test_alerts(browser):
    alerts_page = Alerts(browser)

    alerts_page.visit()
    assert not alerts_page.alert()
    alerts_page.alert_btn.click()
    time.sleep(2)
    assert alerts_page.alert()
    alerts_page.alert().accept()

@allure.title('клик на кнопку алерта')
def test_alert_text(browser):
    alert_text = Alerts(browser)

    alert_text.visit()
    alert_text.alert_btn.click()
    time.sleep(2)
    assert alert_text.alert().text == 'You clicked a button'
    alert_text.alert().accept()
    assert not alert_text.alert()
    alert_text.alert().accept()

@allure.title('отмена алерта')
def test_confirm(browser):
    confirm_window = Alerts(browser)

    confirm_window.visit()
    confirm_window.confirm_btn.click()
    time.sleep(2)
    confirm_window.alert().dismiss()
    assert confirm_window.text_block.get_text() == 'You selected Cancel'
    confirm_window.alert().accept()


@allure.title('проверка ввода текста в алерт')
def test_prompt(browser):
    prompt_window = Alerts(browser)
    name = 'name123'

    prompt_window.visit()
    prompt_window.prompt_btn.click()
    time.sleep(2)
    prompt_window.alert().send_keys(name)
    prompt_window.alert().accept()
    assert prompt_window.text_block_prompt.get_text() == f'You entered {name}'
    time.sleep(2)




