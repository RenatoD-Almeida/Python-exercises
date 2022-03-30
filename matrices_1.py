mat = [[],
       [],
       []]
totaldois = 0

for i in range(0, 3):
    for j in range(0, 3):
        mat[i].append(int(input("Digite o valor da posição [{}, {}]\n".format(i + 1, j + 1))))

print("= " * 10)
for i in range(3):
    for j in range(3):
        print(f"{mat[i][j]:5}", end="")
    print()
print("= " * 10)

l = int(input("Digite a linha que deseja somar: "))

for i in range(3):
        totaldois += mat[l][i]

print(f'Total da soma da segunda linha é {totaldois}')
