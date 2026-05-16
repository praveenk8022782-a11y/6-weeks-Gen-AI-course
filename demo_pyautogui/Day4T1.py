import pyautogui
import time
import os

time.sleep(3)

# Open Chrome
os.system("start chrome")

time.sleep(3)

# Search
pyautogui.write("Python basics")
pyautogui.press("enter")


print("Done")