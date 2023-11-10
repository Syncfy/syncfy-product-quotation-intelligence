import pandas as pd
from flask import Flask, request, jsonify

excel_file_path = './Produtos.xlsx'
df = pd.read_excel(excel_file_path)

app = Flask(__name__)

@app.route('/matching', methods=['POST'])
def matching():
    data = request.json
    matched_products = match_products(df, data)
    return jsonify(matched_products)

def match_products(dataframe, request_data):
    # Extrair o nome do produto da requisição
    product_name = request_data[0].get('Camiseta básica branca')  # Assumindo que o nome do produto está na chave especificada

    if product_name is None:
        return [{"error": "Product name not provided in the request."}]

    # Realizar o matching com base no nome do produto
    matched_data = dataframe[dataframe.iloc[:, 0] == product_name]

    # Verificar se há correspondências e retornar
    if not matched_data.empty:
        # Retornar os dados correspondentes como lista de dicionários
        matched_product = {"produto": matched_data.iloc[0, 0]}  # Assumindo que você deseja apenas o primeiro resultado se houver mais de uma correspondência
        return [matched_product]
    else:
        return [{"error": "Produto não encontrado no arquivo Excel."}]



# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
