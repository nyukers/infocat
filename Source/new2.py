# Gather Bot option.
# This script grab current screenshot to file.
#
# Nyukers (C)opyright, 2021.
#
from mss import mss
import PIL.ImageGrab
import pyautogui

# v1
with mss() as sct:
    sct.shot()
	
# v2	
im = PIL.ImageGrab.grab()
save_path = 'C:\\Users\\User01\\Desktop\\Workshop\\Gather\\screenshot2.jpg'
im.save(save_path)
#im.show()

# v3
screen = pyautogui.screenshot("screenshot3.jpg")