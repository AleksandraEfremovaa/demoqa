from pages.form_page import FormPage
import time


def test_send_keys(browser):
    form = FormPage(browser)

    form.visit()
    form.first_name.send_keys('alex')
    form.last_name.send_keys('efremova')
    form.gender_male.click()
    form.mobile.send_keys('+79105301096')
    time.sleep(7)
