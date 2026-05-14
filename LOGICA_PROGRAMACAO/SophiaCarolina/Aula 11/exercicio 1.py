def nome():
    nome = input("Digite seu nome: ")
    return nome
print(f"Ola, {nome()}!")

def valores():
    print("Digite tres valores:")
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    return a, b, c
print(f"O maior valor é {max(valores())}")

# realizando funções
nome()
valores()

# conceito de chaves
def calcular_dobro(numero):
    return numero * 2
print(calcular_dobro(5))

