print("agora iremos escolher o que comprara")
print("1 = roupa")
print("2 = sapato")
print("3 = perfumes")

cor = int(input("digite o numero da qual voce vai comprar: \n "))

if cor == 1:
    print(" voce escolheu roupa, ela esta com um desconto de 5%")
    compra1 = int(input("Digite o valor da roupa: \n"))
    cor1 =  ((compra1 * 5) /100) 
    print(" O desconto seria:",cor1)
    lol1 = compra1 - cor1
    print("O produto então ficara: ", lol1)
    print("Obrigado pela compra")

elif cor == 2:
    print(" voce escolheu sapato, ele esta com desconto de 10%") 
    compra2 = int(input("Digite o valor do sapato: \n"))
    cor2 = ((compra2 * 10) /100)
    lol2 = compra2 - cor2
    print(" O desconto seria:",cor2)
    print("O produto então ficara: ", lol2)
    print("Obrigado pela compra")

elif cor == 3:
    print(" voce escolheu perfume, ela esta com desconto de 2%")
    compra3 = int(input("Digite o valor do perfume: \n"))
    cor3 =  ((compra3 * 2) /100) 
    print(" O desconto seria:",cor3)
    lol3 = compra3 - cor3
    print("O produto então ficara: ", lol3)
    print("Obrigado pela compra")


else:
    print(" voce não escolheu nenhuma dessas opções")
    print("reiniciar do programa")
