import pyautogui
import pyperclip
from time import sleep


email = pyautogui.prompt(text='email: ',)
senha = pyautogui.password(text='senha:',mask='*')
pyautogui.hotkey('win',duration=2)
sleep(1)
pyautogui.typewrite('bloco')
pyautogui.hotkey('enter',duration=0.5)
sleep(2)
pyperclip.copy(email)
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('enter')
pyperclip.copy(senha)
pyautogui.hotkey('ctrl','v')
