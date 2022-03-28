"""
Verificação de entrada de dados com isalpha e isnumeric para utilização do casting
"""

while True:
    nome = input("Digite o nome do aluno:")
    if(nome.isalpha()):
        break
    else:
        print("nome inválido")
while True:
    n1 = float(input("Digite a primeira nota do aluno:"))
    if n1 > 10:
        print('Apenas valores entre 1 e 10')
    else:
        break

while True:
    n2 = float(input("Digite a primeira nota do aluno:"))
    if n2 > 10:
        print('Apenas valores entre 1 e 10')
    else:
        break

media = (n1 + n2)/2

print('A média do aluno {} é {:.2f}'.format(nome, media))

