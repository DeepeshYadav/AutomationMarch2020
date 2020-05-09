import pyautogui
from PIL import Image, ImageGrab
import time
from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    print("we are in collide function")
    for i in range(240, 300):
        for j in range(450, 500):
            if data[i, j] < 100:
                hit('up')
            return  True

    # Draw rectangle to handle handle bird
    for i in range(240, 300):
        for j in range(300, 450):
            if data[i, j] < 100:
                hit('down')
                return True
    return False


if __name__ == '__main__':
    print("Dino Game About to Start in 3 Seconds....")
    time.sleep(1)
    hit('up')

    while True:
        print("I am in loop")
        image = ImageGrab.grab().convert('L')
        data = image.load() # It will load image in form of array
        isCollide(data)
        #hit('up')
        #print(asarray(image)) # asarray is use to show data in tabular format
        # Draw rectangle to handle cactus
        # for i in range(240, 300):
        #     for j in range(450, 500):
        #         data[i, j] = 0
        #
        # # Draw rectangle to handle handle bird
        # for i in range(240, 300):
        #     for j in range(300, 450):
        #         data[i, j] = 71
        #
        # image.show()
        # break

    #image.show()
