import tkinter as tk
from tkinter import messagebox

def calcular_media():
    try:
        nota1=float(entry_nota1.get())
        nota2=float(entry_nota2.get())
        nota3=float(entry_nota3.get())

        media=(nota1+nota2+nota3)/3

        messagebox.showinfo(f"A media das notas é: {media}")
        
    except ValueError:
        messagebox.showerror(
            "insira apenas números validos."
        )

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x500")

lbl_nota1 = tk.Label(janela, text="Digite 1 valor:")
lbl_nota1.pack(pady=20)
entry_nota1 = tk.Entry(janela)
entry_nota1.pack(pady=20)
lbl_nota2 = tk.Label(janela, text="Digite 2 valor:")
lbl_nota2.pack(pady=20)
entry_nota2 = tk.Entry(janela)
entry_nota2.pack(pady=20)
lbl_nota3 = tk.Label(janela, text="Digite 3 valor:")
lbl_nota3.pack(pady=20)
entry_nota3 = tk.Entry(janela)
entry_nota3.pack(pady=20)

btn_calcular = tk.Button(
    janela, text="Calcular Media", command=calcular_media, bg="red", fg="black"
)
btn_calcular.pack(pady=30)

janela.mainloop()
