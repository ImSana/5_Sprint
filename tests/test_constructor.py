from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait

from tests.conftest import driver_settings_chrome

class TestConstructor:

    def test_sauces_select(self, driver_settings_chrome):

        sauces = WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.SAUCES_TUB))
        sauces.click()
        WebDriverWait(driver_settings_chrome, 10).until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Соусы"))
        is_active = sauces.find_element(*TestLocators.SAUCES_TUB).get_attribute('class')
        assert 'current' in is_active

    def test_select_fuelling(self, driver_settings_chrome):
        fuelling = WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.FILLINGS_TUB))
        fuelling.click()
        WebDriverWait(driver_settings_chrome, 10).until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Начинки"))
        is_active = fuelling.find_element(*TestLocators.FILLINGS_TUB).get_attribute('class')
        assert 'current' in is_active


    def test_bread_select(self, driver_settings_chrome):
        bread = WebDriverWait(driver_settings_chrome, 5).until(ex_cond.element_to_be_clickable(TestLocators.BUNS_TUB))
        bread.find_element(*TestLocators.SAUCES_TUB).click()
        bread.find_element(*TestLocators.BUNS_TUB).click()
        is_active = bread.find_element(*TestLocators.BUNS_TUB).get_attribute('class')
        assert 'current' in is_active
