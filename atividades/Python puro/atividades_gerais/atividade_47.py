limite = int(input("Digite o limite superior: "))

numero = 1
base = int(input("Qual a base: "))

while numero <= limite:
    print(numero)
    numero *= base 

print(f" O limite era: {limite}")