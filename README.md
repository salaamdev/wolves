**FOR THOSE OF YOU WHO CAN NOT WRITE THIS CODE, HERE IS A COMPLETE INSTRUCTIONS FOR YOU**

This [**bot**](https://github.com/RedScorpX/WolvesVilleAutoAds) is brought to you by [**RedScorpion**](https://www.youtube.com/channel/UCldtxjrCMtRHJzCUuA8b3kw), check this [**Video**](https://www.youtube.com/watch?v=QEoIjWfHf2c) to see a visual tutorials contact me on discord RedScorpion#5785

Before using this code, go to [python official website ](https://www.python.org/) and download [python 3.7](https://www.python.org/downloads/release/python-370/).
when installing python, remember to click add [python to PATH](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png).

1. **open up comand prompt as an administrator, then type the following commands one by one.**
* `pip install pyautogui`
* `pip install numpy`
* `pip install keyboard`
* `pip install pywin32`

*if you get an error, re install [python 3.7](https://www.python.org/downloads/release/python-370/) and make sure to check the ["ADD PYTHON TO PATH"](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png).*

2. **You will need an emulator.**
* PC users, download an emulator and install wolvesville from playstore. I recommand [**Bluestacks 5**](https://www.bluestacks.com/).
* MAC users, download an emulator and install wolvesville from playstore. i recommand [**Bluestacks for MAC**](https://www.bluestacks.com/download.html)

3. **Download this zip file https://github.com/caprs/wv/archive/refs/heads/main.zip**
* head over to the file with the name werewolves
* right click on it and choose open with IDLE or PYCHARM
* edit where necessary

**Copy Paste This Script**
* open IDLE, click file - new file - save - save file as wolvesville, then copy this code and paste there
* note you need to change **2** things in this code
```python
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


#changes required
def find_button(): 
    coords = (xcoords, ycoords) # replace the xcoords and y coords to your emulator's bottom pixel seperated by a comma, check the video above 
    for m in range(0, 1079):
        if gui.pixel(coords[0], coords[1])[0] == 255:
            click(coords[0], coords[1])
            break
        else:
            coords = (coords[0], coords[1] - 5)


#changes required
def rich_overnight():            
    find_button()
    time.sleep(numpy.random.randint(7, 8))     
    click(xcoords, ycoords) # replace the xcoords and y coords to your emulator's back button seperated by a comma, check the video above 
    time.sleep(numpy.random.randint(4, 6))  
    find_button()
    time.sleep(numpy.random.randint(16, 17))   



while keyboard.is_pressed('q') == False:
    rich_overnight()
```
