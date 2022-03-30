"""
Crie um programa que vai lar vários números a colocar em uma lista. Depois disso. mostra:

A) Quantos números Foram digitados.
B) A lista da valores ordenada da forma decrescente.
C) 
"""

num_lista = []
num_repetidos = num_total = 0

resp = ''

print(len(num_lista))

while True:
    num = input("Digite um valor numérico: ")

    if num.isnumeric():
        num = int(num)
    else:
        print("Desculpe, apenas valores numéricos.")
        continue

    if len(num_lista) == 0:
        num_lista.append(num)
        num_total += 1
    else:
        for i in num_lista:
            if i == num:
                print("Número repetido, não vou adicionar")
                num_repetidos += 1
                break
        else:
            num_lista.append(num)
            num_total += 1

    resp = input("Deseja continuar? [S/N]\n")
    if resp[0] in "nN":
        break

print(f'valores digitados em ordem crescente: ')

for i in sorted(num_lista):
    if i < num_lista[-1]:
        print(i, end=", ")
    else:
        print("{}.".format(i))

print(f'Total de números digitados: {num_total}')
print(f'Total de números repetidos: {num_repetidos}')