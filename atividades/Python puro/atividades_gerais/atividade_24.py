graus = int(input("Digite a temperatura: "))
chuva = int(input("Var chover? 0 - Não, 1 - Sim: "))

if graus > 20:
    if chuva == 0:
        print("Use jeans e camiseta")
    else:
        print("Use jeans e camiseta mas leve um Guarda Chuva")
    
elif graus >= 10 and graus < 20:
    if chuva == 0:
        print("Use jeans e camiseta e leve um suéter")
    else:
        print("Use jeans e camiseta e leve um suéter. Leve Guarda-Chuva")
        
elif graus >= 5 and graus < 10:
    if chuva == 0:
        print("Eta Pega!! Frio da peste! Não saia de casa")
    else:
        print("Não saia! Frio do Djanho e Muita chuva")
else:
    print("Nem pense! Durma")

