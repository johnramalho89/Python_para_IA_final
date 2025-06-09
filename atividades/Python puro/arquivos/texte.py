with open("atividades/arquivos/pessoas.csv") as novo_arquivo:
    for linha in novo_arquivo:
        # Remove o caractere de quebra de linha (\n) do final de cada linha, para evitar problemas ao dividir ou imprimir.
        linha = linha.replace("\n", "")
        # O Split vai procurar todos os ; na string e cortar a string nesses pontos, criando uma lista com os pedaços:
        partes = linha.split(";")
        # Pega o primeiro item da lista, que representa o nome da pessoa
        nome = partes[0]
        # Pega todos os itens a partir da segunda posição da lista. Representam as notas dessa pessoa.
        notas = partes[1:]
        print("Nome:", nome)
        print("Notas:", notas)
