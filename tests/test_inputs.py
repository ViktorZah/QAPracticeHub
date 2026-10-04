import pytest
from selenium.common.exceptions import InvalidElementStateException, TimeoutException

@pytest.mark.inputs
def test_inputs_name(home_page):
    home_page.navbar.go_to_inputs()
    name_input = home_page.inputs_tab.fill_name("viktor")

    assert name_input.get_attribute(name_input.SIDE_BAR_INPUTS_NAME, "value") == "viktor"

@pytest.mark.inputs
def test_inputs_email(home_page):
    home_page.navbar.go_to_inputs()
    gmail_input = home_page.inputs_tab.fill_email("viktor@gmail.com")

    assert gmail_input.get_attribute(gmail_input.SIDE_BAR_INPUTS_EMAIL, "value") == "viktor@gmail.com"

@pytest.mark.inputs
def test_inputs_password(home_page):
    home_page.navbar.go_to_inputs()
    password_input = home_page.inputs_tab.fill_password("12345678a")

    assert password_input.get_attribute(password_input.SIDE_BAR_INPUTS_PASSWORD, "value") == "12345678a"

@pytest.mark.inputs
def test_inputs_number_input(home_page):
    home_page.navbar.go_to_inputs()
    number_input = home_page.inputs_tab.fill_number("900")

    #Result: This assertion currently passes due to an application bug
    #Expected behavior: invalid number input should not accept "900"
    assert number_input.get_attribute(number_input.SIDE_BAR_INPUTS_NUMBER, "value") == "900"

    home_page.inputs_tab.delete_all_selected_text(number_input.SIDE_BAR_INPUTS_NUMBER)
    assert number_input.get_attribute(number_input.SIDE_BAR_INPUTS_NUMBER, "value") == ""
    #Action way representing user actions and not simple clear as in fill_number.
    #fill_number has .clear().

    number_input = home_page.inputs_tab.fill_number("99")
    home_page.inputs_tab.arrow_up_press(number_input.SIDE_BAR_INPUTS_NUMBER)
    home_page.inputs_tab.arrow_up_press(number_input.SIDE_BAR_INPUTS_NUMBER)
    home_page.inputs_tab.arrow_up_press(number_input.SIDE_BAR_INPUTS_NUMBER)
    assert number_input.get_attribute(number_input.SIDE_BAR_INPUTS_NUMBER, "value") == "100"

    number_input = home_page.inputs_tab.fill_number("2")
    home_page.inputs_tab.arrow_down_press(number_input.SIDE_BAR_INPUTS_NUMBER)
    home_page.inputs_tab.arrow_down_press(number_input.SIDE_BAR_INPUTS_NUMBER)
    home_page.inputs_tab.arrow_down_press(number_input.SIDE_BAR_INPUTS_NUMBER)
    assert number_input.get_attribute(number_input.SIDE_BAR_INPUTS_NUMBER, "value") == "1"


@pytest.mark.inputs
def test_inputs_date_input(home_page):
    home_page.navbar.go_to_inputs()
    date_input = home_page.inputs_tab.fill_date("06/05/2016")

    assert date_input.get_attribute(date_input.SIDE_BAR_INPUTS_DATE, "value") == "2016-05-06"

@pytest.mark.inputs
def test_inputs_time_input(home_page):
    home_page.navbar.go_to_inputs()
    time_input = home_page.inputs_tab.fill_time("16:11")

    assert time_input.get_attribute(time_input.SIDE_BAR_INPUTS_TIME, "value") == "16:11"

    time_input = home_page.inputs_tab.fill_time("25:70")

    assert time_input.get_attribute(time_input.SIDE_BAR_INPUTS_TIME, "value") == "23:59"

@pytest.mark.inputs
def test_inputs_search_input(home_page):
    home_page.navbar.go_to_inputs()
    search_input = home_page.inputs_tab.fill_search("search input text")

    assert search_input.get_attribute(search_input.SIDE_BAR_INPUTS_SEARCH, "value") == "search input text"

@pytest.mark.inputs
def test_inputs_phone_input(home_page):
    home_page.navbar.go_to_inputs()
    country = "Portugal"
    home_page.inputs_tab.expand_phone_by_country(country)

    phone_text = home_page.inputs_tab.fill_phone("5555555555")
    assert f"Valid {country} number: {home_page.inputs_tab.get_country_phone_code(country)} {phone_text.get_attribute(phone_text.SIDE_BAR_INPUTS_PHONE, 'value')}" == home_page.inputs_tab.get_phone_validate_text()

    phone_text = home_page.inputs_tab.fill_phone("55555555555555555555555")
    assert f"Valid {country} number: {home_page.inputs_tab.get_country_phone_code(country)} 555555555" == home_page.inputs_tab.get_phone_validate_text()
    
@pytest.mark.inputs
def test_inputs_textarea_input(home_page):
    home_page.navbar.go_to_inputs()
    textarea_input = home_page.inputs_tab.fill_textarea("jnfjwenjnwcjkwncnjwcnjwojcnwrcnwikn")

    assert textarea_input.get_attribute(textarea_input.SIDE_BAR_INPUTS_TEXTAREA, "value") == "jnfjwenjnwcjkwncnjwcnjwojcnwrcnwikn"

@pytest.mark.inputs
def test_inputs_read_only_input(home_page):
    home_page.navbar.go_to_inputs()

    with pytest.raises(InvalidElementStateException):
            home_page.inputs_tab.fill_read_only("sdfdsfdsfsfsd")

@pytest.mark.inputs
def test_inputs_disabled_input(home_page):
    home_page.navbar.go_to_inputs()

    with pytest.raises(TimeoutException):
            home_page.inputs_tab.click_disabled() #takes 10second to fail no idea.

@pytest.mark.inputs
def test_inputs_disabled_state_input(home_page): #the more ideal solution
    home_page.navbar.go_to_inputs()
    disabled = home_page.inputs_tab.get_attribute(home_page.inputs_tab.SIDE_BAR_INPUTS_DISABLED, "disabled")

    assert disabled == "true"

@pytest.mark.inputs
def test_inputs_type_and_see_input(home_page):
    home_page.navbar.go_to_inputs()

    text_fild = home_page.inputs_tab.fill_input_output("asdasdasd")
    result_text = home_page.inputs_tab.fill_input_output_result()

    assert text_fild == result_text