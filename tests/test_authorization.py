from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
import data
class TestAuthorization:

    def test_go_account(self, driver_settings_chrome):
        # жмём по кнопке «Войти в аккаунт»
        driver_settings_chrome.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(data.email)
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data.password)

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/login"))

        driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/account/profile"))

        driver_settings_chrome.find_element(*TestLocators.ACCOUNT_MENU)
        assert "Bens" == driver_settings_chrome.find_element(*TestLocators.NAME_FIELD).get_attribute("value")
