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
        
    print('programm stopped')

def threaded_function_2():
    global first_MousePos
    global second_MousePos
    while not shouldStop:
        first_MousePos = mouse.get_position()
        time.sleep(0.75)
        second_MousePos = mouse.get_position()
        if second_MousePos == first_MousePos:
            mouse.click('left')
            pyautogui.press('Tab')
            pyautogui.keyUp('Tab')
        

thread = Thread(target = threaded_function)
thread.start()
thread2 =Thread(target = threaded_function_2)
thread2.start()             