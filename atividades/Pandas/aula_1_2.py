import pandas as pd

url_filmes = "netflix_titles.csv"

df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")

#Head() e o Tail()

print("Primeiras 5 linhas do dataFrame de filmes:")
print(df_filmes.head())

#Tail
print("\n Últimas 5 linhas do DataqFrame de filmes:")
print(df_filmes.tail())

#Info

print("\n Informações sobre o dataFrame")
print(df_filmes.info())

print(f"\nO dataframe de filmes tem {df_filmes.shape[0]} e colunas {df_filmes.shape[1]}")

#Describe
#Gera estatística do Data Frame

print("estatística descritiva do dataframe:")
print(df_filmes.describe())

#index
#Traz informações sobre os índices das linhas

print("Informações do índice")
print(df_filmes.index)

