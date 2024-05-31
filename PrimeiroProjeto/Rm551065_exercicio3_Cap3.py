#Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes.
# Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos,
# solicitou que você criasse um sistema capaz de atender ao seguinte requisito:
# o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49)
# e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50).
# O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.
# Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas,
# deve ser exibida uma mensagem no seguinte padrão:

#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.


print("\tCalculo da soma das notas e Média\n")

n_pares = 0
n_impares = 0
media_geral = 0.0

for impares in range(1,51,2):
    n_impares +=float(input(f"Inserindo as notas de alunos ÍMPARES.\nInforme a nota do aluno {impares}: "))

for pares in range(2,51,2):
    n_pares += float(input(f"Inserindo as notas de alunos PARES.\nInforme a nota do aluno {pares}: "))

if n_pares > n_impares:
    media_geral = n_pares / 25
    print(f"A média da turma PAR foi {media_geral}. Maior que a impar! ")

elif n_impares > n_pares:
    media_geral = n_impares / 25
    print(f"A média da turma IMPAR foi {media_geral}. Maior que a par! ")

else:
    media_geral = (n_impares + n_pares) / 50
    print(f"A Média da duas turmas foram {media_geral}")
