

def adicionar_entrada_diario():
    data = input("Digite a data: ")

    descricao = input("Digite a descrição da entrada do diário:\n")

    entrada = {
        "data": data,
        "descricao": descricao
    }

    with open("diario.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(str(entrada) + "\n")

    print("Entrada adicionada com sucesso!")
    
adicionar_entrada_diario()