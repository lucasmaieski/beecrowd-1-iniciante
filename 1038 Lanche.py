'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
cod | especificao | preco
1 | cachorro quente | 4,00
2 | x salada | 4,50
3 | x bacon | 5,00
4 | torrada simples | 2,00
5 | refrigerante | 1,50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.


'''

item, qnt = map(int, input().split())

precos = [4, 4.5, 5, 2, 1.5]

total = qnt * precos[item-1]

print(f"Total: R$ {total:.2f}")
