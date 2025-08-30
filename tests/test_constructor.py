import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators.locators import ConstructorLocators
import time

def test_switch_to_buns(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*ConstructorLocators.SAUCES_TAB).click()
    driver.find_element(*ConstructorLocators.BUNS_TAB).click()
    time.sleep(1)
    active_tab = driver.find_element(*ConstructorLocators.ACTIVE_TAB).text
    assert "Булки" in active_tab

def test_switch_to_sauces(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*ConstructorLocators.SAUCES_TAB).click()
    active_tab = driver.find_element(*ConstructorLocators.ACTIVE_TAB).text
    assert "Соусы" in active_tab

def test_switch_to_fillings(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*ConstructorLocators.FILLINGS_TAB).click()
    active_tab = driver.find_element(*ConstructorLocators.ACTIVE_TAB).text
    assert "Начинки" in active_tab
