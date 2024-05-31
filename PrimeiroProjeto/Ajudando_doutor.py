#Solicitando os dados do aluno
email_aluno = input("Informe o e-mail do aluno")
nota_semestral = input("Informe da nota semestral do aluno: ")

#Convertendo a nota para formato float

nota_semestral = float(nota_semestral)

#Realizando o teste logico

if nota_semestral >=8.5:
    print(F"Enviando e-mail para{email_aluno}")
else:
    print("Desculpe não foi dessa vez :( ")