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


# while True:

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


# ________________________________começo da automação_____________________________________



    # clicar na empressora 
    time.sleep(1)
    pyautogui.click(x=1249, y=1063)

    # Adicionar pagina
    time.sleep(5)
    pyautogui.click(x=1458, y=103)

    # digitalizar
    time.sleep(5)
    pyautogui.click(x=998, y=572)

    # Salvar no PC
    time.sleep(15)
    pyautogui.click(x=1724, y=147)
    # colocar o nome do cliente
    time.sleep(2)
    pyautogui.click(x=926, y=412)

    #   campo do nome 
    pyautogui.keyDown('ctrl')   # segura Ctrl
    pyautogui.press('a')        # aperta 'a' enquanto segura Ctrl
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.write(f'{nam}(1)')


    # Salvar nome de cliente 
    time.sleep(2)
    pyautogui.click(x=1010, y=683)


# # ____________________________________________vasa sitema____________________________________________

#   entrando no sitema vagas
    time.sleep(2)
    pyautogui.click(x=1119, y=1063)



    # clicando na flecha para baixar na nuvem
    time.sleep(2)
    pyautogui.click(x=942, y=80)



    # baixando pelo icone de nuvem
    time.sleep(2)   
    pyautogui.click(x=892, y=97)



    # Pesquisando o nome do cliente
    time.sleep(3)
    pyautogui.write(f'{nam}(1)')
    time.sleep(2)
    pyautogui.press('enter')



    # Fechando janelas inutei de visulização 
    time.sleep(9)
    pyautogui.click(x=1891, y=88)
    time.sleep(1)
    pyautogui.click(x=1890, y=579)



    # Novo documento
    time.sleep(3)
    pyautogui.click(x=593, y=171)
    time.sleep(1)
    pyautogui.click(x=593, y=171)
    time.sleep(1)
    pyautogui.click(x=593, y=171)
    time.sleep(2)


    # Documento
    pyautogui.click(x=627, y=201)




#     # #-----------------------------




    # Colocando documento no sitema para lançamento 
    time.sleep(3)
    pyautogui.click(x=1141, y=390)
    time.sleep(0.5)
    pyautogui.click(x=1141, y=390)
    time.sleep(3)




    # pegando arquivo da nuvem
    pyautogui.click(x=1010, y=463)
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.8) 


    # clicando no nome 
    pyautogui.click(x=1021, y=425)
    time.sleep(0.8)


    # copiando e colando o nome do sujeito no lugar certo 
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.8)
    pyautogui.click(x=1019, y=410)
    time.sleep(0.8)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.8)





    # campo do ano 
    pyautogui.click(x=1007, y=539)

    time.sleep(0.8)
    pyautogui.write(ano)

    # empressora para apagar as coisas
    pyautogui.click(x=1249, y=1063)
    
    for i in range(vezes):
        time.sleep(0.8)
        pyautogui.click(x=53, y=183)
        time.sleep(0.5)
        pyautogui.click(x=53, y=183)  
        time.sleep(0.5)
        pyautogui.click(x=974, y=572) 

    #   voltando ao navegador
    time.sleep(0.8)
    pyautogui.click(x=1134, y=1052)


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
