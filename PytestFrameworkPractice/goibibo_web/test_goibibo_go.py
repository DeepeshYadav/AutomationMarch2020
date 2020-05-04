import pytest
from .initiate_driver import *
import time
from logging import debug

def test_book_flight(test_setup_teardown):
    driver.find_element_by_id("gosuggest_inputSrc").send_keys("Pune")
    time.sleep(1)
    source_elems = driver.find_elements_by_xpath('//ul[contains(@id, "react-autosuggest")]//li')
    for elem in source_elems:
        sr_data = str(elem.text).split("\n")[0]
        if sr_data == 'Pune, India(PNQ)':
            elem.click()

    time.sleep(2)
    driver.find_element_by_id("gosuggest_inputDest").send_keys("Mumbai")
    dest_elems = driver.find_elements_by_xpath('//ul[contains(@id, "react-autosuggest")]//li')
    for elem in dest_elems:
        ds_data = str(elem.text).split("\n")[0]
        if ds_data == 'Mumbai, India(BOM)':
            elem.click()

    time.sleep(2)
    driver.find_element_by_id("departureCalendar").click()
    driver.find_element_by_id("fare_20200520").click()
    time.sleep(2)

    driver.find_element_by_id("returnCalendar").click()
    driver.find_element_by_id("fare_20200525").click()
    time.sleep(2)

    driver.find_element_by_id("pax_link_common").click()
    time.sleep(2)

    driver.find_element_by_id("adultPaxBox").send_keys("2")
    driver.find_element_by_id("childPaxBox").send_keys("2")
    driver.find_element_by_id("infantPaxBox").send_keys("1")

    driver.find_element_by_id('gi_class').click()
    time.sleep(2)
    driver.find_element_by_xpath("//option[@value='B']").click()
    time.sleep(2)
    driver.find_element_by_id('gi_search_btn').click()



