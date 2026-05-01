'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
Perimetro = XX.X
Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
Area = XX.X
Entrada
A entrada contém três valores reais.
Saída
O resultado deve ser apresentado com uma casa decimal.
'''
lados = list(map(float, input().split()))

ordenado = sorted(lados)

if ordenado[2] < (ordenado[0] + ordenado[1]):
  print(f"Perimetro = {sum(lados):.1f}")
else:
  area_trap = ( (lados[0] + lados[1]) * lados[2] ) / 2
  print(f"Area = {area_trap:.1f}")
