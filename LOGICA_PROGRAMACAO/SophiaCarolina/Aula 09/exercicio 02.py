# Exercicio 1:
# Escreva um programa que solicite ao usuario um numero inteiro e calcule a media de uma lista de numeros. O programa deve tratar os seguintes erros:
# - ValueError: se o usuario digitar um valor que não seja um numero inteiro.
lista = 0

print("=-=-=-="*10)
print("Descubra a média entre 5 números!")
print("=-=-=-="*10)
for i in range(5):
    try:
        num = int(input("Digite um número inteiro: "))
        lista += num
    except ValueError:
        print("Erro: Digite um valor inteiro")
        num = int(input("Digite um número inteiro: "))
        lista += num

print(f"Média: {lista/5}")
