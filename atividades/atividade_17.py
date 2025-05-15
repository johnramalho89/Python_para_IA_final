nome = input("Qual seu nome? ")

if nome != "jerry":
    porcao = int(input("Quantidade de Porção que consumiu: "))
    total = porcao * 5.90
    print(f"Total: {total}")

else:
    print("Você é Jerry, ta tudo pago")

    
