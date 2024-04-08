import pandas as pd

def carregar_dados_from_excel(excel_file_path):
    df = pd.read_excel(excel_file_path)
    return df