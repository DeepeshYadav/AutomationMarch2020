from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)

# Implicit wait : It waits for all the element till it is visible for specific time.
# It's life is till web driver is working.


# Explicit Wait : Explicit wait applies on specific element whenever required.



