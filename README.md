# Data Camp 2026/2027

Introduction à Python pour la collecte et l'analyse de données — 36 heures.

> 📱 **Vous travaillez sur tablette ?** Lisez d'abord
> **[Bien démarrer](ressources/setup_tablette.md)**. Cinq minutes de réglages
> vous éviteront la plupart des blocages.

> ⚠️ À l'ouverture de chaque notebook : **Fichier → Enregistrer une copie dans
> Drive**, *avant* de taper quoi que ce soit. Sinon votre travail est perdu à
> la fermeture de l'onglet.

---

## Bloc 2 — Collecter, comprendre et manipuler des données (8h)

Quatre séances de 2h. Pour chacune : le notebook de **cours** est suivi en
séance, les **exercices** se font en autonomie, la **correction** est publiée
après.

| Séance | Sujet | Cours | Exercices | Correction |
|---|---|---|---|---|
| 2.1 | Charger et comprendre un jeu de données | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/corrections/seance1_correction.ipynb) |
| 2.2 | Nettoyer des données réelles | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance2_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/exercices/seance2_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/corrections/seance2_correction.ipynb) |
| 2.3 | Agréger et croiser plusieurs tables | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance3_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/exercices/seance3_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/corrections/seance3_correction.ipynb) |
| 2.4 | Visualiser et conclure — étude de cas | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance4_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/exercices/seance4_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/corrections/seance4_correction.ipynb) |

📄 **[Aide-mémoire pandas](ressources/cheatsheet_pandas.md)** — à garder ouvert pendant les exercices.

---

### Les données du bloc 2

Un détaillant en ligne européen, décembre 2010 à décembre 2011.
Les fichiers se chargent **directement depuis le web** : rien à télécharger.

| Fichier | Lignes | Contenu |
|---|---|---|
| `ventes.csv` | 45 123 | Une ligne par produit vendu : `date`, `cmd_id`, `prod_id`, `qte`, `prix`, `client_id` |
| `clients.csv` | 472 | Un client par ligne : `client_id`, `pays`, `segment`, `date_insc` |
| `produits.csv` | 2 956 | Un produit par ligne : `prod_id`, `libelle`, `categorie` |
| `ventes_sale.csv` | 5 370 | Un extrait **volontairement sale**, pour la séance 2.2 |

Source : [UCI Machine Learning Repository — Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii).
Construction reproductible par [`bloc2_donnees/data/build_data.py`](bloc2_donnees/data/build_data.py).

---

## Bloc 3 — Interpréter des données (8h)

Quatre séances de 2h. Pour chacune : le notebook de **cours** est suivi en
séance, les **exercices** se font en autonomie, la **correction** est publiée
après.

| Séance | Sujet | Cours | Exercices | Correction |
|---|---|---|---|---|
| 3.1 | Décrire une distribution | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/corrections/seance1_correction.ipynb) |
| 3.2 | Comparer deux groupes — hasard ou vrai écart ? | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance2_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/exercices/seance2_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/corrections/seance2_correction.ipynb) |
| 3.3 | Relier deux variables — y a-t-il un lien ? | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance3_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/exercices/seance3_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/corrections/seance3_correction.ipynb) |
| 3.4 | Régression linéaire — expliquer, et de combien | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance4_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/exercices/seance4_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/corrections/seance4_correction.ipynb) |

📄 **[Aide-mémoire statistiques](ressources/cheatsheet_stats.md)** · **[Aide-mémoire pandas](ressources/cheatsheet_pandas.md)** — à garder ouvert pendant les exercices.

---

### Les données du bloc 3

Le même détaillant que le bloc 2, mais à une **maille** différente :
on ne raisonne plus par ligne de vente, on raisonne par commande et
par client — des individus statistiques comparables entre eux.

