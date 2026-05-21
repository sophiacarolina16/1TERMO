import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title("GERENCIAMENTO DE STATUS DE FUNCIONARIO SENAI")
janela.geometry("400x600") 
janela.configure(bg="#000000")

lbl_titulo = tk.Label(janela, text ="Area de Cadastro")
font = ("Arial", 20, "bold")
lbl_titulo.pack(pady=20)


lbl_nota1 = tk.Label(janela, text="Digite seu nome:")
lbl_nota1.pack(pady=20)
entry_nota1 = tk.Entry(janela)
entry_nota1.pack(pady=20)





janela.mainloop()
