import pyautogui

# through PIP we can take screen shot of VM.
from PIL import Image, ImageGrab



# pyguiauto module automates all the keyboard functionality

# while True:
#     pyautogui.keyDown('D')
#     pyautogui.keyDown('E')
#     pyautogui.keyDown('E')
#     pyautogui.keyDown('P')
#     pyautogui.keyDown('E')
#     pyautogui.keyDown('S')
#     pyautogui.keyDown('H')
#


# By default each image is array of pixel.
# Grey scale image means black and white and there value if fix
# white color : 255 and black : 0

def takescreenShot():
    # by default it show colored screenshot
    # image = ImageGrab.grab()

    # convert screen shot in black and white
    image = ImageGrab.grab().convert('L')
    image.show()
    return image


if __name__ == '__main__':
    takescreenShot()