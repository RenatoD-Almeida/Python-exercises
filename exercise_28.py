"""
Crie um programa
que gerencie o
aproveitamento de um
jogador de futabol. 0
programa vai ler o
nome do jogador e
quantas partidas ele
jogou. Depois vai ler a
quantidade de gols
feitos em cada
partida. No final. tudo
isso será guardado em
um dicionario.
incluindo o total de
gols feitos durante o
campeonato.
"""

jogador = dict()
listaJogos = []
jogador["Nome"] = input("Digite o nome do jogador: ")
jogos = int(input(f"Quantos jogos o {jogador['Nome']} jogou?\n"))

for i in range(0, jogos):
    listaJogos.append(int(input("Digite quantos gols foram feitos no jogo {}\n".format(i+1))))

jogador["Partidas"] = jogos
jogador["Gols"] = listaJogos[:]
jogador["TotalGols"] = sum(listaJogos)

print("=" * len("Quadro de jogadores"))
print("Quadro de jogadores".center(15))
print("=" * len("Quadro de jogadores"))
print(jogador)
print("=" * len("Quadro de jogadores"))

for k, v in jogador.items():
    print(f'{k}: {v}')

print("=" * len("Quadro de jogadores"))

print(f'O jogador {jogador["Nome"]}:')
print(f'Jogou {jogador["Partidas"]} jogos e fez')
for i in range(0, len(jogador["Gols"])):
    print(f'{i + 1}° partida:  {jogador["Gols"][i]} gols')
print("Terminando o campeonato com {} gols no total".format(jogador["TotalGols"]))







