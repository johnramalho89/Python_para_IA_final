def frutas():
    dicionario_frutas = {}

    try:
        with open("atividades/arquivos/frutas.csv") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    dados = linha.split(";") 
                    dicionario_frutas[dados[0]] = float(dados[1])
    
    except FileNotFoundError:
        print("Arquivo 'frutas.csv' não encontrado.")
    
    except ValueError:
        print("Erro ao converter o preço para float.")
    
    return dicionario_frutas


print(frutas())