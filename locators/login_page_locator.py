from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Поля формы
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    
    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    # Ссылки
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")