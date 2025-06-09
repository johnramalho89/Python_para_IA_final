import pandas as pd

url_filmes = "netflix_titles.csv"

df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")

print("Primeiras 7 linhas do dataFrame de filmes:")
print(df_filmes.head(7))

print("\n Informações sobre o dataFrame")
print(df_filmes.info())

print(f"\nO dataframe de filmes tem {df_filmes.shape[0]} e colunas {df_filmes.shape[1]}")

print("estatística descritiva do dataframe:")
print(df_filmes.describe())


