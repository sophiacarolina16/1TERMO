# Calculo de notas semestre onde tera duas notas formativas e uma nota somativa pra encerrar o semestre
# os valores de notas é de 0 a 100

print("Vamos calcular suas notas do primeiro semestre")
nota1= int(input("Sua primeira nota formativa foi:"))
nota2=int(input("Sua segunda nota formativa foi:"))
nota3= int(input("Sua nota somativa foi:"))
total= (nota1 + nota2 + nota3) / 3 

print(f"Sua nota foi" ,round(total,2),"no primeiro semestre")

print("Vamos calcular suas notas do segundo semestre")
nota4= int(input("Sua primeira nota formativa foi:"))
nota5=int(input("Sua segunda nota formativa foi:"))
nota6= int(input("Sua nota somativa foi:"))
total2=  (nota4 + nota5 + nota6) / 3 
print(f"Sua nota foi" ,round(total2 ,2), "no segundo semestre")

total3= (total+total2) /2 
print(f" As notas do ano foram" ,round(total,2)," e",round(total2,2),)
