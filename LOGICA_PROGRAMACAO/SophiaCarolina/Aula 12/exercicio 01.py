# TKINTER

# Componentes Widgets

# TK = TK() Janela
# LB = label() Rotulo
# BT = Button() Botão
# ET = Entry() Caixa de Texto

import tkinter as tk
from tkinter import messagebox


# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela GUI")
janela.geometry("400x200") #Largura e Altura

# 2. Criar a função do botão(evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Voce clicou no botão")

# 3. Criar os componentes
lbl_titulo = tk.Label(janela, text ="Bem vindo a nossa aula de Tkinter")
font = ("Arial", 14, "bold")
btn_clique = tk.Button(janela, text= "Clique Aqui", font= ("Arial", 11 ), bg = "#00FF73", fg ="white", command=mostrar_mensagem) 
btn_close = tk.Button(janela, text = "Fechar", font = ("Arial",14,"bold"), bg="#cce2ee" , command=janela.destroy)


# 4. Posicionar componentes

lbl_titulo.pack(pady=20) # 'pady' adciona um espaçamento vertical
btn_clique.pack(pady=10)
btn_close.pack(pady=5)

# 5. Rodar o Loop da interface
janela.mainloop()



