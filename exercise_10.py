"""
Desenvolva um
programa que
pargunte a distância
de uma viagam em Km.
Calcule o preso da
passagam, cobrando
RS0.50 por Km para
viagans da atể 200Km
e R$0.45 para viagens
mais longas.
"""

distancia = float(input("Digite a Quilometragem de sua viagem: "))
if distancia <= 200:
    total = distancia * 0.5
    print("Total a pagar R${:.2f}, com R$0.50 por km".format(total))
else:
    total = distancia * 0.45
    print("Total a pagar R${:.2f}, com R$0.45 por km".format(total))
