"""
Exercício lista

Faça um programa que leia 5 valoras numéricos e guarde-os em uma lista. No Final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lista = list()

for i in range(5):
    a = int(input(f"Digite o {i+1}° valor: "))
    lista.append(a)

print('='*30)
print(f" Maior valor:{max(lista):>15}")
print(f" Menor valor:{min(lista):>15}")
print('='*30)
print(f'posição do maior valor: {lista.index(max(lista)):>4}')
print(f'posição do maior valor: {lista.index(min(lista)):>4}')
print('='*30)
