mat = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(3):
    for j in range(3):
        mat[i][j] = str(input(f"Digite o valor da posição [{i+1}, {j+1}]\n"))


for i in range(3):
    for j in range(3):
        print(f'{mat[i][j]:^5}', end = "")
    print()
