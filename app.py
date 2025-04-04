import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from portfolio_manager import PortfolioManager
from data_collector import update_assets_data
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration de la page
st.set_page_config(
    page_title="Simulateur de Portefeuille",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre de l'application
st.title("Simulateur de Portefeuille")

# Initialisation des variables de session
if 'portfolio_manager' not in st.session_state:
    st.session_state.portfolio_manager = None
if 'returns_df' not in st.session_state:
    st.session_state.returns_df = None
if 'notation_df' not in st.session_state:
    st.session_state.notation_df = None
if 'available_assets' not in st.session_state:
    st.session_state.available_assets = ['', '', '', '', '']
if 'total_investment' not in st.session_state:
    st.session_state.total_investment = 10000
if 'min_rating' not in st.session_state:
    st.session_state.min_rating = 7.0
if 'portfolio_size' not in st.session_state:
    st.session_state.portfolio_size = 5
if 'corresponding_assets' not in st.session_state:
    st.session_state.corresponding_assets = []  



# Section pour la mise à jour des données
st.header("Mise à jour des données")
if st.button("Mettre à jour les données"):
    with st.spinner("Mise à jour des données en cours..."):
        try:
            # Mise à jour des données
            notation_df, returns_df, available_assets = update_assets_data()
            
            if returns_df is not None and not returns_df.empty:
                st.success("Données mises à jour avec succès!")
                
                # Stocker les données dans la session
                st.session_state.returns_df = returns_df
                st.session_state.available_assets = available_assets
                st.session_state.notation_df = notation_df
                
                # Initialiser le gestionnaire de portefeuille
                st.session_state.portfolio_manager = PortfolioManager(
                    notation_df=notation_df,
                    returns_df=returns_df
                )
                
                
            else:
                st.error("Aucune donnée n'a pu être récupérée")
        except Exception as e:
            st.error(f"Erreur lors de la mise à jour des données: {str(e)}")


# Afficher les statistiques des rendements
if st.session_state.returns_df is not None: 
    st.subheader("Statistiques des rendements")
    st.write("Rendements sur la période du 01/01/2023 au 31/12/2024")
    st.dataframe(st.session_state.returns_df.describe())



# Sidebar pour les paramètres
with st.sidebar:
    st.header("Paramètres du Portefeuille")
    
    # Montant total à investir
    st.session_state.total_investment = st.number_input(
        "Montant total à investir (€)",
        min_value=1000,
        value=st.session_state.total_investment,
        step=1000
    )
    st.session_state.portfolio_size = st.number_input(
        "Nombre d'actifs à inclure dans le portefeuille",
        min_value=5,
        max_value=len(st.session_state.available_assets),
        value=st.session_state.portfolio_size,
        step=1
    )
    # Note minimale si des données sont disponibles
    if st.session_state.notation_df is not None:
        st.session_state.min_rating = st.slider(
            "Note environnementale minimale",
            min_value=float(st.session_state.notation_df['Note_Environnementale'].min()),
            max_value=float(st.session_state.notation_df['Note_Environnementale'].max()),
            value=st.session_state.min_rating,
            step=0.1
        )
        st.session_state.corresponding_assets = []

        
        for asset in st.session_state.available_assets:     
            if st.session_state.notation_df[st.session_state.notation_df['Ticker']==asset]['Note_Environnementale'].iloc[0]>= st.session_state.min_rating:
                st.session_state.corresponding_assets.append(asset)
            print('ahha', st.session_state.corresponding_assets)

# Vérifier si des données sont disponibles
if st.session_state.portfolio_manager is None:  
    st.warning("Veuillez d'abord mettre à jour les données des actifs.")

elif st.session_state.portfolio_size>len(st.session_state.corresponding_assets):
    st.warning("Le nombre d'actifs à inclure dans le portefeuille est supérieur au nombre d'actifs correspondant à la note environnementale minimale.")

else:
    # Section pour la création du portefeuille
    st.header("Création du portefeuille")
    # Bouton pour créer le portefeuille
    if st.button("Créer le portefeuille"):
        with st.spinner("Création du portefeuille en cours..."):
            try:
                # Création du portefeuille
                portfolio = st.session_state.portfolio_manager.create_portfolio(
                    total_investment=st.session_state.total_investment,
                    min_notation=st.session_state.min_rating,
                    corresponding_assets=st.session_state.corresponding_assets,
                    size=st.session_state.portfolio_size
                )
                
                # Affichage des résultats
                st.success("Portefeuille créé avec succès!")
                
                # Performance du portefeuille
                st.subheader("Performance du portefeuille")
                st.write(f"Rendement annuel: {portfolio['annual_return']:.2f}%")
                st.write(f"Volatilité: {portfolio['volatility']:.2f}%")
                st.write(f"Ratio de Sharpe: {portfolio['sharpe_ratio']:.2f}")
                
                # Graphique de l'évolution du portefeuille
                st.subheader("Évolution du portefeuille")
                fig = px.line(portfolio['portfolio_value'], title="Valeur du portefeuille au fil du temps")
                st.plotly_chart(fig)
                
                # Répartition du portefeuille
                st.subheader("Répartition du portefeuille")
                fig = px.pie(
                    values=portfolio['weights'].values(),
                    names=portfolio['weights'].keys(),
                    title="Répartition des actifs"
                )
                st.plotly_chart(fig)
                
            except Exception as e:
                st.error(f"Erreur lors de la création du portefeuille: {str(e)}")

        

