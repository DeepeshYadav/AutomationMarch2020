from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)

def test_google_com():
    driver.get("https://www.google.co.in")
    driver.maximize_window()
    driver.find_element_by_name('q').send_keys('Selenium')
    driver.find_element_by_name('btnK').click()
    driver.close()

def test_facebook_page():
    driver.get("https://www.facebook.com")
    time.sleep(5)
    driver.close()
