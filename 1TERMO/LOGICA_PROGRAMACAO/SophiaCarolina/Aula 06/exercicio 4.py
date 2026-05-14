
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa.

print("Bem-Vindo ao trânsito!")
print("Atenção ao semaforo")
print("1 = VERDE")
print("2 = VERMELHO")
print("3 = AMARELO")
semaforo = (input("Digite a opção de cor \n"))

if semaforo == "1":
    from time import sleep
    print(f"VERDE")
    sleep(5)
elif semaforo == "2":
    print(f"VERMELHO")
    sleep(5)
else:
    print(f"AMARELO")
    sleep(5)