
import tkinter as tk
from tkinter import messagebox

def saudar_usuario():
    nome = campo_nome.get()
    
    if nome == "":
        messagebox.showwaring("Aviso","Por favor, digite seu nome!")
    else:
        messagebox.showinfo("Saudações Alunos" , f"ola, {nome} bem vindo ao mundo das interfaces graficas")
        
# Configurações da janela

app = tk.Tk()
app.title("exemplo 1")
app.geometry("350x200")

# componentes
lbl_instrucao = tk.Label(app, text= "Digite seu nome abaixo:")
lbl_instrucao.pack(pady=10)

campo_nome = tk.Entry(app, font= ("Arial", 12))
campo_nome.pack(pady=5)

btn_enviar = tk.Button(app, text="Enviar",command=saudar_usuario)
btn_enviar.pack(pady=15)

app.mainloop()

