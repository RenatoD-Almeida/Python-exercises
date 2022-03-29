"""
modulos em python

"Faça um programa
que laia o comprimento
do cateto oposto e do
cateto adjacente do
triângulo ratângulo.
calcule e mostre o
comprimento da hipo-
tenusa."

"""

from math import sqrt
print("-" * 5, "TRIÂNGULO RETÂNGULO", "-" * 5)
catOp = float(input("Digite o valor do cateto oposto: "))
catAd = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = pow(catOp, 2) + pow(catAd, 2)

print(f'{sqrt(hipotenusa)}')

