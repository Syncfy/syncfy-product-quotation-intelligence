import pandas as pd
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def treinar_e_avaliar_modelo(df):
    try:
        if df is None:
            raise ValueError("O dataframe passado é None.")
        
        if 'name' not in df.columns or 'category' not in df.columns:
            raise ValueError("As colunas necessárias não estão presentes no dataframe.")

        logging.info("Iniciando o processo de treinamento e avaliação do modelo.")

        X = df['name']
        y = df['sub_category']

        logging.info("Dividindo os dados em conjuntos de treino e teste.")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        logging.info("Criando e treinando o modelo de classificação.")
        model = make_pipeline(TfidfVectorizer(), RandomForestClassifier())
        model.fit(X_train, y_train)

        logging.info("Modelo treinado. Realizando predições no conjunto de teste.")
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        logging.info(f"Acurácia do modelo: {accuracy}")
    except ValueError as e:
        logging.error(f"Erro na validação do dataframe: {e}")
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")