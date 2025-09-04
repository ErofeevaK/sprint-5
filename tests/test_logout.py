import pytest
from locators.locators import LoginLocators, NavigationLocators, ProfileLocators
from helpers.generators import generate_unique_email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.auth_helpers import register_user, login_user


class TestLogout:
    def test_logout(self, driver):
        """Тест выхода из системы"""
        # Инициализация WebDriverWait
        wait = WebDriverWait(driver, 10)

        # Генерация уникальных данных для регистрации
        email = generate_unique_email()
        password = "TestPassword123"

        # Регистрация пользователя
        register_user(driver, email, password)

        # Вход пользователя
        login_user(driver, email, password)

        # Переход в профиль
        wait.until(EC.element_to_be_clickable(NavigationLocators.PROFILE_BUTTON)).click()

        # Ожидание загрузки страницы профиля
        wait.until(EC.url_contains("/account/profile"))

        # Выход из системы
        logout_button = wait.until(EC.element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON))
        logout_button.click()

        # Проверка, что произошел переход на страницу логина
        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        # Дополнительная проверка - наличие элементов формы входа
        email_input = wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT))
        password_input = wait.until(EC.visibility_of_element_located(LoginLocators.PASSWORD_INPUT))

        assert email_input.is_displayed(), "Поле email не отображается после выхода"
        assert password_input.is_displayed(), "Поле password не отображается после выхода"
        assert "login" in driver.current_url, "URL не соответствует странице логина"