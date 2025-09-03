from locators.locators import NavigationLocators, LoginLocators
from helpers.generators import generate_unique_email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)

def login_user(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    wait = WebDriverWait(driver, 20)
    # Ожидание и ввод email
    email_input = wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT))
    email_input.send_keys(email)

    # Ожидание и ввод пароля
    password_input = wait.until(EC.visibility_of_element_located(LoginLocators.PASSWORD_INPUT))
    password_input.send_keys(password)

    # Ожидание и клик по кнопке входа
    submit_button = wait.until(EC.element_to_be_clickable(LoginLocators.SUBMIT_BUTTON))
    submit_button.click()

    # Ожидание успешного входа - появление кнопки "Оформить заказ"
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
    logger.info("Вход выполнен успешно")


def test_go_to_profile(driver):
    email = generate_unique_email()
    password = "123456"
    from helpers.auth_helpers import register_user
    register_user(driver, email, password)
    login_user(driver, email, password)

    # После этого кликаем по кнопке профиля
    wait = WebDriverWait(driver, 20)
    profile_button = wait.until(EC.element_to_be_clickable(NavigationLocators.PROFILE_BUTTON))
    profile_button.click()

    # Проверка перехода в профиль
    wait.until(EC.url_contains("/account/profile"))
    assert "/account/profile" in driver.current_url
    logger.info("Успешный переход в профиль")

def test_constructor_from_profile(driver):
    email = generate_unique_email()
    password = "123456"
    from helpers.auth_helpers import register_user
    register_user(driver, email, password)
    login_user(driver, email, password)

    wait = WebDriverWait(driver, 20)

    # Переход в профиль
    profile_button = wait.until(EC.element_to_be_clickable(NavigationLocators.PROFILE_BUTTON))
    profile_button.click()

    # Проверка что мы в профиле
    wait.until(EC.url_contains("/account/profile"))

    # Переход в конструктор
    constructor_link = wait.until(EC.element_to_be_clickable(NavigationLocators.CONSTRUCTOR_LINK))
    constructor_link.click()

    # Проверка перехода в конструктор
    wait.until(EC.url_contains("stellarburgers.nomoreparties.site"))
    assert "stellarburgers" in driver.current_url
    assert "/account/profile" not in driver.current_url
    logger.info("Успешный переход в конструктор из профиля")

def test_logo_from_profile(driver):
    email = generate_unique_email()
    password = "123456"
    from helpers.auth_helpers import register_user
    register_user(driver, email, password)
    login_user(driver, email, password)

    wait = WebDriverWait(driver, 20)

    # Переход в профиль
    profile_button = wait.until(EC.element_to_be_clickable(NavigationLocators.PROFILE_BUTTON))
    profile_button.click()

    # Проверка что мы в профиле
    wait.until(EC.url_contains("/account/profile"))

    # Клик по логотипу
    logo_link = wait.until(EC.element_to_be_clickable(NavigationLocators.LOGO_LINK))
    logo_link.click()

    # Проверка перехода на главную страницу
    wait.until(EC.url_contains("stellarburgers.nomoreparties.site"))
    assert "stellarburgers" in driver.current_url
    assert "/account/profile" not in driver.current_url
    # Дополнительная проверка - наличие кнопки "Оформить заказ"
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
    logger.info("Успешный переход по логотипу на главную страницу")