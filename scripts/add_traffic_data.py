import psycopg2
from psycopg2 import sql
from datetime import datetime, timedelta
import random

# Fonction pour se connecter à PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="my_password"  # Remplacez par votre mot de passe PostgreSQL
    )
    return conn

# Générer des données simulées
def generate_data():
    locations = ["Centre-ville", "Banlieue", "Zone industrielle", "Autoroute"]
    current_time = datetime.now()
    
    # Générer une liste de tuples avec les données simulées
    data = []
    for _ in range(10):  # Génère 10 enregistrements
        location = random.choice(locations)
        vehicle_count = random.randint(50, 500)  # Nombre de véhicules entre 50 et 500
        timestamp = current_time - timedelta(minutes=random.randint(1, 60))  # Dernière heure
        data.append((timestamp, location, vehicle_count))
    return data

# Insérer les données dans la base PostgreSQL
def insert_data_to_db(data):
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        # Requête d'insertion
        insert_query = """
        INSERT INTO traffic_data (timestamp, location, vehicle_count)
        VALUES (%s, %s, %s);
        """
        cursor.executemany(insert_query, data)  # Insérer plusieurs enregistrements
        conn.commit()  # Sauvegarder les changements
        print(f"{len(data)} enregistrements insérés avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'insertion des données : {e}")
    finally:
        cursor.close()
        conn.close()

# Appel des fonctions
if __name__ == "__main__":
    simulated_data = generate_data()
    insert_data_to_db(simulated_data)

