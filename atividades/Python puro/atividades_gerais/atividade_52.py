import random

numero_secreto = random.randint(1, 100)

numeroDeVezes = 0

while True:
    tentativa = int(input("Adivinhe o número (entre 1 e 100): "))
    numeroDeVezes += 1

    if tentativa < numero_secreto:
        print("O número é maior.")
    elif tentativa > numero_secreto:
        print("O número é menor.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {numeroDeVezes} tentativa(s).")
        break
