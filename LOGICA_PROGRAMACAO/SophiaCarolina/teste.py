import tkinter as tk
from tkinter import ttk, messagebox

def verificar():
    nome = entrada_nome.get()
    setor = combo_setor.get()
    nr10 = combo_nr10.get()
    nr35 = combo_nr35.get()

    try:
        ano_brigada = int(entrada_brigada.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um ano válido.")
        return

    resultado = f"Funcionário: {nome}\n"
    resultado += f"Setor: {setor}\n\n"

    if setor == "Eletrica":
        resultado += "ATENÇÃO: Uso obrigatório de luvas de alta tensão e botas dielétricas!\n"

    elif setor == "Trabalho em Altura":
        resultado += "ATENÇÃO: Uso obrigatório de cinturão de segurança e talabarte!\n"

    resultado += f"NR-10: {'Concluído' if nr10 == 'S' else 'Não concluído'}\n"
    resultado += f"NR-35: {'Concluído' if nr35 == 'S' else 'Não concluído'}\n"

    ano_atual = 2026
    diferenca = ano_atual - ano_brigada

    if diferenca > 2:
        resultado += "\nTreinamento vencido! Encaminhar para reciclagem."
    else:
        resultado += "\nTreinamento válido."

    label_resultado.config(text=resultado)

# Janela
janela = tk.Tk()
janela.title("Gerenciamento de Status SENAI")
janela.geometry("500x450")

# Nome
tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

# Setor
tk.Label(janela, text="Setor").pack()
combo_setor = ttk.Combobox(
    janela,
    values=["Eletrica", "Trabalho em Altura"],
    state="readonly"
)
combo_setor.pack()

# NR10
tk.Label(janela, text="NR-10").pack()
combo_nr10 = ttk.Combobox(
    janela,
    values=["S", "N"],
    state="readonly"
)
combo_nr10.pack()

# NR35
tk.Label(janela, text="NR-35").pack()
combo_nr35 = ttk.Combobox(
    janela,
    values=["S", "N"],
    state="readonly"
)
combo_nr35.pack()

# Brigada
tk.Label(janela, text="Último ano da Brigada").pack()
entrada_brigada = tk.Entry(janela)
entrada_brigada.pack()

# Botão
tk.Button(
    janela,
    text="Verificar Status",
    command=verificar
).pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

janela.mainloop()