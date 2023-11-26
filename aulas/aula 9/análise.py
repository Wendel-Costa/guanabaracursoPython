
frase=('Curso de python')

print(len(frase))
# len: quantidade de caracteres

print(frase.count('o'))
# .count: conta a quantidade de letras "o"

print(frase.count('o',0,7))
# .count: conta a quantidade de letras "o" do 0 ao 7

print(frase.find('rso'))
# .find: mostra onde começou o conjunto "rso", caso não tenha o conjunto ele retorna -1

print('Curso' in frase)
# existe "Curso" na frase? (true/false)
