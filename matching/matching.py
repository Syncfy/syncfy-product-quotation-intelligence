from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Lista de descrições dos produtos
produtos = [
    "Smartphone XYZ 64GB",
    "Notebook ABC 15' Core i7",
    "Smartwatch DEF Health Tracker",
    # Adicione mais produtos conforme necessário
]

# Vetorização das descrições dos produtos
vectorizer = TfidfVectorizer()
produtos_tfidf = vectorizer.fit_transform(produtos)

# Função para buscar produtos com base em uma query
def buscar_produtos(query):
    # Vetorização da query
    query_tfidf = vectorizer.transform([query])
    
    # Cálculo da similaridade do cosseno entre a query e os produtos
    similaridade = cosine_similarity(query_tfidf, produtos_tfidf).flatten()
    
    # Ordenação dos produtos por similaridade
    indices_ordenados = similaridade.argsort()[::-1]
    
    resultados = [(produtos[i], similaridade[i]) for i in indices_ordenados]
    return resultados

# Exemplo de busca
query = "smartphone"
resultados = buscar_produtos(query)

# Exibindo os resultados
for produto, score in resultados:
    print(f"Produto: {produto}, Score: {score:.4f}")
