## Instabot Version 1.0 ##
import webbrowser
import time
import pyautogui

users = []

webbrowser.open('https://www.instagram.com/p/CBgt0TlhTxR/')
time.sleep(1.5)

pyautogui.scroll(-2)
time.sleep(2)
i = 0
while i<len(users)-1:
    time.sleep(2)
    if i>56:
        break
    pyautogui.click(x=829, y=641)
    pyautogui.write('@'+users[i])
    pyautogui.click(x=1097,y=649)
    print('@'+users[i])
    i += 1
    time.sleep(3)
