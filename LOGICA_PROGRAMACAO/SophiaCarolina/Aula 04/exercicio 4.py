print("Calculadora com condições")
print("Escolha como quer calcular")
print("1 = soma")
print("2 = subtração")
print("3 = Multiplicação")
print("4 = Divisão")
calculadora = float(input("Digite sua opção para calcular \n"))
if calculadora == 1: 
    print("1 = Voce escolheu soma")
    soma1 = int(input("Digite o primeiro valor  \n"))
    soma2 = int(input("Digite o segundo valor  \n"))
    print(soma1+soma2)

elif calculadora == 2: 
    print("2 = Voce escolheu subtração")
    sub1 = int(input("Digite o primeiro valor  \n"))
    sub2 = int(input("Digite o segundo valor  \n"))
    print(sub1-sub2)

elif calculadora == 3: 
    print("3 = Voce escolheu multiplicação")
    mul1 = int(input("Digite o primeiro valor  \n"))
    mul2 = int(input("Digite o segundo valor  \n"))
    print(mul1*mul2)

elif calculadora == 4: 
    print("4 = Voce escolheu divisão")
    div1 = int(input("Digite o primeiro valor  \n"))
    div2 = int(input("Digite o segundo valor  \n"))
    print(div1/div2)
    
else: 
    print("Voce não escolheu nenhuma das categorias")
    print("sair do programa")

