import pandas as pd
import logging

from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, request
from flask_cors import CORS
from coletores.DataSetToDataFrame import criarDataFrame
from enriquecimento.categorizador import categorizador
from indexacao.indexacao import treinar_e_avaliar_modelo
from matching.converter import dataframe_para_json
from matching.matching import matching
from normalizacao.normalizacao import limparEPadronizarDados, removerDuplicatas

app = Flask(__name__)
CORS(app)

handler = RotatingFileHandler('api.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

prepared_data = None

def prepare_data():
    global prepared_data
    diretorio = 'archive'
    df = criarDataFrame(diretorio)
    df_limpo = limparEPadronizarDados(df)
    df_final = removerDuplicatas(df_limpo)
    
    categorizador(df_final)
    treinar_e_avaliar_modelo(df_final)

    nome_arquivo_json = "products.json"
    dataframe_para_json(df_final, nome_arquivo_json)
    prepared_data = nome_arquivo_json

    # try:
    #     with open(nome_arquivo_json, 'r') as file:
    #         json_content = file.read()
    #         print(json_content)
    # except FileNotFoundError:
    #     print(f"Arquivo {nome_arquivo_json} não encontrado.")
    # except Exception as e:
    #     print(f"Erro ao ler o arquivo {nome_arquivo_json}: {e}")


@app.route('/busca', methods=['GET'])
def api_matching():
    global prepared_data
    query = request.args.get('query', default='', type=str)
    app.logger.info(f"Query recebida: {query}")

    if query and prepared_data:
        produtos_encontrados = matching(prepared_data, query)
        return jsonify({"produtosEncontrados": produtos_encontrados}), 200
    elif not query:
        return jsonify({"error": "Query não fornecida."}), 400
    else:
        return jsonify({"error": "Dados não preparados."}), 500

if __name__ == '__main__':
    prepare_data()  # Prepare data when the server starts
    app.run(debug=True)
