from selenium.webdriver.common.by import By

class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/parent::div//input")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")  # Сообщение об ошибке

class LoginLocators:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка входа на главной
    LOGIN_BUTTON_REGISTRATION = (By.XPATH, "//a[text()='Войти']")  # Кнопка входа в форме регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле пароль
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button') and text()='Войти']")  # Кнопка "Войти"

class NavigationLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO_LINK = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" на странице логина

class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Таб "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Таб "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Таб "Начинки"
    ACTIVE_TAB = (By.XPATH, '//div[@class = ''"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')  # Активный таб

class ProfileLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выйти"

