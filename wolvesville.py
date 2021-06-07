# need help? contact me on discord  RedScorpion#5785
# for visual toturial, this script is explained on youtube, open this link
# https://www.youtube.com/watch?v=QEoIjWfHf2c
# full documentation on how to use this script is on git hub, open this link
# https://github.com/RedScorpX/WolvesVilleAutoAds/
# follow the code, where it says changes are required, change them accordingly

import pyautogui as gui
import win32api as win
import win32con
import keyboard
import time
import numpy

time.sleep(5)


def click(x, y):
    win.SetCursorPos((x, y))
    win.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# changes required
def find_button():
    coords = (1718, 651)
    for m in range(1000):
        if gui.pixel(coords[0], coords[1])[0] == 255:
            click(coords[0], coords[1])
            break
        else:
            coords = (coords[0], coords[1] - 5)
            gui.moveTo(coords[0], coords[1])


# changes required
def rich_overnight():
    find_button()
    time.sleep(numpy.random.randint(40, 43))
    click(1898, 533)
    time.sleep(numpy.random.randint(5, 7))
    find_button()
    time.sleep(numpy.random.randint(16, 17))


while not keyboard.is_pressed("q"):
    rich_overnight()
