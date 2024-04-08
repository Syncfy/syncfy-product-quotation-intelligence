import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from matching.coletores.coletorExcel import carregar_dados_from_excel
from matching.normalizacao.limpeza import limparEPadronizarDados
from matching.normalizacao.desduplicacao import removerDuplicatas

# Passo 5: Matching (como já definido anteriormente)
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


def matching():
    # Exemplo de caminhos de arquivos - ajuste conforme necessário
    excel_file_path = 'caminho/para/seu/arquivo.xlsx'
    json_file_path = 'caminho/para/produtos_simulados.json'
    query = "iphone"
    
    # Passo 1: Coleta - Carregar dados do Excel
    # Supondo que você tenha uma função `carregar_dados_from_excel` definida
    df = carregar_dados_from_excel(excel_file_path)
    
    # Passo 2: Normalização - Processar e limpar os dados
    # Utilize suas funções de normalização aqui
    df_deduplicado = removerDuplicatas(df)
    df_limpo = limparEPadronizarDados(df_deduplicado)
    
    # Aqui você pode converter `df_limpo` para um formato necessário para as próximas etapas
    # Por exemplo, salvar em um arquivo JSON se necessário para o matching
    df_limpo.to_json(json_file_path, orient='records', force_ascii=False)
    
    # Passo 3: Enriquecimento - Extrair atributos de cada produto
    # Esta etapa pode variar dependendo da sua necessidade de enriquecimento
    # Aqui está um exemplo genérico que percorre cada descrição de produto
    for descricao in df_limpo['descricao']:
        extrair_atributos(descricao)
    
    # Passo 4: Indexação - Opcional, dependendo da necessidade de categorizar ou re-categorizar produtos
    # Se necessário, você pode chamar a função `categorizador` aqui
    
    # Passo 5: Matching - Encontrar produtos correspondentes baseados em uma query
    # Esta função busca produtos no arquivo JSON gerado
    resultados = buscar_produtos_from_json(json_file_path, query)
    for produto, score in resultados:
        print(f"Produto: {produto}, Score: {score:.4f}")
