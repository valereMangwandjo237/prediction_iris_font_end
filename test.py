col1, col2 = st.columns([1, 3])  # Colonne 1 pour la navbar (1/4), Colonne 2 pour le contenu (3/4)

with col1:
    st.sidebar.header("Menu")
    option = st.sidebar.selectbox("Choisissez une option :", ["Accueil", "À propos", "Contact"])

# Contenu principal dans la colonne de droite
with col2:
    if option == "Accueil":
        st.subheader("Bienvenue sur la page d'accueil")
        st.write("Voici le contenu de la page d'accueil.")
    elif option == "À propos":
        st.subheader("À propos de cette application")
        st.write("Cette application est un exemple de navigation verticale avec Streamlit.")
    elif option == "Contact":
        st.subheader("Contactez-nous")
        st.write("Vous pouvez nous contacter à : contact@example.com")
