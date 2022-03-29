"""
Tabela de preços com Tuplas
"""

tabela = ("Frango", 13.50, "Macarrão", 2.00, "Almondegas", 7.00, "Sopa", 1.99, "Bife", 19.00)
produtos = tabela[::2]
precos = tabela[1::2]

print("=" * 30)
print(f"{'Tabela de preços':^30}")
print("=" * 30)

for i in range(len(produtos)):
    print(f'{produtos[i]:.<22}R${precos[i]:>6.2f}')
print("=" * 30)
