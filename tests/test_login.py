# tests/test_login.py
import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locator import MainPageLocators
from locators.login_page_locator import LoginPageLocators
from locators.registration_page__locator import RegisterPageLocators
from locators.forgot_password_locator import ForgotPasswordLocators
from data import TEST_CREDENTIALS

class TestLogin:
    
    # Тест входа через кнопку 'Войти в аккаунт' на главной
    def test_login_from_main_page_button(self, driver, wait):
                
        # Загрузка тестовых данных
        test_email = TEST_CREDENTIALS["email"]  
        test_password = TEST_CREDENTIALS["password"]
        
        # Шаги входа в систему
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        
        # Ожидание загрузки страницы логина
        wait.until(EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE))
        
        # Заполнение формы логина
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ожидание загрузки главной страницы и проверка активности кнопки "Оформить заказ"
        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()

    # Тест входа через кнопку 'Личный кабинет'
    def test_login_from_personal_account_button(self, driver, wait):
                
        # Загрузка тестовых данных
        test_email = TEST_CREDENTIALS["email"]  
        test_password = TEST_CREDENTIALS["password"]
        
        # Шаги входа в систему
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Ожидание загрузки страницы логина
        wait.until(EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE))
        
        # Заполнение формы логина
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ожидание загрузки главной страницы и проверка активности кнопки "Оформить заказ"
        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()

    # Тест входа через кнопку в форме регистрации
    def test_login_from_registration_form(self, driver, wait):
                
        # Загрузка тестовых данных
        test_email = TEST_CREDENTIALS["email"]  
        test_password = TEST_CREDENTIALS["password"]
        
        # Шаги входа в систему через форму регистрации
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        
        # Ожидание страницы логина и переход к регистрации
        wait.until(EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE))
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        
        # Ожидание страницы регистрации и возврат к логину
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.PAGE_TITLE))
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        
        # Заполнение формы логина
        wait.until(EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ожидание загрузки главной страницы и проверка активности кнопки "Оформить заказ"
        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()

    # Тест входа через кнопку в форме восстановления пароля
    def test_login_from_password_recovery_form(self, driver, wait):
                
        # Загрузка тестовых данных
        test_email = TEST_CREDENTIALS["email"]  
        test_password = TEST_CREDENTIALS["password"]
        
        # Шаги входа в систему через форму восстановления пароля
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        
        # Ожидание страницы логина и переход к восстановлению пароля
        wait.until(EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE))
        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        
        # Ожидание страницы восстановления пароля и возврат к логину
        wait.until(EC.visibility_of_element_located(ForgotPasswordLocators.PAGE_TITLE))
        driver.find_element(*ForgotPasswordLocators.LOGIN_LINK).click()
        
        # Заполнение формы логина
        wait.until(EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ожидание загрузки главной страницы и проверка активности кнопки "Оформить заказ"
        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()