"""

Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastra-los em uma lista. Caso o número já exista
lá dantro. ele não será adicionado. No final, serão exibidos
todos os valoras únicos digitados, em ordem crescente.
"""

valoresList = list()

while True:

    valores = input("Digite um valor numérico: ")

    if valores.isnumeric():
        valores = int(valores)
        valoresList.append(valores)
    else:
        print("Apenas valores numéricos por favor.")
        continue

    resp = input("Deseja continuar? [S / N]\n")
    if resp[0] in "nN":
        break
print(f'Os valores digitados em ordem crescente são: {sorted(valoresList)}')
