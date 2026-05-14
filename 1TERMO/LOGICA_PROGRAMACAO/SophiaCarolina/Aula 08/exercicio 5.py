with open("notas.txt", "w") as arquivo:
    arquivo.write("log de atividades")


with open("notas.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)