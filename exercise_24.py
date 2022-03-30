"""
Façaa um programa que ajuda um jogador da MEGA SENA e criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo. cadastrando tudo em uma lista
composta.
"""

from random import randint

palpites = list()

jogos = int(input("Quantos jogos você pretente jogar?\n"))

for i in range(jogos):
    palpites.append([randint(1, 61), randint(1, 61), randint(1, 61),
                     randint(1, 61), randint(1, 61), randint(1, 61)])

for i in range(len(palpites)):
    print(f'{i+1}° jogo')
    print(f'{"palpites"}: {sorted(palpites[i])}')
