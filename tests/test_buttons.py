import pytest
import time

@pytest.mark.buttons
def test_primary_button(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.press_primary_button()

    assert "Primary button clicked." == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_secondary_button(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.press_secondary_button()
    assert "Secondary button clicked." == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_left_click_button(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.press_left_click_button()
    assert "Left click detected!" == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_outline_button(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.press_outline_button()
    assert "Outline button clicked." == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_disabled_button(home_page):
    home_page.navbar.go_to_buttons()
    home_page.buttons_tab.press_disabled_button()

@pytest.mark.buttons
def test_click_me_count_button(home_page):
    home_page.navbar.go_to_buttons()

    number = 10
    for i in range(number):
        home_page.buttons_tab.press_counter_button()
        assert f"Click Me ({1 + i})" == home_page.buttons_tab.press_counter_count()

@pytest.mark.buttons
def test_double_click_button(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.double_click(home_page.buttons_tab.SIDE_BAR_BUTTONS_DOUBLE_CLICK_BUTTON)

    assert "Double click detected!" == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_right_click_button(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.right_click(home_page.buttons_tab.SIDE_BAR_BUTTONS_RIGHT_CLICK_BUTTON)

    assert "Right click detected!" == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_hover_over_button(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.hover_over_button()

    assert "Mouse entered the hover button." == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_danger_button(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.press_danger_button()

    assert "Danger button clicked." == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_next_page_button(home_page):#doesnt work
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.press_next_page()#asserts inside the fucntion

@pytest.mark.buttons
def test_download_file_button(home_page):#not implemented yet
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.press_download_sample_file()

    #assert "" == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_open_popup_button(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.press_open_popup()

    assert "Popup closed." == home_page.buttons_tab.get_global_result_info_message()

@pytest.mark.buttons
def test_click_info(home_page):
    home_page.navbar.go_to_buttons()
    home_page.buttons_tab.press_click_info()

    assert "This info opens when you click the (i) button. Click anywhere on the page to close it." == home_page.buttons_tab.info_button_message()

@pytest.mark.buttons
def test_hover_info(home_page):
    home_page.navbar.go_to_buttons()

    home_page.buttons_tab.hover_info()

    assert "This info opens when you hover over the (i) button. It closes when you move the mouse away." == home_page.buttons_tab.info_hover_message()