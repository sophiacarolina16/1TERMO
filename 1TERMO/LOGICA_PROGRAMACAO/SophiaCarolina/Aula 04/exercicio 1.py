#if: "Se" a condição for verdadeira
# elif: "Senão, se" (Usado para multiplas condições)
# else: "Senão" (executa se nenhuma das anteriores for verdadeira)

print("Expressões logicas")
idade= int(input("Digite sua idade:"))

if idade >= 18:
    print("Voce é maior de idade.")
    print("Pode tirar carta de motorista.")
elif idade >= 16:
    print("Voce ainda não é maior de idade, mas ja pode votar.")
else:
    print("Voce é menor de idade.")
