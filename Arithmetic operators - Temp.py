"""
Conversão de medidas para trabalhar operadores aritméticos
"""

Celcius = float(input("Digite a temperatura desejada em C°: "))
print("\nTemperatura: {:.2f} C°".format(Celcius))
# print("Temperatura convertida: {.2f}F°".format((Celcius*1.8)+32))
F = (Celcius * 1.8) + 32
print("Temperatura convertida: {:.2f} F°".format(F))
