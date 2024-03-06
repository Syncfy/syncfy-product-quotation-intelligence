import pandas as pd

def padronizar_categorias(df):
    categorias_padrao = {
        'eletronicos': 'Eletrônicos',
        'notebooks': 'Computadores',
        'wearables': 'Acessórios'
    }
    df['categoria'] = df['categoria'].apply(lambda x: categorias_padrao.get(x, x))
    return df

