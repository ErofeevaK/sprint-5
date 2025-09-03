import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from locators.locators import LoginLocators, RegistrationLocators

logger = logging.getLogger(__name__)


def register_user(driver, email, password):
    """
    Регистрация нового пользователя
    """
    wait = WebDriverWait(driver, 20)
    logger.info("Открытие страницы регистрации")
    driver.get("https://stellarburgers.nomoreparties.site/register")

    try:
        logger.info("Ожидание загрузки формы регистрации")
        wait.until(EC.presence_of_element_located(RegistrationLocators.REGISTER_BUTTON))

        logger.info("Ввод имени")
        name_input = wait.until(EC.element_to_be_clickable(RegistrationLocators.NAME_INPUT))
        name_input.send_keys("Тест")

        logger.info("Ввод email")
        email_input = wait.until(EC.element_to_be_clickable(RegistrationLocators.EMAIL_INPUT))
        email_input.send_keys(email)

        logger.info("Ввод пароля")
        password_input = wait.until(EC.element_to_be_clickable(RegistrationLocators.PASSWORD_INPUT))
        password_input.send_keys(password)

        logger.info("Нажатие кнопки регистрации")
        register_button = wait.until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BUTTON))
        register_button.click()

        # Проверка наличия ошибок с явным ожиданием
        logger.info("Проверка наличия ошибок валидации")
        try:
            # Ждем появления ошибок не более 2 секунд
            error_wait = WebDriverWait(driver, 2)
            errors = error_wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "input__error"))
            )
            if errors:
                error_msg = f"Ошибка при регистрации: {errors[0].text}"
                logger.error(error_msg)
                driver.save_screenshot("register_error.png")
                raise Exception(error_msg)
        except TimeoutException:
            # Ошибок нет, продолжаем
            logger.info("Ошибки валидации не обнаружены")

        logger.info("Ожидание редиректа на /login")
        wait.until(EC.url_contains("/login"))

        # Проверка редиректа после регистрации
        assert "login" in driver.current_url, "Не произошел редирект на страницу логина после регистрации"
        logger.info("Регистрация завершена успешно")

    except TimeoutException as e:
        logger.error(f"Timeout при регистрации: {e}")
        driver.save_screenshot("register_timeout.png")
        raise


def login_user(driver, email, password):
    """
    Авторизация пользователя
    """
    wait = WebDriverWait(driver, 20)

    logger.info("Ожидание поля email")
    email_input = wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT))
    logger.info("Ввод email")
    email_input.send_keys(email)

    logger.info("Ожидание поля пароля")
    password_input = wait.until(EC.visibility_of_element_located(LoginLocators.PASSWORD_INPUT))
    logger.info("Ввод пароля")
    password_input.send_keys(password)

    logger.info("Ожидание кнопки входа")
    submit_button = wait.until(EC.element_to_be_clickable(LoginLocators.SUBMIT_BUTTON))
    logger.info("Нажатие кнопки входа")
    submit_button.click()

    logger.info("Ожидание успешного входа")
    try:
        # Ожидание появления кнопки "Оформить заказ" или перехода на главную
        wait.until(EC.any_of(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")),
            EC.url_contains("stellarburgers.nomoreparties.site")
        ))

        # Дополнительная проверка успешного входа
        order_button = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))
        )
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не найдена после входа"

        logger.info("Вход выполнен успешно")
        return True

    except TimeoutException:
        # Проверяем, не появились ли ошибки авторизации
        try:
            auth_error = driver.find_element(By.CLASS_NAME, "input__error")
            error_msg = f"Ошибка авторизации: {auth_error.text}"
            logger.error(error_msg)
            driver.save_screenshot("login_auth_error.png")
            raise Exception(error_msg)
        except NoSuchElementException:
            driver.save_screenshot("login_failed.png")
            logger.error("Не удалось выполнить вход: кнопка 'Оформить заказ' не найдена и ошибок не обнаружено")
            raise Exception("Не удалось выполнить вход")