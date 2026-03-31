# locators/profile_page_locator.py
from selenium.webdriver.common.by import By

class ProfilePageLocators:
    """Локаторы для страницы профиля"""
    
    # Навигация
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    
    # Кнопки
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    LOGO = (By.XPATH, "//div[contains(@class, 'logo')]")
    
    # Заголовок страницы
    PROFILE_PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Профиль')]")
    
    # Поля профиля
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")