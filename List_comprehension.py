"""
exercício list comprehension
"""

string = "01234567890123456789012345678901234567890123456789012345678901234567890123456789"

n = 10

l1 = [string[i: i + n] for i in range(0, len(string), n)]

print(l1)


"""
Escreva descrições usando listas, para as seguintes listas constantes
a) múltiplos de 5 maiores que 0 e menores que 80;
b) meses de um ano;
c) número de dias por cada mês de um ano;
d) dias da semana;
e) relação das disciplinas em que você está matriculado
"""

l1 = [x for x in range(81) if x % 5 == 0]

print(l1)

meses = [x for x in range(1, 13)]
print(meses)

dias = [30 if x % 2 == 0 else 31 for x in meses]

print(f'meses: {meses}\ndias: {dias}')