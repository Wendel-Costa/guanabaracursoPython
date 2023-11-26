frase=input('Diga uma frase: ').strip().upper()

print('A frase possui {} letra(s) "A".'.format(frase.count("A")))


print('A letra "A" aparece primeiro na posição {} e por último na posição {}.'.format(frase.find("A")+1,frase.rfind("A")+1))

