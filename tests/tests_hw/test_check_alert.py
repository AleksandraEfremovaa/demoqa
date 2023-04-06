from pages.alerts import Alerts
import time


def test_check_alert(browser):
    check_alert = Alerts(browser)

    check_alert.visit()
    assert check_alert.time_alert_btn.visible()
    check_alert.time_alert_btn.click()
    time.sleep(6)
    assert check_alert.alert()
