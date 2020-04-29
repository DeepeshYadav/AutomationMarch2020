from selenium import  webdriver

driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)


def close_browser():
    driver.close()