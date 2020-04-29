from browser_initiator import *

def test_to_about_page(setup_teardown):
    driver.find_element_by_xpath('//span[text()="About"]').click()
    driver.find_element_by_xpath('//a[text()="About"]').click()
    assert driver.find_element_by_xpath('//h1[text()="About Selenium"]')

def test_go_to_download_page(setup_teardown):
    driver.find_element_by_xpath('//a[text()="Downloads"]').click()
    assert driver.find_element_by_xpath('//h1[text()="Downloads"]')
