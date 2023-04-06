from pages.form_page import FormPage
import time


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.btn_state_a_city.click_force()
    time.sleep(3)
    form_page.user_form.send_keys()




