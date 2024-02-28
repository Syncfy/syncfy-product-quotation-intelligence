# Supondo que 'produtos' é a nossa lista normalizada de produtos
produtos = [
  {"id": 1, "nome": "smartphone xyz 64gb", "categoria": "smartphones", "preço": 999.99},
  {"id": 2, "nome": "notebook abc 15' core i7", "categoria": "notebooks", "preço": 2499.99},
  {"id": 3, "nome": "smartwatch def health tracker", "categoria": "wearables", "preço": 199.99}
]

def buscar_produto(query):
    query = query.lower()
    resultados = [produto for produto in produtos if query in produto["nome"]]
    return resultados

# Exemplo de busca
query = "smartphone"
resultados = buscar_produto(query)

for produto in resultados:
    print(f'Produto: {produto["nome"]}, Preço: {produto["preço"]}')
