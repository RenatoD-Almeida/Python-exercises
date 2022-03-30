"""
Crie um programa
onde 4 jogadores
joguem um dado a
tenham resultados
aleatórios. Guarde
essas resultados em
um dicionário. No final.
coloque esse
dicionário em ordem.
sabendo que o
vencedor tirou o maior
número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

input()
jogadas = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6)
}

for k, v in jogadas.items():
    print(f'{k} jogou o número {v}')
    sleep(0.7)

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('===', f'{"Ranking"}', '===')

for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]} pontos')
