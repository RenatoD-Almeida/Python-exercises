"""
tuplas

Crie um programa
que tenha uma tupla
totalmente
preenchida com uma
contagem por
extanso, da zero até
vinte.
Seu programa daverá
ler um número pelo
teclado (entre O a 20)
e mostrá-lo por
extenso.

"""
num1 = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
num2 = ("Um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    verif = int(input("Digite um numero entre 1 e 20: "))
    if verif < 1 or verif > 20:
        input("Numero invalido, Enter para continuar...")
    else:
        for i in range(0, len(num1)):
            if verif == num1[i]:
                print(f'Você digitou o número {num2[i]}')

