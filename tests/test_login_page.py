from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
import data
from tests.conftest import driver_settings_chrome


class TestLoginPage:

    def test_login_by_button_on_main_page(self, driver_settings_chrome):

        driver_settings_chrome.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(data.email)
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data.password)

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url


    def test_login_by_personal_account_button(self, driver_settings_chrome,):
        driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))


        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(data.email)
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data.password)


        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url


    def test_login_across_button_in_registration(self, driver_settings_chrome):
        driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver_settings_chrome.find_element(*TestLocators.LINK_REGISTRATION).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/register"))


        driver_settings_chrome.find_element(*TestLocators.ENTER_LINK).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))


        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(data.email)
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data.password)

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url


    def test_login_across_button_in_password_recovery(self, driver_settings_chrome):
        driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))


        driver_settings_chrome.find_element(*TestLocators.RECOVERY_LINK).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/forgot-password"))

        driver_settings_chrome.find_element(*TestLocators.ENTER_LINK).click()
        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(data.email)
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data.password)

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()

        WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url
