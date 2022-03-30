"""
Crie um programa
que leia nome, ano de
nascimento e carteira
de trabalho e
cadastre-os (com
idade) em um dicionário
se por acaso a CTPS
for diferente de ZERO.
o dicionário receberá
também o ano de
contrataçÃO e o
salário. Calcule e
acrescente, além da
idade, com quantos
anos a passoa vai se
aposentar.
"""
from datetime import date

cadastro = {}

cadastro['nome'] = input("Digite seu nome: ")
ano_nasc = int(input("Digite o ano de nascimento: "))
cadastro['idade'] = date.today().year - ano_nasc

if cadastro['idade'] >= 18:
    cadastro['CTPS'] = int(input("Digite sua carteira de trabalho: "))

    if cadastro["CTPS"] > 0:
        cadastro['ano_contratacao'] = int(input("Digite o ano de sua contratação: "))
        cadastro['salario'] = float(input("Digite seu salário: "))
        cadastro['aposentadoria'] = (cadastro['ano_contratacao'] + 30) - ano_nasc

for k, v in cadastro.items():
    print(f'{k} é {v}')
