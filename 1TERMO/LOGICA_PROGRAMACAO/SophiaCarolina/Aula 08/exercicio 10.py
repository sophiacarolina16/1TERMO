with open("notas.txt", "w") as f:
    f.write("15\n")
    f.write("60\n")
    f.write("90\n")



with open("notas.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

if conteudo > 70:
    print("Alerta!")
elif conteudo < 70:
    print("Normal")