from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

# Exemplo de dados: descrições de produtos e suas categorias
data = [
    ("Smartphone XYZ com 64GB de memória", "Eletrônicos"),
    ("Tênis de corrida ABC", "Vestuário"),
    ("Blender elétrico 300W para cozinha", "Eletrodomésticos"),
    # Adicione mais exemplos conforme necessário...
]

# Separando os dados
X, y = zip(*data)  # Descompacta em listas de descrições e categorias

# Dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
model = make_pipeline(TfidfVectorizer(), RandomForestClassifier())
model.fit(X_train, y_train)

# Avaliando o modelo
y_pred = model.predict(X_test)
print(f"Acurácia: {accuracy_score(y_test, y_pred)}")
