"""

Crie um programa onde o usuário possa digitar cinco valoras
numéricos e cadastre-os em uma lista. já na posição correta
da inserção (sem usar o sort()). No final. mostra a lista
ordenada na tela.
"""

valorlista = []
cont = 0

# while cont < 5:
#     valor = int(input("Digite um valor: "))
#     if valor not in valorlista:
#         valorlista.append(valor)
#         cont += 1
#     else:
#         print("Desculpe, valor já integrado na lista.")


while cont < 5:
    valor = int(input(f"Digite {cont + 1}° valor: "))
    if cont == 0 or valor > valorlista[-1]:
        valorlista.append(valor)
        print(f"Valor adicionado na ultima posição")
    else:
        pos = 0
        while pos < len(valorlista):
            if valor <= valorlista[pos]:
                valorlista.insert(pos, valor)
                print(f"Valor adicionado na posição {pos} entre os valores {valorlista[pos - 1]} e {valorlista[pos + 1]}")
                break
            else:
                pos += 1
    cont += 1
print(valorlista)


