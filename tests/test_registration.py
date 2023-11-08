from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import helpers
import data


class TestRegistration:

    def test_registration_with_correct_data_successful(self, driver_settings_chrome):

        driver_settings_chrome.get("https://stellarburgers.nomoreparties.site/register")
        driver_settings_chrome.find_element(*TestLocators.NAME_FIELD).send_keys(data.name)
        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(helpers.generate_login() + '@ya.ru')
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(helpers.generate_password())
        driver_settings_chrome.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 3).until(expected_conditions.url_contains("/login"))
        assert driver_settings_chrome.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_registration_without_name_failed(self, driver_settings_chrome):
        driver_settings_chrome.get("https://stellarburgers.nomoreparties.site/register")
        email = helpers.generate_login() + '@ya.ru'
        password = helpers.generate_password()
        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)
        driver_settings_chrome.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        assert driver_settings_chrome.current_url == "https://stellarburgers.nomoreparties.site/register"
        assert driver_settings_chrome.find_element(*TestLocators.NAME_FIELD).get_attribute("value") == ""
        assert driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).get_attribute("value") == email
        assert driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).get_attribute("value") == password

    def test_registration_with_short_password_failed(self, driver_settings_chrome):
        driver_settings_chrome.get("https://stellarburgers.nomoreparties.site/register")
        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys("benks")
        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(helpers.generate_login() + '@ya.ru')
        password = helpers.generate_password()[:-3]
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)
        driver_settings_chrome.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ERROR_REGISTRATION))
        assert driver_settings_chrome.find_element(*TestLocators.ERROR_REGISTRATION).text == 'Некорректный пароль'

    def test_registration_with_bad_email_failed(self, driver_settings_chrome):
        driver_settings_chrome.get("https://stellarburgers.nomoreparties.site/register")
        driver_settings_chrome.find_element(*TestLocators.NAME_FIELD).send_keys("benks")
        driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(helpers.generate_login())
        driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(helpers.generate_password())
        driver_settings_chrome.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver_settings_chrome, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ERROR_REGISTRATION))
        assert driver_settings_chrome.find_element(*TestLocators.ERROR_REGISTRATION).text == 'Такой пользователь уже существует'
