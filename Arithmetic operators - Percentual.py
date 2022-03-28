"""
Trabalhando com porcentagem, de diferentes maneiras
"""

valor = float(input('Digite o valor da compra: '))
porc = float(input('Digite o valor da porcentagem: '))

print(f'\nvalor = R${valor:.2f}')
print(f'{porc}% de desconto = {valor*(1-(porc/100))}')

# porc /= 100
# print(f'{porc}% de desconto = {valor*(1-porc)}')

# desconto = 1 - porc/100
# print(f'{porc}% de desconto = {valor * desconto}')

# desconto = valor - (valor * porc)/100
# print(f'{porc}% de desconto = {desconto}')


print(f'\nvalor = R${valor:.2f}')
print(f'{porc}% de acréscimo = {valor*(1+(porc/100))}')

