aluno=input('Diga o nome do aluno: ')

n1=float(input('Diga a primeira nota do(a) {}: '.format(aluno)))
n2=float(input('Diga a segunda nota do(a) {}: '.format(aluno)))

print('A média do(a) {} é {}. '.format(aluno,(n1+n2)/2))