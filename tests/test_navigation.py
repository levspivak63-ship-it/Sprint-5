# tests/test_navigation.py
import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locator import MainPageLocators
from locators.login_page_locator import LoginPageLocators
from locators.profile_page_locator import ProfilePageLocators
from data import BASE_URL, TEST_CREDENTIALS

class TestNavigation:
    # Тест перехода в личный кабинет
    def test_navigate_to_personal_account(self, driver, wait):
                
        test_email = TEST_CREDENTIALS["email"]
        test_password = TEST_CREDENTIALS["password"]
        
        # Вход в систему
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ждем загрузки главной страницы после входа
        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        
        # Переход в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверяем что открылся личный кабинет (видна ссылка "Профиль")
        profile_link = wait.until(EC.visibility_of_element_located(MainPageLocators.PROFILE_LINK))
        assert profile_link.is_displayed()

    # Тест перехода из личного кабинета в конструктор по кнопке «Конструктор»
    def test_navigate_from_personal_account_to_constructor_via_button(self, driver, wait):
        
        test_email = TEST_CREDENTIALS["email"]
        test_password = TEST_CREDENTIALS["password"]
        
        # Вход в систему
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ждем загрузки главной страницы после входа
        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        
        # Переход в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверяем что открылся личный кабинет
        profile_link = wait.until(EC.visibility_of_element_located(MainPageLocators.PROFILE_LINK))
        assert profile_link.is_displayed()
        
        # Переход обратно в конструктор через кнопку «Конструктор»
        driver.find_element(*ProfilePageLocators.CONSTRUCTOR_BUTTON).click()
        
        # Проверяем что вернулись на главную страницу (конструктор)
        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed() and BASE_URL in driver.current_url

    # Тест перехода из личного кабинета в конструктор по логотипу Stellar Burgers
    def test_navigate_from_personal_account_to_constructor_via_logo(self, driver, wait):
        
        test_email = TEST_CREDENTIALS["email"]
        test_password = TEST_CREDENTIALS["password"]
        
        # Вход в систему
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ждем загрузки главной страницы после входа
        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        
        # Переход в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверяем что открылся личный кабинет
        profile_link = wait.until(EC.visibility_of_element_located(MainPageLocators.PROFILE_LINK))
        assert profile_link.is_displayed()
        
        # Переход обратно в конструктор через логотип Stellar Burgers
        driver.find_element(*ProfilePageLocators.LOGO).click()
        
        # Проверяем что вернулись на главную страницу (конструктор)
        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed() and BASE_URL in driver.current_url