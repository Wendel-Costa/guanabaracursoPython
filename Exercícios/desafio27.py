nome=input('Diga um nome: ').strip()

nomes = nome.split()

print('Primeiro nome: {} \nÚltimo nome: {}'.format(nomes[0],nomes[len(nomes)-1]))