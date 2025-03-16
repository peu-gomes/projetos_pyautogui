import pyautogui
from time import sleep

pyautogui.hotkey('win')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('delete')
pyautogui.typewrite('edge')
pyautogui.hotkey('enter')
sleep(3)
pyautogui.hotkey('win','drow')
#pyautogui.moveTo(1296,17)
#pyautogui.click()