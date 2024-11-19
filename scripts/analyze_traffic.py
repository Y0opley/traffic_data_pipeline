import psycopg2
import matplotlib.pyplot as plt

# Connexion à la base PostgreSQL
try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="my_password"  # Mot de passe correct
    )
    print("Connexion réussie à PostgreSQL")
except Exception as e:
    print(f"Erreur de connexion : {e}")
    exit()

try:
    # Analyse des données de trafic : Total véhicules par zone
    with conn.cursor() as cur:
        query_totals = """
            SELECT location, SUM(vehicle_count) AS total_vehicles
            FROM traffic_data
            GROUP BY location
            ORDER BY total_vehicles DESC;
        """
        cur.execute(query_totals)
        total_results = cur.fetchall()

        print("\nAnalyse des données de trafic :")
        for row in total_results:
            print(f"Zone : {row[0]}, Total véhicules : {row[1]}")

    # Moyenne des véhicules par zone
    with conn.cursor() as cur:
        query_avg = """
            SELECT location, AVG(vehicle_count) AS avg_vehicles
            FROM traffic_data
            GROUP BY location
            ORDER BY avg_vehicles DESC;
        """
        cur.execute(query_avg)
        avg_results = cur.fetchall()

        print("\nMoyenne des véhicules par zone :")
        for row in avg_results:
            print(f"Zone : {row[0]}, Moyenne véhicules : {row[1]:.2f}")

    # Identifier les zones les plus congestionnées
    with conn.cursor() as cur:
        query_congestion = """
            SELECT location, MAX(vehicle_count) AS peak_vehicles,
            CASE
                WHEN MAX(vehicle_count) > 150 THEN 'High'
                WHEN MAX(vehicle_count) BETWEEN 100 AND 150 THEN 'Medium'
                ELSE 'Low'
            END AS congestion_level
            FROM traffic_data
            GROUP BY location
            ORDER BY peak_vehicles DESC;
        """
        cur.execute(query_congestion)
        congestion_results = cur.fetchall()

        print("\nNiveau de congestion par zone :")
        for row in congestion_results:
            print(f"Zone : {row[0]}, Véhicules max : {row[1]}, Congestion : {row[2]}")

    # Visualiser les données avec un graphique
    with conn.cursor() as cur:
        cur.execute("SELECT location, SUM(vehicle_count) AS total_vehicles FROM traffic_data GROUP BY location;")
        graph_results = cur.fetchall()

        locations = [row[0] for row in graph_results]
        totals = [row[1] for row in graph_results]

        plt.bar(locations, totals, color='blue')
        plt.title("Total des véhicules par zone")
        plt.xlabel("Zones")
        plt.ylabel("Nombre total de véhicules")
        plt.show()

except Exception as e:
    print(f"Erreur lors de l'exécution : {e}")

finally:
    if conn:
        conn.close()
        print("Connexion fermée")

