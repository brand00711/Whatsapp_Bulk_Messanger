import webbrowser as web
import time
import pyautogui as pg
import os
import pandas as pd
import socket
import datetime

loc_enter=None

def func(n,m,x):
    
    if x%30==0:
        web.open('https://web.whatsapp.com/send?phone=+'+n+'&text='+m)
        time.sleep(17)
        loc_enter = pg.locateOnScreen('C:/Users/joshu/OneDrive/Desktop/Projects/whatsapp_simple/enter_button.png', grayscale=True, confidence=.5)
        print("loc_enter = ",loc_enter)
        pg.press("enter")
        time.sleep(0.5)
    else:
        web.open('https://web.whatsapp.com/send?phone=+'+n+'&text='+m)
        time.sleep(9)
        loc_enter = pg.locateOnScreen('C:/Users/joshu/OneDrive/Desktop/Projects/whatsapp_simple/enter_button.png', grayscale=True, confidence=.5)
        print("loc_enter = ",loc_enter)
        if loc_enter is not None:
            pg.press("enter")
            time.sleep(0.5)

n = "91970447"
m ="hi"
x=1

func(n,m,x)