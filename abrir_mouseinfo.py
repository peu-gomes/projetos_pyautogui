import pyautogui
from time import sleep

pyautogui.hotkey('win')
pyautogui.typewrite('terminal')
pyautogui.hotkey('enter')
sleep(5)
pyautogui.typewrite('python')
pyautogui.hotkey('enter')
sleep(2)
pyautogui.typewrite('import mouseinfo')
pyautogui.hotkey('enter')
sleep(2)
pyautogui.typewrite('from mouseinfo import mouseInfo')
pyautogui.hotkey('enter')
sleep(2)
pyautogui.typewrite('mouseInfo()')
pyautogui.hotkey('enter')
