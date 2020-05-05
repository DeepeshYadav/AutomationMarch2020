from .initiate_driver import *
from selenium import webdriver
from .ui_locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

wait = WebDriverWait(driver, 20)
# This is explicit wait which will apply on specific element.

def go_to_hotel_page(driver : webdriver):
    """ This function will navigate to hotel booking page
    :param driver:
    :return:
    """
    hotel_element = wait.until(EC.presence_of_element_located((By.XPATH, HOTEL_ICON_XPATH)))
    hotel_element.click()

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


def handle_alert_box(driver : webdriver):
    driver.find_element_by_id(DISPLAY_ALERT_ID).click()
    alert = driver.switch_to.alert
    alert.accept()
    msg_element = driver.find_element_by_id(MESSAGE_LOCATOR_ID)
    return msg_element.text


def handle_confirm_box(driver : webdriver, accept=True):
    driver.find_element_by_id(DISPLAY_CONFIRM_BOX_ID).click()
    alert = driver.switch_to.alert
    if accept:
        alert.accept()
    else:
        alert.dismiss()
    time.sleep(5)
    msg_element = driver.find_element_by_id(MESSAGE_LOCATOR_ID)
    return msg_element.text


def handle_prompt_box(driver : webdriver, input=None):
    driver = webdriver.Chrome()
    driver.find_element_by_id(DISPLAY_PROMPT_BOX_ID).click()
    alert = driver.switch_to.alert
    if input:
        alert.send_keys(input)
        alert.accept()
        time.sleep(5)
        msg_element = driver.find_element_by_id(MESSAGE_LOCATOR_ID)
        return msg_element.text
    else:
        alert.dismiss()
        return None


