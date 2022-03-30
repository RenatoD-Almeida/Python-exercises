"""
Faça um programa
que tenha uma Função
chamada maior(). que
receba vários
parâmetros com
valores inteiros.
Seu programa tem que
analisar todos os
valoras e dizar qual
deles é o maior.
"""


def maior(*args):
    print('foram passados',len(args), "valores")
    print(f'foram passados os valores: {args}')
    print(f'O maior valor foi {max(args)}')


maior(1, 2, 3, 4, 5, 6)
maior(0, 7, 2)