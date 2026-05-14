# Exercicio 2:

# escreva um programa que solicite ao usuario uma lista de palavras e conte quantas vezes cada palavra aparece na lista. o programa deve tratar os seguintes erros

# - ValueError: se o usuario digitar um valor que não seja string.

while True:
    try:

        palavras = (input("DIGITE UMA PALAVRA: ")).split()
        contagem = {}

        for palavra in palavras:
            if palavra in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1
            print("contagem das palavras:")
        for palavra, contagem in contagem.items():
            print(f"{palavra}: {contagem}")
        
    except ValueError:
        print("ERRO: ENTRADA INVALIDA. POR FAVOR, DIGITE UMA LISTA DE PALAVRAS SEPARADAS POR ESPAÇO.")
    
    if palavras == 'sair':
        break