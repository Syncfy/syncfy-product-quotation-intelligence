import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def carregar_descricoes_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        produtos = json.load(file)
    descricoes = [produto['nome'] for produto in produtos]
    return descricoes

def buscar_produtos_from_json(json_file_path, query):
    descricoes = carregar_descricoes_from_json(json_file_path)

    vectorizer = TfidfVectorizer()
    produtos_tfidf = vectorizer.fit_transform(descricoes)

    query_tfidf = vectorizer.transform([query])

    similaridade = cosine_similarity(query_tfidf, produtos_tfidf).flatten()

    resultados = [(descricoes[i], similaridade[i]) for i in range(len(descricoes)) if similaridade[i] > 0]
    return resultados

if __name__ == "__main__":
    json_file_path = 'coletores/produtos/produtos_simulados.json'
    query = "iphone"
    resultados = buscar_produtos_from_json(json_file_path, query)

    for produto, score in resultados:
        print(f"Produto: {produto}, Score: {score:.4f}")
