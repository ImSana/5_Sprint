from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait

from tests.conftest import driver_settings_chrome


def test_personal_account_in_constructor(driver_settings_chrome):
    # Нажать кнопку «Войти в аккаунт»
    driver_settings_chrome.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "uncle_Bens111@ya.ru"
    password = "123123"
    driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # Жмём по кнопке входа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/login"))

    # Идём в личный кабинет
    driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/account/profile"))

    # Переход в конструктор по вкладке Конструктор
    driver_settings_chrome.find_element(*TestLocators.CONSTRUCTOR_TAB).click()
    WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/account/profile"))

    # страница с конструктором
    assert "Соберите бургер" == driver_settings_chrome.find_element(*TestLocators.INGREDIENTS_HEADER).text
    assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url


def test_go_to_account_in_constructor_by_logo(driver_settings_chrome):
    # По кнопке «Войти в аккаунт»
    driver_settings_chrome.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "uncle_Bens111@ya.ru"
    password = "123123"
    driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # Жмём по кнопке входа
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/login"))

    # Переход в личный кабинет
    driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.url_contains("/account/profile"))

    # Переход в конструктор по логотипу Stellar Burgers
    driver_settings_chrome.find_element(*TestLocators.LOGO_BUTTON).click()
    WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/account/profile"))

    # Отображается страница с конструктором
    assert "Соберите бургер" == driver_settings_chrome.find_element(*TestLocators.INGREDIENTS_HEADER).text
    assert "https://stellarburgers.nomoreparties.site/" == driver_settings_chrome.current_url
