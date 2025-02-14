import streamlit as st
import requests
import joblib
import numpy as np
import pandas as pd

# Fonction pour envoyer les données à l'API
def send_data_to_api(data):
    response = predict(data)
    return response.json()

def load_model():
    # Charger le modèle
    model = joblib.load('model_classifier_iris.pkl')
    scale = joblib.load("scaler.pkl")

    return model, scale

def predict(data):
    model, scale = load_model()
    try:
        
        # Extraire les caractéristiques
        sepal_length = data['sepal_length']
        sepal_width = data['sepal_width']
        petal_length = data['petal_length']
        petal_width = data['petal_width']
        
        # Créer un tableau NumPy des caractéristiques
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Convertir en DataFrame
        X_train = pd.DataFrame(features, columns=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'])

        # Normalisation
        X_train_normalized = scale.transform(X_train)
        
        # Faire la prédiction
        prediction = model.predict(X_train_normalized)
        
        # Renvoie la prédiction
        return prediction[0]
        
    except Exception as e:
        return 



st.markdown("<h1 style='text-align: center;'>PREDICTION DU TYPE DE FLEUR D'IRIS</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("Longueur du sépal", 0.0, 10.0, value=0.0, step=0.1)

with col2:
    sepal_width = st.slider("Largeur du sépal", 0.0, 10.0, value=0.0, step=0.1)

# Deuxième ligne avec deux autres curseurs
col3, col4 = st.columns(2)

with col3:
    petal_length = st.slider("Longueur du pétale", 0.0, 10.0, value=0.0, step=0.1)

with col4:
    petal_width = st.slider("Largeur du pétale", 0.0, 10.0, value=0.0, step=0.1)




# Bouton pour envoyer les données à l'API
if st.button("Prédire la fleur...", help="Cliquez pour envoyer les données", type="primary"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    
    # Envoyer les données à l'API
    response = predict(data)
    #model, sca = load_model()
    
    # Afficher la réponse de l'API
    st.write("<p style='font-size: 20px; font-weight: bold;'>Votre fleur semble être : <span style='color: #ff4b4b;'>", response , "</span></p>", unsafe_allow_html=True)
