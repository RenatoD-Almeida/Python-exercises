"""
modulo python

O mesmo professor
do dasafio anterior
quer sortear a ordam
da aprasentaSão de
trabalhos dos alunos.
Faça um programa que
leia o nome dos quatro
alunos a mostra a
ordem sorteada.

"""
from random import shuffle

print("- " * 5, "Alunos a apresentar", " -" * 5)
nome1 = input("Digite o nome do primeiro aluno: ")
nome2 = input("Digite o nome do segundo aluno: ")
nome3 = input("Digite o nome do terceiro aluno: ")
nome4 = input("Digite o nome do quarto aluno: ")
print("- " * 21,)

list = [nome1, nome2, nome3, nome4]
shuffle(list)

for i, k in enumerate(list):
    print(f'{i+1}° aluno a apresentar:{k:>20}\n')

# for i in \
#         (list):
#     print(i, end=" ")