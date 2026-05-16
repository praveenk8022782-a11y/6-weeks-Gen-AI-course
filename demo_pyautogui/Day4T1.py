import pyautogui
import time
import os

time.sleep(3)

# Open Chrome
os.system("start chrome")

time.sleep(3)

# Search
pyautogui.write("Python tutorial")
pyautogui.press("enter")

time.sleep(3)

# Screenshot
pyautogui.screenshot("google_search.png")

print("Done")