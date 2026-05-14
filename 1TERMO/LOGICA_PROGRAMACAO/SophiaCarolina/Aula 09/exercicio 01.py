# Tratamento de erros com o Python
# erros comum

# ValueError
# indexerror
# keyerror


# exemplo
print("exemplo de tratamento de erros")

try:
    num1 = int(input("Digite o primeiro numero..."))
    num2 = int(input("Digite o segundo numero..."))
    resultado = num1 / num2
    print(f"O resultado da divisão é {resultado:.2f}")

except ZeroDivisionError:
     print("Erro: Não é possivel dividir por zero.")

except ValueError:
    print("Erro: Entrada invalida. Por favor digite um numero inteiro.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

    if num1> 100:
        print("O numero digitado é maior que 100.")
        for i in range(1,6):
            print(f"{num1} x {i} = {num1 * i}")
        if e * i > 1000:
            print("O resultado da multiplicação é maior que 1000.")
            try:
                pass
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
    else:
        print("O numero digitado é menor ou igual a 100.")


except NameError:
    print("Erro: Variavel não definida.")


