# Application Web d'analyse des sentiments
## Installation
### Mettre en place l'environnement virtuel 
```bash
python -m venv .venv
```

### Lancer l'environnement virtuel
#### Windows 
```bash
.venv/Scripts/Ativate.ps1
```
#### Unix 
```bash
source .venv/bin/activate
```
### Installation des dépendances
```bash
pip install -r requirement.txt
```
## Comment utiliser ce repo ?
### Les notebooks
Vous trouverez 2 notebooks dans ce repo : 
- `ethic.ipynb` : correspond à l'analyse et au traitement éthique des données (suppression et traitement des informations sensibles)
- `explo.ipynb` : correspond au nettoyage des données
Le traitement éthique des données aboutit au jeu de données `data/ethical_data.csv`.  
Le nettoyage des données aboutit au jeu de données `data/cleaned_data.csv`
### Le preprocessor
Plutôt que de passer par le second notebook (`explo.ipynb`) les données issues de `data/ethical_data.csv` peuvent être traîtées par la pipeline du preprocessor créé dans le module `modules/preprocess.py`, stocké ici : `models/preprocessor.pkl`