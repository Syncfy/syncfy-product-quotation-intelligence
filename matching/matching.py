import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def carregar_descricoes_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        produtos = json.load(file)
    descricoes = [produto['nome'] for produto in produtos]
    return descricoes

# Função para buscar produtos com base em uma query
def buscar_produtos_from_json(json_file_path, query):
    descricoes = carregar_descricoes_from_json(json_file_path)

    # Vetorização das descrições dos produtos
    vectorizer = TfidfVectorizer()
    produtos_tfidf = vectorizer.fit_transform(descricoes)

    # Vetorização da query
    query_tfidf = vectorizer.transform([query])

    # Cálculo da similaridade do cosseno entre a query e os produtos
    similaridade = cosine_similarity(query_tfidf, produtos_tfidf).flatten()

    # Filtragem dos produtos com score maior que 0
    resultados = [(descricoes[i], similaridade[i]) for i in range(len(descricoes)) if similaridade[i] > 0]
    return resultados

if __name__ == "__main__":
    # Exemplo de busca
    json_file_path = 'produtos_simulados.json'
    query = "smartphone"
    resultados = buscar_produtos_from_json(json_file_path, query)

    # Exibindo os resultados
    for produto, score in resultados:
        print(f"Produto: {produto}, Score: {score:.4f}")
