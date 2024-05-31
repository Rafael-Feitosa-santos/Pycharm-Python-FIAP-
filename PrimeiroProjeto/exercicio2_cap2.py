#Dados da viagem
valor_total = float(input("Digite o valor da viagem: "))
categoria = input("Informe o tipo de Classe: Economica = 1 , Executiva = 2 e Primeira Classe = 3: ")
quantidade_viajantes = int(input("Informe a quantidade de viajantes: "))
valor_desconto = 0

if categoria == "1":
    if quantidade_viajantes == 2:
        valor_desconto = valor_total * 0.03
    elif quantidade_viajantes == 3:
        valor_desconto = valor_total * 0.04
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_total * 0.05

elif categoria == "2":
    if quantidade_viajantes == 2:
        valor_desconto = valor_total * 0.05
    elif quantidade_viajantes == 3:
        valor_desconto = valor_total * 0.07
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_total * 0.08

elif categoria == "3":
    if quantidade_viajantes == 2:
        valor_desconto = valor_total * 0.10
    elif quantidade_viajantes == 3:
        valor_desconto = valor_total * 0.15
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_total * 0.20
else:
    print("Categoria inexistente, não será concedido nenhum desconto!")

valor_liquido = valor_total - valor_desconto
media_viajante = valor_liquido / quantidade_viajantes
print(f"O valor da viagem é de R${valor_total}. Após os descontos de R${valor_desconto}, a viagem custará R$ {valor_liquido}."
      f"Cada passageiro tem um custo médio de R${media_viajante}")



