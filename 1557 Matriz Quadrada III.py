'''Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho T justificados à direita e separados por espaço, onde T é igual ao número de dígitos do maior número da matriz. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.

Exemplo de Entrada
1
2
3
4
5
0

Exemplo de Saída
1

1 2
2 4

 1  2  4
 2  4  8
 4  8 16

 1  2  4  8
 2  4  8 16
 4  8 16 32
 8 16 32 64

  1   2   4   8  16
  2   4   8  16  32
  4   8  16  32  64
  8  16  32  64 128
 16  32  64 128 256
'''

def imprimir(matriz, tamanho, n):
  for linha in matriz:
    print(" ".join(f"{numero:{tamanho}d}" for numero in linha))
  print()

def tamanho_campo(matriz, n):
  return len(str(matriz[n-1][n-1]))

def criar_matriz(n):
  matriz = []
  for posicao_linha in range(n):
    linha = []
    i = 2 ** posicao_linha

    for posicao_coluna in range(n):
      linha.append(i)
      i *= 2
    
    matriz.append(linha)
  return matriz

def inicio():
  while True:
    n = int(input())

    if n == 0:
      break
    
    matriz = criar_matriz(n)
    tamanho = tamanho_campo(matriz, n)
    imprimir(matriz, tamanho, n)

if __name__ == "__main__":
  inicio()
