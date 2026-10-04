import pytest

@pytest.mark.forms
def test_login(home_page):
    home_page.navbar.go_to_forms()
    home_page.form_tab.set_username()
    home_page.form_tab.set_password()

    home_page.form_tab.click(home_page.form_tab.SIDE_BAR_FORM_LOGIN_BUTTON)
    assert "Login successful! Welcome, tester." == home_page.form_tab.get_attribute(home_page.form_tab.SIDE_BAR_FORM_LOGIN_MESSAGE_SUCCESS, "innerText")

@pytest.mark.forms
def test_password_visible(home_page):
    home_page.navbar.go_to_forms()
    home_page.form_tab.set_password()
    home_page.form_tab.click(home_page.form_tab.SIDE_BAR_FORM_PASSWORD_VISIBLE_TOGGLE)

    visible = home_page.form_tab.get_attribute(home_page.form_tab.SIDE_BAR_FORM_PASSWORD_VISIBLE_TOGGLE, "aria-pressed")
    assert visible == "true"

    home_page.form_tab.click(home_page.form_tab.SIDE_BAR_FORM_PASSWORD_VISIBLE_TOGGLE)
    
    visible = home_page.form_tab.get_attribute(home_page.form_tab.SIDE_BAR_FORM_PASSWORD_VISIBLE_TOGGLE, "aria-pressed")
    assert visible == "false"

@pytest.mark.forms
def test_forgot_password(home_page):
    home_page.navbar.go_to_forms()
    home_page.form_tab.click(home_page.form_tab.SIDE_BAR_FORM_FORGOT_PASSWORD_BUTTON)

    home_page.form_tab.set_username_forget_password_form()
    home_page.form_tab.click(home_page.form_tab.SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_SUBMIT_BUTTON)

    assert "Password: password123" == home_page.form_tab.get_attribute(home_page.form_tab.SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_SUBMIT_MESSAGE, "innerText")

    home_page.form_tab.click(home_page.form_tab.SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_FIELD)
    home_page.form_tab.type_text(home_page.form_tab.SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_FIELD, "sadas")
    home_page.form_tab.click(home_page.form_tab.SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_SUBMIT_BUTTON)

    assert "Username not found." == home_page.form_tab.get_attribute(home_page.form_tab.SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_SUBMIT_MESSAGE_FAIL, "innerText")

@pytest.mark.forms
def test_registration_form(home_page):
    home_page.navbar.go_to_forms()
    home_page.form_tab.set_name_registration_form("David")
    home_page.form_tab.set_last_name_registration_form("Iceland")
    home_page.form_tab.set_email_registration_form("Davidiceland@gmail.com")
    home_page.form_tab.set_country("Portugal")

    home_page.form_tab.click(home_page.form_tab.SIDE_BAR_FORM_REGISTER_BUTTON)

    assert "Registration successful for David Iceland!" == home_page.form_tab.form_complete_message()
        
    home_page.form_tab.set_name_registration_form("")
    home_page.form_tab.set_last_name_registration_form("")
    home_page.form_tab.set_email_registration_form("")
    home_page.form_tab.click(home_page.form_tab.SIDE_BAR_FORM_REGISTER_BUTTON)

    assert "Please fill in all required fields." == home_page.form_tab.form_complete_message()

@pytest.mark.forms
def test_clear_registration_form(home_page):
    home_page.navbar.go_to_forms()
    home_page.form_tab.set_name_registration_form("David")
    home_page.form_tab.set_last_name_registration_form("Iceland")
    home_page.form_tab.set_email_registration_form("Davidiceland@gmail.com")
    home_page.form_tab.set_country("Portugal")

    home_page.form_tab.clear_form()

    assert "" == home_page.form_tab.get_attribute(home_page.form_tab.SIDE_BAR_FORM_REGISTER_NAME, "innerText")
    assert "" == home_page.form_tab.get_attribute(home_page.form_tab.SIDE_BAR_FORM_REGISTER_LAST_NAME, "innerText")
    assert "" == home_page.form_tab.get_attribute(home_page.form_tab.SIDE_BAR_FORM_REGISTER_EMAIL, "innerText")
    assert "" == home_page.form_tab.get_attribute(home_page.form_tab.SIDE_BAR_FORM_REGISTER_COUNTRY, "value")