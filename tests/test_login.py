import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from helpers.generators import generate_unique_email
from helpers.auth_helpers import register_user, login_user
from locators.locators import LoginLocators

logger = logging.getLogger(__name__)


def test_login_main_button(driver):
    """Тест входа через кнопку 'Войти в аккаунт' на главной странице"""
    email = generate_unique_email()
    password = "test1234"
    register_user(driver, email, password)

    logger.info("Открытие главной страницы")
    driver.get("https://stellarburgers.nomoreparties.site")

    # Проверка загрузки главной страницы
    wait = WebDriverWait(driver, 20)
    wait.until(EC.url_contains("stellarburgers.nomoreparties.site"))
    assert "stellarburgers" in driver.current_url
    assert "Соберите бургер" in driver.page_source

    logger.info("Ожидание кнопки 'Войти в аккаунт'")
    login_button = wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_MAIN))
    assert login_button.is_displayed()
    logger.info("Клик по кнопке 'Войти в аккаунт'")
    login_button.click()

    # Проверка перехода на страницу логина
    wait.until(EC.url_contains("/login"))
    assert "login" in driver.current_url

    login_user(driver, email, password)

    # Проверка успешного входа
    order_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))
    )
    assert order_button.is_displayed()

    # Дополнительная проверка - что мы на главной странице после входа
    wait.until(EC.url_contains("stellarburgers.nomoreparties.site"))
    assert "stellarburgers" in driver.current_url
    assert "Соберите бургер" in driver.page_source


def test_login_from_registration_form(driver):
    """Тест входа через ссылку 'Войти' на странице регистрации"""
    email = generate_unique_email()
    password = "test1234"
    register_user(driver, email, password)

    logger.info("Открытие страницы регистрации")
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Проверка загрузки страницы регистрации
    wait = WebDriverWait(driver, 20)
    wait.until(EC.url_contains("/register"))
    assert "register" in driver.current_url
    assert "Регистрация" in driver.page_source

    logger.info("Ожидание ссылки 'Войти'")
    login_link = wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_REGISTRATION))
    assert login_link.is_displayed()
    logger.info("Клик по ссылке 'Войти'")
    login_link.click()

    # Проверка перехода на страницу логина
    wait.until(EC.url_contains("/login"))
    assert "login" in driver.current_url

    login_user(driver, email, password)

    # Проверка успешного входа
    order_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))
    )
    assert order_button.is_displayed()

    # Дополнительная проверка - что мы на главной странице после входа
    wait.until(EC.url_contains("stellarburgers.nomoreparties.site"))
    assert "stellarburgers" in driver.current_url
    assert "Соберите бургер" in driver.page_source