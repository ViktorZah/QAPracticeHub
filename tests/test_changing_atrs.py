import pytest


@pytest.mark.changing_attributes
def test_clock_timestamp_changes(home_page):
    home_page.navbar.go_to_changing_attributes()
    tab = home_page.changing_attr_tab

    old_timestamp = tab.get_clock_button_atr()
    tab.wait_for_clock_to_change(old_timestamp)
    new_timestamp = tab.get_clock_button_atr()

    assert new_timestamp != old_timestamp


@pytest.mark.changing_attributes
def test_rotating_status(home_page):
    home_page.navbar.go_to_changing_attributes()
    tab = home_page.changing_attr_tab

    tab.wait_for_status_ready()

    assert tab.get_badge_button_status() == "ready"


@pytest.mark.changing_attributes
def test_changing_id(home_page):
    home_page.navbar.go_to_changing_attributes()
    tab = home_page.changing_attr_tab

    old_id = tab.get_changing_id()
    tab.wait_for_id_to_change(old_id)
    new_id = tab.get_changing_id()

    assert new_id != old_id


@pytest.mark.changing_attributes
def test_countdown(home_page):
    home_page.navbar.go_to_changing_attributes()
    tab = home_page.changing_attr_tab

    tab.wait_for_countdown()

    assert "Ready" in tab.get_countdown_output()

@pytest.mark.changing_attributes
def test_dynamic_link(home_page):
    home_page.navbar.go_to_changing_attributes()
    tab = home_page.changing_attr_tab

    old_href = tab.get_link_href()
    tab.wait_for_link_to_change(old_href)
    new_href = tab.get_link_href()

    assert new_href != old_href