import pandas as pd

# Exemplo de criação de um DataFrame com dados fictícios
dados = {
    'nome': ['Smartphone XYZ 64GB ', ' Notebook ABC 15\' ', 'Smartwatch DEF ', 'Smartphone XYZ 64GB'],
    'categoria': ['Eletronicos ', ' Notebooks', 'Wearables', 'eletronicos'],
    'preço': [999.99, 2499.99, 199.99, 999.99]
}

df = pd.DataFrame(dados)

# Limpeza de dados
df['nome'] = df['nome'].str.strip().str.lower()
df['categoria'] = df['categoria'].str.strip().str.lower()

print(df)
