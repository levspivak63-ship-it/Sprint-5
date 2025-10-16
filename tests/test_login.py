# tests/test_login.py
import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locator import MainPageLocators
from locators.login_page_locator import LoginPageLocators
from locators.registration_page__locator import RegisterPageLocators
from locators.forgot_password_locator import ForgotPasswordLocators
from data import BASE_URL

class TestLogin:
    # Тест входа через кнопку 'Войти в аккаунт' на главной
    def test_login_from_main_page_button(self, driver, wait, test_data):
        
        test_email = test_data["email"]
        test_password = test_data["password"]
        
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()
        
        driver.quit()

    # Тест входа через кнопку 'Личный кабинет'
    def test_login_from_personal_account_button(self, driver, wait, test_data):
        
        test_email = test_data["email"]
        test_password = test_data["password"]
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()
        
        driver.quit()

    # Тест входа через кнопку в форме регистрации
    def test_login_from_registration_form(self, driver, wait, test_data):
        
        test_email = test_data["email"]
        test_password = test_data["password"]
        
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()
        
        driver.quit()

    # Тест входа через кнопку в форме восстановления пароля
    def test_login_from_password_recovery_form(self, driver, wait, test_data):
       
        test_email = test_data["email"]
        test_password = test_data["password"]
        
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*ForgotPasswordLocators.LOGIN_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()
        
        driver.quit()