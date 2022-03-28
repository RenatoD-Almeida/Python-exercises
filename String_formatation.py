"""
Formatação de string
"""

nome = "Renato"
idade = 22
anoNasc = 2022

# print(f'{"nome:":<10}{nome}\n{"idade:":<10}{idade}\n{"ano:":<10}{anoAtual}')

# print("{:<10}{:<10}{}".format(("Nome"), ("Idade"), ("Data nascimento")))
# print("-=" * 19)
# print(f"{nome:<10}{idade:<10}{anoNasc}")

print(f'{"Nome":<6}{"Idade":^15}{"data_nascimento":^15}')
print("=" * 35)
print(f'{nome}{idade:^15}{anoNasc:^15}')