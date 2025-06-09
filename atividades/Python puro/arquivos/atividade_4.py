try:
    with open("dados.txt", "r") as arquivo:
        total_linhas = 0
        for linha in arquivo:
            total_linhas += 1
        print(f"O arquivo contém {total_linhas} linha(s).")

except FileNotFoundError:
    print("O arquivo 'texto.txt' não foi encontrado.")