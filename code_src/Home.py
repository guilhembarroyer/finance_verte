import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Investir avec Impact",
    page_icon="🌱",
    layout="wide"
)

# Titre principal
st.title("🌱 Investir avec Impact : Notre Engagement pour la Diversité et l'Inclusion")


st.write("Répertoire courant :", os.getcwd())
st.write("Contenu du dossier 'data' :", os.listdir("data"))

# Lecture des données Excel
try:

    df = pd.read_excel('data/actifs.xlsx')
    st.subheader("Données des Actifs et Notes D&I")
    st.info("""
    Les notations D&I (Diversité et Inclusion) sont définies préalablement dans ce fichier Excel pour chaque actif.
    Ces notes sont calculées selon notre méthodologie et prennent en compte tous les critères mentionnés ci-dessous.
    """)
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error("Impossible de charger les données Excel. Assurez-vous que le fichier data/actifs.xlsx existe.")

# Contenu du README
st.markdown("""
## Notre Philosophie d'Investissement

Bienvenue sur notre plateforme d'investissement responsable. Nous avons fait le choix stratégique et éthique de nous concentrer principalement sur les entreprises françaises, avec une attention particulière portée aux critères extra-financiers, notamment l'aspect social à travers le prisme de la Diversité et l'Inclusion.

La diversité et l'inclusion représentent des critères extra-financiers essentiels à nos yeux. Ces indicateurs reflètent l'engagement des organisations envers l'équité, la représentativité et le respect des différences au sein de leur structure.

## Notre Méthodologie d'Évaluation

Pour constituer notre portefeuille, nous avons analysé une quarantaine d'entreprises françaises selon une méthodologie rigoureuse et transparente, combinant labels officiels, engagements concrets et indicateurs de risque.

### Les Labels et Certifications que nous valorisons :
- **Label Diversité** : Délivré par l'AFNOR et reconnu par l'État français, ce label atteste de l'engagement concret d'une organisation à prévenir les discriminations et à promouvoir la diversité dans sa gestion des ressources humaines.
- **Label Égalité Professionnelle Hommes/Femmes** : Également délivré par l'AFNOR, il certifie les actions mises en œuvre pour garantir l'égalité professionnelle, incluant l'égalité de rémunération et l'accès équitable aux promotions.
- **Top Employer France** : Cette certification internationale reconnaît l'excellence des pratiques RH, incluant les politiques de diversité et d'inclusion dans un cadre plus large de bien-être au travail.
- **Collectif Économie Plus Inclusive** : Les membres de ce collectif s'engagent activement pour favoriser l'insertion professionnelle des personnes éloignées de l'emploi et soutenir une économie plus inclusive.
- **Charte de la Diversité** : Bien que non contraignante juridiquement, cette signature démontre un engagement public en faveur de la diversité et de la non-discrimination.

### Les Indicateurs de Risque que nous surveillons :
Pour équilibrer notre analyse, nous intégrons également des indicateurs de risque issus de Yahoo Finance (Sustainalytics) :

- **Score de Risque Social** : Ce score évalue la performance d'une entreprise sur les aspects sociaux, incluant les relations avec les employés, la diversité, les droits de l'homme, et l'impact communautaire (score de 0 = risque faible = positif).
- **Niveau de Controverse** : Ce score évalue l'implication d'une entreprise dans des incidents controversés qui peuvent avoir un impact négatif sur les parties prenantes, l'environnement ou les opérations de l'entreprise (score allant de 1 : controverse négligeable à 5 : controverse sévère).

Ces indicateurs de risque sont normalisés sur une échelle de 0 à 1 pour faciliter la comparaison.

### Notre Formule de Notation :
```
Score D&I = 1,2 × Label Diversité + 1,2 × Label Égalité Pro + 0,5 × Top Employer + Collectif Économie Plus Inclusive + Charte Diversité - Score de Risque Social normalisé - 0,5 × Niveau de Controverse normalisé
```

Cette formule accorde une importance particulière (coefficient 1,2) aux labels officiels de diversité et d'égalité professionnelle, qui sont les plus rigoureux et exigeants en termes d'engagement.

Le Top Employer est pondéré à 0,5 car, bien qu'important, il ne se concentre pas exclusivement sur la diversité et l'inclusion.

Les adhésions au Collectif Économie Plus Inclusive et à la Charte de la Diversité sont valorisées de manière standard (coefficient 1).

Les scores de risque social et de controverse viennent en déduction, pénalisant ainsi les entreprises confrontées à des problèmes dans ces domaines. Le niveau de controverse est pondéré à 0,5, lui accordant une importance moindre que les autres critères, tout en gardant un impact significatif sur la notation finale.


---

👉 Utilisez le menu à gauche pour accéder à la gestion de votre portefeuille.
""") 