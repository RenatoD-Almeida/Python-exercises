"""
Exercícios lista, 042 melhorado.

faça um programa que leia valores ilimitados pelo usuário (até que ele peça para parar),
armazene os valores digitados em uma lista e os repetidos em outra lista, ambas em uma única lista.
Depois mostre os valores digitados e os repetidos utilizando o for, depois o total de valores, e por
 ultimo as litas
"""

numList = [[], []]  # 1° - números repetidos | 2° números digitados.
i = True
resp = ""

while i:

    num = input("Digite um valor: ")

    if num.isnumeric():  # Verifica se é um número digitado / check if is a integer value
        num = int(num)
    else:
        print("Perdão, apenas valores numéricos.")
        continue

    if num in numList[1]:
        if num in numList[0]:
            print("Esse valor já foi digitado")
            continue
        else:
            numList[0].append(num)
        print("Número repetido, não iria adicionar!")
    else:
        numList[1].append(num)

    while True:
       resp = input("Deseja continuar? [S/N]\n")

       if resp in "SNsn":
           if resp in "Ss":
               break
           elif resp in "Nn":
               i = False
               break
       else:
           print("resposta invalida, apenas \'S\' ou \'N\'")

print("~~" * 15)
print(f"|{'Valores':^28}|")
print("~~" * 15)
print("{:^15}{:^15}".format("digitados", "repetidos"))

for i in range(len(numList[1])):
    print(f'{numList[1][i]:^15}', end="")
    if i < len(numList[0]):
        print(f'{numList[0][i]:^15}')
    else:
        print("{:^15}".format(" "))

print("~~" * 15)
print(f'{"Total de números digitados":^30}\n{len(numList[1]):^30}')
print(f'{"Total de números repetidos":^30}\n{len(numList[0]):^30}')
print("~~" * 15)
print(f'{"Lista de digitados":^30}\n{sorted((numList[1]))}')
print(f'{"Lista de repetidos":^30}\n{sorted(numList[0])}')
print("~~" * 15)
