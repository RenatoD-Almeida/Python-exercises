"""
Calcule quanta tinta precisa para pintar uma parede, considere 2 metros para 1 L
"""
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

print("área = {}m²".format((altura*largura)))

tinta = (altura*largura)/2

print(f'serão necessários {tinta}L para pintar a {altura*largura}m² de parede')