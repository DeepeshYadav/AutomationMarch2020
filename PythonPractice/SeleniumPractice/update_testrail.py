from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

import re
with open('testid_file.txt', 'r+') as file:
    data = file.read()
    id_list = re.findall('([0-9]+)', data)

print(id_list)

base_url = 'https://testrail.storagecraft.com/index.php?/cases/view/'
cell_id = 'cell_custom_automated'

username = 'deepesh.yadav@calsoftinc.com'
password = '5TC.CalSoft6!'

total_update_count = 0
test_count = 0
def check_exists_by_locator(webdriver, locator):

    try:
        if locator[0] == 'id':
            webdriver.find_element_by_id(locator[1])
        if locator[0] == 'name':
            webdriver.find_element_by_name(locator[1])
        if locator[0] == 'xpath':
            webdriver.find_element_by_xpath(locator[1])
        if locator[0] == 'css':
            webdriver.find_element_by_css_selector(locator[1])
    except NoSuchElementException:
        return False

    return True

def check_for_login(driver):
    driver.get(f'{base_url}')
    print(f'{base_url}')
    if driver.find_element_by_id('form-inner'):
        driver.find_element_by_id('name').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_css_selector('span[class="single-sign-on"]').click()
    else:
        print("No login page available")

check_for_login(driver)
#id_list = ['135729']
for test_id in id_list:
    test_count += 1
    url = f'{base_url}{test_id}'
    try:
        print(url)
        driver.get(url)
        print("Wait for Five seconds")
        time.sleep(5)
        element_id = driver.find_element_by_id(cell_id)
        if element_id is None:
            print(f"URL is Not valid : {base_url}{test_id}")
            continue
        else:
            elem_value = element_id.text
            data_value = elem_value.split("\n")[1]
            print(data_value)
            if data_value == 'No':
                driver.find_element_by_xpath("//a[contains(@class,'button-edit')]").click()
                driver.find_element_by_id('custom_automated').click()

                # Check for review field
                if check_exists_by_locator(driver, ('id', "custom_peerreview")):
                    driver.find_element_by_id('custom_peerreview').click()
                    driver.find_element_by_xpath("//*[@id='custom_peerreview']//option[@value='3']").click()
                else:
                    print("Review field is not visible")

                # Check for OS
                if check_exists_by_locator(driver, ('id', "custom_tested_os_select_chzn")):
                    os_entry = driver.find_elements_by_xpath("//*[@id='custom_tested_os_select_chzn']/ul/li")
                    if len(os_entry) > 1:
                        print("No Change needed for director")
                    else:
                        os_field = driver.find_element_by_id('custom_tested_os_select_chzn')
                        driver.execute_script("arguments[0].scrollIntoView();", os_field)
                        os_field.click()
                        driver.find_element_by_id('custom_tested_os_select_chzn_o_0').click()
                        os_field.click()
                        driver.find_element_by_id('custom_tested_os_select_chzn_o_1').click()
                else:
                    print("OS option is not visible")


                #Check for director
                if check_exists_by_locator(driver, ('id', "custom_testing_director_select_chzn")):
                    dire_entry = driver.find_elements_by_xpath("//div[@id='custom_testing_director_select_chzn']/ul/li")
                    if len(dire_entry) > 1:
                        print("No Change needed for OS field")
                    else:
                        dire_field = driver.find_element_by_id('custom_testing_director_select_chzn')
                        driver.execute_script("arguments[0].scrollIntoView();", dire_field)
                        dire_field.click()
                        driver.find_element_by_id('custom_testing_director_select_chzn_o_0').click()
                        dire_field.click()
                        driver.find_element_by_id('custom_testing_director_select_chzn_o_1').click()
                else:
                    print("Director option is not visible")

                save_button = driver.find_element_by_id('accept')
                driver.execute_script("arguments[0].scrollIntoView();", save_button)
                save_button.click()
                total_update_count += 1
                print("Update Count :", total_update_count )
                time.sleep(10)
    except Exception as e:
        print(f"Exception :{url}")
        continue

print("Total Test Count :", test_count)
driver.close()