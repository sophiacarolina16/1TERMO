def contar_frequencia():
    contagem = {}
    
    print("Digite as palavras uma por uma (digite 'sair' ou deixe em branco para finalizar):")
    
    while True:
        try:
            # Solicita a entrada do usuário
            entrada = input("Digite uma palavra: ")
            
            # Condição de parada
            if entrada.lower() == 'sair' or entrada == "":
                break
                
            # Verifica se a entrada é numérica (o que configuraria um erro de tipo "palavra")
            if entrada.isdigit():
                raise ValueError("A entrada não pode ser um número.")
            
            # Adiciona ou atualiza a contagem
            # .lower() garante que "Casa" e "casa" sejam contadas como a mesma palavra
            palavra = entrada.lower()
            contagem[palavra] = contagem.get(palavra, 0) + 1
            
        except ValueError as e:
            print(f"Erro: {e} Por favor, digite uma string válida.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    # Exibe o resultado
    print("\nContagem de palavras:")
    for palavra, frequencia in contagem.items():
        print(f"{palavra}: {frequencia}")

# Executa a função
contar_frequencia()