from itertools import product

combinacao = "ABCDABCDABCDABCABDCBADCABCBA"

combinacaoSet = sorted(set(combinacao))

combinacaoDic = {}

for i in combinacaoSet:
    for k in combinacaoSet:
        combinacaoDic.setdefault(i+k, 0)

for k in range(0 ,len(combinacao)-1):
    combinacaoDic[combinacao[k]+combinacao[k+1]] += 1

print(combinacaoDic)

# ==========================================


def separa2(string):
    x = {}
    for i in range(0, len(string) - 1, 2):
        x.setdefault(string[i] + string[i+1], 0)
        x[string[i] + string[i+1]] += 1
    return x


combinacao = "ABCDABCDABCDABCABDCBADCABCBA"
teste = separa2(combinacao)
print(teste)










