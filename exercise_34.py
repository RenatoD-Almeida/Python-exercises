"""
Faça um programa
que tenha uma lista
chamada números e
duas Funçoes
chamadas sorteia() e
somaPar(). A primaira
Função vai sortear 5
números e vai colocá-
los dentro da lista e a
segunda função vai
mostrar a soma entra
todos os valores
PARES sortados pela
Função anterior.
"""

from random import randint


def sorteia():
    list = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
    return sorted(list)


def somaPar(a):
    totalPar = 0
    for i in a :
        if i % 2 == 0:
            totalPar += i
    return totalPar


numeros = sorteia()
print(numeros)
print(somaPar(numeros))