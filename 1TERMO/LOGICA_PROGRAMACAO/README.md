# Cronograma de Aulas: Lógica de Programação com Python

## 📋 Estrutura do Curso

### Aula 1: Introdução ao Python e Ambiente de Desenvolvimento
* **Conteúdo:** História do Python, filosofia de design (The Zen of Python) e instalação do interpretador.
* **Prática:** Configuração do ambiente (VS Code ou Thonny IDE) e execução do primeiro script ("Hello, World!").
* **Clean Code:** Importância da legibilidade do código, indentação obrigatória e uso correto de comentários.

### Aula 2: Variáveis, Tipos de Dados e Operadores
* **Conteúdo:** Conceito de variáveis, tipagem dinâmica e tipos primitivos (`str`, `int`, `float`, `bool`).
* **Prática:** Operações aritméticas, manipulação de strings e entrada/saída de dados com `input()` e `print()`.
* **Clean Code:** Padrão PEP 8 para nomenclatura de variáveis (uso do estilo `snake_case`) e escolha de nomes significativos.

### Aula 3: Estruturas Condicionais (`if`, `elif`, `else`)
* **Conteúdo:** Operadores relacionais (de comparação) e operadores lógicos (`and`, `or`, `not`).
* **Prática:** Tomada de decisão no código, validação de dados e encadeamento de condições complexas.
* **Clean Code:** Evitar aninhamentos excessivos de condições (*Arrow Anti-pattern*) e buscar simplicidade lógica.

### Aula 4: Estruturas de Repetição (`for`, `while`)
* **Conteúdo:** Conceito de loops, iteração sobre sequências e loops baseados em condições booleanas.
* **Prática:** Uso da função `range()`, interrupção de loops com `break` e continuidade com `continue`.
* **Clean Code:** Evitar loops infinitos acidentais no `while` e dar preferência ao `for` para iterar sobre coleções conhecidas.

### Aula 5: Modularização e Importação de Bibliotecas (`import`)
* **Conteúdo:** Organização de código em módulos, reaproveitamento de lógica e consumo de pacotes externos.
* **Prática:** Importação de módulos nativos do Python (como `math`, `random` e `time`) e criação de módulos próprios.
* **Clean Code:** Organização dos comandos `import` no topo do arquivo e importação apenas do que será explicitamente utilizado.

---

## 📌 Pilares de Clean Code Aplicados (Boas Práticas Gerais)

* **Legibilidade:** O código deve ser escrito para que seres humanos entendam, não apenas a máquina.
* **Regra do Escoteiro:** Deixe o código mais limpo do que como você o encontrou ao fazer alterações.
* **Nomes Reveladores:** Funções e variáveis devem expressar claramente sua intenção (ex: usar `total_vendas` em vez de apenas `t`).
* **Refatoração:** Processo contínuo de reestruturação do código para melhorar a arquitetura sem alterar seu comportamento externo.
