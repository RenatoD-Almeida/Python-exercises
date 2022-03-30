"""
Faça um programa que leia nome e peso de várias pessoas. guardando tudo em uma lista. No final. mostre:

• Quantas pessoas foram cadastradas.
• Uma listagem com as pessoas mais pesadas.
• Uma listagem com as pessoas mais leves.
"""

pessoas = [[],
           []]
total_pessoas = 0
total_peso = 0
total_n = 0

while True:

    nome = input("Cadastre o nome: ")

    if nome:
        pessoas[0].append(nome)
        total_pessoas += 1
    else:
        print("É necessário digitar um nome:")
        continue

    peso = input("Digite o peso: ")

    if peso.replace(".", "").isnumeric():
        peso = float(peso)
        total_peso += 1
    else:
        peso = "< Não registrado >"
        total_n += 1
    pessoas[1].append(peso)

    resp = (input("Deseja continuar? [ S / N ]\n"))

    if resp in "nN":
        break
    else:
        continue

print("=" * 50)
print("{:^50}".format("Clientes cadastrados"))
print("=" * 50)
print(f"{'Nomes':^25}{'Pesos':^25}")
print("-""" * 50)

for i in range(len(pessoas[1])):
    print(f'{pessoas[0][i]:^25}{pessoas[1][i]:^25}')

print("-""" * 50)
print(f'Total de pessoas cadastradas: {total_pessoas}')
print(f'Total de pesos cadastrados: {total_peso}')
print(f'Total de pesos não cadastrados: {total_n}')