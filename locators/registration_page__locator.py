from selenium.webdriver.common.by import By

class RegisterPageLocators:
    # Поля формы
    NAME_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    
    # Кнопки
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Ссылки
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")