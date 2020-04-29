from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element_by_name('q').send_keys("Hello Keyword")
driver.find_element_by_class_name('hp vasq').click()
driver.find_element_by_name('btnK').click()