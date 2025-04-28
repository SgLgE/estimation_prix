# Estimation du Prix de Produits avec IA (Django)

Projet développé dans le cadre du module de développement Full Stack.

## 📌 Description

Cette application permet d'estimer automatiquement le prix d'un produit en fonction de son poids grâce à un modèle d'intelligence artificielle de type régression linéaire (scikit-learn).  
Le projet est entièrement développé avec Django pour le backend et Bootstrap pour l'interface utilisateur.

---

## 🛠 Technologies utilisées

- **Backend** : Django 5.1
- **IA / Machine Learning** : Python 3.11 + scikit-learn
- **Base de données** : SQLite
- **Frontend** : Bootstrap 5
- **Versionning** : Git + GitHub

---

## 🚀 Fonctionnalités principales

- **Ajout de produit** (Nom, Poids, Prix réel)
- **Estimation automatique** du prix via un modèle IA
- **Enregistrement** des produits dans la base de données
- **Comparaison** prix réel vs prix estimé
- **Interface simple** et rapide avec Bootstrap

---

## ⚙️ Installation et lancement du projet

### 1. Cloner le dépôt GitHub

```bash
git clone https://github.com/SgLgE/estimation_prix.git
cd estimation_prix

# Créer un environnement virtuel (optionnel mais recommandé)

python -m venv env
source env/bin/activate  # MacOS/Linux
env\Scripts\activate     # Windows

# Installer les dépendances nécessaires

pip install django scikit-learn pandas

#  Lancer les migrations de la base de données

cd estimation
python manage.py makemigrations
python manage.py migrate

# Démarrer le serveur

python manage.py runserver

Accéder à l'application sur :
http://127.0.0.1:8000/

📊 Fonctionnement du modèle IA
Le modèle utilise une régression linéaire pour estimer le prix en fonction du poids du produit.

Le modèle est entraîné à partir de données d'exemple et sauvegardé sous model.pkl.

Lors de l'ajout d'un produit, l'IA prédit automatiquement le prix basé sur le poids renseigné.



