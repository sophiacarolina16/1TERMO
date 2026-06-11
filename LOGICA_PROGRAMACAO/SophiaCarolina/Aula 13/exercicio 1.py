import tkinter as tk
from tkinter import ttk, messagebox

# DEF funcoes em bloco
def cadastrar_usuario():
    nome_usuario = ent_nome_usuario.get()
    curso_usuario = ent_curso_usuario.get()
    escola_usuario = combo_escola.get()
    

    if nome_usuario == "" or curso_usuario == "" or escola_usuario == "":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos de cadastro!")
    else:

        lbl_nome_usuario.grid_forget()
        ent_nome_usuario.grid_forget()
        lbl_curso_usuario.grid_forget()
        ent_curso_usuario.grid_forget()
        lbl_escola_usuario.grid_forget()
        combo_escola.grid_forget()
        btn_realizar_cadastro.grid_forget()
        

        texto_resumo = f" Cadastro Realizado com Sucesso!\n\n Nome: {nome_usuario}\n Curso: {curso_usuario}\n Escola: {escola_usuario}"
        
        lbl_resultado = tk.Label(janela, text=texto_resumo, font=("Arial", 14), fg="#333333", bg="#FFFFFF", justify="left")

        lbl_resultado.grid(row=0, column=0, columnspan=2, pady=20, padx=20)
        

        lbl_imagem.grid(row=1, column=1, columnspan=0, pady=10)
        btn_fechar_janela.grid(row=2, column=1, columnspan=0, pady=20)


# 0 - Etapa Janela
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("550x450") 
janela.configure(bg="#FFFFFF")


# 1 - Etapa Componentes
# labels = Rotulos
lbl_nome_usuario = tk.Label(janela, text="Digite seu nome: ", font=("Arial", 14), fg="#000000", bg="#FFFFFF")
lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)

lbl_curso_usuario = tk.Label(janela, text="Digite seu curso: ", font=("Arial", 14), fg="#000000", bg="#FFFFFF")
lbl_curso_usuario.grid(row=1, column=0, pady=10, padx=10)

lbl_escola_usuario = tk.Label(janela, text="Selecione sua escola: ", font=("Arial", 14), fg="#000000", bg="#FFFFFF")
lbl_escola_usuario.grid(row=2, column=0, pady=10, padx=10)

# entrys = caixa de texto
ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_nome_usuario.grid(row=0, column=1, pady=10, padx=10)

ent_curso_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_curso_usuario.grid(row=1, column=1, pady=10, padx=10)

# combobox = caixa de seleção
combo_escola = ttk.Combobox(janela, values=["SESI005", "SESI408"], state="readonly", font=("Arial", 14), width=23)
combo_escola.grid(row=2, column=1, pady=10, padx=10)


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