from locators.locators import NavigationLocators, LoginLocators
from helpers.generators import generate_unique_email
import time

def login_user(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
    time.sleep(2)

def test_go_to_profile(driver):
    email = generate_unique_email()
    password = "123456"
    from tests.test_login import register_user
    register_user(driver, email, password)
    login_user(driver, email, password)

    # После этого кликаем по кнопке профиля
    driver.find_element(*NavigationLocators.PROFILE_BUTTON).click()

def test_constructor_from_profile(driver):
    email = generate_unique_email()
    password = "123456"
    from tests.test_login import register_user
    register_user(driver, email, password)
    login_user(driver, email, password)

    driver.find_element(*NavigationLocators.PROFILE_BUTTON).click()
    driver.find_element(*NavigationLocators.CONSTRUCTOR_LINK).click()
    assert "stellarburgers" in driver.current_url

def test_logo_from_profile(driver):
    email = generate_unique_email()
    password = "123456"
    from tests.test_login import register_user
    register_user(driver, email, password)
    login_user(driver, email, password)

    driver.find_element(*NavigationLocators.PROFILE_BUTTON).click()
    driver.find_element(*NavigationLocators.LOGO_LINK).click()
    assert "stellarburgers" in driver.current_url