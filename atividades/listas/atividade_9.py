def lista_crescente():
    numeros = []

    while True:
        numero = int(input("Digite um número: "))
        numeros.append(numero)

        if len(numeros) > 1 and numeros[-1] < numeros[-2]:
            break

    numeros_ordenados = sorted(numeros)
    print("Números digitados (ordem crescente):", numeros_ordenados)
    
lista_crescente()