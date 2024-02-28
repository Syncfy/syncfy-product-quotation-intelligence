from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

# Exemplo de dataset
data = {
    'descrições': ['Smartphone 64GB', 'Tênis de corrida', 'Blender 300W', 'Notebook 15\' i7'],
    'categorias': ['Eletrônicos', 'Vestuário', 'Eletrodomésticos', 'Eletrônicos']
}

X = data['descrições']
y = data['categorias']

# Dividindo os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Criando o pipeline de classificação
pipeline = make_pipeline(TfidfVectorizer(), RandomForestClassifier())
pipeline.fit(X_train, y_train)

# Avaliando o modelo
y_pred = pipeline.predict(X_test)
print(f"Acurácia: {accuracy_score(y_test, y_pred)}")
