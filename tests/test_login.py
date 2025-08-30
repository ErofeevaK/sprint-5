from locators.locators import LoginLocators, RegistrationLocators
from helpers.generators import generate_unique_email
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def register_user(driver, email, password):
    wait = WebDriverWait(driver, 20)
    print("Открытие страницы регистрации")
    driver.get("https://stellarburgers.nomoreparties.site/register")

    try:
        print("Ожидание загрузки формы регистрации")
        wait.until(EC.presence_of_element_located(RegistrationLocators.REGISTER_BUTTON))

        print("Ввод имени")
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Тест")

        print("Ввод email")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)

        print("Ввод пароля")
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)

        print("Нажатие кнопки регистрации")
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        # Проверка наличия ошибки
        time.sleep(1)
        errors = driver.find_elements(By.CLASS_NAME, "input__error")
        if errors:
            print("Ошибка при регистрации:", errors[0].text)
            driver.save_screenshot("register_error.png")
            raise Exception("Ошибка регистрации: " + errors[0].text)

        print("Ожидание редиректа на /login")
        wait.until(EC.url_contains("/login"))
        print("Регистрация завершена успешно")

    except TimeoutException as e:
        print("Timeout при регистрации:", e)
        driver.save_screenshot("register_timeout.png")
        raise


def login_user(driver, email, password):
    wait = WebDriverWait(driver, 20)
    print("Ввод email")
    wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).send_keys(email)

    print("Ввод пароля")
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)

    print("Нажатие кнопки входа")
    driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

    print("Ожидание входа или появления кнопки 'Оформить заказ'")
    try:
        # Ожидание появления элемента, указывающего на успешный вход
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        print("Вход выполнен успешно")
    except TimeoutException:
        driver.save_screenshot("login_failed.png")
        raise Exception("Не удалось выполнить вход: кнопка 'Оформить заказ' не найдена")


def test_login_main_button(driver):
    email = generate_unique_email()
    password = "test1234"
    register_user(driver, email, password)

    print("Открытие главной страницы")
    driver.get("https://stellarburgers.nomoreparties.site")

    wait = WebDriverWait(driver, 20)
    print("Клик по кнопке 'Войти в аккаунт'")
    wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_MAIN)).click()

    login_user(driver, email, password)


def test_login_from_registration_form(driver):
    email = generate_unique_email()
    password = "test1234"
    register_user(driver, email, password)

    print("Открытие страницы регистрации повторно")
    driver.get("https://stellarburgers.nomoreparties.site/register")

    wait = WebDriverWait(driver, 20)
    print("Клик по ссылке 'Войти'")
    wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_REGISTRATION)).click()

    login_user(driver, email, password)