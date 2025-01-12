# Gestion des Départements et des Professeurs

## Description

Ce projet est une application web développée avec **Django**, permettant de gérer les départements et les professeurs d'une institution. L'application offre une interface utilisateur intuitive, avec des fonctionnalités modernes et un design responsive. Elle inclut également une API pour la gestion des données liées aux professeurs.

---

## Fonctionnalités

### Gestion des Départements
- Ajouter un département via :
  - Un formulaire 100% HTML
  - Un formulaire combinant HTML et Django.
- Afficher la liste complète des départements.

### Gestion des Professeurs
- Ajouter un professeur avec :
  - Nom complet
  - Contact
  - Date d'adhésion au format **JJ/MM/AAAA**.
  - Associer un professeur à un ou plusieurs départements.
- Afficher la liste complète des professeurs.
- Gérer les relations entre professeurs et départements (ex. chefs de départements).

### API pour le Modèle Professeur
- **Lister tous les professeurs :** Retourne une liste complète des professeurs avec leurs informations (nom, contact, date d'adhésion et départements associés).
- **Afficher les détails d’un professeur spécifique :** Retourne les informations détaillées d’un professeur, y compris les départements où il est chef.

### Interface Utilisateur
- Barre de navigation fixe avec mise en évidence des liens actifs.
- Design responsive adapté à toutes les tailles d’écran.
- Footer simple et esthétique présent sur toutes les pages.

---

## Installation

1. **Clonez le repository** ou **téléchargez le fichier .zip et extrayez-le** :
   - Pour cloner :
     ```bash
     git clone https://github.com/diopmedoune/medoune-diop.git
     ```
   - Pour télécharger le fichier .zip :
     - Allez sur la page [GitHub du repository](https://github.com/diopmedoune/medoune-diop).
     - Cliquez sur le bouton "Code" puis sur "Download ZIP".
     - Extrayez le fichier .zip téléchargé dans le répertoire de votre choix.

2. **Créer un environnement virtuel** :  
   - Linux/Mac : `python3 -m venv env`  
   - Windows : `python -m venv env`

3. **Activer l'environnement** :  
   - Linux/Mac : `source env/bin/activate`  
   - Windows : `.\env\Scripts\activate`

4. **Installer les dépendances** :  
   `pip install -r requirements.txt`
