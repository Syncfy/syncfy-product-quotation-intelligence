import unicodedata

def limparEPadronizarDados(dados):
    dados['nome'] = dados['nome'].str.lower().str.strip()
    dados['categoria'] = dados['categoria'].str.lower().str.strip()
    dados['nome'] = dados['nome'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII'))
    dados['categoria'] = dados['categoria'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII'))

    return dados
