'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

inic_h, inic_m, fin_h, fin_m = list(map(int, input().split()))

inic_tot = inic_h * 60 + inic_m
fin_tot = fin_h * 60 + fin_m

duracao = (fin_tot - inic_tot) % 1440

if duracao == 0:
  duracao = 1440

horas = duracao // 60
minutos = duracao % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
