from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
url = 'https://www.google.co.in'
driver.get(url)
driver.maximize_window()
try:
    driver.find_element_by_name('q').send_keys("Selenium")
    time.sleep(2)
    driver.find_element_by_name('q').send_keys()
    driver.find_element_by_id('searchform')
    time.sleep(2)
    # Example by name
    # driver.find_element_by_name('btnK').click()
    # Example by xpath
    # driver.find_element_by_xpath("//*[@value='Google Search']").click()
    # Examples by CSS selector
    # driver.find_element_by_css_selector("input[value='Google Search']").click()
    time.sleep(5)
except Exception as e:
    raise e
finally:
    driver.quit()