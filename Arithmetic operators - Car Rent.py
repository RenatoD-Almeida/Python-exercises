"""
Exercício aluguél de carros.
"""

print('=-' * 6, 'ALUGUEL DE CARROS', '-=' * 6)
dias = int(input('Quantos dias foi utilizado o carro?\n'))
km = float(input("Quantos kilometros foi rodado?\n"))

# total = (dias * 60) + (km * 0.15)
# print("O total a se pagar é de R${:.2f}".format(total))

print("O total a se pagar é R${}".format(((dias * 60) + (km * 0.15))))