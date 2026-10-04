from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def build_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=800,800")
    return webdriver.chrome(options=options)