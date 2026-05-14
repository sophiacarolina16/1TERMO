print("Vamos ver suas notas:")

nota = int(input("digite sua primeira nota: \n"))
nota2 = int(input("digite sua segunda nota: \n"))

total = (nota +nota2) /2

print("Sua nota total foi :", total)
if total > 7:
    print("Voce passou de ano")
elif total == 7:
    print("Voce passou na media")
else:
    print("Voce repetiu")