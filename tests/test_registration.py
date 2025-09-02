from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import RegistrationLocators
from helpers.generators import generate_unique_email  # Импортируем функцию из generators.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_registration(driver):
    wait = WebDriverWait(driver, 10)

    # Открываем страницу и ждем загрузки формы
    driver.get("https://stellarburgers.nomoreparties.site/register")
    wait.until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT))

    # Заполняем форму
    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Тестовый")

    email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Email']/..//input")))
    email_input.send_keys(generate_unique_email())

    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("TestPassword123!")

    # Кликаем и ждем перенаправления
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    # Ждем перенаправления на страницу логина
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert "login" in driver.current_url