import math
#solicitando os valores A,B e C
a = float(input("Informe o valor de A "))
b = float(input("Informe o valor de B "))
c = float(input("Informe o valor de C "))
#Cálculo do delta
delta = b * b - 4 * a * c
#verificação das condições com if encadeado
if delta >0.0:
    #Cálculo de 2 valores para x
    x1= (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Para a equação {a}x² + {b}x + {c} = 0, obtivemos o seguintes valores: x1{x1} e x2 = {x1}")
elif delta == 0.0:
    #Cálculo de 1 valor para x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Para a equação {a}x² + {b}x + {c} = 0, obtivemos o seguinte valor: x = {x} ")
else:
    #Exibição da mensagem
    print(f"Para equação {a}x² + {b}x + {c} = 0, não existem valores reais para x")
