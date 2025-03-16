import pyautogui
from time import sleep
import pyperclip

pyautogui.hotkey('win')
sleep(1)
pyautogui.hotkey('ctrl','a')
sleep(1)
pyautogui.hotkey('delete')
pyautogui.typewrite('bloco')
pyautogui.hotkey('enter')
sleep(1)
pyperclip.copy('Automação é incrível!')
pyautogui.hotkey('ctrl','v')

pyautogui.hotkey('ctrl','a')
sleep(1)
pyautogui.hotkey('del')

print(pyautogui.KEYBOARD_KEYS)