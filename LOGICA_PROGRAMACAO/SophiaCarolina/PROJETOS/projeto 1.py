# Contexto
# O Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho
# (SESMT) precisa automatizar o controle de treinamentos obrigatórios (como CIPA,
# Brigada de Incêndio e NR-35) e a entrega de Equipamentos de Proteção Individual (EPIs).
# Objetivo
# Desenvolva um programa em Python que gerencie o status de conformidade dos
# funcionários de uma empresa.
# Requisitos do Programa
# 1. Cadastro de Funcionários:
# ○ Armazene o nome, setor e o status dos treinamentos (NR-10, NR-35 e
# Brigada).

# 2. Verificação de EPI (NR-6):
# ○ O sistema deve receber o setor do funcionário.
# ○ Se o setor for "Elétrica", liste a obrigatoriedade de luvas de alta tensão e
# botas dielétricas.
# ○ Se o setor for "Trabalho em Altura", liste o cinturão de segurança e
# talabarte.
# 3. Alerta de Reciclagem:
# ○ Crie uma função que receba o ano do último treinamento da Brigada de
# Incêndio.
# ○ Se o treinamento tiver mais de 2 anos, exiba a mensagem: "Treinamento
# Vencido! Encaminhar para reciclagem."
# ○ Caso contrário, exiba: "Treinamento Válido."


from time import sleep

print("GERENCIAMENTO DE STATUS DE FUNCIONARIO SENAI")

for i in range(1, 3):
    sleep(1.0)

print("AREA DE CADASTRO")

sleep(1.0)

while True:
    def informações():

        return informações
    nome = input("Digite seu nome: ")
    setor = input("Digite seu setor: ")
    status1 = input("NR-10 status(S/N): ")
    status2 = input("NR-35 status(S/N): ")
    status3 = int(input("Brigada ultimo ano feito: "))
    if setor == "eletrica":
        print("ATENÇÂO: Uso obrigatorio de luvas de alta tensão e botas dielétricas!")
    elif setor == "trabalho em altura":
        print("ATENÇÂO: Uso obrigatorio de cinturão de segurança e talabarte!")
    if status1 == "S":
        print("NR-10 concluido")
    elif status1 == "N":
        print("NR-10 não concluido")
        
    if status2 == "S":
        print("NR-35 concluido")
    elif status2 == "N":
        print("NR-35 não concluido")
    
    if status3 > 2:
        print("Treinamento vencido! Encaminhar para reciclagem")
    elif status3 == "N":
        print("Treinamento Valido")
        
    sleep(3.0)
    print("RETOMANDO A AREA DE CADASTRO")
    sleep(3.0)
        