# locators/forgot_password_locator.py
from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    """Локаторы для страницы восстановления пароля"""
    
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    
    # Кнопки
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    
    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")
    
    # Сообщения
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")