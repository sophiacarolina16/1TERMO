# uma balanca industrial esta pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistemas aceita variações

medidas = [50, 49, 52, 48, 54]

for pecas in medidas:
    print("O peso deu", pecas)
    if pecas == 50.0:
        print("Aprovado atingiu o peso ideal") 
    elif pecas < 50.0:
        print("Esta abaixo do peso ideal")
        BA = 50 - pecas
        print("para atingir o peso ideal deve aumentar", BA)
    elif pecas > 50.0:
        print("Esta acima do peso ideal")
        AB = pecas - 50
        print("para atingir o peso ideal deve diminuir", AB)
        