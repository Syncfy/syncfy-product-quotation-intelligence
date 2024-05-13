import os
import pandas as pd
import logging

def criarDataFrame(diretorio):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    dados = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.csv'):
            caminho_completo = os.path.join(diretorio, arquivo)
            logging.info(f'Tentando ler o arquivo {arquivo}')
            try:
                df = pd.read_csv(caminho_completo)
                df['categoria'] = arquivo
                dados.append(df)
                logging.info(f'Arquivo {arquivo} lido com sucesso e adicionado ao dataframe.')
            except Exception as e:
                logging.error(f'Erro ao ler o arquivo {arquivo}: {e}')
    df_final = pd.concat(dados, ignore_index=True)
    logging.info('Todos os arquivos foram processados e concatenados em um único dataframe.')
    return df_final
