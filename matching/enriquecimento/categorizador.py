import logging
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def categorizador(data):
    logging.info("Iniciando a função de categorização.")
    X = data['main_category']
    y = data['sub_category']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    logging.info("Dados divididos em conjuntos de treinamento e teste.")
    pipeline = make_pipeline(TfidfVectorizer(), RandomForestClassifier())
    pipeline.fit(X_train, y_train)
    logging.info("Modelo treinado.")
    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    logging.info(f"Acurácia do modelo: {acc}")