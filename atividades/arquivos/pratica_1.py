try:
    def numeros():
        with open("atividades/arquivos/numeros.txt") as arquivo:
            maior = 0
            for linha in arquivo:
                numero = int(linha)
                if numero > maior:
                    maior = numero
            print("Maior número:", maior)
except FileNotFoundError:
    print("Arquivo 'numeros.txt' não encontrado.")
except ValueError:
    print("Erro: o arquivo contém dados que não são números inteiros.")
    
numeros()