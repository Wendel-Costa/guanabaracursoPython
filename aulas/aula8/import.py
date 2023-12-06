# import algo: mecanismo para importar uma biblioteca de funções
# from algo import coisa: para importar apenas uma função da biblioteca

import math
# ou "from math import sqrt"
num = int(input('Digite um número: '))

raiz=math.sqrt(num)

print('A raiz quadrada de {} é {}.'.format(num,raiz))