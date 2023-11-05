from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait

from tests.conftest import driver_settings_chrome


def test_login_by_button_on_main_page(driver_settings_chrome,):
    # жмём по кнопке «Войти в аккаунт»
    driver_settings_chrome.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "uncle_Bens111@ya.ru"
    password = "123123"
    driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # жмём по кнопке входа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()

    # Окно сменилось на главное с кнопкой оформления заказа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
    assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url


def test_login_by_personal_account_button(driver_settings_chrome,):
    # жмём по кнопке «Личный кабинет»
    driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "uncle_Bens111@ya.ru"
    password = "123123"
    driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # жмём по кнопке входа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()

    # Окно сменилось на главное с кнопкой оформления заказа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
    assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url


def test_login_across_button_in_registration(driver_settings_chrome):
    # Переход на форму регистрации
    driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver_settings_chrome.find_element(*TestLocators.LINK_REGISTRATION).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/register"))

    # жмём по ссылке входа
    driver_settings_chrome.find_element(*TestLocators.ENTER_LINK).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "uncle_Bens111@ya.ru"
    password = "123123"
    driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # жмём по кнопке входа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()

    # Окно сменилось на главное с кнопкой оформления заказа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
    assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url


def test_login_across_button_in_password_recovery(driver_settings_chrome):
    # Переход на форму авторизации
    driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

    # жмём по ссылке восстановления пароля
    driver_settings_chrome.find_element(*TestLocators.RECOVERY_LINK).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/forgot-password"))

    # жмём по ссылке входа
    driver_settings_chrome.find_element(*TestLocators.ENTER_LINK).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "uncle_Bens111@ya.ru"
    password = "123123"
    driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # жмём по кнопке входа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()

    # Окно сменилось на главное с кнопкой оформления заказа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
    assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url
