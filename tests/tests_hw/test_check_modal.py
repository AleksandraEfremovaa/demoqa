from pages.modal_dialogs import ModalDialogs
import time


def test_check_modal(browser):
    check_modal = ModalDialogs(browser)

    check_modal.visit()
    assert check_modal.small_modal.exist()
    assert check_modal.large_modal.exist()
    check_modal.small_modal.click()
    time.sleep(2)
    assert check_modal.modal_window_small.visible()
    check_modal.close_small_modal.click()
    time.sleep(2)
    assert not check_modal.modal_window_small.exist()
    check_modal.large_modal.click()
    time.sleep(2)
    assert check_modal.modal_window_large.visible()
    check_modal.close_large_modal.click()
    time.sleep(2)
    assert not check_modal.modal_window_large.exist()

