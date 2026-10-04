import pytest

@pytest.mark.tables
def test_filter_names(home_page):
    home_page.navbar.go_to_tabs()

    tab = home_page.tables_tab
    tab.filter_names("John")
    names = tab.get_visible_names()

    assert names
    assert all("john" in name.lower() for name in names)

@pytest.mark.tables
def test_user_is_selected(home_page):
    home_page.navbar.go_to_tabs()

    tab = home_page.tables_tab
    tab.select_user(1)

    assert tab.is_user_selected(1)

@pytest.mark.tables
def test_sort_names(home_page):
    home_page.navbar.go_to_tabs()

    tab = home_page.tables_tab
    tab.sort_names()
    tab.wait_for_names_sorted()

    assert tab.get_visible_names() == sorted(tab.get_visible_names(), key=str.lower)

@pytest.mark.tables
def test_sort_ages(home_page):
    home_page.navbar.go_to_tabs()
    tab = home_page.tables_tab
    tab.sort_ages()
    tab.wait_for_ages_sorted()

    assert tab.get_visible_ages() == sorted(tab.get_visible_ages())

@pytest.mark.tables
def test_remove_user(home_page):
    home_page.navbar.go_to_tabs()

    tab = home_page.tables_tab
    tab.remove_user_by_id(1)
    tab.wait_until_user_gone(1)

    assert not tab.is_user_visible(1)

@pytest.mark.tables
def test_add_new_user(home_page):
    home_page.navbar.go_to_tabs()
    
    tab = home_page.tables_tab
    tab.add_new_user(user_id=101, name="John Doe", email="john.doe@example.com", role="Admin", age=30)

    assert "John Doe" in tab.get_visible_names()
