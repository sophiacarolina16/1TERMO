# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.


for i in range(5):
    consumo = float(input("Digite o consumo \n"))
    total = consumo + i
    print("o valor de consumo é ", total)


total = 0
for i in range(1,6):
    consumo = float(input(f"Digite o consumo da {i} maquina \n"))
    total+= consumo
    print(f"Consumo total da fabrica", total)