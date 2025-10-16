from selenium.webdriver.common.by import By

class ProfilePageLocators:
    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    
    # Кнопки
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")