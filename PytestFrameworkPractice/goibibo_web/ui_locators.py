HOTEL_ICON_XPATH = "//a[@href='/hotels/']//span[@class='iconText ' and text()='Hotels'] "
SEARCH_HOTEL_INPUT_BOX_ID = "downshift-1-input"
DROP_DOWN_MENU_ID = "downshift-1-menu"
SEARCH_PLACE_XPATH = F"//ul[@id='{DROP_DOWN_MENU_ID}']//li//span"

CHECK_IN_DATE_XAPTH = "(//div[text()='Check-in']//following::div)[1]"
CHECK_OUT_XPATH = "(//div[text()='Check-out']//following::div)[1]"
GUESTS_ROOMS_XPATH = "(//*[text()='Guests & Rooms']//following::div)[1]"
ADD_ROOM_XPATH = "(//*[text()='Guests & Rooms']//following::span[text()='+'])[1]"
ADD_ADULTS_XPATH = "(//*[text()='Guests & Rooms']//following::span[text()='+'])[2]"
ADD_CHILD_XPATH = "(//*[text()='Guests & Rooms']//following::span[text()='+'])[2]"
ADD_ROOMS_GUEST_DONE_BUTTON_XPATH = "(//span[text()='Guests & Rooms']//following::button)[1]"
SEARCH_HOTEL_BUTTON = "//button[text()='Search Hotels']"

############################  ALERTS ELEMENTS #####################

DISPLAY_ALERT_ID = 'alert'
DISPLAY_CONFIRM_BOX_ID = 'confirm'
DISPLAY_PROMPT_BOX_ID = 'prompt'
MESSAGE_LOCATOR_ID = 'msg'