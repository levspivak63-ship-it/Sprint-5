# tests/test_navigation.py
import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locator import MainPageLocators
from locators.login_page_locator import LoginPageLocators
from locators.profile_page_locator import ProfilePageLocators
from data import BASE_URL

class TestNavigation:
    # Тест перехода в личный кабинет
    def test_navigate_to_personal_account(self, driver, wait, test_data):
                
        test_email = test_data["email"]
        test_password = test_data["password"]
        
        # Вход в систему
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ждем загрузки главной страницы после входа
        order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
        
        # Переход в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверяем что открылся личный кабинет
        profile_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))
        assert profile_link.is_displayed()
        
        driver.quit()

    # Тест перехода из личного кабинета в конструктор по кнопке «Конструктор»
    def test_navigate_from_personal_account_to_constructor_via_button(self, driver, wait, test_data):
        
        test_email = test_data["email"]
        test_password = test_data["password"]
        
        # Вход в систему
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ждем загрузки главной страницы после входа
        order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
        
        # Переход в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверяем что открылся личный кабинет
        profile_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))
        assert profile_link.is_displayed()
        
        # Переход обратно в конструктор через кнопку «Конструктор»
        driver.find_element(*ProfilePageLocators.CONSTRUCTOR_BUTTON).click()
        
        # Проверяем что вернулись на главную страницу (конструктор)
        order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
        assert order_button.is_displayed() and BASE_URL in driver.current_url
        
        driver.quit()

    # Тест перехода из личного кабинета в конструктор по логотипу Stellar Burgers
    def test_navigate_from_personal_account_to_constructor_via_logo(self, driver, wait, test_data):
        
        test_email = test_data["email"]
        test_password = test_data["password"]
        
        # Вход в систему
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ждем загрузки главной страницы после входа
        order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
        
        # Переход в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверяем что открылся личный кабинет
        profile_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))
        assert profile_link.is_displayed()
        
        # Переход обратно в конструктор через логотип Stellar Burgers
        driver.find_element(*ProfilePageLocators.LOGO).click()
        
        # Проверяем что вернулись на главную страницу (конструктор)
        order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
        assert order_button.is_displayed() and BASE_URL in driver.current_url
        
        driver.quit()