# locators/main_page_locator.py
from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//div[span[text()='Булки']]")
    SAUCES_SECTION = (By.XPATH, "//div[span[text()='Соусы']]")
    FILLINGS_SECTION = (By.XPATH, "//div[span[text()='Начинки']]")
    
    # Активный раздел конструктора
    ACTIVE_SECTION = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")
    
    # Кнопка оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Элементы личного кабинета
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")