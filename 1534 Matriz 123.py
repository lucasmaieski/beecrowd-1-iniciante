'''Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.

Entrada
A entrada contém vários casos de teste e termina com EOF. Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70), que determina o tamanho (linhas e colunas) de uma matriz que deve ser impressa.

Saída
Para cada N lido, apresente a saída conforme o exemplo fornecido.

Exemplo de Entrada
4
7

Exemplo de Saída
1332
3123
3213
2331
1333332
3133323
3313233
3332333
3323133
3233313
2333331'''

while True:
  try:
    linha = input()
    if not linha:
      break
    n = int(linha)
    
    for pos_linha in range(n):
      linha_atual = []

      for posicao_coluna in range(n):
        if pos_linha + posicao_coluna == n-1:
          incluir = 2
        elif pos_linha == posicao_coluna:
          incluir = 1
        else:
          incluir = 3
        
        linha_atual.append(incluir)
      
      print("".join(str(v) for v in linha_atual))

  except EOFError:
    break
