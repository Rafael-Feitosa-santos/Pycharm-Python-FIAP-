pontuacao = int(input("Insira a sua pontuação"))
if pontuacao >=1000:
    print("Você ganhou 3GB de Bônus")
else:
    if pontuacao >=500:
        print("Você ganhou 1,5GB de Bônus")
    else:
        if pontuacao >=200:
            print("Você ganhou 500mb de Bônus")
        else:
            print("O cliente não recebe Bônus!")

