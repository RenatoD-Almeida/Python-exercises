"""
Modulos em python

Um professor quer
sortear um dos seus
quatro alunos para
apagar o quadro. Faça
um programa que ajuda
ele. lendo o nome delas
e escravando o nome
do escolhido.

"""

from random import randint

print("-=" * 5, "Escolhido para apaguar o quadro", "=-" * 5)
nome1 = input("Digite o nome do aluno 1: ")
nome2 = input("Digite o nome do aluno 2: ")
nome3 = input("Digite o nome do aluno 3: ")
nome4 = input("Digite o nome do aluno 4: ")
print("-=" * 27)
list = [nome1, nome2, nome3, nome4]
# sort = randint(1, 4)
# print(f'O aluno sortiado foi {list[sort]]}')

print(f'O Aluno que irá apagar o quadro é o \'{list[randint(0,3)]}\'')

# print("professor sorteou:", end=" ")
# #
# # if (sort == 1):
# #     print(nome1, end=" ")
# # elif (sort == 2):
# #     print(nome2, end=" ")
# # elif (sort == 3):
# #     print(nome3, end=" ")
# # elif (sort == 4):
# #     print(nome4, end=" ")


