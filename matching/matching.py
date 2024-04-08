import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from matching.coletores.coletorExcel import carregar_dados_from_excel
from matching.normalizacao.limpeza import limparEPadronizarDados
from matching.normalizacao.desduplicacao import removerDuplicatas

def carregar_categoria_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        produtos = json.load(file)
    descricoes = [produto['Nome'] for produto in produtos]
    return descricoes

def buscar_produtos_from_json(json_file_path, query):
    descricoes = carregar_categoria_from_json(json_file_path)
    vectorizer = TfidfVectorizer()
    produtos_tfidf = vectorizer.fit_transform(descricoes)
    query_tfidf = vectorizer.transform([query])
    similaridade = cosine_similarity(query_tfidf, produtos_tfidf).flatten()
    resultados = [(descricoes[i], similaridade[i]) for i in range(len(descricoes)) if similaridade[i] > 0]
    return resultados


def matching(query):
    excel_file_path = 'matching/coletores/produtos/produtos.xlsx'
    json_file_path = 'matching/coletores/produtos/produtos.json'
    
    # Passo 1 - Coleta de dados
    df = carregar_dados_from_excel(excel_file_path)
    print("Dados carregados com sucesso." + str(df))

    # Passo 2: Normalização - Processar e limpar os dados
    df_deduplicado = removerDuplicatas(df)
    print("Duplicatas removidas." + str(df_deduplicado))
    
    df_limpo = limparEPadronizarDados(df_deduplicado)
    print("Nome e Categoria padronizados." + str(df_limpo))

    # Salvar os dados limpos em um arquivo JSON
    df_limpo.to_json(json_file_path, orient='records', force_ascii=False)
    print("df_limpo salvo em JSON.")
    print(str(df_limpo))
    
    # Passo 5: Matching - Encontrar produtos correspondentes baseados em uma query
    # Esta função busca produtos no arquivo JSON gerado
    produtosEncontrados = []
    resultados = buscar_produtos_from_json(json_file_path, query)
    for produto, score in resultados:
        print(f"Produto: {produto}, Score: {score:.4f}")
        produtosEncontrados.append(f"Produto: {produto}, Score: {score:.4f}")

    return produtosEncontrados
    
    # Passo 3: Enriquecimento - Extrair atributos de cada produto
    # for descricao in df_limpo['descricao']:
    #     extrair_atributos(descricao)
    
    # Passo 4: Indexação - Opcional, dependendo da necessidade de categorizar ou re-categorizar produtos
    # Se necessário, você pode chamar a função `categorizador` aqui