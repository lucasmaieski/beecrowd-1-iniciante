'''Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.'''

hr_inic, hr_fin = list(map(int, input().split()))

duracao = (hr_fin - hr_inic) % 24

if duracao == 0 and hr_inic == hr_fin:
  duracao = 24

print(f"O JOGO DUROU {duracao} HORA(S)")
