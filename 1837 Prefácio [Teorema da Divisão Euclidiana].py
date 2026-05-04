'''
o quociente e o resto da divisão de um inteiro a por um inteiro não-nulo b são respectivamente os únicos inteiros q e r tais que 0 ≤ r < |b| e:

a = b × q + r

Caso você não saiba, o teorema que garante a existência e a unicidade dos inteiros q e r é conhecido como ‘Teorema da Divisão Euclidiana’ ou ‘Algoritmo da Divisão’.

Entrada
A entrada é composta por dois números inteiros a e b (-1.000 ≤ a, b < 1.000).

Saída
Imprima o quociente q seguido pelo resto r da divisão de a por b.
'''

import sys

for linha in sys.stdin:
  if not linha:
    continue

  dividendo, divisor = map(int, linha.split())

  resto = dividendo % abs(divisor)

  quociente = (dividendo - resto) // divisor

  print(f"{quociente} {resto}")
