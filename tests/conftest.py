import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Registration:
    def __init__(self, email, password, name):
        self. email = email
        self.password = password
        self.name = name


@pytest.fixture
def get_user_correct():
    random_numbers = random.randint(10, 99)
    return Registration(f"uncle_Bens{random_numbers}@ya.ru", "123123", "Bens")


@pytest.fixture
def get_not_user_correct():
    return Registration("Bens@ya", "12312", "   ")


@pytest.fixture
def driver_settings_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver_settings_chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver_settings_chrome.get("https://stellarburgers.nomoreparties.site/")
    yield driver_settings_chrome
    driver_settings_chrome.quit()
