# crie um programa que receba dois dados: a pressão atual (float) e as horas de uso acumuladas (int) de uma turbina.
# o programa deve classificar o estado da maquina sequindo essa hierarquia:
# critico(prioridade 1): se a pressão for maior que 100 ou as horas de uso forem maiores 10000
# mensagem "Parada imediata: risco de falha catrastrofica"
# alerta(prioridade 2) se a pressão estiver 88 a 100
# mensgaem: manutenção agendada: pressão acima do idea
# monitoramneto(prioridade 3) se as horas de uso forem entre 8000 e 10000
# mensagem "Aviso: maquina aproximando-se da revisão de 10k horas"
# normal: para qualquerr outro caso que não se encaixe nos acima
# mensagem: sistema operal: todos os parametros dentro da normalidade
