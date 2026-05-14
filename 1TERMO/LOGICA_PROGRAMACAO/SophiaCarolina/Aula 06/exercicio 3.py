# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no ite 5).

for i in range (1, 11):
    from time import sleep
    if i == 5:
     continue
    print(f"Falha ao ler o número {i}")
    sleep(1.8)
    continue
print("Acabou")
