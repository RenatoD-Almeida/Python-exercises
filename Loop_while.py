"""
Exercício tabuada com ciclo while
"""

print("XXX TABUADA XXX")
valor = int(input("Digite um valor para calcular a taboada:"))
i = 1

print('=' * 15)
while i <= 10:
    print(f'| {valor} x {i:2} = {i * valor:2} |')
    i += 1
print('=' * 15)

