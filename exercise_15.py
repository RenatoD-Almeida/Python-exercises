email = ["asensi9222@uorak.com", "flaviu2808@uorak.com",
         "tirma5591@uorak.com", "aouicha62@uorak.com",
         "sohora176@uorak.com", "bernabe1927@uorak.com"]

telefone = ["(95) 2151-6219", "(89) 2133-4423",
            "(97) 3394-7126", "(69) 2868-3378",
            "(69) 2868-3378", "(69) 2868-3378"]

t1 = [email, telefone]

print("=-=" * 20)
print(f'{"Email:":^30}{"Telefone":^30}')

for i in range(0, len(email)):
    print(f'{email[i]:^30}{telefone[i]:^30}')


