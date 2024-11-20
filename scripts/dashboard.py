import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px

# Fonction pour se connecter à PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="my_password"  # Remplacez par votre mot de passe PostgreSQL
    )
    return conn

# Charger les données depuis PostgreSQL
def load_data():
    conn = connect_to_db()
    query = "SELECT * FROM traffic_data;"
    df = pd.read_sql_query(query, conn)  # Charger les données dans un DataFrame Pandas
    conn.close()
    return df

# Titre de l'application
st.title("Traffic Data Dashboard")
st.write("Analyse des données de trafic en temps réel.")

# Charger les données
try:
    df = load_data()

    # Afficher les données sous forme de tableau
    st.write("### Données récupérées de la base PostgreSQL :")
    st.dataframe(df)

    # Ajouter un graphique interactif
    st.write("### Visualisation du trafic par localisation :")
    fig = px.bar(df, x="location", y="vehicle_count", color="location",
                 title="Nombre de véhicules par zone",
                 labels={"location": "Localisation", "vehicle_count": "Nombre de véhicules"})
    st.plotly_chart(fig)

    # Graphique temporel
    st.write("### Variation temporelle du trafic :")
    fig_time = px.line(df, x="timestamp", y="vehicle_count", color="location",
                       title="Variation du trafic au fil du temps",
                       labels={"timestamp": "Temps", "vehicle_count": "Nombre de véhicules"})
    st.plotly_chart(fig_time)

except Exception as e:
    st.error(f"Erreur lors de la récupération ou de l'affichage des données : {e}")
import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px

# Fonction pour se connecter à la base PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",        # Hôte local (Docker expose PostgreSQL sur localhost)
        database="postgres",     # Nom de la base de données
        user="postgres",         # Nom d'utilisateur PostgreSQL
        password="my_password"   # Mot de passe PostgreSQL
    )
    return conn

# Titre de l'application
st.title("Traffic Data Dashboard")
st.write("Bienvenue dans le tableau de bord pour visualiser les données de trafic.")

# Récupérer les données de PostgreSQL
try:
    # Se connecter à la base
    conn = connect_to_db()
    cursor = conn.cursor()

    # Exécuter une requête SQL pour récupérer les données
    cursor.execute("SELECT * FROM test;")
    rows = cursor.fetchall()

    # Transformer les données en DataFrame Pandas
    df = pd.DataFrame(rows, columns=["id", "name"])

    # Ajouter une option de filtrage par ID
    st.write("### Filtrage des données :")
    id_filter = st.selectbox("Sélectionnez un ID :", options=df["id"].unique())
    filtered_df = df[df["id"] == id_filter]

    # Afficher les données filtrées
    st.write("Données filtrées :")
    st.table(filtered_df)

    # Graphique avec les données filtrées
    st.write("Graphique interactif basé sur la sélection :")
    fig = px.pie(filtered_df, names="name", title="Répartition par Nom")
    st.plotly_chart(fig)

    # Fermer la connexion
    cursor.close()
    conn.close()
except Exception as e:
    st.error(f"Erreur lors de la connexion à la base de données : {e}")
import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px

# Fonction pour se connecter à la base PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",        # Hôte local (Docker expose PostgreSQL sur localhost)
        database="postgres",     # Nom de la base de données
        user="postgres",         # Nom d'utilisateur PostgreSQL
        password="my_password"   # Mot de passe PostgreSQL
    )
    return conn

# Titre de l'application
st.title("Traffic Data Dashboard")
st.write("Bienvenue dans le tableau de bord pour visualiser les données de trafic.")

# Récupérer les données de PostgreSQL
try:
    # Se connecter à la base
    conn = connect_to_db()
    cursor = conn.cursor()

    # Exécuter une requête SQL pour récupérer les données
    cursor.execute("SELECT * FROM test;")
    rows = cursor.fetchall()

    # Transformer les données en DataFrame Pandas
    df = pd.DataFrame(rows, columns=["id", "name"])

    # Afficher les données dans un tableau
    st.write("Voici les données récupérées de la base PostgreSQL :")
    st.table(df)

    # Générer un graphique interactif avec Plotly
    st.write("Graphique des données récupérées :")
    fig = px.bar(df, x="id", y="name", title="Graphique des noms en fonction des IDs")
    st.plotly_chart(fig)

    # Fermer la connexion
    cursor.close()
    conn.close()
except Exception as e:
    st.error(f"Erreur lors de la connexion à la base de données : {e}")

