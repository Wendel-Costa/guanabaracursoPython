pessoa=input('Diga seu nome completo: ').strip()

print('Nome todo maiúsculo: {}'.format(pessoa.upper()))

print('Nome todo minúsculo: {}'.format(pessoa.lower()))

letras= len(pessoa) - pessoa.count(' ')
print('O nome {} possui {} letras no total.'.format(pessoa,letras))

primeiro = pessoa.split()
print('O primeiro nome ({}) possui {} letras'.format(primeiro[0], len(primeiro[0])))