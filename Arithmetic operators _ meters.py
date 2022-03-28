"""
trabalhando com operadores aritméticos
"""

metro = float(input("Digite um valor: "))

print('=-'* 26)
print("|  km  |  hm  |  dam  |   m   |  dm  |  cm  |  mm  |")
print('=-'* 26)
print(f"Km = {metro/1000}")
print(f"hm = {metro/100}")
print(f"dam = {metro/10}")
print(f"m = {metro}")
print(f"dm = {metro*10}")
print(f"cm = {metro*100}")
print(f"mm = {metro*1000}")
