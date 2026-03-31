# tests/test_logout.py
import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locator import MainPageLocators
from locators.login_page_locator import LoginPageLocators
from locators.profile_page_locator import ProfilePageLocators
from data import BASE_URL, TEST_CREDENTIALS

# Тест выхода из аккаунта по кнопке «Выйти» в личном кабинете
def test_logout_from_personal_account(driver, wait):
    
    test_email = TEST_CREDENTIALS["email"]
    test_password = TEST_CREDENTIALS["password"]
    
    # Вход в систему
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    
    # Ожидаем загрузки страницы логина
    wait.until(EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE))
    
    # Заполняем форму логина
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
    # Ждем загрузки главной страницы после входа (индикатор успешного входа)
    wait.until(EC.element_to_be_clickable(LoginPageLocators.SUCCESS_LOGIN_INDICATOR))
    
    # Переход в личный кабинет
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    
    # Проверяем что открылся личный кабинет
    profile_link = wait.until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))
    assert profile_link.is_displayed()
    
    # Выход из аккаунта через кнопку «Выйти»
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
    
    # Проверяем что произошел переход на страницу логина
    login_header = wait.until(EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE))
    assert login_header.is_displayed() and driver.current_url == f"{BASE_URL}/login"