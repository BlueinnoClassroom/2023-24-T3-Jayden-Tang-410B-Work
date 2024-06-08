import pyautogui as curtis
from PIL import ImageGrab
import multiprocessing
import multiprocessing.process


# curtis.displayMousePosition()
curtis.Pause = 0.01


UPGRADE_AREA_TOP = 290
UPGRADE_AREA_BOTTOM = 570
SCROLL_BAR_X = 1430

def click_capybara_task():
    cap_x = 999
    cap_y = 444

    try:
        while True:
            curtis.click(cap_x, cap_y)
    except curtis.FailSafeException:
        print('Fail safe triggered, exiting click capy task')
        return

def click_upgrade_buttons_tasks():
    scroll_segment = 0
    max_scroll_segments = 4

    try:
        btn_x = SCROLL_BAR_X - 50
        while True:

            offset = scroll_segment * ((UPGRADE_AREA_BOTTOM - UPGRADE_AREA_TOP) / max_scroll_segments)
            curtis.mouseDown(SCROLL_BAR_X, UPGRADE_AREA_TOP + offset)
            
            screenshot = ImageGrab.grab()
            pixels = screenshot.load()

            for y in range(UPGRADE_AREA_BOTTOM, UPGRADE_AREA_TOP, -1):
                px = pixels[btn_x * 2, y * 2]
                r = px[0]
                g = px[1]
                b = px[2]
                if (r > 230) and (g > 230) and (b > 230):
                    curtis.click(btn_x, y)
            
            scroll_segment += 1
            if (scroll_segment > max_scroll_segments):
                scroll_segment = 0
            

    except curtis.FailSafeException:
        print('Fail safe triggered, exiting click_upgrade_buttons_tasks')
        return


def main():
    cappy_process = multiprocessing.Process(target=click_capybara_task)
    upg_process = multiprocessing.Process(target=click_upgrade_buttons_tasks)

    procesess = [
        cappy_process,
        upg_process,
    ]

    for p in procesess:
        p.start()

    try:
        for p in procesess:
            p.join()
    except KeyboardInterrupt:
        for p in procesess:
            p.terminate()

if __name__ == '__main__':
    main()