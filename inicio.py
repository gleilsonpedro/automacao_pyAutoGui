import pyautogui
import time
import pyperclip as pc

time.sleep(3)
local = pyautogui.position()
pyautogui.moveTo(local)

def baixando():   # baixando ebook 
    #pyautogui.PAUSE = 0.5
    pyautogui.moveTo(local) # move o mouse para as cordenadas encontradas x e y
    pyautogui.click(button='right')# clica com o botão direito do mouse
    pyautogui.hotkey('s') # salva
    time.sleep(0.8) # dependendo da velocidade do seu computador aumente esse tempo
    pyautogui.hotkey('alt','l') # na janela que abrir ele salva
    time.sleep(0.8)
    pyautogui.click() # clica novamente na página
    for i in range(3): #apertando 3 pagedown
        pyautogui.hotkey('pgdn')
    for i in range (5): # apertando 5 setas pra cima
        pyautogui.hotkey('up')


for i in range(x):# onde tem o x execute a quantidade de paginas do projeto
    baixando()
print('Baixou mah!')
