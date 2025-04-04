# Simulateur de Portefeuille Vert

Une application Streamlit pour simuler et optimiser des portefeuilles d'investissement avec une approche verte.

## Fonctionnalités

- Mise à jour automatique des données depuis Yahoo Finance
- Filtrage des actifs selon leur note environnementale
- Optimisation du portefeuille basée sur le ratio de Sharpe
- Rebalancement hebdomadaire
- Visualisation des performances et de la répartition du portefeuille

## Installation

1. Cloner le repository :
```bash
git clone https://github.com/v/finance-verte.git
cd finance-verte
```

2. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix/macOS
# ou
venv\Scripts\activate  # Sur Windows
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Lancer l'application :
```bash
streamlit run app.py
```

2. Dans l'interface :
   - Mettre à jour les données des actifs
   - Définir le montant total à investir
   - Choisir la note environnementale minimale
   - Créer et visualiser le portefeuille

## Structure du Projet

- `app.py` : Application Streamlit principale
- `portfolio_manager.py` : Gestion de la logique du portefeuille
- `data_collector.py` : Récupération et mise à jour des données
- `data/actifs.csv` : Données des actifs et leurs notes environnementales

## Dépendances

- streamlit
- pandas
- numpy
- plotly
- yfinance
- matplotlib
- seaborn
- scipy

## Licence

MIT 