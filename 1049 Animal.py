'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''

dicionario = {
   "vertebrado" : {
       "ave" : {
           "carnivoro" : "aguia",
           "onivoro" : "pomba"
            },
        'mamifero' : {
            'onivoro' : 'homem',
            'herbivoro' : 'vaca'
            }
    },
    'invertebrado' : {
        'inseto' : {
            'hematofago' : 'pulga',
            'herbivoro' : 'lagarta'
            },
        'anelideo' : {
            'hematofago' : 'sanguessuga',
            'onivoro' : 'minhoca'
            }
        }
    }

p1 = input().strip()
p2 = input().strip()
p3 = input().strip()

resultado = dicionario[p1][p2][p3]

print(resultado)
