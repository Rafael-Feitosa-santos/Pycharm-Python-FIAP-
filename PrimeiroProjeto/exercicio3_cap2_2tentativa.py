membro1 = input("Vote no console que deseja ganhar: PLAYSTATION, XBOX e NINTENDO: ")
membro2 = input("Vote no console que deseja ganhar: PLAYSTATION, XBOX e NINTENDO: ")
membro3 = input("Vote no console que deseja ganhar: PLAYSTATION, XBOX e NINTENDO: ")
membro4 = input("Vote no console que deseja ganhar: PLAYSTATION, XBOX e NINTENDO: ")
membro5 = input("Vote no console que deseja ganhar: PLAYSTATION, XBOX e NINTENDO: ")

#Variáveis
Playstation = 0
Xbox = 0
Nintendo = 0

if membro1.upper() == "PLAYSTATION":
    Playstation += 1

elif membro1.upper() =="XBOX":
    Xbox +=1

elif membro1.upper() == "NINTENDO":
    Nintendo +=1

else:
    print("O membro 1 digitou um console inexistente, será desconsiderado")

if membro2.upper() == "PLAYSTATION":
    Playstation += 1

elif membro2.upper() == "XBOX":
    Xbox += 1

elif membro2.upper() == "NINTENDO":
    Nintendo += 1

else:
    print("O membro 2 digitou um console inexistente, será desconsiderado")

if membro3.upper() == "PLAYSTATION":
    Playstation += 1

elif membro3.upper() == "XBOX":
    Xbox += 1

elif membro3.upper() == "NINTENDO":
    Nintendo += 1

else:
    print("O membro 3 digitou um console inexistente, será desconsiderado")

if membro4.upper() == "PLAYSTATION":
    Playstation += 1

elif membro4.upper() == "XBOX":
    Xbox += 1

elif membro4.upper() == "NINTENDO":
    Nintendo += 1

else:
    print("O membro 4 digitou um console inexistente, será desconsiderado")

if membro5.upper() == "PLAYSTATION":
    Playstation += 1

elif membro5.upper() == "XBOX":
    Xbox += 1

elif membro5.upper() == "NINTENDO":
    Nintendo += 1

else:
    print("O membro 5 digitou um console inexistente, será desconsiderado")

if Playstation > Xbox and Playstation > Nintendo:
    print("O Console escolhido foi Playstation")

elif Xbox > Playstation and Xbox > Nintendo:
    print("O Console escolhido foi Xbox")

elif Nintendo > Xbox and Nintendo > Playstation:
    print("O Console escolhido foi Nintendo")

else:
    print("Houve empate, acionar a direção")
