"""
Exercicio condições

Escreva um
programa qua faça o
computador "pensar"
em um número inteiro
entre O e 5 e paça para
o usuário tantar
dascobrir qual Foi o
número escolhido pelo
computador.

O programa daverá
escraver na tela se o
usUário venceu ou
perdeu.

"""

from random import randint as sortear

print("-=" * 15)
print(f'{"Jogo da advinhação":^30}')

while True:
    print("-=" * 15)
    print(f'{"Deseja jogar?":^30}')
    print("{:^30}".format("1 - Sim"))
    print("{:^30}".format("2 - Não"))
    print("-=" * 15)
    op = input("-> ")
    if (op != "1") and (op != "2"):
        print("opção invalida")
        break
    elif(op == "1"):
        print("-=" * 25)
        print("{:^50}".format("O jogo vai começar"))
        print("-=" * 25)
        jogada = int(input("Escolha um valor entre 1 e 5: "))
        if jogada > 5 or jogada < 1:
            print("Jogada invalida")
        else:
            computador = sortear(1, 5)
            print(f"\n   Jogador: {jogada:>30}\n\n   Computador: {computador:>27}\n")
            if (jogada == computador):
                print("{:^50}".format("Jogador venceu!"))
            else:
                print("{:^50}".format("Jogador computador!"))
            print("-=" * 25)
    elif(op == "2"):
        print("Você iria perder mesmo...")
        break