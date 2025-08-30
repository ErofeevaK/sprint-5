from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import RegistrationLocators
from helpers.generators import generate_unique_email  # Импортируем функцию из generators.py

def test_successful_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Вводим имя
    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Тестовый")

    # Обновленный локатор для поля Email
    email_input = driver.find_element(By.XPATH, "//label[text()='Email']/..//input")
    email_input.send_keys(generate_unique_email())  # Используем функцию для генерации уникального email

    # Вводим пароль
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("TestPassword123")


    # Кликаем по кнопке регистрации
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()


    # Закрытие браузера
    driver.quit()