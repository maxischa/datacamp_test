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

📄 **[Aide-mémoire pandas](ressources/cheatsheet_pandas.md)** — à garder ouvert
pendant les exercices.

---

## Les données du bloc 2

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

## Pour l'équipe enseignante

Ce dépôt est **purement étudiant**. La chaîne de production du cours reste sur
la machine de l'enseignant et n'est pas publiée :

| Reste local | Pourquoi |
|---|---|
| `bloc2_donnees/intervenant/` | cours minuté, notes de passation, pièges attendus |
| `outils/` | la source dont les notebooks sont générés — contient les mêmes notes et toutes les solutions |
| `Syllabus*.docx` | documents de travail de l'équipe |

Les quatre variantes d'une séance (cours, intervenant, exercices, correction)
sont **générées depuis une source unique**, une variante par usage. Un énoncé
ne peut donc pas diverger entre le notebook d'exercices et sa correction, et
une solution ne peut pas se retrouver par accident dans le notebook remis aux
étudiants.

Côté enseignant, deux commandes :

```bash
python outils/construire_notebooks.py   # regenere les 16 notebooks
python outils/verifier_notebooks.py     # les execute tous et controle les regles
```

L'adresse de ce dépôt est définie à un seul endroit (`outils/depot.py`) :
la changer et regénérer suffit à mettre à jour tous les badges « Open in
Colab » et toutes les URL de données.
