#Variável para armazenar o peso total das caixas
peso_total = 0.0

#Loop para repetir por 100 vezes a solicitação de peso
for x in range (1,10):
    #Cada volta do loop, solicitar o peso da caixa
    peso_atual = float(input("Informe o peso da caixa: "))
    #Para cada peso solicitado, somar ao peso total
    peso_total = peso_total + peso_atual

#Ao final do loop, calcular a media aritmetica
media = peso_total / 10

#Exibição dos resultados
print(f"O peso total é {peso_total}. A média de peso é {media}")
