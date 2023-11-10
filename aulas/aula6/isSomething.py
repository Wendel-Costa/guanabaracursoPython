# elemento.isnumeric() : vai dizer se é um numeral independente do tipo primitivo
# elemento.isalpha() : dizer se é um texto
# elemento.isalnum() : é alfanumérico
# muitos outros...

n=input("Digite algo: ")

print('É número?', n.isnumeric())
print('É texto?', n.isalpha())
print('É alfanumérico?', n.isalnum())