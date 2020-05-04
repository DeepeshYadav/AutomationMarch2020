from .initiate_driver import *
from selenium import webdriver
from .ui_locators import *
import time

def go_to_hotel_page(driver : webdriver):
    """ This function will navigate to hotel booking page
    :param driver:
    :return:
    """
    driver.find_element_by_xpath(HOTEL_ICON_XPATH).click()

def search_hotel(driver: webdriver, placename):
    """ This City name and search it

    :param driver:
    :param placename:
    :return:
    """
    #import pdb;pdb.set_trace()
    driver.find_element_by_id(SEARCH_HOTEL_INPUT_BOX_ID).send_keys(placename)
    time.sleep(2)
    sugget_elements = driver.find_elements_by_xpath(SEARCH_PLACE_XPATH)
    for element in sugget_elements:
        if element.text == placename:
            element.click()
            break
        else:
            continue

def select_checkin_checkout_date(driver: webdriver, checkindate, checkoutdate):
    """ This function will select checkindate and check out date

    :param driver:
    :param checkindate:
    :param checkoutdate:
    :return:
    """
    driver.find_element_by_xpath(CHECK_IN_DATE_XAPTH).click()
    driver.find_element_by_xpath(f"//span[text()='{checkindate}']").click()
    driver.find_element_by_xpath(f"//span[text()='{checkoutdate}']").click()

def select_guest_and_room(driver: webdriver, rooms, adults, children):
    """ This function will add rooms , guest and children and guest count.

    :param driver:
    :param rooms:
    :param adults:
    :param children:
    :return:
    """
    driver.find_element_by_xpath(GUESTS_ROOMS_XPATH).click()
    time.sleep(2)
    # for _ in range(int(rooms)):
    #     driver.find_element_by_xpath(ADD_ROOM_XPATH).click()
    for _ in range(int(adults)):
        driver.find_element_by_xpath(ADD_ADULTS_XPATH).click()
    for _ in range(int(children)):
        driver.find_element_by_xpath(ADD_CHILD_XPATH).click()
        time.sleep(2)
    driver.find_element_by_xpath(ADD_ROOMS_GUEST_DONE_BUTTON_XPATH).click()
    driver.find_element_by_xpath(SEARCH_HOTEL_BUTTON).click()
    time.sleep(5)