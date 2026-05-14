with open("desliga.bat", "w") as desliga:
    desliga.write("shutdown -s -t 3600 -c\"Desligamento programado para daqui a 1 hora. Salve seu trabalho!\"")

    # -s comando pra desligar
    # -t tempo definir
    # -a cancelar desligamneto

with open ("desliga.bat", "r") as desliga:
    conteudo = desliga.read()
    print(conteudo)
