algo=input('Diga algo: ')

print('É número?', algo.isnumeric())
print('É texto?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('É todo maiusculo?', algo.isupper())
print('É todo minusculo?', algo.islower())