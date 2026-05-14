# calcular gorjetas receba o valor da conta de um restaurantes e retorne o valor da gorjeta(considerando o valor da conta)
x1= float(input("Digite o valor da conta no restaurante: \n"))
print(" A gorjeta é de 10%")
total = x1 / 10
print("o total da gorjeta é ", round(total,2))
total2 = total + x1
print("A conta com a gorjeta sera: ", round(total2,2))