"""
Exercício condicionais

Escreva um
programa que leia a
valocidade de um
carro.
Se ela ultrapassar
80Km/h.mostre uma
mensagem dizendo
qua ela foi multado.
A multa vai custar
RS7.00 por cada Km
acima do limite.

"""

print("{:^50}".format("Calculadora de multa"))
velocidade = float(input("Digite a velocidade do carro na hora da multa.(em Km/h)\n-> "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado, o valor da multa será de R${:.2f}".format(multa))
else:
    print("Você não foi multado, o valor a ser pago é de R$300.00") # brincadeira saudável
