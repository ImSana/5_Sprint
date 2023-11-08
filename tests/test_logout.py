from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
import data
class TestLogout:
    def test_logout_by_button_in_personal_account(self, driver_settings_chrome):

        driver_settings_chrome.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome,5).until(ex_cond.url_contains("/login"))

        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(data.email)
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data.password)


        WebDriverWait(driver_settings_chrome,5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver_settings_chrome,5).until_not(ex_cond.url_contains("/login"))


        driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome,5).until(ex_cond.url_contains("/account/profile"))


        driver_settings_chrome.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver_settings_chrome,5).until_not(ex_cond.url_contains("/account/profile"))

        assert "" == driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).get_attribute("value")
        assert "" == driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).get_attribute("value")
        assert "https://stellarburgers.nomoreparties.site/login" == driver_settings_chrome.current_url
