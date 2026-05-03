'''Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área superior da matriz, conforme ilustrado abaixo (área verde).

x  0   1   2   3   4   5   6   7   8   9   10  11
0 [i] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [i]
1 [ ] [i] [x] [x] [x] [x] [x] [x] [x] [x] [i] [ ]
2 [ ] [ ] [i] [x] [x] [x] [x] [x] [x] [i] [ ] [ ]
3 [ ] [ ] [ ] [i] [x] [x] [x] [x] [i] [ ] [ ] [ ]
4 [ ] [ ] [ ] [ ] [i] [x] [x] [i] [ ] [ ] [ ] [ ]
5 [ ] [ ] [ ] [ ] [ ] [i] [i] [ ] [ ] [ ] [ ] [ ]
6 [ ] [ ] [ ] [ ] [ ] [i] [i] [ ] [ ] [ ] [ ] [ ]
7 [ ] [ ] [ ] [ ] [i] [ ] [ ] [i] [ ] [ ] [ ] [ ]
8 [ ] [ ] [ ] [i] [ ] [ ] [ ] [ ] [i] [ ] [ ] [ ]
9 [ ] [ ] [i] [ ] [ ] [ ] [ ] [ ] [ ] [i] [ ] [ ]
10[ ] [i] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [i] [ ]
11[i] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [i]

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem 144 valores com ponto flutuante de dupla precisão que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.'''

def imprimir(valor):
  print(f"{valor:.1f}")

def somar(matriz):
  soma = 0
  contagem = 0
  for i in range(5):
    for j in range(1+i, 11-i):
      soma += matriz[i][j]
      contagem += 1
  return soma, contagem

def criar_matriz():
  lista_de_listas = []
  for _ in range(12):
    linha = []
    for _ in range(12):
      linha.append(float(input()))
    lista_de_listas.append(linha)
  return lista_de_listas

def inicio():
  operacao = input().upper()

  matriz = criar_matriz()

  if operacao == 'S':
    resultado, quantidade = somar(matriz)
  elif operacao == 'M':
    resultado, quantidade = somar(matriz)
    resultado = resultado / quantidade

  imprimir(resultado)

if __name__ == "__main__":
  inicio()
