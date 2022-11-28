import pyautogui
import time
import pyperclip as pc

time.sleep(3)
local = pyautogui.position()
pyautogui.moveTo(local)

def baixando():   # baixando ebook 
    #pyautogui.PAUSE = 0.5
    pyautogui.moveTo(local)
    pyautogui.click(button='right')
    pyautogui.hotkey('s')
    time.sleep(0.8)
    pyautogui.hotkey('alt','l')
    time.sleep(0.8)
    pyautogui.click()
    for i in range(3):
        pyautogui.hotkey('pgdn')
    for i in range (5):
        pyautogui.hotkey('up')


for i in range(215):
    baixando()
print('Baixou mah!')
