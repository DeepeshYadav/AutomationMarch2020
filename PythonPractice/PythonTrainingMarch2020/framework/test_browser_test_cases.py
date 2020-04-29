from selenium import webdriver
import time





def test_google_com():
    url = 'https://www.google.co.in'
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_name('q').send_keys('Selenium')
    driver.find_element_by_name('btnK').click()
    time.sleep(5)

def test_facebook_page():
    url = 'https://www.facebook.com'
    driver.get(url)
    time.sleep(10)
    driver.close()