'''
Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada (largura e altura) que será preenchida da seguinte forma: a parte externa é preenchida com 0, a parte interna é preenchida com 1, a diagonal principal é preenchida com 2, a diagonal secundária é preenchida com 3 e o ponto central contém o valor 4, conforme os exemplos abaixo.

Obs: o quadrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. A linha e a coluna começam em zero (0).

Entrada
A entrada contém vários casos de teste e termina com EOF (fim de arquivo. Cada caso de teste consiste de um valor inteiro ímpar N (5 ≤ N ≤ 101) que é o tamanho da matriz.

Saída
Para cada caso de teste, imprima a matriz correspondente conforme o exemplo abaixo. Após cada caso de teste, imprima uma linha em branco.

Exemplo de Entrada
5
11

Exemplo de Saída
20003
01110
01410
01110
30002

20000000003
02000000030
00200000300
00011111000
00011111000
00011411000
00011111000
00011111000
00300000200
03000000020
30000000002
'''

import sys

for linha in sys.stdin:
  n = int(linha)
  
  for i in range(n):
    linha = []
    for j in range(n):
      x = 0
      if int(n/2) == i and int(n/2) == j:
        x = 4
      elif (int(n/3) <= i < (n-(int(n/3)))) and (int(n/3) <= j < (n-(int(n/3)))):
        x = 1
      elif i == j:
        x = 2
      elif i+j == n-1:
        x = 3
      
      linha.append(x)
      
    print("".join(str(item) for item in linha))
  print()
