# locators/registration_page_locator.py
from selenium.webdriver.common.by import By

class RegisterPageLocators:
    """Локаторы для страницы регистрации"""
    
    # Поля ввода
    NAME_INPUT = (By.XPATH, "//input[@type='text' and contains(@name, 'name')]")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and contains(@name, 'email')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    # Кнопки
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    
    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Регистрация')]")
    
    # Сообщения об ошибках
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")