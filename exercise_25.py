"""

Crie um programa que leia nome a duas notas da vários
alunos e guarda tudo em uma lista composta. No final,
mostra um boletim contendo a média da cada um a permita
que o usuário possa mostrar as notas de cada aluno individualmente.
"""

alunos = []
contador = 1
repete = True

while repete:

    nome = input(f"Digite o nome do {contador}° aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno {}: ".format(contador)))
    nota2 = float(input("Digite a segunda nota do aluno {}: ".format(contador)))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    contador += 1

    resp = input("Deseja continuer? [S / N]\n")
    repete = False if resp in "nN" else True

print(alunos)

print(f"{'N°':<5}{'Nomes':<15}{'Nota 1':<15}{'Nota 2':<15}{'Média'}")
print('=' * 55)
for i, v in enumerate(alunos):
    print(f'{i:<5}{v[0]:<15}{v[1][0]:<15}{v[1][1]:<15}{v[-1]}')









