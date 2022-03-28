"""
Verificando os tipos primitivos
"""

n1 = int(input("Digite um valor: "))
print(type(n1))

n2 = str(input("Digite um valor: "))
print(f'O tipo primitivo desse {n2} é {type(n2)}')

n2 = int(n2) #  Só funciona se for um número.

print(f'a soma entre {n1} e {n2} vale {n1+n2}')