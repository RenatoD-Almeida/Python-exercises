"""
funções

Faça um programa
que tenha uma Função
chamada cabecalho).
que receba um texto
qualquer como
parâmatro a mostra
uma mansagam com
tamanho adaptával.
"""


def cabecalho(msg):
    print("=" * (len(msg)+8))
    print(msg.center(len(msg)+8))
    print("=" * (len(msg)+8))


