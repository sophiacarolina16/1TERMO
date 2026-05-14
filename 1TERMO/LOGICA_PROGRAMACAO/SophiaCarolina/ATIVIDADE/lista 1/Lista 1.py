# Exercicio 1

# Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da programação em Python!".

print("Bem-vindo ao mundo da programação em Python!")

# Exerciico 2

# Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.

A1= str(input("Digite seu nome:\n"))
A2= int(input("Digite sua idade:\n"))
print("Seu nome é", A1, ", e sua idade é", A2 )

# Exercicio 3

# Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512 por 128. Cada resultado deve ser exibido em uma linha separada.
A3 = 135 + 246
print("O resultado da conta 135 + 246 é \n", A3)
A4= 512 - 128
print("o resultado da conta 512 - 128 é \n", A4)

# Exercicio 4

# Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da divisão de 78 por 3.

A5 = 15 * 8
print("O resultado da conta 15 * 8 é \n", A5)
A6 = 78 * 3
print("O resultado da conta 78 * 3 é \n", A6)

# Exercicio 5

# Calcule e exiba o resultado de "5 elevado à 3a potência" (53).

A7=(5 * 5) * 5
print("O resultado de 5 elevado a 3 potencia é:\n", A7)


# Exercicio 6

# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
A8 = "Sophia "
A9 = "Carolina"
print(" Meu nome é " , A8 +  A9 , )

# Exercicio 7

# Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule e exiba a taxa de aproveitamento (peças boas / total).

B1 = float(input(" Digite a quantidade de peças produzidas:\n"))
B2 = float(input(" Digite a quantidade de peças defeituosas:\n"))
B3 = float((B2/B1) * 100)
B4 = float(100 - B3)
print("A taxa de aproveitamento foi:\n ", round(B4,3) ,"%")
print("Taza de prejuizo: \n", round(B3,3), "%")

# Exercicio 8

# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados: "Eu tenho 25 anos e, em 10 anos, terei 35 anos."

B5 = int(input("Digite sua idade:"))

if B5==25:
    (print ("Eu tenho 25 anos e, em 10 anos, eu terei 35 anos"))
else:
    (print("numero esperado incorreto"))



# Exercicio 9

# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.

print("O custo do hotel por noite foi 250.50\n  O custo da passagem é 412.00")

B6 = float(250.50 + 412.00)
print("o custo total para a viagem é ", B6 ," por noite")

# Exercicio 10

# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a saída de forma organizada.


Pr=input("digite nome do produto:\n")
Pr2=int(input("Digite o preço do produto:\n"))
Qu=int(input("Digite a quantidade vendida:\n"))
tp = Pr2 * Qu
print("RELATORIO DE VENDAS")
print("Produto: ", Pr)
print("Quantidade vendida: ", Qu)
print("Preço unitario: ", Pr2)
print("Tota de vendas: ", tp)