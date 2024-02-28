from bs4 import BeautifulSoup
import requests

# Exemplo de URL de um site fictício
url = "https://www.exemplo.com/produtos"

# Enviando um pedido GET para o site
response = requests.get(url)

if response.status_code == 200:
    # Parsing do HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrando elementos específicos, supondo que cada produto esteja em um <div class="produto">
    produtos = soup.find_all('div', class_='produto')
    
    for produto in produtos:
        nome = produto.find('h2').text
        categoria = produto.find('span', class_='categoria').text
        preço = produto.find('span', class_='preço').text
        print(f'Nome: {nome}, Categoria: {categoria}, Preço: {preço}')
else:
    print("Erro ao acessar o site")
