import pyautogui
from time import sleep
import pyperclip

pyautogui.hotkey('win')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('del')
pyautogui.typewrite('bloco')
pyautogui.hotkey('enter')
sleep(1)
pyperclip.copy('Automação é incrível!')
pyautogui.hotkey('ctrl','v')
