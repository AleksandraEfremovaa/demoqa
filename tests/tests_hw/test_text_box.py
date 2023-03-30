from pages.text_box import TextBox


def test_text_box(browser):
    box_pages = TextBox(browser)

    box_pages.visit()
    box_pages.full_name.send_keys('tester')
    box_pages.current_address.send_keys('Spb')
    box_pages.submit_btn.click_force()
    assert box_pages.name.get_text() == 'Name:tester'
    assert box_pages.address.get_text() == 'Current Address:Spb'
