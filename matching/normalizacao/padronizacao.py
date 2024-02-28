# Supondo que já realizamos a limpeza inicial

# Padronização adicional (exemplo: padronizar categorias)
categorias_padrao = {
    'eletronicos': 'Eletrônicos',
    'notebooks': 'Computadores',
    'wearables': 'Acessórios'
}

df['categoria'] = df['categoria'].apply(lambda x: categorias_padrao.get(x, x))

print(df)
