
def test_home_page(home_page):
    home_page.navbar.go_to_inputs()
    assert "#inputs" in home_page.driver.current_url