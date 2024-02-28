import pandas as pd
from flask import Flask, request, jsonify

excel_file_path = './Produtos.xlsx'
df = pd.read_excel(excel_file_path)

app = Flask(__name__)

@app.route('/matching', methods=['POST'])
def matching():
    data = request.json
    product_name = data.get('produto')
    user_description = data.get('descricao', '')

    if product_name is None:
        return jsonify({"error": "Product name not provided in the request."})

    matched_products = match_products(df, product_name, user_description)
    return jsonify(matched_products)

def match_products(dataframe, product_name, user_description):
    # Inicializar a lista de produtos correspondentes
    matched_products = []

    # Iterar sobre todas as linhas do DataFrame
    for _, row in dataframe.iterrows():
        produto = row.iloc[0]
        descricao = row.iloc[1] if len(row) > 1 else ""  # Verificar se há uma coluna de descrição

        # Verificar se o nome do produto está presente na coluna de produto
        # e se a descrição fornecida pelo usuário está parcialmente contida na descrição do produto
        if product_name.lower() in produto.lower() and user_description.lower() in descricao.lower():
            matched_product = {"produto": produto, "descricao": descricao}
            matched_products.append(matched_product)

    # Verificar se foram encontrados produtos e retornar
    if matched_products:
        return matched_products
    else:
        return [{"error": f"Nenhuma correspondência encontrada para '{product_name}' com a descrição '{user_description}' no arquivo Excel."}]

if __name__ == '__main__':
    app.run(debug=True)
