pontuacao = int(input("Insira a sua pontuação"))
if pontuacao >=1000:
     print("Você ganhou 3GB de Bônus")
elif pontuacao >=500:
     print("Você ganhou 1,5GB de Bônus")
elif pontuacao >=200:
     print("Você ganhou 500mb de Bônus")
else:
     print("O cliente não recebe Bônus!")