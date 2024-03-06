import pandas as pd

def limpar_dados(df):
    df['nome'] = df['nome'].str.strip().str.lower()
    df['categoria'] = df['categoria'].str.strip().str.lower()
    return df
