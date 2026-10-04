import pytest

@pytest.mark.select
def test_gender_buttons(home_page):
    home_page.navbar.go_to_selection()

    home_page.selection_tab.pick_gender("male")
    assert "male" == home_page.selection_tab.get_gender_selection_output()

    home_page.selection_tab.pick_gender("female")
    assert "female" == home_page.selection_tab.get_gender_selection_output()

    home_page.selection_tab.pick_gender("other")
    assert "other" == home_page.selection_tab.get_gender_selection_output()

@pytest.mark.select
def test_skills_buttons(home_page):
    home_page.navbar.go_to_selection()

    skills = ["selenium" , "playwright" , "cypress" , "appium"]
    home_page.selection_tab.pick_skills(skills)

    assert "selenium, playwright, cypress, appium" == home_page.selection_tab.get_skills_output()
    #reset
    home_page.selection_tab.unpick_skills(skills)

    skills = ["selenium" , "playwright" , "appium"]
    home_page.selection_tab.pick_skills(skills)

    assert "selenium, playwright, appium" == home_page.selection_tab.get_skills_output()
    #reset
    home_page.selection_tab.unpick_skills(skills)

    skills = ["selenium" , "appium"]
    home_page.selection_tab.pick_skills(skills)

    assert "selenium, appium" == home_page.selection_tab.get_skills_output()
    #reset
    home_page.selection_tab.unpick_skills(skills)
    
    skills = ["appium"]
    home_page.selection_tab.pick_skills(skills)

    assert "appium" == home_page.selection_tab.get_skills_output()

@pytest.mark.select
def test_single_select_country(home_page):
    home_page.navbar.go_to_selection()

    home_page.selection_tab.select_country("Portugal")

    assert "Portugal" == home_page.selection_tab.get_country_output()

@pytest.mark.select
def test_multi_select_listbox(home_page):
    home_page.navbar.go_to_selection()

    languages = ["JavaScript" , "Python" , "Java" , "C#" , "Ruby"]

    home_page.selection_tab.select_multi_languages(languages)
    assert "JavaScript, Python, Java, C#, Ruby" == home_page.selection_tab.get_languages_output()

@pytest.mark.select
def test_select_frameworks(home_page):
    home_page.navbar.go_to_selection()

    frameworks = ["Selenium" , "Playwright" , "Cypress" , "Appium" , "TestNG" , "JUnit"]
    home_page.selection_tab.select_multi_framework(frameworks)

    assert "Selenium, Playwright, Cypress, Appium, TestNG, JUnit" == home_page.selection_tab.get_framework_output()

@pytest.mark.select
def test_years_of_experience(home_page):
    home_page.navbar.go_to_selection()

    years = 15
    home_page.selection_tab.experience_slider(years)

    assert "15 years" == home_page.selection_tab.experience_output()

    years = 1
    home_page.selection_tab.experience_slider(years)
    
    assert "1 years" == home_page.selection_tab.experience_output()

@pytest.mark.select
def test_toggle_notification(home_page):
    home_page.navbar.go_to_selection()

    home_page.selection_tab.toggle_button()

    assert "On" == home_page.selection_tab.get_toggle_message()

    home_page.selection_tab.toggle_button()

    assert "Off" == home_page.selection_tab.get_toggle_message()

@pytest.mark.select
def test_auto_comple(home_page):
    home_page.navbar.go_to_selection()
    trio = "ind"
    country = "Indonesia"
    home_page.selection_tab.set_auto_complete(trio, country)

    assert country == home_page.selection_tab.get_auto_complete()