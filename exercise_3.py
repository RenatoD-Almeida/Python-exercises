"""
Modulo em python

Faça um programa
que leia um ângulo
qualquer a mostra na
tela o valor do seno.
cosseno a tangenta
dasse ângulo.

"""

from math import cos, sin, tan, radians

angulo = float(input("Digite um ângulo: "))

print("=-" * 15)
print(f"Angulo: {angulo:>20}°")
print(f"Angulo em radianos: {radians(angulo):>8.2f}°R")
print(f'\nSeno:{sin(radians(angulo)):23.2f}')
print(f'Cosseno:{cos(radians(angulo)):20.2f}')
print(f'Tangente:{tan(radians(angulo)):19.2f}')
print("=-" * 15)
