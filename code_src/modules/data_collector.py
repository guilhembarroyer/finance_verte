import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import time
import logging
from typing import Optional, Dict, List
import random

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_collector.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def download_asset(ticker: str, start_date: str = '2023-01-01', end_date: str = '2024-12-31') -> Optional[pd.DataFrame]:
    """
    Télécharge les données d'un actif depuis Yahoo Finance.
    
    Args:
        ticker: Symbole de l'actif
        start_date: Date de début au format 'YYYY-MM-DD'
        end_date: Date de fin au format 'YYYY-MM-DD'
        
    Returns:
        Optional[pd.DataFrame]: Les données de l'actif ou None en cas d'erreur
    """
    try:
        # Ajout d'un délai aléatoire entre 1 et 3 secondes pour éviter les limites de requêtes
        time.sleep(3)
        
        # Téléchargement des données avec yfinance
        stock = yf.Ticker(ticker)
        info = stock.info

        # Calcul des rendements hebdomadaires (vendredi soir)
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2024, 12, 31)
        
        # Télécharger les données avec un intervalle hebdomadaire
        data = stock.history(start=start_date, end=end_date, interval='1wk')
        
        if data.empty:
            print(f"⚠️ Aucune donnée historique disponible pour {ticker}")
            return None

        # Calculer les rendements hebdomadaires
        data['returns'] = data['Close'].pct_change()
        
        # Ne garder que la colonne des rendements avec la date en indice
        data = data[['returns']]
        
        data.fillna(0, inplace=True)
        
        return data
        
    except Exception as e:
        logger.error(f"Erreur lors du téléchargement des données pour {ticker}: {str(e)}")
        return None

def update_assets_data():
    """
    Met à jour les données de tous les actifs et sauvegarde les résultats.
    """
    try:
        # Lecture du fichier Excel
        assets_df = pd.read_excel('data/actifs.xlsx')
        available_assets=[]
        # Initialisation du DataFrame pour stocker les rendements
        returns_data = {}
        
        
        # Téléchargement des données pour chaque actif
        for index, row in assets_df.iterrows():
            ticker = row['Ticker']
            logging.info(f"Téléchargement des données pour {ticker}")
            
            data = download_asset(ticker)

            if data is not None:
                returns_data[ticker] = data['returns']
                available_assets.append(ticker)
            else:
                assets_df=assets_df.drop(index=index)
                logging.error(f"Erreur lors du téléchargement des données pour {ticker}")
        # Création du DataFrame final
        if returns_data:
            # Créer un DataFrame avec toutes les dates uniques
            
            returns_df = pd.DataFrame()
            
            # Ajouter les rendements de chaque actif
            for ticker, returns in returns_data.items():
                returns_df[ticker] = returns
            
            returns_df.fillna(0, inplace=True)  
            # Sauvegarde des données
            returns_df.to_csv('data/returns.csv')
            logging.info("Données sauvegardées avec succès")
            
            print(assets_df)
            print(returns_df)
            print(available_assets)

            return assets_df, returns_df, available_assets
        else:
            logging.error("Aucune donnée n'a pu être téléchargée")
            return None
            
    except Exception as e:
        logging.error(f"Erreur lors de la mise à jour des données: {str(e)}")
        return None

if __name__ == "__main__":
    update_assets_data() 

