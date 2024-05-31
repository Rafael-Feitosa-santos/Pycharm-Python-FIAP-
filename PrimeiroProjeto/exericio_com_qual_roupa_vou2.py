#Solicitando os dados do cliente
valor_compra = input("Informe o valor da compra realizada: ")
cupom = input("Digite o cupom de desconto: ")

#Realizando o teste logico com o cupom em maisculas
if cupom.upper() == "NIVER10":

#Calculo de 10% de desconto
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")

#Exibindo o valor final da compra

print(f"Valor final da compra é {valor_final}")