#Criação da variável com um valor inicial
resposta = 0
tentativas = 3
i = 0

#Enquanto a resposta não for 42, a repetição ocorre

while (resposta != "42" and i < tentativas):

#Para cada um das repetições, o usuário vai submeter uma resposta
    resposta = input("Qual a resposta para a vida, o universo e tudo mais? ")
    i +=1

#Quanto o laço terminar, a mensagem é exibida

if resposta == "42":
    print("Parabéns, você acertou!")
else:
    print("Você excedeu o número de tentativas!")