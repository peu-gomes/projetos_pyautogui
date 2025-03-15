import pyautogui
import pyperclip

#abrir o whatsapp apertando no icone na barra de tarefas
pyautogui.moveTo(650,741,duration=2)
pyautogui.click(duration=0.5)

#repetir 
for i in range(4):

    #mover para o campo de digitar
    pyautogui.moveTo(612,694,duration=0.5)
    pyautogui.click(duration=0.5)

    #escrever
    pyperclip.copy('olá')
    pyautogui.hotkey('ctrl','v')

    #apertar pra enviar
    pyautogui.move(730,0,duration=0.5)
    pyautogui.click(duration=0.5)