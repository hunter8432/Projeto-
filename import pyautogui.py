import pyautogui
import time
import mouse
import keyboard

#  756 7514 chrome
pyautogui.press('win')
time.sleep(3)

pyautogui.write('https://mail.google.com/mail/u/0/?pli=1#starred/FMfcgzQbfLbQSQnQdljGpqWvrLXnBRXz')
time.sleep(1.5)

pyautogui.press('enter')

mouse.move(579, 598, absolute=True, duration=0.3)
time.sleep(3)
mouse.click('left')
time.sleep(6)
mouse.click('left')
time.sleep(6)


# 447 60/ 599 6136 barra de pesquisa
# escrever gmail.com
#3101 122 entrar estrela
# 500 3165 abrir arquivo
# entrar de vez 705 6681








