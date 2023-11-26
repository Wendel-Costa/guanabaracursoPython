cidade=input('Diga sua cidade: ')
cid=cidade.upper().split()
print('A afirmação de que a cidade começa com "São" é {}!'.format('SÃO' in cid[0]))