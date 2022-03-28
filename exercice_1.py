"""
Modulos em python

"Cria um programa
que leia um número
Real qualquer palo
taclado a mostra na
tela a sua porç ão
Inteira."

"""

from math import trunc
num = float(input("Digite um valor numérico: "))
num = trunc(num)
print(f'{num}')