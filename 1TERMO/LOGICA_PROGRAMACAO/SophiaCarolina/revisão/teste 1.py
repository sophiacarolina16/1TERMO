# 1
print("Resgistro de Operador")
operador = input("digite seu nome: \n")
turno = input("digite seu turno: \n")
print(f"Operador {operador} registrado no turno {turno}. Boa jornada!")

# 2
print("calculo de produção")
produção_hora = int(input(" Digite a quantidade de peças produzidas em 1 hora..."))
produção_turno = produção_hora * 8
print(f"Quantidade de peças produzidas em um turno de 8 horas: {produção_turno}")

# 3
print("conversor de unidade")
pressao_bar = float(input("Digite a pressão em Bar..."))
pressao_psi = pressao_bar * 14.5
print(f" pressão em PSI: {pressao_psi:.2f}")
print(f"pressão em PSI: {pressao_psi}", round (pressao_psi,2))

# 4
print("Inspeção de Peças")
n1 = float(input("Digite a nota de inspeção 1 (0 a 10)..."))
n2 = float(input("Digite a nota de inspeção 2 (0 a 10)..."))
n3 = float(input("Digite a nota de inspeção 3 (0 a 10)..."))

media = (n1 + n2 + n3)/ 3
print(f"Media de qualidade de peça: {media:.2}")
print("media de qualidade de peças: ", round (media,2))

# 5
print("termostato inteligente")
temperatura = float(input(" Digite a temperatura do motor:..."))
if temperatura < 40:
    print("baixa carga")
elif temperatura > 70: 
    print(" Alerta: resfriamento ativado!")
else:
    print("normal")

# 6
print("Classificador de lotes")
codigo_produto =input(" Digite o codigo do produto")
if codigo_produto.startswith ("A"):
    print("Alimentos")
elif codigo_produto.startswith ("E"):
    print("eletronicos")
else:
    print("Desconhecido")


# 7
print("segurança de Operação")
sensor_porta= input(" digite o status de sensor da porta (fechada/aberta)...")
botao_emergencia= input("Digite o status do botão de emergencia (ligada/delisgado)...")
if sensor_porta == "fechada" and botao_emergencia == "desligado":
    print("A maquina pode iniciar.")
else:
    print("A maquina não pode iniciar")

# 8

print("Cálculo de Descarte")
total_pecas = int(input("Digite o total de peças produzidas..."))
total_defeituosas = int(input("Digite o total de peças defeituosas..."))
descarte_percentual = (total_defeituosas / total_pecas) * 100
if descarte_percentual > 5:
    print("Revisar Processo")
else:
    print("Processo Otimizado")
print(f"Descarte percentual: {descarte_percentual:.2f}%")

# 9
print("Validação de Medida")
medida = float(input("Digite a medida da peça em mm..."))
if medida < 9.8:
    print("A peça esta abaixo da tolerançia.")
elif medida > 10.2:
    print("A peça esta acima da tolerancia.")
else:
    print("A peça esta dentro da tolerancia.")

# 10
print("contagem regressiva de setup")
for contagem in range (10,0,-1):
    print(contagem)
print("Prensa ativada!")

# 11
print("soma de produção(acumulador)")
peso_total= 0
while True:
    peso_caixa = float(input("digite o peso da caixa(0 para parar)..."))
    if peso_caixa ==0:
        break 
    peso_total += peso_caixa
    print(f"Peso total acumulador: {peso_total:.2f}kg")

# 12
print("Multiplas leituras")
temperaturas = []
for i in range(1,6):
    temp = float(input(f"Digite a temperatura do sensor {i}"))
    temperaturas.append(temp)

print(f"Maior temperatura lida: {max(temperaturas):.2f}")


# 13

print("painel de login")
senha_correta = "admin123"
tentativas = 3
while tentativas > 0:
    senha = input("Digite a senha do supervisor ...")
    if senha == senha_correta:
        print("Acesso permitido")
        break
    else:
        tentativas -=1
        print(f"Acesso Negado. Tentativas restantes: {tentativas}")
if tentativas == 0:
    print("Painel bloqueado.")

# 14

("Simulador de estoque:")
estoque = 100
while True:
    print("\menu:")
    print("1. Adcionar itens.")
    print("2. Remover itens.")
    print("3. Sair.")
    escolha = input("Escolha uma opção (1,2 ou 3)...")
    
    if escolha == 1:
        quantidade = int(input("Digite a quantidade de itens a adcionar..."))
        estoque += quantidade
        print(f"Estoque atualizado: {estoque} itens")
    elif escolha == "2":
        quantidade = int (input("digite a quantidade de itens a remover..."))
        estoque -= quantidade
        print(f"Estoque atualizado: {estoque} itens")
        if estoque < 10:
            print("estoque critico!")

    elif escolha == 3:
        print("Saindo do simulador de estoque...")
        break

    else:
        print("Opção invalida. tente novamente.")


    # 15

    print("relatorios de turno completo")
    total_pecas = 5
    pecas_aprovadas = 0

    for i in range(1, total_pecas + 1):
        diametro = float(input(f"Digite o diametro da peça {i} em mm..."))
        if 19.9 <= diametro <= 20.1:
            pecas_aprovadas += 1
    eficiencia = (pecas_aprovadas / total_pecas)* 100
    print(f"total de peças aprovadas: {pecas_aprovadas}")
    print(f"eficiencia do lote: {eficiencia:.2}% ")



