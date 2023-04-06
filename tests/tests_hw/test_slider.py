from pages.slider_page import SliderPage
import time
from selenium.webdriver import ActionChains


def test_slider_page(browser):
    slider_page = SliderPage(browser)
    acrion_chains = ActionChains(browser)

    slider_page.visit()
    assert slider_page.slider_btn_25.exist()
    assert slider_page.text_field_25.exist()
    assert slider_page.slider_btn_25.get_dom_attribute('value') == '25'
    acrion_chains.drag_and_drop(slider_page.slider_btn_25.find_element(), slider_page.slider_btn_50.find_element()).perform()
    time.sleep(2)
    assert slider_page.slider_btn_50.get_dom_attribute('value') == '50'
