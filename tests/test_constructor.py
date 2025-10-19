# tests/test_constructor.py
import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locator import MainPageLocators

class TestConstructor:
    
    # Тест перехода к разделу 'Соусы'
    def test_constructor_sauces_section(self, driver, wait):
                
        # Переходим из раздела "Булки" (по умолчанию) в раздел "Соусы"
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
        
        # Проверяем что раздел "Соусы" стал активным
        active_section = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION))
        assert "Соусы" in active_section.text

    # Тест перехода к разделу 'Начинки'
    def test_constructor_fillings_section(self, driver, wait):
        
        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()
        
        # Проверяем что раздел "Начинки" стал активным
        active_section = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION))
        assert "Начинки" in active_section.text

    # Тест перехода к разделу 'Булки'
    def test_constructor_buns_section(self, driver, wait):
               
        # Переходим в раздел Соусы (не является изначально активным), чтобы исключить ошибки теста
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
        
        # Ждем активации раздела Соусы
        active_section = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION))
        assert "Соусы" in active_section.text
        
        # Переходим обратно в раздел "Булки"
        driver.find_element(*MainPageLocators.BUNS_SECTION).click()
        
        # Проверяем что раздел "Булки" стал активным
        active_section = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_SECTION))
        assert "Булки" in active_section.text