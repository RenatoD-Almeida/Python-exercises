"""
Crie um programa que leia nome.
sexo e idade de várias pessoas.
guardando os dados de cada pessoa
em um dicionário e todos os dicionários
Dentro de uma lista; No final. mostre:

A) Quantas passoas
cadastradas

B) A média de idada.

C) Uma lista com
mulheras.

"""

listaMulheres = []
listaPessoas = list()
pessoas = dict()
mediaIdade = totalCad = totalF = 0
resp = ""

while True:
    pessoas["Nome"] = input("Nome: ")

    while True:
        pessoas["Sexo"] = input("Sexo [M/F]: ").upper()

        if len(pessoas["Sexo"]) != 1 or pessoas["Sexo"] not in "MmFf":
            print("Inválido, Apenas \'M\' ou \'F\'")
            continue
        else:
            if pessoas["Sexo"] in "fF":
                totalF += 1
            break

    while True:
        pessoas["Idade"] = input("Idade: ")
        if pessoas["Idade"].isnumeric():
            pessoas["Idade"] = int(pessoas["Idade"])
            mediaIdade += pessoas["Idade"]
            break
        else:
            print("Apenas valores numéricos. Tente novamente")

    if pessoas["Sexo"] == "F":
        listaMulheres.append(pessoas.copy())

    listaPessoas.append(pessoas.copy())
    totalCad += 1
    resp = input("Deseja continuar? [S / N]\n").strip().upper()[0]

    if resp in "N":
        mediaIdade /= totalCad
        break

print(f'{totalCad} pessoas foram cadastradas: ')
print(f'{mediaIdade} é a media de idades cadastradas ')

for i in listaPessoas:
    print("~" * 30)
    for k in i.keys():
        print(f'{k}: {i[k]}'.center(30))
print("~" * 30)


print(f'{totalF} mulheres foram cadastradas, e são elas:')

for i in listaMulheres:
    for k in i.keys():
        print(f'{k}: {i[k]}')
    print("~" * 30)




