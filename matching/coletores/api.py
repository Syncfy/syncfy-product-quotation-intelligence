import requests
import json

# Exemplo de URL de uma API fictícia que retorna dados de produtos
url = "https://api.exemplo.com/produtos"

# Enviando um pedido GET para a API
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Convertendo a resposta de JSON para um dicionário Python
    produtos = response.json()
    
    # Exemplo de processamento dos dados
    for produto in produtos:
        print(f'Nome: {produto["nome"]}, Categoria: {produto["categoria"]}, Preço: {produto["preço"]}')
else:
    print("Erro ao acessar a API")
