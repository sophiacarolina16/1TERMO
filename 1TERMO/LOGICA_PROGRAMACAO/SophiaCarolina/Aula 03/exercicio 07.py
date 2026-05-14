x1 =  float(input("Digite o preço do primeiro livro que deseja comprar: \n"))
x2 =  float(input("Digite o preço do segundo livro que deseja comprar: \n"))
x3 =  float(input("Digite o preço do terceiro livro que deseja comprar: \n"))
T1 = x1 - x1 / 5 
T2 = x2 - x2 / 5 
T3 = x3 - x3 / 5 
total = T1 + T2 + T3
print("O primeiro livro com desconto de 5% adcionada sera:" ,T1)
print("O segundo livro com desconto de 5% adcionada sera:" ,T2)
print("O terceiro livro com desconto de 5% adcionada sera:",T3)
print("O total da compra adcionando o desconto sera:" , total)
