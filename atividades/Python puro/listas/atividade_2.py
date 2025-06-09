def nomes_unicos():
    nomes = []

    while len(nomes) < 5:
        nome = input(f"Digite o {len(nomes)+1}º nome: ").strip()

        if nome in nomes:
            print("Nome já digitado. Tente outro.")
        else:
            nomes.append(nome)

    print("Nomes cadastrados:")
    for nome in nomes:
        print(nome)