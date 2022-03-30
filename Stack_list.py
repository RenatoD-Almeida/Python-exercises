conta = input("Digite uma expressão matemática\n")
pilha = []

for i in conta:
    if i == "(":
        pilha.append("(")
    elif i == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")

if pilha in "(":
    print("Houve mais parentenses abertos do que fechados")
else:
    print("Há uma quantidade iguais de parênteses")

if pilha in ")":
    print("Houve mais parenteses fechados do que abertos")
else:
    print("Há uma  quantidade iguais de parenteses")