# Finance Verte - Optimisation de Portefeuille

Ce projet implémente une stratégie d'investissement vert optimisée, basée sur les notations environnementales des actifs et l'optimisation du ratio de Sharpe.

## Structure du Projet

```
finance-verte/
├── code_src/
│   ├── data_collector.py    # Collecte des données de prix
│   ├── portfolio_manager.py # Gestion et optimisation du portefeuille
│   └── app.py              # Interface utilisateur Streamlit
├── data/
│   └── actifs.xlsx         # Données des actifs et leurs notations
└── requirements.txt        # Dépendances Python
```

## Installation

1. Cloner le repository :
```bash
git clone https://github.com/guilhembarroyer/finance-verte.git
cd finance-verte
```

2. Créer un environnement virtuel :
```bash
# Sur macOS/Linux
python -m venv venv
source venv/bin/activate

# Sur Windows
python -m venv venv
venv\Scripts\activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Mettre à jour les données des actifs :
```bash
python code_src/data_collector.py
```

2. Lancer l'application Streamlit :
```bash
streamlit run code_src/app.py
```

## Fonctionnalités

- Collecte automatique des données de prix depuis Yahoo Finance
- Optimisation du portefeuille basée sur les notations environnementales
- Interface utilisateur interactive avec Streamlit
- Rebalancement hebdomadaire du portefeuille
- Calcul des métriques de performance (rendement, volatilité, ratio de Sharpe)

## Configuration

Le fichier `data/univers_gestion_verte.xlsx` contient :
- Les tickers des actifs
- Les notations environnementales
- Les métriques de performance

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

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