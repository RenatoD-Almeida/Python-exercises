"""
Listas em python,
Fatiamento
Append, insert, pop, del, clear, extend, +
min, max,
range.
"""


texto = 'valor'
lista = [1, 2, 3, 4, "acabou", "Qualquer valor", True, False] # São iteráveis

for i in lista:
    if type(i) == str:
        for j in i:
            print(j, end=" ")

print("=" * 30)

t = tuple("Testandoo") #Ambos os jeitos serão adicionados a lista/tupla, por caractere
t1 = list("Testandoo")
t1.append(list("bla bla bla")) # adiciona lista a lista t1