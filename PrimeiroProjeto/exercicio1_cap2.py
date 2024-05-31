bpm = int(input("Informe o valor do BPM: "))
idade = int(input("Informe a sua idade: "))

if (bpm >= 120 and bpm <= 140) and idade <= 2:
    print("Frequência normal para idade")

elif (bpm >= 80 and bpm <= 100) and idade >= 8 and idade <= 17:
    print("Frequência normal para idade")

elif (bpm >= 70 and bpm <= 80) and idade >= 18 and idade <= 65:
    print("Frequência normal para idade")

elif (bpm >= 50 and bpm <=60) and idade >=66:
    print("Frequência normal para idade")

else:
    print("CUIDADO: Frequência fora do normal!")