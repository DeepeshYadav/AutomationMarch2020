from selenium import webdriver
from time import sleep



driver = webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
URL = "https://www.facebook.com/"

def element_is_visible(locator, element):
    try:
        if locator == 'xpath':
            driver.find_elements_by_xpath(element)
        elif locator == 'id':
            driver.find_elements_by_id(element)
        elif locator == 'name':
            driver.find_elements_by_name(element)
        elif locator == 'css':
            driver.find_elements_by_css_selector(element)
        return True
    except Exception as e:
        return False

def login_facebook():
    driver.get(URL)
    driver.find_element_by_id('email').send_keys('8668272878')
    driver.find_element_by_id('pass').send_keys('165323277deep')
    driver.find_element_by_xpath('//input[@value="Log In"]').submit()
    sleep(20)



def go_to_profile_get_group_list():
    driver.get(f'{URL}sqa.tools/groups')
    target_elem = "//div[@id='pagelet_timeline_medley_groups']//ul//div[@class='mtm']//a[text()='Software Testing JAVA & SQL']"
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(1)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    sleep(10)
    href_links = []
    elements = driver.find_elements_by_xpath("//div[@id='pagelet_timeline_medley_groups']//ul//div[@class='mtm']//a")

    for elem in elements:
        value = elem.get_attribute('href')
        if value not in href_links:
            href_links.append(value)
        sleep(2)

    print(len(href_links))

#####################################################
    post_msg = """Hello Folks,
Let's upgrade your self with free online software testing courses.Please Like, Share and Subscribe the channel and motivate us for  creating a more useful training video for all of you.

https://www.youtube.com/watch?v=z49LHy0dKIY&t=294s
    """
    for url in href_links:
        try:
            print(url)
            driver.get(url)
            if element_is_visible('name', 'xhpc_message_text'):
                driver.find_element_by_name('xhpc_message_text').click()
                sleep(2)
                driver.find_element_by_xpath('//div[@role="presentation"]//div[@role="combobox"]').send_keys(post_msg)
                driver.find_element_by_xpath('//*[@type="submit"]//span[text()="Post"]').click()
                continue
            elif element_is_visible('xpath', "//span[text()='Start Discussion']"):
                driver.find_element_by_xpath("//span[text()='Start Discussion']").click()
                sleep(2)
                driver.find_element_by_xpath('//div[@role="presentation"]//div[@role="combobox"]').send_keys(post_msg)
                driver.find_element_by_xpath('//*[@type="submit"]//span[text()="Post"]').click()
                continue
            else:
                continue
        except Exception as e:
            pass


login_facebook()
go_to_profile_get_group_list()
