n1=int(input('Diga um número: '))
n2=int(input('Outro um número: '))
n3=int(input('Outro um número: '))

if n1 > n2:
    if n3 > n2:
        menor=n2
        if n1 > n3:
            maior=n1
        else:
            maior=n3
    else:
        menor=n3
        maior=n1
else:
    if n3 > n1:
        menor=n1
        if n2 > n3:
            maior=n2
        else:
            maior=n3
    else:
        menor=n3
        maior=n2
print
print('Maior número: {} \nMenor número: {}'.format(maior,menor))