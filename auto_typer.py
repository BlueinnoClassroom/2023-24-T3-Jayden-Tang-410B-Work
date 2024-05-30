import pyautogui as curtis
import pytesseract
import time
from PIL import ImageGrab

curtis.displayMousePosition()

left = 840
right = 1320
top = 700
bottom = 780

FILE_NAME = 'words.png'

curtis.click(1000,450)
time.sleep(2)

screenshot = ImageGrab.grab(bbox=(left,top,right,bottom))
screenshot.save(FILE_NAME)

height = bottom - top
top += height
bottom += height

while(True):

    text = pytesseract.image_to_string(FILE_NAME, lang='eng')
    print(text)

    curtis.typewrite(text)
    curtis.typewrite(' ')

    screenshot = ImageGrab.grab(bbox=(left,top,right,bottom))
    screenshot.save(FILE_NAME)








