import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import time
import logging
from typing import Optional, Dict, List

# Configuration du logging
logging.basicConfig(level=logging.INFO)
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
        time.sleep(1)
        
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

def update_assets_data(csv_path: str = 'data/actifs.csv', start_date: str = '2023-01-01', end_date: str = '2024-12-31') -> pd.DataFrame:
    """
    Met à jour les données de rendement et volatilité pour tous les actifs
    Args:
        csv_path: Chemin vers le fichier CSV des actifs
        start_date: Date de début au format 'YYYY-MM-DD'
        end_date: Date de fin au format 'YYYY-MM-DD'
    Returns:
        pd.DataFrame: DataFrame mis à jour avec les données historiques
    """
    try:
        # Lecture du fichier CSV
        csv_df = pd.read_csv(csv_path)
        data_df = pd.DataFrame()
        available_assets = []

        # Mise à jour des données pour chaque actif
        for index, row in csv_df.iterrows():
            ticker = row['Ticker']
            returns_df = download_asset(ticker, start_date, end_date)
            if returns_df is None:
                logger.warning(f"Impossible de récupérer les données pour {ticker}")
                csv_df = csv_df.drop(index)
                csv_df.to_csv(csv_path, index=False)
                
                logger.info(f"Actif {ticker} supprimé du fichier CSV")

            else:
                available_assets.append(ticker)
                # Renommer la colonne returns avec le ticker
                returns_df = returns_df.rename(columns={'returns': f'{ticker}_returns'})
                
                if data_df.empty:
                    data_df = returns_df
                else:
                    data_df = data_df.join(returns_df, how='outer')
                
                logger.info(f"Données ajoutées pour {ticker}")
                
        
        # Trier par date
        data_df = data_df.sort_index()
        
        logger.info(f"Données fusionnées avec succès. {len(data_df)} lignes créées.")
        return csv_df, data_df, available_assets
        
    except Exception as e:
        logger.error(f"Erreur lors de la mise à jour des données: {str(e)}")
        raise




if __name__ == "__main__":
    # Exemple d'utilisation
    print("Mise à jour des données des actifs...")
    try:
        updated_df = update_assets_data()
        print("Données mises à jour avec succès!")
        print("\nAperçu des données mises à jour:")
        print(updated_df)
    except Exception as e:
        print(f"Erreur lors de la mise à jour des données: {str(e)}") 