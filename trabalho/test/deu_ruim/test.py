
import pyautogui
import time

time.sleep(2)

s = pyautogui.locateOnScreen('Dark.png', confidence=0.9)
print(s)