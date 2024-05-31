voto1 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")
voto2 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")
voto3 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")
voto4 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")
voto5 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")

#Variaveis
Playstation = 0
Xbox = 0
Nintendo = 0

if voto1.upper() == "PLAYSTATION":
    Playstation +=1

elif voto1.upper() == "XBOX":
    Xbox +=1

elif voto1.upper() == "NINTENDO":
    Nintendo +=1

else: print("O colaborador 1 digitou um console inexistente e seu voto será desconsiderado")

if voto2.upper() == "PLAYSTATION":
    Playstation +=1

elif voto2.upper() == "XBOX":
    Xbox +=1

elif voto2.upper() == "NINTENDO":
    Nintendo +=1

else: print("O colaborador 2 digitou um console inexistente e seu voto será desconsiderado")

if voto3.upper() == "PLAYSTATION":
    Playstation +=1

elif voto3.upper() == "XBOX":
    Xbox +=1

elif voto3.upper() == "NINTENDO":
    Nintendo +=1

else: print("O colaborador 3 digitou um console inexistente e seu voto será desconsiderado")

if voto4.upper() == "PLAYSTATION":
    Playstation +=1

elif voto4.upper() == "XBOX":
    Xbox +=1

elif voto4.upper() == "NINTENDO":
    Nintendo +=1

else: print("O colaborador 4 digitou um console inexistente e seu voto será desconsiderado")

if voto5.upper() == "PLAYSTATION":
    Playstation +=1

elif voto5.upper() == "XBOX":
    Xbox +=1

elif voto5.upper() == "NINTENDO":
    Nintendo +=1

else: print("O colaborador 5 digitou um console inexistente e seu voto será desconsiderado")

if Playstation > Xbox and Playstation > Nintendo:
    print("O console escolhido foi Playstation")

elif Xbox > Playstation and Xbox > Nintendo:
    print("O console escolhido foi Xbox")

elif Nintendo > Playstation and Nintendo > Xbox:
    print("O console escolhido foi Nintendo")

else:
    print("Houve empate, favor entrar em contato com a direção")
