bpm = int(input("Digite sua frequência cardíaca: "))
idade = int(input("Digite a sua idade: "))

if idade <= 2 and bpm >= 120 and bpm <= 140:
    print("Batimento dentro do normal!")

elif idade >= 8 and idade <= 17 and bpm >= 80 and bpm <= 100:
    print("Batimento dentro do normal!")

elif idade >=18 and idade <=65 and bpm >= 70 and bpm <=80:
    print("Batimento dentro do normal!")

elif idade >=66 and bpm >= 50 and bpm <=60:
    print("Batimento dentro do normal!")

else:
    print("CUIDADE: Frequência cardíaca fora do normal!!")
