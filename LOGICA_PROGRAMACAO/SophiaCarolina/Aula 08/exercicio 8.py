with open("notas.txt", "r") as notas:
    conteudo = notas.read()
with open("notas_backup.txt", "w") as backup:
    backup.write(conteudo)
