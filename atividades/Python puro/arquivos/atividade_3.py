try:
    with open("dados.txt", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("O arquivo 'entrada.txt' não foi encontrado.")