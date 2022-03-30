"""
funções


1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.

2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre
eles.

3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.


4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.

"""


def saudacao(nome, saudacao = "Olá"):
    return f'{nome}, {saudacao}'


def soma(n, n1, n2):
    return n + n1 + n2


def acrescimo(n, n1):
    n1 /= 100
    return n + (n*n1)


def desconto(n, n1):
    n1 /= 100
    return n - (n*n1)


def func(n):
    if n % 5 == 0 and n % 3 == 0:
        return "Fizz-Buzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return 'Numero inválido'


print(saudacao("Renato", "Oiii, prazer em conhecer"))
print(soma(3, 4, 5))
print(acrescimo(1000, 20))
print(desconto(100, 20))
print(func(45))

