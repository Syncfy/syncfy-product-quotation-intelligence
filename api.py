from flask import Flask, jsonify, request
from matching.matching import matching

app = Flask(__name__)

@app.route('/matching', methods=['POST'])
def api_matching():
    data = request.get_json()
    print(f"Data recebida: {data}")
    query = data.get('query', '')
    print(f"Query recebida: {query}")
    if query:
        produtos_encontrados = matching(query)
        return jsonify({"produtosEncontrados": produtos_encontrados}), 200
    else:
        return jsonify({"error": "Query não fornecida."}), 400

if __name__ == '__main__':
    app.run(debug=True)
