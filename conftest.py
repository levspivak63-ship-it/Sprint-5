# conftest.py
# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from data import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    
    return WebDriverWait(driver, 10)