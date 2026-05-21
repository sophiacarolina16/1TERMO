import tkinter as tk


janela = tk.Tk()
janela.title("GERENCIAMENTO DE STATUS DE FUNCIONARIO SENAI")
janela.geometry("400x600") 
janela.configure(bg="#FFFFFF")

lbl_titulo = tk.Label(janela, text ="Area de Cadastro")
font = ("Arial", 20, "bold")
lbl_titulo.pack(pady=20)


lbl_nome = tk.Label(janela, text="Digite seu nome:")
lbl_nome.pack(pady=20)
entry_nome = tk.Entry(janela)
entry_nome.pack(pady=20)

lbl_setor = tk.Label(janela, text="Digite seu setor:")
lbl_setor.pack(pady=20)
entry_setor = tk.Entry(janela)
entry_setor.pack(pady=20)
# if setor == "eletrica":
#     "ATENÇÂO: Uso obrigatorio de luvas de alta tensão e botas dielétricas!"
# elif setor == "trabalho em altura":
#     "ATENÇÂO: Uso obrigatorio de cinturão de segurança e talabarte!"


janela.mainloop()
