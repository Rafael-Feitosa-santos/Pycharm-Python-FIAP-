valor_compra = float(input("Digite o valor da compra: "))
forma_pagamento = int(input("1 - Dinheiro/ 2 - Cartão"))

if valor_compra >=100 and forma_pagamento == 1:
    valor_compra = valor_compra * 0.09
    print("Você tem direito a um desconto!")

print(f"O valor a pagar é {valor_compra}")
