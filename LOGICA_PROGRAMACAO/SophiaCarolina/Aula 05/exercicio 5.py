opcao = ""

while opcao !="sair" and "SAIR":
    opcao = input("digite a leitura do sensor ou 'sair' para fechar:").upper().lower()
    if opcao != "sair" and "SAIR":
        print(f"Dado '{opcao}' registrado no banco de dados")
print("Sistema encerrado.")


