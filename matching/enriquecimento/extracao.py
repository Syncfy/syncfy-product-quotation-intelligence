import re
import spacy

def extrair_atributos(descricao):
    # Expressões regulares para extrair marca, modelo e cor
    marca_regex = r"(Smartphone|Notebook|Blender|Tênis)"
    modelo_regex = r"Modelo (\d+)"
    cor_regex = r"Cor (\w+)"
    
    marca = re.search(marca_regex, descricao)
    modelo = re.search(modelo_regex, descricao)
    cor = re.search(cor_regex, descricao)
    
    # Carregando um modelo pré-treinado do spaCy
    nlp = spacy.load("en_core_web_sm")  # Substitua por "pt_core_news_sm" para português
    
    # Processando a descrição do produto
    doc = nlp(descricao)
    
    # Extraindo entidades
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")
    
    if marca:
        print(f"Marca: {marca.group(0)}")
    if modelo:
        print(f"Modelo: {modelo.group(1)}")
    if cor:
        print(f"Cor: {cor.group(1)}")
