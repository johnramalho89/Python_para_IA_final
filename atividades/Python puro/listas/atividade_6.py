def eliminar_duplicados():
    numeros = []
    while len(numeros) < 10:
       
            num = int(input(f"Digite o {len(numeros)+1}º número: "))
            numeros.append(num)
    unicos = []
    repetidos = []
    i = 0
    while i < len(numeros):
        if numeros[i] not in unicos:
            unicos.append(numeros[i])
        else:
            repetidos.append(numeros[i])
        i += 1

    print("Números únicos:", unicos)
    print("Números:", numeros)
    print("Números Repetidos:", repetidos)
eliminar_duplicados()