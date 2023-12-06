frase=('Curso de python')

print(frase.replace('Curso','Aula'))
# subistitui "Curso" por "Aula"

print(frase.upper())
# transforma tudo em maiúsculo
print(frase.upper().count('O'))

print(frase.lower())
# transforma em minúsculo

print(frase.capitalize())
# Só o primeiro caractere em maiúsculo

print(frase.title())
# A primeira letra de cada palava em maiúscula

frasedois=('   Curso de python ')

print(frasedois.strip())
# Desconsidera os espaços vazios no começo e no fim

print(frasedois.rstrip())
# Desconsidera os espaços vazios na direita

print(frasedois.lstrip())
# Desconsidera os espaços vazios na esquerda

frase = (frase.replace('Curso','Aula'))
# Substituir a frase em definitivo
print(frase)