'''
testando o "as" para importação de modulo
- estudo com tuplas

Crie um programa que vai gerar cinco números aleatórios a
colocar em uma tupla. Depois disso. mostra a listagem de
números gerados e também indique o menor e o maíor valor que
estão na tupla.

'''

from random import randint as teste

numeros = (teste(0, 10), teste(0, 10), teste(0, 10), teste(0, 10), teste(0, 10), )

for i, k in enumerate(numeros):
    print(f'{i + 1}° número - {k}')

print("\nMaior número: {}".format(max(numeros)))
print("\nMenor número: {}".format(min(numeros)))
