"""
Dissecando string
"""
algo = input('Digite algo:')

if algo.isnumeric():
    print('é um valor numérico')
elif(algo.isalpha()):
    print("é um valor Alfabético")
elif(algo.isalnum()):
    print('é um valor alfa-numérico')
elif(algo.isspace()):
    print('É apenas espaço')

if(algo.islower()):
    print('Texto escrito em minúsculo')
elif(algo.isupper()):
    print('Texto escrito em maiúsculo')
elif(algo.istitle()):
    print("Texto capitalizado")
else:
    print('Nenhuma formatação encontrada')