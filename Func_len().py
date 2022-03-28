"""
Trabalhando a função len
"""

nome = input('Digite um nome com pelo menos 6 caracteres:\n')

if len(nome) > 6:
    print("Nome invalido")
else:
    print("Nome aprovado, {}".format(nome))

    