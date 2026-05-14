
def configurar_conexao(servidor,porta=8080):
     print(f"conectando a {servidor} na porta {porta}...")

configurar_conexao("192.168.1.1")
configurar_conexao("10.0.0.1", 3000)
configurar_conexao("192.168.1.2")
configurar_conexao("10.0.0.2", 3001)

