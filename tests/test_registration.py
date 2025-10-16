# tests/test_registration.py
import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locator import MainPageLocators
from locators.login_page_locator import LoginPageLocators
from locators.registration_page__locator import RegisterPageLocators
from helpers import generate_email
from data import BASE_URL

class TestRegistration:

    # Тест успешной регистрации с валидными данными
    def test_successful_registration(self, driver, wait):
                
        # Переход на страницу регистрации
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        
        # Валидные данные для заполнения формы регистрации
        name = "TestUser"
        email = generate_email()
        password = "123456"
        
        # Заполняем форму
        name_inputs = driver.find_elements(*RegisterPageLocators.NAME_INPUT)
        name_inputs[0].send_keys(name)
        name_inputs[1].send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем переход на страницу логина
        wait.until(EC.url_to_be(f"{BASE_URL}/login"))
        assert driver.current_url == f"{BASE_URL}/login"
        
        driver.quit()

    # Тест регистрации с некорректным паролем
    def test_registration_invalid_password(self, driver, wait):
        
        # Переход на страницу регистрации
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        
        # Данные для заполнения формы регистрации с некорректным паролем
        name = "TestUser"
        email = generate_email()
        password = "123"  # слишком короткий пароль
        
        # Заполняем форму
        name_inputs = driver.find_elements(*RegisterPageLocators.NAME_INPUT)
        name_inputs[0].send_keys(name)
        name_inputs[1].send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем ошибку
        error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "input__error"))).text
        assert "Некорректный пароль" in error_message
        
        driver.quit()