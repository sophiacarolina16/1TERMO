# Cria uma aplicação que faça o calculo de idade de pessoas.
# Deve perguntar o nome da pessoa e o ano de nascimento.


import tkinter as tk
from tkinter import ttk, messagebox

# DEF funcoes em bloco
def cadastrar_usuario():
    nome_usuario = ent_nome_usuario.get()
    idade_usuario = int(ent_idade_usuario.get())

    

    if nome_usuario == "" or idade_usuario =="":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos de cadastro!")
    else:

        lbl_nome_usuario.grid_forget()
        ent_nome_usuario.grid_forget()
        lbl_idade_usuario.grid_forget()
        ent_idade_usuario.grid_forget()
        btn_realizar_cadastro.grid_forget()
        
        ano_atual = 2026
        ano_nascimento = ano_atual - idade_usuario 
        
        texto_resumo = f" Cadastro Realizado com Sucesso!\n\n Nome: {nome_usuario}\n Ano de Nascimento: {ano_nascimento} "
        
        lbl_resultado = tk.Label(janela, text=texto_resumo, font=("Arial", 14), fg="#333333", bg="#FFFFFF", justify="left")

        lbl_resultado.grid(row=0, column=0, columnspan=2, pady=20, padx=20)
        

        lbl_imagem.grid(row=4, column=1, columnspan=0, pady=10)
        btn_fechar_janela.grid(row=5, column=1, columnspan=0, pady=20)
    


# 0 - Etapa Janela
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("550x450") 
janela.configure(bg="#FFFFFF")


# 1 - Etapa Componentes
# labels = Rotulos
lbl_nome_usuario = tk.Label(janela, text="Digite seu nome: ", font=("Arial", 14), fg="#000000", bg="#FFFFFF")
lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)

lbl_idade_usuario = tk.Label(janela, text="Digite sua idade: ", font=("Arial", 14), fg="#000000", bg="#FFFFFF")
lbl_idade_usuario.grid(row=1, column=0, pady=10, padx=10)

 # entrys = caixa de texto
ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_nome_usuario.grid(row=0, column=1, pady=10, padx=10)
ent_idade_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_idade_usuario.grid(row=1, column=1, pady=10, padx=10)

# Botões
btn_realizar_cadastro = tk.Button(janela, text="Cadastrar", font=("Arial", 14), fg="red", command=cadastrar_usuario)
btn_realizar_cadastro.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), command=janela.destroy)
btn_fechar_janela.grid(row=3, column=1, pady=10, padx=10)


# Imagem
lbl_imagem = tk.Label(janela, bg="#FFFFFF")
lbl_imagem.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

try:
    imagem_original = tk.PhotoImage(file="senai.png")
    imagem_diminuida = imagem_original.subsample(1, 1) 
    
    lbl_imagem.config(image=imagem_diminuida)
    lbl_imagem.image = imagem_diminuida  
except Exception:
    messagebox.showerror("Erro", "Arquivo 'senai.png' não encontrado!")
    

# 4 - Etapa Loop:
janela.mainloop()