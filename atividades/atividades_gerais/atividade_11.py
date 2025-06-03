capital = int(input("Qual capital inicial? "))
taxa = int(input("Qual taxa de jurus? "))
tempo = int(input("Quantos anos?"))
juros = capital * (taxa / 100) * tempo
montante = capital + juros
print(f"Jurus simples: {montante}")