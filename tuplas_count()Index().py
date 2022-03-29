"""
funções e metodos de uma tupla. (count, index)
"""

num = (int(input("Digite um valor: ")),
       int(input("Digite outro valor: ")),
       int(input("Digite mais um valor: ")),
       int(input("Digite o ultimo valor: ")))

print("\nValores digitados:")

for i in num:

       print(i,end=" ")

print("\nO valor 9 foi digitado {} vezes".format(num.count(9)))

if (num.count(3) > 0):
       print("O valor número 3 apareceu a primeira vez na posição")

print("Numeros pares digitados: ")
for i in num:
       if i % 2 == 0:
              print(f'{i}', end="")

