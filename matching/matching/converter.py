import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def dataframe_para_json(df, nome_arquivo):
    try:
        logging.info("Iniciando a conversão do DataFrame para JSON.")
        df.to_json(nome_arquivo, orient='records')
        logging.info(f"Arquivo JSON '{nome_arquivo}' foi criado com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao converter DataFrame para JSON: {e}")