# this code is made and distributed by RedScorpion
# need help? contact me on discord  RedScorpion#5785
# for visual toturial, open this link on your browser
# https://www.youtube.com/watch?v=g7m6EBFWzKM
# for documentation, open this link on your browser
# https://github.com/capRS/wolves/

import pyautogui as gui
import win32api as win
import keyboard
import win32con
import numpy
import time

time.sleep(5)


# given x and y are the mouse coordinates, this sends a left click
def click(x, y):
    win.SetCursorPos((x, y))
    win.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# finds the watch video button, clicks if it is there
def find_button():
    coords = (mom, dad)
    for m in range(1000):
        if gui.pixel(coords[0], coords[1])[0] == 255:
            click(coords[0], coords[1])
            break
        else:
            coords = (coords[0], coords[1] - 5)


def rich_overnight():
    find_button()
    time.sleep(numpy.random.randint(40, 43))
    click(me, you) # clicks the back button
    time.sleep(numpy.random.randint(5, 7))
    find_button()
    time.sleep(numpy.random.randint(16, 17))


while True:
    rich_overnight()
