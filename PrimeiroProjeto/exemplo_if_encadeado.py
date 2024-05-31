rm = input("Insira seu RM ")
idade = input("Insira a sua idade ")

if int(idade) >= 18:
    print(f"Sua participação foi autorizada, aluno de RM{rm}")
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else:
    autorizado = input("Você possui autorização dos responsáveis? S - SIM ou N - NÃO ")
    if autorizado =="S":
        print(f"Sua participação foi autorizada, aluno de RM{rm}")
        print("Mais informações serão enviadas para seu e-mail cadastrado!")
    else:
        print("Sua participação não foi autorizada por causa de idade")

