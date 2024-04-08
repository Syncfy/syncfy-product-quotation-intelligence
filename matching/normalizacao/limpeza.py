import unicodedata

def limparEPadronizarDados(dados):
    dados['Nome'] = dados['Nome'].str.lower().str.strip()
    dados['Categoria'] = dados['Categoria'].str.lower().str.strip()
    dados['Nome'] = dados['Nome'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII'))
    dados['Categoria'] = dados['Categoria'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII'))

    return dados