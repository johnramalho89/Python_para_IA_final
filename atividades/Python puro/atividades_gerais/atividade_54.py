while True:
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")

    if len(palavra1) == len(palavra2):
        print("São de tamanhos iguais")
        break
    else:
        print("Tamanhos diferentes")