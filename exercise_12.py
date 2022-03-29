"""
exercício listas.
"""


tabela = ("Flamengo - RJ", "Internacional - RS", "Atlético - MG",
          "São Paulo - SP", "Fluminense - RJ", "Grêmio - RS", "Palmeiras - SP",
          "Santos - SP", "Athletico Paranaense - PR", "Red Bull Bragantino - SP",
          "Ceará - CE", "Corinthians - SP", "Atlético - GO", "Bahia - BA", "Sport - PE",
          "Fortaleza - CE", "Vasco da Gama - RJ", "Goiás - GO", "Coritiba - PR",
          "Botafogo - RJ")

while True:
    print("=" * 30)
    print("{:^30}".format(("Menu")))
    print("=" * 30)
    print("1 - Mostrar todos \n"
          "2 - Ultimos colocados \n"
          "3 - Times em ordem alfabetica \n"
          "4 - Sair")
    print("=" * 30)
    op = int(input("Opção: "))

    if (op == 1):
        print('=-=' * 20)
        print("{:^60}".format(("Tabela do brasileirão")))
        print('=-=' * 20)
        print(f'{"Times":^30}{"Colocação":^30}')
        print('=' * 60)
        for i, v in enumerate(tabela):
            print(f'{v:^30}{i + 1:^30}')
        print('=' * 60)
        op1 = int(input("Deseja continuar? [1 / 0]: "))
        if op1 == 1:
            pass
        else:
            break

    elif (op == 2):
        print('=-=' * 20)
        print("{:^60}".format(("Ultimos colocados")))
        print('=-=' * 20)
        print(f'{"Times":^30}{"Colocação":^30}')
        print('=' * 60)
        for i, v in enumerate(tabela[16:]):
            print(f'{v:^30}{i + 16:^30}')
        print('=' * 60)
        op1 = int(input("Deseja continuar? [1 / 0]: "))
        if op1 == 1:
            pass
        else:
            break

    elif (op == 3):
        print('=-=' * 20)
        print("{:^60}".format(("Ordem Alfabética")))
        print('=-=' * 20)
        print(f'{"Times":^30}{"Colocação":^30}')
        print('=' * 60)
        tabelaOrganizada = sorted(tabela)
        for i in range (0, len(tabela)):
            for j in range(0, len(tabelaOrganizada)):
                if tabela[i] == tabelaOrganizada[j]:
                    print("{:^30}{:^30}".format(tabelaOrganizada[j], j+1))
        op1 = int(input("Deseja continuar? [1 / 0]: "))
        print('=' * 60)
        if op1 == 1:
            pass
        else:
            break

    elif(op == 4):
        break

    else:
        print("0pção Inválida")





