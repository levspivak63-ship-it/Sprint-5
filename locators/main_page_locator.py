from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//div[span[text()='Булки']]")
    SAUCES_SECTION = (By.XPATH, "//div[span[text()='Соусы']]")
    FILLINGS_SECTION = (By.XPATH, "//div[span[text()='Начинки']]")