from statistics import quantiles
from threading import Thread
import time
import mouse
import pyautogui
import keyboard

first_MousePos = mouse.get_position()
second_MousePos = mouse.get_position()
shouldStop = False
 
def threaded_function():
    global shouldStop
    while True:
       if keyboard.read_key() == "x":
            shouldStop = True
            break

thread = Thread(target = threaded_function)
thread.start()

while not shouldStop:
    first_MousePos = mouse.get_position()
    time.sleep(1)
    second_MousePos = mouse.get_position()
    if second_MousePos == first_MousePos:
        mouse.click('left')
        pyautogui.press('q')
        pyautogui.keyUp('q')

print('programm stopped')