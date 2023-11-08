from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
import data
from tests.conftest import driver_settings_chrome

class TestGoToConstructor:
    def test_personal_account_in_constructor(self, driver_settings_chrome):

        driver_settings_chrome.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))


        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(data.email)
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data.password)

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/login"))

        driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/account/profile"))

        driver_settings_chrome.find_element(*TestLocators.CONSTRUCTOR_TAB).click()
        WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/account/profile"))

        assert "Соберите бургер" == driver_settings_chrome.find_element(*TestLocators.INGREDIENTS_HEADER).text
        assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url

    def test_go_to_account_in_constructor_by_logo(self, driver_settings_chrome):

        driver_settings_chrome.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(data.email)
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data.password)

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/login"))

        driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/account/profile"))

        driver_settings_chrome.find_element(*TestLocators.LOGO_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/account/profile"))

        assert "Соберите бургер" == driver_settings_chrome.find_element(*TestLocators.INGREDIENTS_HEADER).text
        assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url
