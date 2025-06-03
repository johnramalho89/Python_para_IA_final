print("1")

try:
    numero = 10
    numero.append(5)  
except AttributeError:
    print("Erro: Este tipo de objeto não possui o método solicitado.")

print("2")
try:
    dados = {"nome": "João", "idade": 30}
    print(dados["altura"])  
except KeyError:
    print("Erro: Chave inexistente no dicionário.")

print("3")
try:
    import modulo_inexistente  
except ImportError:
    print("Erro: Módulo não encontrado ou inexistente.")
