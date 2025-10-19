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

    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    
    # Сообщения об ошибках
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")

    # Успешный вход (редирект)
    SUCCESS_LOGIN_INDICATOR = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")