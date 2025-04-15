# Investir avec Impact : Notre Engagement pour la Diversité et l'Inclusion

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

Cette méthodologie permet d'obtenir un score global qui équilibre engagements formels et performance réelle des entreprises en matière de diversité et d'inclusion.

## Notre Portefeuille

Les entreprises présentées dans votre portefeuille ont été sélectionnées par cette méthode et représentent notre vision d'un investissement qui concilie performance économique et impact social positif. Les valeurs sont pondérées dans le portefeuille en fonction de la taille et de leurs notes environnementales. 

Explorez notre sélection et découvrez comment investir avec nous pour soutenir les entreprises qui façonnent un avenir plus inclusif et équitable.

## Installation

1. Clonez le repository :
```bash
git clone https://github.com/votre-username/finance-verte.git
cd finance-verte
```

2. Créez un environnement virtuel et activez-le :
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix/MacOS
# ou
venv\Scripts\activate  # Sur Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Lancez l'application Streamlit :
```bash
streamlit run code_src/app.py
```

2. Dans l'interface :
   - Mettez à jour les données des actifs (cela prend un certain temps car téléchargement en ligne (yahoo finance) des données boursièress dans une démarche de modularité du projet)
   - Ajustez les paramètres du portefeuille dans la barre latérale
   - Créez votre portefeuille et visualisez les résultats

## Structure du Projet

```
finance-verte/
├── code_src/
│   ├── app.py              # Interface Streamlit
│   ├── portfolio_manager.py # Gestion du portefeuille
│   └── data_collector.py   # Collecte des données
├── data/
│   └── actifs.xlsx         # Données des actifs
├── requirements.txt        # Dépendances
└── README.md              # Documentation
```


## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 