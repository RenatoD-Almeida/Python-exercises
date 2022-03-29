"""
Joguinho de advinhar
"""

palavra_secreta = "divino"
digitadas = list()
tentativas = 5



while True:

    print("=" * 50)
    print(f"{'Jogo da forca':^50}")
    print("=" * 50)
    print("{}: {} letras.{:>27}: {}".format(("Palavra"), (len(palavra_secreta)), ("Tentativas"), (tentativas)))


    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Não vale, apenas uma letra.")
        continue
    else:
        digitadas.append(letra)

    if letra in palavra_secreta:
        print("Acertou mizerávi")
    else:
        print("Não foi dessa vez!")
        tentativas -= 1
        digitadas.pop()

    if tentativas < 1:
        print("Você perdeu!!!")
        break

    palavra_resultado = ""
    for i in palavra_secreta:
        if i in digitadas:
            palavra_resultado += i
        else:
            palavra_resultado += "*"
    print(f'Status da palavra: {palavra_resultado}')
