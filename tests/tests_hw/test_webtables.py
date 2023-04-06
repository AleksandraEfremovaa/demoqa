from pages.webtables_page import Webtables
import time
import allure


# @allure.feature('тест таблицы Web tables' )
# @allure.story('проверка формы ввода данных')
# @allure.severity(allure.severity_level.CRITICAL)
# def test_webtables(browser):
#     web_tables = Webtables(browser)
#     first_name = 'tester'
#     last_name = 'testov'
#     email = 'test@rrw.com'
#     age = '30'
#     new_first_name = 'TTTEsTer'
#
#     web_tables.visit()
#     web_tables.add_btn.click()
#     time.sleep(2)
#     assert web_tables.registration_form.visible()
#     web_tables.submit_btn.click()
#     assert web_tables.registration_form.visible()
#     web_tables.first_name.send_keys(first_name)
#     web_tables.last_name.send_keys(last_name)
#     web_tables.email.send_keys(email)
#     web_tables.age.send_keys(age)
#     web_tables.salary.send_keys('70000')
#     web_tables.department.send_keys('spb')
#     web_tables.submit_btn.click()
#     time.sleep(2)
#     # assert not web_tables.registration_form.visible()
#     assert web_tables.first_name_table.get_text() == first_name
#
#     web_tables.pencil.click()
#     time.sleep(2)
#     web_tables.first_name.clear()
#     time.sleep(2)
#     web_tables.first_name.send_keys(new_first_name)
#     web_tables.submit_btn.click()
#     time.sleep(2)
#     web_tables.trashcan.click()
#
#




# def test_webtables(browser):
#     web_tables = Webtables(browser)
#
#     web_tables.visit()
#     assert not web_tables.no_rows_found.exist()
#     while web_tables.btn_delete_row.exist():
#         web_tables.btn_delete_row.click()
#     time.sleep(2)
#     assert web_tables.no_rows_found.exist()
#


