preco = int(input("Qual valor do preco: "))

desconto = int(input("Qual valor do desconto: "))

precoDesconto = int((preco * desconto) / 100)

precoFinal = ((100-desconto) * preco) / 100

print(f"O valor de desconto é: {precoDesconto}\n \nNovo preço: {precoFinal}")