import pyautogui
from time import sleep

for i in range(9):
#ir para um arquivo com base em uma coordenada
    pyautogui.moveTo(911,155,duration=1)
#apertar, puxar e soltar para outra coordenada

    pyautogui.drag(0,359,duration=1.5)


#repetir 9x