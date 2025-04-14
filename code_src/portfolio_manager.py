import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import logging
from typing import Dict

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PortfolioManager:
    def __init__(self, notation_df, returns_df):
        """
        Initialise le gestionnaire de portefeuille
        Args:
            notation_df (pd.DataFrame): DataFrame contenant les informations des actifs
            returns_df (pd.DataFrame): DataFrame contenant les rendements des actifs
        """
        if not isinstance(notation_df, pd.DataFrame) or notation_df.empty:
            raise ValueError("Le DataFrame des actifs ne peut pas être vide")
        
        self.notation_df = notation_df
        self.returns_df = returns_df

        self.portfolio_history = None
        self.weights = None
        self.total_investment = None

    def create_portfolio(self, total_investment: float = 10000, min_notation: float = 1.0, corresponding_assets: list = [], size: int = 5) -> Dict:
        """
        Crée un portefeuille avec rebalancement hebdomadaire optimisé
        
        Args:
            total_investment: Montant total à investir
            min_notation: Note minimale requise
            corresponding_assets: Liste des actifs à inclure dans le portefeuille
            size: Nombre d'actifs à sélectionner
            
        Returns:
            Dict: Dictionnaire contenant les métriques et l'historique du portefeuille
        """
        try:
            # Initialiser les DataFrames pour stocker les résultats
            portfolio_value = pd.DataFrame(index=self.returns_df.index)
            portfolio_value['value'] = total_investment
            
            # Sélectionner les size actifs les mieux notés
            asset_notes = {asset: self.notation_df[self.notation_df['Ticker'] == asset]['Note'].iloc[0] 
                         for asset in corresponding_assets}
            
            # Trier les actifs par note et prendre les size premiers
            sorted_assets = sorted(asset_notes.items(), key=lambda x: x[1], reverse=True)[:size]
            selected_assets = [asset for asset, _ in sorted_assets]
            
            # Calculer les poids basés sur les notes des actifs sélectionnés
            total_notes = sum(note for _, note in sorted_assets)
            weights = {asset: note/total_notes for asset, note in sorted_assets}

            # Pour chaque semaine, calculer les rendements
            for i in range(len(self.returns_df)):
                # Calculer le rendement du portefeuille pour cette semaine
                weekly_return = 0
                for asset, weight in weights.items():
                    weekly_return += self.returns_df[asset].iloc[i] * weight
                
                # Mettre à jour la valeur du portefeuille
                if i > 0:
                    portfolio_value.iloc[i] = portfolio_value.iloc[i-1] * (1 + weekly_return)

            # Calculer les métriques finales
            returns = portfolio_value['value'].pct_change().dropna()
            annual_return = ((1 + returns.mean()) ** 52 - 1) * 100
            volatility = returns.std() * np.sqrt(52) * 100
            sharpe_ratio = annual_return / volatility if volatility != 0 else 0
            
            return {
                'annual_return': annual_return,
                'volatility': volatility,
                'sharpe_ratio': sharpe_ratio,
                'portfolio_value': portfolio_value['value'],
                'weights': weights,  # Poids basés sur les notes
                'selected_assets': selected_assets  # Liste des actifs sélectionnés
            }
            
        except Exception as e:
            logger.error(f"Erreur lors de la création du portefeuille : {str(e)}")
            raise

    def get_portfolio_metrics(self):
        """
        Calcule les métriques du portefeuille
        Returns:
            dict: Dictionnaire contenant les métriques du portefeuille
        """
        if self.portfolio_history is None:
            raise ValueError("Le portefeuille n'a pas été créé")
        
        try:
            # Calcul des rendements
            returns = self.portfolio_history.pct_change().dropna()
            
            # Métriques
            total_return = (self.portfolio_history.iloc[-1] / self.portfolio_history.iloc[0] - 1) * 100
            annual_return = ((1 + total_return/100) ** (1/2) - 1) * 100  # Sur 2 ans
            volatility = returns.std() * np.sqrt(252) * 100  # Volatilité annualisée
            
            # Note environnementale moyenne
            env_rating = 0
            for ticker, weight in self.weights.items():
                asset_rating = self.assets_df[self.assets_df['Ticker'] == ticker]['Note'].iloc[0]
                env_rating += (weight / 100) * asset_rating
            
            return {
                'Total Return': total_return,
                'Annual Return': annual_return,
                'Volatility': volatility,
                'Environmental Rating': env_rating
            }
        except Exception as e:
            logger.error(f"Erreur lors du calcul des métriques: {str(e)}")
            raise

    def get_portfolio_breakdown(self):
        """
        Retourne la répartition actuelle du portefeuille
        Returns:
            pd.DataFrame: DataFrame contenant la répartition du portefeuille
        """
        if self.weights is None:
            raise ValueError("Les poids du portefeuille n'ont pas été définis")
        
        try:
            breakdown = []
            for ticker, weight in self.weights.items():
                asset_data = self.assets_df[self.assets_df['Ticker'] == ticker].iloc[0]
                breakdown.append({
                    'Ticker': ticker,
                    'Name': asset_data['Nom'],
                    'Type': asset_data['Type'],
                    'Weight': weight,
                    'Investment': self.total_investment * (weight / 100),
                    'Environmental Rating': asset_data['']
                })
            
            return pd.DataFrame(breakdown)
        except Exception as e:
            logger.error(f"Erreur lors de la génération du breakdown: {str(e)}")
            raise 