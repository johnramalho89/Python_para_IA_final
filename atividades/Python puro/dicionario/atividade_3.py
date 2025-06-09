def invert(dicionario):
    novo_dicionario = {}

    for chave in dicionario:
        valor = dicionario[chave]
        novo_dicionario[valor] = chave

    for chave in novo_dicionario:
        dicionario[chave] = novo_dicionario[chave]

    for chave in list(dicionario):
        if isinstance(dicionario[chave], int) or isinstance(dicionario[chave], str):
            if dicionario[chave] != chave:
                del dicionario[dicionario[chave]]
                
d = {"a": 1, "b": 2, "c": 3}
invert(d)
print(d) 