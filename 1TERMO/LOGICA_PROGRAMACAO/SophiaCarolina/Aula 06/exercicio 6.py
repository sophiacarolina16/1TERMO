#  Percorra uma lista de medidas de peças:
# Medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

medidas = [50.1, 49.8, 52.0, 50.0, 48.5]

for pecas in medidas:
    print(pecas)
    if pecas >= 50.0:
        print("Aprovado") 

    elif pecas < 50.0:
        print("Reprovado")
    else:
        print("Encerrar")
