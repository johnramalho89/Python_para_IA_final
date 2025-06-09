
numero = int(input("Quantas vezes:"))

def mesaXadrez(tamanho):
    contador = 0
    contador2 = 0
    while contador < tamanho:
        
        while contador2 < tamanho:
            if contador2 % 2 == 0:
                linha_texto += "1"
            else:
                linha_texto += "0"
            contador2 += 1
        contador += 1
        
mesaXadrez(numero)