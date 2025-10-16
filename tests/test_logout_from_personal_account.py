# tests/test_logout.py
import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locator import MainPageLocators
from locators.login_page_locator import LoginPageLocators
from locators.profile_page_locator import ProfilePageLocators
from data import BASE_URL

# Тест выхода из аккаунта по кнопке «Выйти» в личном кабинете
def test_logout_from_personal_account(driver, wait, test_data):
    
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
    
    # Выход из аккаунта через кнопку «Выйти»
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
    
    # Проверяем что произошел переход на страницу логина
    login_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    assert login_header.is_displayed() and driver.current_url == f"{BASE_URL}/login"
    
    driver.quit()