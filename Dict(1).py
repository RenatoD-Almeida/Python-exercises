"""
Faça um programa
que leia nome e
média de um aluno.
guardando também a
SituaSão em um
dicionário. No final.
mostre o conteúdo da
estrutura na tela.
"""

alunos = dict()

# nome = input("Digite o nome do aluno: ")
# media = input("Digite a média do aluno: ")

alunos['nome'] = input("Digite o nome do aluno: ")
alunos['media'] = input("Digite a média do aluno: ")

# if float(alunos['media']) >= 7:
#     alunos['situação'] = "aprovado"
# else:
#     alunos['situação'] = "reprovado"

alunos['situação'] = 'aprovado' if float(alunos['media']) >= 7 else "reprovado"

for k, v in alunos.items():
    print(f'{k} é {v}')