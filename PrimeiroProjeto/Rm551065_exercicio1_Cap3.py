# 1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria:
# um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade.
# O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado
# por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.
#Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba
# qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

#Porcentagem sobre o faturamento: Basic 30%, Silver 20%, Gold 10%, Platinum 5%


faturamento_anual = float(input("Por favor, informe o faturamento anual: "))
tipo_assinatura = input("Informe o tipo de assinatura: Basic - 1, Silver - 2, Gold - 3, Platinum - 4 ")
percentual = 0


if tipo_assinatura == "1":
    percentual = faturamento_anual * 0.30

elif tipo_assinatura == "2":
    percentual = faturamento_anual * 0.20

elif tipo_assinatura == "3":
    percentual = faturamento_anual * 0.10

elif tipo_assinatura == "4":
    percentual = faturamento_anual * 0.05

else:
    print("Tipo de assinatura inválida!!")

print(f"O valor do bonus a receber é R${percentual:.2f}")


