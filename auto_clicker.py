import pyautogui as curtis
from PIL import ImageGrab
# curtis.displayMousePosition()



left = 840
right = 1320
top = 700
bottom = 780


#upgrades
upgx = 1352

#top of scroll bar
x1 = 1427
y1 = 260

#bottom of scroll bar

x2 = 1427
y2 = 600

# curtis.moveTo(x1, y1)
# curtis.click()
# curtis.drag(x2-x1, y2-y1, duration=0.2, button='left')

FILE_NAME = 'perks.png'
while True:
    screenshot = ImageGrab.grab()
    screenshot.save(FILE_NAME)
    pixels = screenshot.load()
    for y in range(y1, y2):
        print(upgx, y)
        px = pixels[upgx, y]
        if (px[0] > 200) and(px[0] > 200) and(px[0] > 200):
            curtis.click()

    curtis.click()




