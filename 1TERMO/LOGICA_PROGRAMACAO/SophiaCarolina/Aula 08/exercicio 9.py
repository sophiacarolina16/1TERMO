import os
pasta = os.listdir()
for arquivo in pasta:
    if arquivo.endswith(".tmp"):
        os.remove(arquivo)
        print(f"Arquivo {arquivo} excluido.")
print("limpeza de arquivos concluida")