# Remoção de duplicatas
df_deduplicado = df.drop_duplicates(subset=['nome', 'categoria', 'preço'])

print(df_deduplicado)
