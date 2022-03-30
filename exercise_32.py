"""
1 - Crie uma função1 que recebe uma função2
como parâmetro e retorne o valor da função2
executada. Faça a função1 executar duas funções
que recebam um número diferente de argumentos.

"""
from ex061 import cabecalho

def soma(n, n1, n2):
    return n1 + n + n2


def master(funcao, *args,  **kwargs):
    return funcao(*args,  **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


print(master(soma, 10, 20, 30))
print(master(fala_oi, "Renato"))

cabecalho("Testando neste programaaa")


