# Exo-1 — API Flask de gestion de tâches

Une petite application Flask écrite en Python, permettant de gérer des tâches (ajout, affichage, suppression)

## Fonctionnalités

- Création d’une tâche (POST)
- Récupération de la liste des tâches (GET)
- Mise à jour ou suppression d’une tâche (PUT / DELETE)
- Gestion des données côté serveur (en mémoire ou fichier JSON)

## Technologies utilisées

- Python 3.9+
- Flask

## Installation

Créer un environnement virtuel

python -m venv venv
source venv/bin/activate # Linux/macOS

Installer les dépendances

pip install -r requirements.txt

Lancer le serveur Flask

python app.py

Structure du projet

Exo-1-Eric_Semedo_Tavares/
│
├── app.py # Point d'entrée principal Flask
├── main.py # Script ou logique secondaire
├── models/
│ └── task.py # Modèle de données (classe Task)
├── requirements.txt # Dépendances Python
├── .gitignore # Fichiers ignorés par Git
└── README.md # Documentation

Tests

Teste des routes avec curl ou Postman :

# Lister les tâches

curl http://127.0.0.1:5000/tasks

# Ajouter une tâche

curl -X POST -H "Content-Type: application/json" -d '{"title": "Faire les courses"}' http://127.0.0.1:5000/tasks
