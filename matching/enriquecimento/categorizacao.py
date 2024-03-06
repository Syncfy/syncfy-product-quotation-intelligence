from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

def categorizador(data):
    X = data['descrições']
    y = data['categorias']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    pipeline = make_pipeline(TfidfVectorizer(), RandomForestClassifier())
    pipeline.fit(X_train, y_train)
    
    y_pred = pipeline.predict(X_test)
    print(f"Acurácia: {accuracy_score(y_test, y_pred)}")