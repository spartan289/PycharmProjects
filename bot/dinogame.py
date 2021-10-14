import pyautogui
from PIL import Image, ImageGrab,ImageOps
import time
import numpy as np
def click(key):
    print("jump")
    pyautogui.keyDown(key)
    return
def imagegrab():

    box = (675,270,
           825,300)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())
    x = a.sum()
    print(x)
    return x
if __name__ == '__main__':
    time.sleep(3)
    click('up')
    while True:

        if imagegrab()!=4755 and imagegrab()!=10132:
            click('up')
            print("jump")
