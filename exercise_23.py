"""
Cria um programa onda o usuário possa digitar sete valoras
numéricos e cadastre-os em uma lista única que mantenha
separados OS valoras paress a impares. No final. mostra
os valoras pares e impares em ordem crescente.
"""

valores = [[],[]]

i = 0

while i < 7:
    numeros = input("Digite o {}° valor: ".format(i+1))

    if numeros.isnumeric():
        numeros = int(numeros)

        if numeros % 2 == 0:
            valores[1].append(numeros)
        else:
            valores[0].append(numeros)

    else:
        print("Apenas valores numéricos")
        continue

    i += 1

print("= " * 25)
print("{:^50}".format("Números"))
print("= " * 25)
print(f"Pares: {sorted(valores[1])}")
print(f"Impares: {sorted(valores[0])}")



