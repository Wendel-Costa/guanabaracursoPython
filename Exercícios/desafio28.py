import random

numero= random.randint(0,5)
aposta = int(input('Adivinhe um número de 0 a 5: '))
if aposta == numero:
    print('Correto! O número certo é {}.'.format(numero))
else:
    print('Errado! O número certo é {}'.format(numero))
print('Obrigado')