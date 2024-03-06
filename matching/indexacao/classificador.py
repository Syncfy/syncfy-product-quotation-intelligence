from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

data = [
    ("Smartphone XYZ com 64GB de memória", "Eletrônicos"),
    ("Tênis de corrida ABC", "Vestuário"),
    ("Blender elétrico 300W para cozinha", "Eletrodomésticos"),
]

X, y = zip(*data)  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = make_pipeline(TfidfVectorizer(), RandomForestClassifier())
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Acurácia: {accuracy_score(y_test, y_pred)}")
