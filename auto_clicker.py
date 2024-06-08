import pyautogui as curtis
from PIL import ImageGrab
import multiprocessing
import multiprocessing.process


# curtis.displayMousePosition()
curtis.Pause = 0.01

while True:
    curtis.click()
# curtis.PAUSE = 1

# def click_capybara_task():
#     cap_x = 999
#     cap_y = 444

#     try:
#         while True:
#             curtis.click(cap_x, cap_y)
#     except curtis.FailSafeException:
#         print('Fail safe triggered, exiting click capy task')
#         return

# def click_upgrade_buttons_tasks():
#     left = 840
#     right = 1320
#     top = 700
#     bottom = 780

#     #upgrades
#     upgx = 1266

#     #top of scroll bar
#     x1 = 1427
#     y1 = 260

#     #bottom of scroll bar
#     x2 = 1427
#     y2 = 600


#     try:
#         scroll_x = 1430
#         btn_x = 1381
#         while True:
#             curtis.click(scroll_x,  333)
#             curtis.click(btn_x,  321)
#             curtis.click(btn_x,  386)
#             curtis.click(btn_x,  448)
#             curtis.click(btn_x,  506)

#             curtis.click(scroll_x,  373)
#             curtis.click(btn_x,  321)
#             curtis.click(btn_x,  386)
#             curtis.click(btn_x,  448)
#             curtis.click(btn_x,  506)

#             curtis.click(scroll_x,  457)
#             curtis.click(btn_x,  321)
#             curtis.click(btn_x,  386)
#             curtis.click(btn_x,  448)
#             curtis.click(btn_x,  506)

#             curtis.click(scroll_x,  393)


#             curtis.click(scroll_x,  454)


#             curtis.click(scroll_x,  525)


#     except curtis.FailSafeException:
#         print('Fail safe triggered, exiting click capy task')
#         return


# def main():
#     cappy_process = multiprocessing.Process(target=click_capybara_task)
#     upg_process = multiprocessing.Process(target=click_upgrade_buttons_tasks)

#     procesess = [
#         cappy_process,
#         upg_process,
#     ]

#     for p in procesess:
#         p.start()

#     try:
#         for p in procesess:
#             p.join()
#     except KeyboardInterrupt:
#         for p in procesess:
#             p.terminate()

# if __name__ == '__main__':
#     main()