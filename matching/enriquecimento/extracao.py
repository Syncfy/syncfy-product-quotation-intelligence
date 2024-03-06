import re
import spacy

def extrair_atributos(descricao):
    marca_regex = r"(Smartphone|Notebook|Blender|Tênis)"
    modelo_regex = r"Modelo (\d+)"
    cor_regex = r"Cor (\w+)"
    
    marca = re.search(marca_regex, descricao)
    modelo = re.search(modelo_regex, descricao)
    cor = re.search(cor_regex, descricao)
    
    nlp = spacy.load("en_core_web_sm")  
    
    doc = nlp(descricao)
    
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")
    
    if marca:
        print(f"Marca: {marca.group(0)}")
    if modelo:
        print(f"Modelo: {modelo.group(1)}")
    if cor:
        print(f"Cor: {cor.group(1)}")
