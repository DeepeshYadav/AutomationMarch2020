from selenium import webdriver
import time
import pytest


driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)

@pytest.fixture(scope='module')
def setup_teardown():
    url = 'https://www.selenium.dev/'
    driver.maximize_window()
    driver.get(url)
    yield
    driver.close()

def test_to_about_page(setup_teardown):
    driver.find_element_by_xpath('//span[text()="About"]').click()
    driver.find_element_by_xpath('//a[text()="About"]').click()
    assert driver.find_element_by_xpath('//h1[text()="About Selenium"]')

def test_go_to_download_page(setup_teardown):
    driver.find_element_by_xpath('//a[text()="Downloads"]').click()
    assert driver.find_element_by_xpath('//h1[text()="Downloads"]')