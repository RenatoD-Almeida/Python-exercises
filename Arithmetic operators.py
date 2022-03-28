"""
Operadores aritméticos: Ordem de preferencia **, (), *, /, +, -
"""

print("SUCESSORES E ANTECESSORES")
n1 = input("Digite um valor:")
if n1.isnumeric():
    n1 = int(n1)
    print(f'Valor {n1}\nsucessor:{n1+1}\nantecessor:{n1-1}')
else:
    print('Esse valor não é numérico.')
