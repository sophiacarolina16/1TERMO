import tkinter as tk
from tkinter import messagebox

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela GUI")
janela.geometry("600x800") # Aumentei a altura para caber a imagem

# 2. Criar a função do botão (evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão")
   
    # Carrega a imagem (substitua pelo caminho do seu arquivo .png ou .gif)
    # Importante: mantenha uma referência da imagem usando 'lbl_imagem.image' para evitar que o Python a apague da memória
    try:
        imagem = tk.PhotoImage(file="imagem.png")
        lbl_imagem.config(image=imagem)
        lbl_imagem.image = imagem
    except Exception:
        messagebox.showerror("Erro", "Arquivo de imagem não encontrado!")

# 3. Criar os componentes
lbl_titulo = tk.Label(janela, text="Bem vindo a nossa aula de Tkinter", font=("Arial", 14, "bold"))
btn_clique = tk.Button(janela, text="67", font=("Arial", 14), bg="#00FF73", fg="black", command=mostrar_mensagem)

# Criamos um label vazio que vai receber a imagem depois do clique
lbl_imagem = tk.Label(janela)

# 4. Posicionar componentes
lbl_titulo.pack(pady=50)
btn_clique.pack(pady=30)
lbl_imagem.pack(pady=20) # Posiciona o local da imagem

# 5. Rodar o Loop da interface
janela.mainloop()