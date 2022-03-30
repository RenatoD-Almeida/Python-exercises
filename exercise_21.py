"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso. crie duas listas extras que vão conter apenas os valoras pares e os valores impares digitados.
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

numeros = []
pares = []
impares = []
resp = ""

while True:
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    resp = input("Deseja continuar? [S/N]")
    if resp in "sS":
        continue
    else:
        break

numeros.append(pares[:])
numeros.append(impares[:])
print(numeros)