| Fichier | Lignes | Contenu |
|---|---|---|
| `commandes.csv` | 1 955 | Une commande par ligne : `cmd_id`, `date`, `jour`, `ca`, `nart`, `qte`, `pays`, `client_id` |
| `clients_ca.csv` | 472 | Un client par ligne : `client_id`, `ca`, `ncmd`, `nprod`, `anc`, `pays` |

Dérivées des fichiers du bloc 2 par [`bloc3_stats/data/build_data.py`](bloc3_stats/data/build_data.py).

---

## Bloc 4 — Introduction au machine learning (8h)

Quatre séances de 2h. Pour chacune : le notebook de **cours** est suivi en
séance, les **exercices** se font en autonomie, la **correction** est publiée
après.

| Séance | Sujet | Cours | Exercices | Correction |
|---|---|---|---|---|
| 4.1 | Prédire un nombre — expliquer n'est pas prédire | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/corrections/seance1_correction.ipynb) |
| 4.2 | Prédire une décision — qui va résilier ? | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance2_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/exercices/seance2_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/corrections/seance2_correction.ipynb) |
| 4.3 | Arbres et forêts — ce qui fait vraiment la prédiction | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance3_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/exercices/seance3_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/corrections/seance3_correction.ipynb) |
| 4.4 | Segmenter sans étiquette — quatre clients, quatre traitements | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance4_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/exercices/seance4_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/corrections/seance4_correction.ipynb) |

📄 **[Aide-mémoire machine learning](ressources/cheatsheet_ml.md)** · **[Aide-mémoire pandas](ressources/cheatsheet_pandas.md)** — à garder ouvert pendant les exercices.

---

### Les données du bloc 4

Deux terrains. Le détaillant des blocs 2 et 3 sert à prédire un montant
et à segmenter la clientèle ; un opérateur télécom sert à prédire une
résiliation, parce qu'il offre une cible binaire nette et des facteurs
explicatifs bien plus riches.

| Fichier | Lignes | Contenu |
|---|---|---|
| `churn.csv` | 7 043 | Un abonné télécom par ligne : `anc`, `mensuel`, `total`, `contrat`, `internet`, `paiement`, `senior`, `couple`, `support`, `churn` |
| `commandes.csv` | 1 955 | Une commande du détaillant, reprise du bloc 3 |
| `clients_rfm.csv` | 472 | Un client par ligne : `recence`, `freq`, `montant`, `pays` |
| `produits_profil.csv` | 1 263 | Une référence vendue au moins 10 fois : `nb_cmd`, `qte`, `ca`, `prix`, `pays`, `clients`, `part_q4` |

Churn : [IBM Telco Customer Churn](https://github.com/IBM/telco-customer-churn-on-icp4d). Le reste dérive des
fichiers du bloc 2. Construction reproductible par [`bloc4_ml/data/build_data.py`](bloc4_ml/data/build_data.py).

---

## Pour l'équipe enseignante

Ce dépôt est **purement étudiant**. La chaîne de production du cours reste sur
la machine de l'enseignant et n'est pas publiée :

| Reste local | Pourquoi |
|---|---|
| `bloc*/intervenant/` | cours minuté, notes de passation, pièges attendus |
| `outils/` | la source dont les notebooks sont générés — contient les mêmes notes et toutes les solutions |
| `Syllabus*.docx` | documents de travail de l'équipe |

Les quatre variantes d'une séance (cours, intervenant, exercices, correction)
sont **générées depuis une source unique**, une variante par usage. Un énoncé
ne peut donc pas diverger entre le notebook d'exercices et sa correction, et
une solution ne peut pas se retrouver par accident dans le notebook remis aux
étudiants.

Côté enseignant, trois commandes :

```bash
python outils/construire_notebooks.py   # regenere les notebooks
python outils/construire_readme.py      # regenere cette page
python outils/verifier_notebooks.py     # les execute tous et controle les regles
```

L'adresse de ce dépôt est définie à un seul endroit (`outils/depot.py`) :
la changer et regénérer suffit à mettre à jour tous les badges « Open in
Colab », tous les liens de cette page et toutes les URL de données.
