import webbrowser
import pyautogui
from time import sleep

webbrowser.open('https://pt.wikipedia.org/wiki/Brasil')
pyautogui.moveTo(673,147,duration=2)
pyautogui.scroll(-3250)