# Projeto Cancelar Automatica
# Criar um algoritmo que consiga gerenciar entrada e saida de veiculos, inserindo valores por hora permanecida.
# A forma de entrada e saida deve ser especificada e permitir o usuario inserir os dados necessarios para registro do veiculo.

# passos
# 1 - Pressionar botão, imprimiu im ticket.
    # abrir e fechar cancelas
    # calcular tempo de permanencia
    # pagar o ticket
    # devolver o ticket na saida
    # liberar e fechar cancelas

# 2 - Acesso por TAGs(Sem parar, conect car..)
    # abrir e fechar cancelas
    # calcular tempo de permanencia
    # gerar pagamento de fatura
    # liberar e fechar cancelas

# 3 - Erros
# verificar sinal de trasmissão da TAG
# verificar acesso por ticket ou tag ao mesmo tempo
# perdeu o ticket(levantar informações)
# problemas com cancela



from time import sleep

print("="*40)
print(" 🏬 BEM-VINDO AO SHOPPING DA SOPHIA 🏬")
print("="*40)


while True:
    try:
        A1 = int(input("\n[1] Liberar Ticket\n[2] Acesso com TAG\n👉 Escolha uma opção: "))
        if A1 in [1, 2]:
            break
        else:
            print("❗ Opção inválida! Digite apenas 1 ou 2.")
    except ValueError:
        print("❗ Erro: Digite apenas o NÚMERO 1 ou 2.")

if A1 == 1:
    print("\n🎫 STATUS: Você escolheu acesso por Ticket")
    
    
    while True:
        A5 = input("🔍 Verificando se há TAG instalada (s/n): ").lower()
        if A5 == "n":
            print("❌ Sem TAG detectada. Prosseguindo com Ticket...")
            break
        elif A5 == "s":
            print("⚠️ TAG detectada! Porém, alterando para modo Ticket...")
            break
        else:
            print("❗ Digite apenas 's' para SIM ou 'n' para NÃO.")

    print("\n⏳ Aguarde um momento...")
    for i in range(1, 6):
        print(f"   [{i}]...")
        sleep(1.0)

    print("\n📥 Liberando Ticket...")
    sleep(2.0)

    print("🚧 Abrindo cancelas...")
    sleep(2.0)

    
    while True:
        A6 = input("\n❓ Ocorreu algum erro na cancela? (s/n): ").lower()
        if A6 == "s":
            print("🚨 Chamando interfone...\n🛠️ Arrumando o erro...\n✅ Abrindo cancelas...")
            sleep(2.0)
            break
        elif A6 == "n":
            break
        else:
            print("❗ Responda com 's' ou 'n'.")

    print("🔒 Fechando cancelas...")
    sleep(2.0)

    print("\n" + "$" * 40)
    print("      💳 ÁREA DE PAGAMENTO")
    print("$" * 40)
    
    
    while True:
        A4 = input("\n[1] Inserir Ticket\n[2] Perdi meu Ticket\n👉 Opção: ")
        if A4 in ["1", "2"]:
            break
        else:
            print("❗ Opção inválida! Escolha 1 ou 2.")

    if A4 == "1":
        while True:
            try:
                A2 = float(input("🕒 Quantas horas você permaneceu no shopping? "))
                break
            except ValueError:
                print("❗ Erro: Digite um número válido para as horas.")
        
        A3 = 12.99 * A2
        print(f"\n💰 VALOR TOTAL: R$ {A3:.2f}")
        
        sleep(2.0)
        print("💳 Registrando pagamento...")
        sleep(2.0)
        
        print("\n📢 AVISO: Devolva o Ticket na saída.")
        sleep(2.0)

        print("\n--- SAÍDA SHOPPING DA SOPHIA ---")
        print("📥 Recolhendo o Ticket...")
        sleep(2.0)
        print("😊 Obrigado, volte sempre!")
        sleep(2.0)
        print("🚧 Abrindo cancelas...")
        sleep(2.0)
        
        while True:
            A7 = input("\n❓ Ocorreu algum erro na cancela? (s/n): ").lower()
            if A7 == "s":
                print("🚨 Chamando interfone...\n🛠️ Arrumando o erro...\n✅ Abrindo cancelas...")
                sleep(2.0)
                break
            elif A7 == "n":
                break
            else:
                print("❗ Responda com 's' ou 'n'.")
        print("🔒 Fechando cancelas.")

    elif A4 == "2":
        print("\n🏢 Por favor, dirija-se ao caixa da administração.")
        sleep(2.0)
        print("📂 Levantando informações...")
        sleep(2.0)
        print("\n--- SAÍDA SHOPPING DA SOPHIA ---")
        print("👋 Obrigado, volte sempre!")
        sleep(2.0)
        print("🚧 Abrindo cancelas...")
        sleep(2.0)
        
        while True:
            A8 = input("\n❓ Ocorreu algum erro na cancela? (s/n): ").lower()
            if A8 == "s":
                print("🚨 Chamando interfone...\n🛠️ Arrumando o erro...\n✅ Abrindo cancelas...")
                sleep(2.0)
                break
            elif A8 == "n":
                break
            else:
                print("❗ Responda com 's' ou 'n'.")
        print("🔒 Fechando cancelas.")

