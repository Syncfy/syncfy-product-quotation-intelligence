import pandas as pd

def remover_duplicatas(df):
    df_deduplicado = df.drop_duplicates(subset=['nome', 'categoria', 'preço'])
    return df_deduplicado