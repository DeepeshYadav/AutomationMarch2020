from browser_initiator import *
from ui_locators import *

def test_to_about_page(setup_teardown):
    driver.find_element_by_xpath(ABOUT_PAGE_XPATH).click()
    driver.find_element_by_xpath(ABOUT_PAGE_XPATH2).click()
    assert driver.find_element_by_xpath(ABOUT_SELENIUM_XPATH_MSG)

def test_go_to_download_page(setup_teardown):
    driver.find_element_by_xpath(DOWNLOAD_PATH_XPATH).click()
    assert driver.find_element_by_xpath(GRID_SERVER_XPATH)