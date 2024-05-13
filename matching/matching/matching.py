import json
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def carregar_produtos_from_json(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            produtos = json.load(file)
        logging.info("Produtos carregados com sucesso do arquivo JSON.")
        return produtos
    except Exception as e:
        logging.error(f"Erro ao carregar o arquivo JSON: {e}")
        return []

def buscar_produtos_por_query(produtos, query):
    vectorizer = TfidfVectorizer()
    names = [produto['name'] for produto in produtos]
    produtos_tfidf = vectorizer.fit_transform(names)
    query_tfidf = vectorizer.transform([query])
    similaridade = cosine_similarity(query_tfidf, produtos_tfidf).flatten()
    
    resultados = []
    for i, score in enumerate(similaridade):
        if score > 0:
            produto = produtos[i]
            produto['Score'] = score
            resultados.append(produto)
    
    return resultados

def matching(arquivo_json, query):
    produtos_encontrados = []
    produtos = carregar_produtos_from_json(arquivo_json)
    if produtos:
        resultados = buscar_produtos_por_query(produtos, query)
        for produto in resultados:
            logging.info(f"Produto: {produto['name']}, Score: {produto['Score']:.4f}")
            produtos_encontrados.append(produto)
    return produtos_encontrados