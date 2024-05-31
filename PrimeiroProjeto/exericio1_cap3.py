total_alimentos = int(input("Digite o total de alimentos consumidos hoje: "))
total_calorias = 0

for alimento in range(1,total_alimentos + 1):
    caloria = int(input(f"Informe a quantidade calorias do {alimento}º alimentos "))
    total_calorias = total_calorias + caloria

print(f"Foram consumidas {total_calorias} calorias ao longo do dia")