## Instabot Version 1.0 ##
import webbrowser
import time
import pyautogui

webbrowser.open('https://www.instagram.com/p/CBf_OshBEzk/?hl=pt-br')
time.sleep(1.5)

pyautogui.scroll(-2)
time.sleep(1.5)


pyautogui.moveTo(829,641)
pyautogui.click()
pyautogui.write('@nicabral_')
time.sleep(0.5)
pyautogui.moveTo(1097,649)
pyautogui.click()


