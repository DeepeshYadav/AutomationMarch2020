from selenium import webdriver
import pytest
import time

driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)


@pytest.fixture(scope='module')
def setup_teardown():
    url = 'https://www.selenium.dev/'
    time.sleep(10)
    driver.maximize_window()
    driver.get(url)