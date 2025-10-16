# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from data import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(BASE_URL)
    return driver

@pytest.fixture
def wait(driver):
    from selenium.webdriver.support.wait import WebDriverWait
    return WebDriverWait(driver, 3)

@pytest.fixture
def test_data():
    """Фикстура с тестовыми данными для входа"""
    return {
        "email": "Lev_Spivak_32_125@yandex.ru",
        "password": "123456"
    }