
texto = input("Digite um texto: ")
try:
    with open("saida.txt", "w") as arquivo:
        arquivo.write(texto)
    print("Texto salvo com sucesso no arquivo 'saida.txt'.")
except Exception as erro:
    print("Ocorreu um erro ao salvar o arquivo:", erro)
