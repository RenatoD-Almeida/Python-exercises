birthday = {"Alice": "Apr 1th",
            "Bob": "Dec 12th",
            "Carol": "Mar 4th"}

while True:
    name = input("Enter your name (Blank to quit)\n").title().strip()
    if name == "":
        break

    if name in birthday.keys():
        print(f'{name}\'s birthday is {birthday[name]}')
    else:
        print("No information about {}\'s birthday".format(name))
        # print(f"What is {name}\'s birthday?\n")
        bday = input(f"What is {name}\'s birthday?\n")
        birthday[name] = bday
        print('Birthday database updated.')

    resp = input("Deseja continuar? [S/N]")

    if resp in "nN":
        break

print("~" * 30)
print("Birthday's list".center(30))
print("~" * 30)

for k, v in birthday.items():
    print(f'{k:<15}{v:>15}')

