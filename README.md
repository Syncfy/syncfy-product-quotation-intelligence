# Sistema de Matching de Produtos

Este projeto visa criar um sistema de matching de produtos que permite aos usuários buscar e encontrar produtos relevantes com base em suas queries de busca. Inspirado no funcionamento do Buscapé, o sistema abrange desde a coleta e normalização de dados até a implementação de algoritmos de busca inteligente e indexação de dados.

## Etapas do Projeto

### 1. Coleta de Dados

- **Fontes de Dados:** Identificação de diversas fontes de dados para obter informações sobre produtos, incluindo APIs de varejistas, feeds de dados de produtos, e técnicas de web scraping, quando permitido.
- **Extração de Dados:** Utilização de técnicas de web scraping e APIs para extrair dados relevantes, como nomes de produtos, descrições, categorias, preços e imagens.

### 2. Normalização de Dados

- **Limpeza e Padronização dos Dados:** Remoção de inconsistências, erros de digitação e informações irrelevantes. Conversão dos dados para um formato padronizado, garantindo consistência nos nomes de produtos, descrições e categorias.
- **Desduplicação:** Implementação de algoritmos para identificar e remover duplicatas, assegurando a unicidade de cada produto na base de dados.

### 3. Enriquecimento de Dados

- **Categorização:** Utilização de técnicas de machine learning para categorizar produtos automaticamente.
- **Extração de Atributos de Produtos:** Aplicação de técnicas de processamento de linguagem natural (NLP) para extrair ou enriquecer os dados com atributos relevantes dos produtos, como marca, modelo, cor, etc.

### 4. Indexação de Dados

- **Estrutura de Dados:** Escolha de uma estrutura de dados apropriada para armazenar e indexar os produtos de forma eficiente.
- **Indexação:** Indexação dos produtos para permitir buscas rápidas e eficientes.

### 5. Desenvolvimento do Algoritmo de Matching

- **Algoritmos de Busca:** Implementação de algoritmos de busca que compreendem a intenção do usuário e encontram produtos correspondentes.
- **Pontuação de Relevância:** Desenvolvimento de um sistema de pontuação baseado em critérios como correspondência de palavras-chave, popularidade, avaliações, e preço.

### 6. Interface do Usuário

- **Desenvolvimento Front-end:** Criação de uma interface de usuário amigável para permitir buscas fáceis e exibir os resultados de forma clara e organizada.

### 7. Testes e Otimização

- **Testes:** Execução de testes para garantir a precisão e eficiência do sistema.
- **Aprendizado Contínuo:** Uso de feedback e dados de uso para melhorar continuamente os algoritmos de matching e busca.

## Implementação

O README inclui exemplos de código e explicações detalhadas para cada uma das etapas acima, orientando o usuário desde a configuração inicial do ambiente de desenvolvimento até a implementação final e os testes do sistema de matching de produtos.

## Considerações Finais

Este documento fornece um guia abrangente para a criação de um sistema de matching de produtos. Ao seguir estas etapas, desenvolvedores podem construir um sistema robusto e eficiente que melhora significativamente a experiência de busca dos usuários, aproximando-os dos produtos que desejam encontrar.


## Como rodar a Aplicação
### 1.Baixar as dependencias nessesarias:
    pip install flask
    pip install scikit-learn
### 2 Com o comando abaixo executar a aplicação e subir o servidor
    python api.py
### 3 Fazer o import da collection no Postam  
### 4 Executar a requisão de matching  
     






