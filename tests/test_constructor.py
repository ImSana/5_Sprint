from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait

from tests.conftest import driver_settings_chrome


def test_select_bread_default(driver_settings_chrome):
    # Выбрана вкладка булок
    assert "Булки" == driver_settings_chrome.find_element(*TestLocators.SELECTED_INGREDIENT_TAB).text

    # Начинки и соусы не выбраны
    selected_not_tabs = driver_settings_chrome.find_elements(*TestLocators.UNSELECTED_INGREDIENT_TABS)
    for tab in selected_not_tabs:
        assert "Соусы" in tab.text or "Начинки" in tab.text


def test_sauces_select(driver_settings_chrome):
    # жмём по вкладке соусов в конструкторе
    sauces = WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.SAUCES_TUB))
    sauces.click()
    WebDriverWait(driver_settings_chrome, 10).until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Соусы"))
    assert "Соусы" == driver_settings_chrome.find_element(*TestLocators.SELECTED_INGREDIENT_TAB).text

    # Вкладки булок и начинок не выбраны
    selected_not_tabs = driver_settings_chrome.find_elements(*TestLocators.UNSELECTED_INGREDIENT_TABS)
    for tab in selected_not_tabs:
        assert "Булки" in tab.text or "Начинки" in tab.text


def test_select_fuelling(driver_settings_chrome):
    # жмём по вкладке начинок в конструкторе
    WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.FILLINGS_TUB))
    driver_settings_chrome.find_element(*TestLocators.FILLINGS_TUB).click()
    WebDriverWait(driver_settings_chrome, 10).until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Начинки"))
    assert "Начинки" == driver_settings_chrome.find_element(*TestLocators.SELECTED_INGREDIENT_TAB).text

    # Булки и соусы не выбраны
    selected_not_bread_sauces = driver_settings_chrome.find_elements(*TestLocators.UNSELECTED_INGREDIENT_TABS)
    for tab in selected_not_bread_sauces:
        assert "Булки" in tab.text or "Соусы" in tab.text


def test_bread_select(driver_settings_chrome):
    # жмём по вкладке начинок в конструкторе
    fuellings = WebDriverWait(driver_settings_chrome,5).until(ex_cond.element_to_be_clickable(TestLocators.FILLINGS_TUB))
    try:
        fuellings.click()
    except ElementClickInterceptedException:
        driver_settings_chrome.execute_script("arguments[0].click()", fuellings)

    # Выбрана вкладка начинки
    WebDriverWait(driver_settings_chrome,10). \
        until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Начинки"))

    # жмём по вкладке булок в конструкторе
    bread = WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.BUNS_TUB))
    try:
        bread.click()
    except ElementClickInterceptedException:
        driver_settings_chrome.execute_script("arguments[0].click()", bread)

    # Выбрана вкладка булок
    WebDriverWait(driver_settings_chrome, 10).until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Булки"))

    # Вкладки соусов и начинок не выбраны
    selected_not_tabs = driver_settings_chrome.find_elements(*TestLocators.UNSELECTED_INGREDIENT_TABS)
    for tab in selected_not_tabs:
        assert "Соусы" in tab.text or "Начинки" in tab.text
