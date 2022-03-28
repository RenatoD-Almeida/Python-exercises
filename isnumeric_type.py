"""
Testando funções isnumeric junto com type.
"""

# print("Olá, mundo") comando CNTL + / comenta automaticamente a linha

a = input("Digite um valor:")
print(type(a))

if a.isnumeric():
    a = int(a)
else:
    print("Esse valor nao é numerico.")
    a = 0

b = input('digite um outro valor:')
print(type(b))

if b.isnumeric():
    b = int(b)
else:
    print('esse valor nao é numerico')
    b = 0

print(f'A soma entre {a} e {b} é igual a {a+b}')