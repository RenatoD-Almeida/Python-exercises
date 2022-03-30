def separa(string):
    x = {}
    for i in range(0, len(string) - 1, 2):
        x.setdefault(string[i] + string[i+1], 0)
        x[string[i] + string[i+1]] += 1
    return x

codigo = "LRVOVORLRVOLOLVRROLVVLORLVRO"

combinacao = separa(codigo)
print(combinacao)
