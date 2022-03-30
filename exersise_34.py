"""
Faça um programa
que tenha uma Função
chamada contador().
que receba três
parâmetros: inicio, fim
e passo a realize a
contagam.
Seu programa tem que
realizar três
contagens através da
Função criada:

a) De 1 até 10. de 1 em 1

b) De 10 até 0, de 2 em 2

c) Uma contagem pacsonalizada
"""


def contar(n, n1, cont=1):
    if n < n1:
        print(f'Contagem de {n} até {n1} de {cont} em {cont}')
        for i in range(n, n1, cont):
            print(i)
    else:
        print(f'Contagem de {n} até {n1} de {cont} em {cont}')
        cont = cont * (-1)
        for i in range(n, n1, cont):
            print(i)


contar(1, 10)
contar(10, 0)
contar(10, 100, 2)
