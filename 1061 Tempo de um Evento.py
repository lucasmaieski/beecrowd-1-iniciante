'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.
'''

linha_inic_dia = input().split()
inic_dia = int(linha_inic_dia[1])

h1, m1, s1 = map(int, input().split(" : "))

linha_fim_dia = input().split()
fim_dia = int(linha_fim_dia[1])
h2, m2, s2 = map(int, input().split(": "))


inic_seg = s1 + (m1 * 60) + (h1 * 3600) + (inic_dia * 86400)
fim_seg = s2 + (m2 * 60) + (h2 * 3600) + (fim_dia * 86400)

duracao = fim_seg - inic_seg

dias = duracao // 86400
duracao = (duracao % 86400)
horas = duracao // 3600
duracao = (duracao % 3600)
min = duracao // 60
seg = duracao % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{min} minuto(s)")
print(f"{seg} segundo(s)")
