import pyautogui as curtis
from PIL import ImageGrab
import numpy as np
# curtis.displayMousePosition()



left = 950
top = 400
right = 1215
bottom = 530

zone_img = ImageGrab.grab(bbox=(left,top,right,bottom))
zone_img.save('zone_img.png')


keys = ['s', 'd', 'f', 'space', 'j', 'k', 'l']  
division_width = (right - left) // len(keys)    

rest_divs = []                                  
for i in range(len(keys)):                      
    start_x = i * division_width                
    end_x = (i + 1) * division_width            

    div = zone_img.crop((start_x, 0 ,end_x, zone_img.height))                       
    div.save(f'div_{i}.png')  

    img_gray = div.convert('L')
    div = np.array(img_gray)
    rest_divs.append(div)


curtis.PAUSE = 0
print('you may start the game now!')
while True:
    latest_img = ImageGrab.grab(bbox=(left, top, right, bottom))
    # latest_img.save('latest_img.png')

    # Copy from codeshare.io/444666
    active_divs = []
    for i in range(len(keys)):
        start_x = i * division_width
        end_x = (i + 1) * division_width

        div = latest_img.crop((start_x, 0, end_x, zone_img.height))
        img_gray = div.convert('L')
        div = np.array(img_gray)
        active_divs.append(div)

    for i in range(len(keys)):                              
        img1 = rest_divs[i]                                 
        img2 = active_divs[i]                               

        diff = img1.astype('float') - img2.astype('float')  
        diff = np.sum(diff ** 2)                            
        diff /= float(img1.shape[0] * img2.shape[1])    

        if (diff >1500):
            curtis.keyDown(keys[i])
        else:
            curtis.keyUp(keys[i])

    #     print(f'{int(diff):<5}', end=' | ')                 
    # print()                                                 





