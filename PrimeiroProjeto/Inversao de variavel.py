#Esse Programa inverte os conteúdos de duas variáveis

A = input("Digite o conteúdo da variável 1:")
B = input("Digite o conteúdo da variável 2:")
troca = A
A = B
B = troca
print("Agora que trocamos, a variável A contém {} e a variável B contém {}". format(A,B))

# Podemos usar o exemplo abaixo para ter o mesmo resultado de cima
print(f"Agora que trocamos, a variável A comtém {A} e a variável B contém {B}")