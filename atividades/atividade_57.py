texto = input("Digite uma frase ou palavra: ")

if len(texto) < 20:
    asteriscos = "*" * (20 - len(texto))
    resultado = asteriscos + texto
else:
    resultado = texto[:20]

print("Resultado formatado:", resultado)