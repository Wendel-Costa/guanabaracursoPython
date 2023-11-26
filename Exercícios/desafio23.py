n=input('Escreva um número de até 4 algarismos (desconsideraremos o excesso): ')
n=(n.strip()[:4])
n=int(n)
u= n // 1 % 10
d= n // 10 % 10
c= n // 100 % 10
m= n // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))