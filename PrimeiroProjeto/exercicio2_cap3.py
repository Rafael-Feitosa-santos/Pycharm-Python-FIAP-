total_transacoes = int(input("Informe a quantidade de transações realizada no dia: "))
valor_total = 0

for transacoes in range(1,total_transacoes + 1):
    valores = float(input(f"Informe os valores das operações {transacoes}º: "))
    valor_total = valor_total + valores

media_de_valores = valor_total / total_transacoes
print(f"O valor total de transações é R$ {valor_total:.2f}. A média de cada operação é R$ {media_de_valores:.2f}")
