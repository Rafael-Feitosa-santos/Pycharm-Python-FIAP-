valor_total = float(input("Digite o valor da viagem: "))
categoria = input("Informe sua categoria: ECONOMICA, EXECUTIVA e PRIMEIRA CLASSE: ")
quantidade_viajantes = int(input("Informe a quantidade de viajantes: "))
valor_desconto = 0

if categoria.upper() == "ECONOMICA":
    if quantidade_viajantes ==2:
        valor_desconto = valor_total * 0.03
    elif quantidade_viajantes == 3:
        valor_desconto = valor_total * 0.04
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_total * 0.05

elif categoria.upper() == "EXECUTIVA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_total * 0.05
    elif quantidade_viajantes == 3:
        valor_desconto = valor_total * 0.07
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_total * 0.08

elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajantes == 2:
        valor_desconto = valor_total * 0.10
    elif quantidade_viajantes == 3:
        valor_desconto = valor_total * 0.15
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_total * 0.20
else:
    print("Categoria Inexistente")

valor_liquido = valor_total - valor_desconto
media_viajante = valor_liquido / quantidade_viajantes

print(f" O valor total da viagem é R$:{valor_total:.2f}. O valor do desconto é R$:{valor_desconto:.2f},"
          f" o valor liquido fica R$:{valor_liquido:.2f}.O valor medio por viajante é R${media_viajante:.2f}")



