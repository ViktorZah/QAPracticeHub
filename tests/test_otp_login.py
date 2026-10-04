import pytest
from selenium.common.exceptions import WebDriverException

@pytest.mark.otp
def test_username(home_page):
    home_page.navbar.go_to_otp_login()
    home_page.otp_login_tab.fill_username("someText")

    assert "someText" == home_page.get_attribute(home_page.otp_login_tab.SIDE_BAR_OTP_LOGIN_USERNAME_FIELD, "innerText")

@pytest.mark.otp
def test_submit(home_page):
    home_page.navbar.go_to_otp_login()
    home_page.otp_login_tab.submit_button_otp_click()

    assert "Please enter your username." == home_page.otp_login_tab.get_success_message_text()

    home_page.otp_login_tab.fill_username("someText")
    home_page.otp_login_tab.submit_button_otp_click()

    assert "Please enter all 6 OTP digits." == home_page.otp_login_tab.get_success_message_text()


@pytest.mark.otp
def test_submit(home_page):
    home_page.navbar.go_to_otp_login()

    with pytest.raises(WebDriverException):
        home_page.otp_login_tab.fetch_otp_button_click()

    test_username = "someText"
    home_page.otp_login_tab.fill_username(test_username)

    original_tab = home_page.driver.current_window_handle
    old_tabs = home_page.driver.window_handles.copy()

    home_page.otp_login_tab.fetch_otp_button_click()

    home_page.switch_to_new_tab(old_tabs)
    otp_code = home_page.otp_login_tab.get_otp_code()
    home_page.driver.switch_to.window(original_tab)

    home_page.otp_login_tab.type_text(home_page.otp_login_tab.SIDE_BAR_OTP_LOGIN_OTP_FIELD, otp_code)
    home_page.otp_login_tab.submit_button_otp_click()
    assert f"Login successful! Welcome, {test_username}." == home_page.otp_login_tab.get_success_message_text()

@pytest.mark.otp
def test_resend_otp(home_page):
    home_page.navbar.go_to_otp_login()

    test_username = "someText"
    home_page.otp_login_tab.fill_username(test_username)
    
    original_tab = home_page.driver.current_window_handle
    old_tabs = home_page.driver.window_handles.copy()   
    #first fetch
    home_page.otp_login_tab.fetch_otp_button_click()
    
    home_page.switch_to_new_tab(old_tabs)
    home_page.driver.switch_to.window(original_tab)

    #refetch
    home_page.otp_login_tab.resend_otp_button_click()
    home_page.switch_to_new_tab(old_tabs)
    otp_code = home_page.otp_login_tab.get_otp_code()
    home_page.driver.switch_to.window(original_tab)

    home_page.otp_login_tab.type_text(home_page.otp_login_tab.SIDE_BAR_OTP_LOGIN_OTP_FIELD, otp_code)
    home_page.otp_login_tab.submit_button_otp_click()
    assert f"Login successful! Welcome, {test_username}." == home_page.otp_login_tab.get_success_message_text()


