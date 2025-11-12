import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

import keyboard

# ...existing code...

if keyboard.is_pressed('esc'):  # ou qualquer tecla, como 'q'
    exit()
    print("Parando o script!")
    exit()


# # while True:

#_______________________________

def executar():
    nam = entry_nome.get()
    ano = entry_ano.get()
    vezes = int(entry_vezes.get())

    if not nam or not ano:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return


# nam=input("digite o nome do arquivo: ")
# ano=input("digite o ano do arquivo: ")


    # time.sleep(3)
    # x=pyautogui.position()
    # print(x)


    time.sleep(1)
    pyautogui.click(x=904, y=753)


    time.sleep(5)

    # impresora 
    pyautogui.click(x=941, y=93)

    # digitalizar
    time.sleep(1)
    pyautogui.click(x=941, y=93)

    time.sleep(5)
    pyautogui.click(x=729, y=419)

    time.sleep(11)
    pyautogui.click(x=1127, y=138)

    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.write(f'{nam}(1)')

    # ________________________________

    time.sleep(2)
    pyautogui.click(x=710, y=529)



    time.sleep(2)
    pyautogui.click(x=773, y=747)

    time.sleep(2)
    pyautogui.click(x=678, y=81)
    time.sleep(2)   
    pyautogui.click(x=618, y=95)


    time.sleep(3)
    pyautogui.write(f'{nam}(1)')
    time.sleep(2)
    pyautogui.press('enter')






    time.sleep(9)
    pyautogui.click(x=1334, y=92)
    time.sleep(1)
    pyautogui.click(x=1330, y=415)







    time.sleep(3)
    pyautogui.click(x=408, y=171)
    time.sleep(1)
    pyautogui.click(x=408, y=171)
    time.sleep(1)
    pyautogui.click(x=408, y=171)
    time.sleep(2)


    pyautogui.click(x=402, y=193)



    time.sleep(3)
    pyautogui.click(x=845, y=246)
    time.sleep(0.5)
    pyautogui.click(x=845, y=246)
    time.sleep(3)



    # #-----------------------------


    pyautogui.click(x=726, y=311)
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.8) 


    pyautogui.click(x=745, y=279)
    time.sleep(0.8)



    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.8)
    pyautogui.click(x=679, y=262)
    time.sleep(0.8)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.8)






    pyautogui.click(x=722, y=389)

    time.sleep(0.8)
    pyautogui.write(ano)


    pyautogui.click(x=904, y=753)
    
    for i in range(vezes):
        time.sleep(0.8)
        pyautogui.click(x=54, y=181)
        time.sleep(0.5)
        pyautogui.click(x=54, y=181)  
        time.sleep(0.5)
        pyautogui.click(x=690, y=413) 

    time.sleep(0.8)
    pyautogui.click(x=776, y=745)


    # time.sleep(0.5)
    # pyautogui.click(x=595, y=623)


    # --------- Interface Tkinter ----------


root = tk.Tk()
root.title("Automação PyAutoGUI")

# Nome
tk.Label(root, text="Nome do Arquivo:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

# Ano
tk.Label(root, text="Ano do Arquivo:").grid(row=1, column=0, padx=10, pady=5)
entry_ano = tk.Entry(root)
entry_ano.grid(row=1, column=1, padx=10, pady=5)

# Quantidade de repetições
tk.Label(root, text="Quantas vezes repetir:").grid(row=2, column=0, padx=10, pady=5)
entry_vezes = tk.Entry(root)
entry_vezes.grid(row=2, column=1, padx=10, pady=5)

# Botão
btn_executar = tk.Button(root, text="Executar Automação", command=executar, bg="green", fg="white")
btn_executar.grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()
