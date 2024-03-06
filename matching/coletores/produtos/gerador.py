import pandas as pd
import numpy as np

def gerarProdutos(quantidade):
    np.random.seed(42)  # Para reprodutibilidade

    # Nomes de produtos simulados
    produtos_nomes = [
        'Smartphone XYZ 64GB', 'Notebook ABC 15\' Core i7', 'Smartwatch DEF Health Tracker',
        'Tablet GHI 10\' 128GB', 'Câmera JKL 20MP Zoom Óptico', 'Headphone MNO Bluetooth Noise Cancelling',
        'Console de Jogos PQR 1TB', 'E-reader STU 8GB Luz Integrada', 'Drone VWX Câmera 4K',
        'Impressora YZA Jato de Tinta', 'Roteador 123 Wi-Fi 6', 'Monitor 456 27\' 4K UHD', 'Teclado 789 Mecânico RGB',
        'Mouse ABC Ergonômico', 'Caixa de Som DEF Portátil Waterproof', 'Carregador GHI Veicular Turbo',
        'Fone de Ouvido JKL Intra-auricular', 'Mochila MNO para Notebook', 'Relógio Inteligente PQR com GPS',
        'Lâmpada STU Inteligente Wi-Fi', 'Aspirador de Pó VWX Robô', 'Air Fryer YZA Digital 4L',
        'Mixer 123 3 em 1 Inox', 'Ventilador 456 de Mesa Silencioso', 'Aquecedor 789 Cerâmico',
    ]

    # Categorias simuladas
    categorias = ['Eletrônicos', 'Eletrodomésticos', 'Informática', 'Acessórios', 'Periféricos']

    # Gerando dados simulados
    num_linhas = int(quantidade) # Número de linhas desejado
    dados = {
        'id': np.arange(1, num_linhas + 1),
        'nome': np.random.choice(produtos_nomes, num_linhas),
        'categoria': np.random.choice(categorias, num_linhas),
        'preço': np.round(np.random.uniform(50, 3000, num_linhas), 2)
    }

    df = pd.DataFrame(dados)

    # Salvando o JSON em um arquivo
    json_file_path = './produtos_simulados.json'
    df.to_json(json_file_path, orient='records')

    print("Arquivo JSON salvo em:", json_file_path)
    return df
    

