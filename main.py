import time
import mouse
import pyautogui

first_MousePos = mouse.get_position()
second_MousePos = mouse.get_position()
while True:
    first_MousePos = mouse.get_position()
    time.sleep(1)
    second_MousePos = mouse.get_position()
    if second_MousePos == first_MousePos:
        mouse.click('right')
        pyautogui.press('Tab')

