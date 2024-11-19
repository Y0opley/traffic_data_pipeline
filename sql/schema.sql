-- Création de la table pour les données de trafic
CREATE TABLE traffic_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    location TEXT NOT NULL,
    vehicle_count INT NOT NULL
);

