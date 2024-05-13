import pandas as pd
import unicodedata
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def limparEPadronizarDados(dados):
    logging.info("Iniciando a limpeza e padronização dos dados.")

    dados['name'] = dados['name'].str.lower().str.strip()
    dados['name'] = dados['name'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII'))
    logging.info("Dados da coluna 'name' limpos e padronizados.")

    dados['main_category'] = dados['main_category'].str.lower().str.strip()
    dados['main_category'] = dados['main_category'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII'))
    logging.info("Dados da coluna 'main_category' limpos e padronizados.")

    dados['sub_category'] = dados['sub_category'].str.lower().str.strip()
    dados['sub_category'] = dados['sub_category'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII'))
    logging.info("Dados da coluna 'sub_category' limpos e padronizados.")

    logging.info("Limpeza e padronização dos dados concluída.")
    return dados

def removerDuplicatas(df):
    linhas_antes = len(df)
    logging.info(f"Total de linhas antes da remoção de duplicatas: {linhas_antes}")
    df_deduplicado = df.drop_duplicates(subset=['name', 'main_category', 'sub_category', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price'])
    linhas_depois = len(df_deduplicado)
    logging.info(f"Total de linhas após a remoção de duplicatas: {linhas_depois}")
    duplicatas_removidas = linhas_antes - linhas_depois
    logging.info(f"Duplicatas removidas: {duplicatas_removidas}")
    return df_deduplicado