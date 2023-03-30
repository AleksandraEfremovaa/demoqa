from pages.form_page import FormPage
import time


def test_login_form(browser):
    form = FormPage(browser)

    form.visit()
    assert not form.modal_dialog.exist()
    time.sleep(2)
    form.first_name.send_keys('alex')
    form.last_name.send_keys('efremova')
    form.user_email.send_keys('sashaefrr9977@mail.ru')
    form.gender_female.click()
    form.user_number.send_keys('79105301096')
    time.sleep(2)
    form.btn_submit.click_force()
    time.sleep(2)
    assert form.modal_dialog.exist()
    form.btn_close_modal.click_force()



