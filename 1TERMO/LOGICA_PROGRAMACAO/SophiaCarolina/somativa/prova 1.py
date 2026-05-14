# variaveis: A1, A10 -> B1, B10....


# Exercicio 01
# Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
A1=input("Digite seu nome: \n")
A2=input("Digite seu turno:\n A \n B \n C \n")
print("Operador", A1, " registrado no Turno", A2 ,". Boa jornada!" )

# Exercicio 02
# Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.
A3=int(input("Digite quantidade de peças produzidas em 1 hora: \n"))
A4= A3 * 8
print("Quantidade de peças produzidas em um turno de 8 horas sera: \n", A4)

# Exercicio 03
# Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

print("convertor de unidade de Bar para PSI")
A5=float(input("Digite a quantidade que deseja converter:\n"))
A6= A5 * 14.5
print("O resultado deu: \n", round(A6,2) )
      
# Exercicio 04
# Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
A7= int(input("Digite a nota da peça numero 1 de 0 a 10: "))
A8= int(input("Digite a nota da peça numero 2 de 0 a 10: "))
A9= int(input("Digite a nota da peça numero 3 de 0 a 10: "))
A10= ( A7 + A8 + A9)/ 3
print(" O resulyado da nota total da pessa foi " , A10)

# Exercicio 05
# Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

print("TERMOSTATO INTELIGENTE")
B1=int(input("Digite a temperatura do motor \n"))
if B1 < 40:
    print("Baixa carga")
elif B1 >= 40:
    print("Normal")
elif B1 > 70:
    print("ALERTA: Resfriamento Ativado!")


# Exercicio 06
# Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

print("Classificador de Lotes")

B2=int(input("Digite o codigo do produto \n"))
if B2 == "A":
    print("Alimentos")
elif B2 == "E":
    print("Eletrônicos")
else:
    print("Desconhecido")



# Exercicio 07
# Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o 
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode iniciar.
B3 = input("Sensor Porta : ")
B4 = input("Botão Emergencia : ")

if B3 == "fechada":
    print("porta fechada")
    if B4 == "desligado":
        print("Botão emergencia desligado") 

    B5= input("Deseja iniciar a maquina? \n")

    if B5 == "sim":
        print("Iniciando...")
    elif B5== "não":
        print("desligando...")   
else:
    print("Não é possivel iniciar maquina")
    

# obs aluno: essa foi a mais legal de se fazer.

# Exercicio 08
# Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total,exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

B6 = int(input("Digite o total de peças que foram produzidas: "))
B7 = int(input("Digite o total de peças defeituosas: "))
B8 = (B7 / B6) * 100
if B8 > 5:
    print("Revisar Processo")
else:
    print("Processo Otimizado")


# Exercicio 09
# Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.
B9 = int(input("Digite a medida da peça: "))
if B9 == 9.8:
    print("esta dentro da tolerancia")
elif B9 < 9.8:
    print("Abaixo da medida esperada")
elif B9 > 10.2:
    print("Acima da medida esperada")


# Exercicio 10
# Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

print("Contagem Regressiva de Setup")
for a in range(10, 0 , -1):
    from time import sleep
    print(f"Numero", a)
    sleep(1)
print("Prensa Ativada!")

# Exercicio 11
# Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.




# Exercicio 12
# Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
# Ao final, mostre qual foi a maior temperatura lida.



# Exercicio 13
# Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
# Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
# Se esgotar, exiba "Painel Bloqueado".



# Exercicio 14
# Simulador de Estoque: Comece com estoque = 100. Crie um menu (while) onde o
# usuário pode: (1) Adicionar itens, (2) Remover itens ou (3) Sair. Se o estoque ficar
# abaixo de 10, avise: "Estoque Crítico!".

# Exercicio 15
# Relatório de Turno Completo: Use um for para processar 5 peças. Para cada peça,
# peça o diâmetro. Se a peça for aprovada (entre 19.9 e 20.1), conte-a. No final do
# loop, exiba o total de peças aprovadas e a porcentagem de eficiência do lote.