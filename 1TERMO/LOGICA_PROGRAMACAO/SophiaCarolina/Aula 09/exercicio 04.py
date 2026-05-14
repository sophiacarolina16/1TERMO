# mandar usuario digitar um numero, se digitar uma palavra vai dar erro.

print("--------"*10)
print(".........................Programa tratamento de erros...........................")
print("--------"*10)
try:
    num1 = int(input("                         Digite o primeiro numero: "))
    num2 = int(input("                         Digite o segundo numero:  "))
    resultado = num1 / num2
    print(f"O resultado da divisão é {resultado:.2f}")

except ZeroDivisionError:
     print("Erro: Não é possivel dividir por zero.")

except ValueError:
    print("Erro: Entrada invalida. Por favor digite um numero inteiro.")

