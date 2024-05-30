import pyautogui as gui
from PIL import ImageGrab
# gui.displayMousePosition()
gui.PAUSE = 0 

x1 = 888 *2
x2 = 999*2
x3 = 1111*2
x4 = 1234*2
y = 555*2


while True:
    screenshot = ImageGrab.grab()
    pixels = screenshot.load()
    
    p1 = pixels[x1, y]
    p2 = pixels[x2, y]
    p3 = pixels[x3, y]
    p4 = pixels[x4, y]
    
    # px[0] --> R
    # px[1] --> G
    # px[2] --> B
    if (p1[1] > 200):
        gui.press('h')
    if (p2[1] > 200):
        gui.press('j')
    if (p3[1] > 200):
        gui.press('k')
    if (p4[1] > 200):
        gui.press('l')