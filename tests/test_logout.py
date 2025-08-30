from locators.locators import LoginLocators, NavigationLocators, ProfileLocators
from helpers.generators import generate_unique_email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_logout(driver):
    email = generate_unique_email()
    password = "test1234"
    from tests.test_login import register_user
    register_user(driver, email, password)

    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
    time.sleep(1)

    wait = WebDriverWait(driver, 5)
    driver.find_element(*NavigationLocators.PROFILE_BUTTON).click()
    wait.until(EC.element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON)).click()

