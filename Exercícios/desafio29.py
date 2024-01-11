v=int(input('Velocidade do carro:'))

if v > 80:
    print('O carro foi multado e o total da multa é R${}.'.format((v-80)*7))
else:
    print('Não foi multado')