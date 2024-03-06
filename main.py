import pandas as pd
from limpeza import limpar_dados
from padronizacao import padronizar_categorias
from desduplicacao import remover_duplicatas
from categorizacao import categorizador
from extracao import extrair_atributos

def main():
    dados = {
        'nome': ['Smartphone XYZ 64GB ', ' Notebook ABC 15\' ', 'Smartwatch DEF ', 'Smartphone XYZ 64GB'],
        'categoria': ['Eletronicos ', ' Notebooks', 'Wearables', 'eletronicos'],
        'preço': [999.99, 2499.99, 199.99, 999.99]
    }

    try:
        df = pd.DataFrame(dados)
        df = limpar_dados(df)
        df = padronizar_categorias(df)
        df = remover_duplicatas(df)
        print("Dados finais após normalização:")
        print(df)
        # Treinamento e avaliação do modelo de categorização
        categorizador(data)
        # Extração de atributos
        extrair_atributos(descricao)
    except Exception as e:
        print(f"Erro durante a execução do processo de normalização: {e}")

if __name__ == "__main__":
    main()