elif A1 == 2:
    print("\n🚗 STATUS: Acesso via TAG")
    sleep(2.0)
    
    
    while True:
        B1 = input("📡 Verificando transmissão da TAG... (s/n): ").lower()
        if B1 in ["s", "n"]:
            break
        else:
            print("❗ Responda com 's' ou 'n'.")

    if B1 == "s":
        print("✅ TAG validada! Abrindo cancelas...")
        sleep(2.0)
        
        while True:
            A9 = input("\n❓ Ocorreu algum erro na cancela? (s/n): ").lower()
            if A9 == "s":
                print("🚨 Chamando interfone...\n🛠️ Arrumando o erro...\n✅ Abrindo cancelas...")
                sleep(2.0)
                break
            elif A9 == "n":
                break
            else:
                print("❗ Responda com 's' ou 'n'.")
        
        print("🔒 Fechando cancelas...")
        sleep(2.0)

        print("\n--- SAÍDA SHOPPING DA SOPHIA ---")
        sleep(2.0)
        print("📧 Enviando boleto para o e-mail cadastrado...")
        print("👋 Volte sempre!")
        
        sleep(2.0)
        print("🚧 Abrindo cancelas...")
        sleep(2.0)
            
        while True:
            A10 = input("\n❓ Ocorreu algum erro na cancela? (s/n): ").lower()
            if A10 == "s":
                print("🚨 Chamando interfone...\n🛠️ Arrumando o erro...\n✅ Abrindo cancelas...")
                sleep(2.0)
                break
            elif A10 == "n":
                break
            else:
                print("❗ Responda com 's' ou 'n'.")
        print("🔒 Fechando cancelas.")

    elif B1 == "n":
        print("\n⚠️ Falha na transmissão da TAG.")
        while True:
            L1 = input("🎫 Deseja entrar retirando um Ticket? (s/n): ").lower()
            if L1 == "n":
                print("🚫 ACESSO BLOQUEADO.")
                break
            elif L1 == "s":
                print("\n📥 Liberando Ticket...")
            for i in range(1, 3):
                sleep(1.0)
            print("🚧 Abrindo cancelas...")
            for i in range(1, 3):
                sleep(1.0)
            
            K6 = input("\n❓ Ocorreu algum erro na cancela? (s/n): ")
            if K6 == "s":
                print("🚨 Chamando interfone...")
                print("🛠️ Arrumando o erro...")
                print("✅ Abrindo cancelas...")
                for i in range(1, 3):
                    sleep(1.0)
            
            print("🔒 Fechando cancelas...")
            for i in range(1, 5):
                sleep(1.0)

            print("\n" + "$" * 40)
            print("      💳 ÁREA DE PAGAMENTO")
            print("$" * 40)
            K4 = input("\n[1] Inserir Ticket\n[2] Perdi meu Ticket\n👉 Opção: ")

            if K4 == "1":
                K2 = float(input("🕒 Tempo de permanência (horas): "))
                K3 = 12.99 * K2
                print(f"\n💰 TOTAL: R$ {K3:.2f}")
                for i in range(1, 3):
                    sleep(1.0)
                print("💳 Registrando pagamento...")
                for i in range(1, 3):
                    sleep(1.0)
                print("📢 AVISO: Devolva o Ticket na saída.")
                for i in range(1, 5):
                    sleep(1.0)
                
                print("\n--- SAÍDA SHOPPING DA SOPHIA ---")
                print("Recolhendo Ticket...")
                for i in range(1, 3):
                    sleep(1.0)
                print("😊 Obrigado, volte sempre!")
                for i in range(1, 3):
                    sleep(1.0)
                print("🚧 Abrindo cancelas...")
                for i in range(1, 3):
                    sleep(1.0)
                
                K7 = input("\n❓ Ocorreu algum erro na cancela? (s/n): ")
                if K7 == "s":
                    print("🚨 Chamando interfone...")
                    print("🛠️ Arrumando o erro...")
                    print("✅ Abrindo cancelas...")
                    for i in range(1, 3):
                        sleep(1.0)
                print("🔒 Fechando cancelas.")

            elif K4 == "2":
                print("\n🏢 Dirija-se à administração.")
                for i in range(1, 3):
                    sleep(1.0)
                print("📂 Processando dados...")
                for i in range(1, 3):
                    sleep(1.0)
                print("\n--- SAÍDA SHOPPING DA SOPHIA ---")
                print("👋 Obrigado, volte sempre!")
                for i in range(1, 3):
                    sleep(1.0)
                print("🚧 Abrindo cancelas...")
                for i in range(1, 3):
                    sleep(1.0)
                
                A8 = input("\n❓ Ocorreu algum erro na cancela? (s/n): ")
                if A8 == "s":
                    print("🚨 Chamando interfone...")
                    print("🛠️ Arrumando o erro...")
                    print("✅ Abrindo cancelas...")
                    for i in range(1, 3):
                        sleep(1.0)
                    print("🔒 Fechando cancelas.")
            else:
                print("❗ Responda com 's' ou 'n'.")