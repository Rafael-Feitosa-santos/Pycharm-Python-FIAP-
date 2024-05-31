#Esse programa calcula a velocidade média de um patinete

#Primeiro vamos pedir a distância e o tempo
distancia = input("Qual foi a distáncia em metro percorrida pelo patinete?")
tempo = input("Quantos minuntos o patinete demorou para percorrer essa distância?")

#Realizando o cálculo
velocidade_media = float(distancia) / float(tempo)

#Exibindo o resultado
print("O patinete atingiu uma velocidade de {0:.2f} km/h".format(velocidade_media))

# Podemos usar o exemplo abaixo para ter o mesmo resultado de cima
print(f"O patinete atingiu uma velocidade de {velocidade_media:.2f} km/h")