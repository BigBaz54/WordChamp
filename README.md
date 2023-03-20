# Contexte
Wordle-like réalisé avec Malo Damien, Tristan Smagghe et Jules Brunet dans le cadre du projet du second semestre de 1ère année à TÉLÉCOM Nancy.

Il contient une application web et un solveur.

# Installation (production)

## Pré-requis

 - Docker et Docker Compose

## Étapes

 - `git clone https://gitlab.telecomnancy.univ-lorraine.fr/ppii2k22/project2-E15`
 - `cd project2-E15`
 - `docker-compose build` (peut prendre une ou deux minutes)
 - `docker-compose up -d`

 - Le site est alors accessible sur : `http://localhost:8080`

# Installation (développement)

## Pré-requis

 - Python 3 (3.10 si possible)
 - NPM (dispo [ici](https://nodejs.org/en/))

## Python :

 - Aller dans `backend`
 - Mise en place de l'environnement : `python -m venv env`
 - Installation des dépendances : `pip install -r requirements.txt`
 - Lancer le backend : `python ./app.py`

## Vue.JS :

 - Aller dans `frontend`
 - Installation des dépendances : `npm install`
 - Lancer le frontend : `npm run serve`

 # Manquant

 - CI/CD et dockerisation
