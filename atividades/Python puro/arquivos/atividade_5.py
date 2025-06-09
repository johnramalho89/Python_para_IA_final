try:
    with open("atividades/arquivos/dados.csv", "r") as arquivo_entrada:
        with open("dados_maiores.csv", "w") as arquivo_saida:
            for linha in arquivo_entrada:
                linha = linha.replace("\n","")
                if linha:
                    partes = linha.split(",")
                    nome = partes[0]
                    idade = partes[1]
                    if len(idade) <= 3:
                        if int(idade) >= 18:
                            arquivo_saida.write(linha + "\n")
    print("Arquivo 'dados_maiores.csv' criado com sucesso.")

except FileNotFoundError:
    
    print("Arquivo 'dados.csv' não encontrado.")

except ValueError:
    print("Erro: Verifique se o arquivo está no formato 'nome,idade'.")