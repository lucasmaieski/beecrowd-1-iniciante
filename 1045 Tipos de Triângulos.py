'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A² = B² + C², apresente a mensagem: TRIANGULO RETANGULO
se A² > B² + C², apresente a mensagem: TRIANGULO OBTUSANGULO
se A² < B² + C², apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
'''
lados = list(map(float, input().split()))

A, B, C = sorted(lados, reverse=True)

if A >= (B + C):
  print("NAO FORMA TRIANGULO")
else:
  quad_a = A ** 2
  quad_bc = B ** 2 + C ** 2

  if quad_a == quad_bc:
    print("TRIANGULO RETANGULO")
  elif quad_a > quad_bc:
    print("TRIANGULO OBTUSANGULO")
  else:
    print("TRIANGULO ACUTANGULO")
  
  if A == B == C:
    print("TRIANGULO EQUILATERO")
  elif A == B or A == C or B == C :
    print("TRIANGULO ISOSCELES")
