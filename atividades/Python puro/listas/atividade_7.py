def verificar_presenca(produtos):
    while True:
        nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

        if nome == "sair":
            print("Encerrando verificação.")
            break

        if nome in produtos:
            print("Produto disponível.")
        else:
            print("Produto não encontrado.")
            
produtos = ["mouse","bike","caneta"]
verificar_presenca(produtos)
#encerrou a verificação da lista produtos

produtos3 = ["cadeira","celular","CONTROLE"]
verificar_presenca(produtos3)
#aqui encerrou e não funciona mais

frutas = ["malancia","laranja","pera"]
verificar_presenca(frutas)