import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators.locators import ConstructorLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructorTabs:
    @pytest.mark.parametrize("tab_locator, expected_text", [
        (ConstructorLocators.SAUCES_TAB, "Соусы"),
        (ConstructorLocators.FILLINGS_TAB, "Начинки")
    ])
    def test_switch_tabs(self, driver, tab_locator, expected_text):
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Ждем, когда элемент станет кликабельным и кликаем
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(tab_locator)
        )
        element.click()

        # Ждем, пока активная вкладка станет ожидаемой
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, expected_text)
        )

        # Проверяем текст активной вкладки
        active_tab = driver.find_element(*ConstructorLocators.ACTIVE_TAB).text
        assert expected_text in active_tab

    def test_switch_from_sauces_to_buns(self, driver):
        """Тест для перехода с соусов на булки"""
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переходим на соусы
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)
        )
        sauces_tab.click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Соусы")
        )

        # Возвращаемся на булки
        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB)
        )
        buns_tab.click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Булки")
        )

        active_tab = driver.find_element(*ConstructorLocators.ACTIVE_TAB).text
        assert "Булки" in active_tab

    def test_buns_tab_active_by_default(self, driver):
        """Тест, что вкладка 'Булки' активна по умолчанию"""
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Ждем загрузки страницы и проверяем, что активна вкладка "Булки"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorLocators.ACTIVE_TAB, "Булки")
        )

        active_tab = driver.find_element(*ConstructorLocators.ACTIVE_TAB).text
        assert "Булки" in active_tab