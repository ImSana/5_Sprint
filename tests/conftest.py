import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver_settings_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver_settings_chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver_settings_chrome.get("https://stellarburgers.nomoreparties.site/")
    yield driver_settings_chrome
    driver_settings_chrome.quit()
