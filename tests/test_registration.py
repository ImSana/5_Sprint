from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait


def test_registration_with_correct_data_passes(driver_settings_chrome, get_user_correct):
    # Переход на форму регистрации
    driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver_settings_chrome.find_element(*TestLocators.LINK_REGISTRATION).click()

    # Ввод корректных данных для регистрации
    driver_settings_chrome.find_element(*TestLocators.NAME_FIELD).send_keys(get_user_correct.name)
    driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(get_user_correct.email)
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(get_user_correct.password)

    # жмём по кнопке регистрации
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.REGISTRATION_BUTTON).click()

    # Окно сменилось на форму входа
    WebDriverWait(driver_settings_chrome, 5).until_not(ex_cond.url_contains("/register"))
    assert "https://stellarburgers.nomoreparties.site/login" == driver_settings_chrome.current_url


def test_registration_without_name(driver_settings_chrome, get_user_correct):
    # Переход на страницу регистрации
    driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver_settings_chrome.find_element(*TestLocators.LINK_REGISTRATION).click()

    # Ввод почты и пароля
    email = get_user_correct.email
    password = get_user_correct.password
    driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # жмём по кнопке регистрации, без имени
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.REGISTRATION_BUTTON).click()

    # остались на той же форме регистрации
    assert driver_settings_chrome.find_element(*TestLocators.NAME_FIELD).get_attribute("value") == ""
    assert driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).get_attribute("value") == email
    assert driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).get_attribute("value") == password


def test_registration_invalid_email(driver_settings_chrome, get_not_user_correct):
    # Переход на форму регистрации
    driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver_settings_chrome.find_element(*TestLocators.LINK_REGISTRATION).click()

    # Ввод почты с неверным форматом
    name = get_not_user_correct.name
    email = get_not_user_correct.email
    password = f'{get_not_user_correct.password}6'
    driver_settings_chrome.find_element(*TestLocators.NAME_FIELD).send_keys(name)
    driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # Кнопка регистрации
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.REGISTRATION_BUTTON).click()

    # остались на той же форме регистрации
    assert driver_settings_chrome.find_element(*TestLocators.NAME_FIELD).get_attribute("value") == name
    assert driver_settings_chrome.find_element(*TestLocators.EMAIL_FIELD).get_attribute("value") == email
    assert driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).get_attribute("value") == password
    # ошибка регистрации
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ERROR_REGISTRATION))
    assert "Такой пользователь уже существует" == driver_settings_chrome.find_element(*TestLocators.ERROR_REGISTRATION).text


def test_registration_password_less_6(driver_settings_chrome, get_not_user_correct):
    # Переход регистрацию
    driver_settings_chrome.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver_settings_chrome.find_element(*TestLocators.LINK_REGISTRATION).click()

    # Ввод пароля 5 символов
    driver_settings_chrome.find_element(*TestLocators.PASSWORD_FIELD).send_keys(get_not_user_correct.password)
    # кнопка регистрации
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON))
    driver_settings_chrome.find_element(*TestLocators.REGISTRATION_BUTTON).click()

    # ошибка
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.visibility_of_element_located(TestLocators.ERROR_REGISTRATION))
    assert "Некорректный пароль" == driver_settings_chrome.find_element(*TestLocators.ERROR_REGISTRATION).text

