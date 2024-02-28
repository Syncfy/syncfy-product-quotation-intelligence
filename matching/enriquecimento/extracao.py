import re
import spacy

# Exemplo de descrição de produto
descricao = "Smartphone XYZ Modelo 2020 Cor Azul"

# Expressões regulares para extrair marca, modelo e cor
marca_regex = r"(Smartphone|Notebook|Blender|Tênis)"
modelo_regex = r"Modelo (\d+)"
cor_regex = r"Cor (\w+)"

marca = re.search(marca_regex, descricao)
modelo = re.search(modelo_regex, descricao)
cor = re.search(cor_regex, descricao)

if marca:
    print(f"Marca: {marca.group(0)}")
if modelo:
    print(f"Modelo: {modelo.group(1)}")
if cor:
    print(f"Cor: {cor.group(1)}")

# Carregando um modelo pré-treinado do spaCy
nlp = spacy.load("en_core_web_sm")  # Substitua por "pt_core_news_sm" para português

# Processando a descrição do produto
doc = nlp("Smartphone XYZ Modelo 2020 Cor Azul")

# Extraindo entidades (neste exemplo simplificado, pode não identificar corretamente sem treinamento adicional)
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")
