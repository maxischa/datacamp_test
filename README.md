# Data Camp 2026/2027

Introduction à Python pour la collecte et l'analyse de données — 36 heures.

> 📱 **Vous travaillez sur tablette ?** Lisez d'abord
> **[Bien démarrer](ressources/setup_tablette.md)**. Cinq minutes de réglages
> vous éviteront la plupart des blocages.

> ⚠️ À l'ouverture de chaque notebook : **Fichier → Enregistrer une copie dans
> Drive**, *avant* de taper quoi que ce soit. Sinon votre travail est perdu à
> la fermeture de l'onglet.

---

## Bloc 1 — Prise en main de Python et de Colab (2h)

Une séance de 2h. Le notebook de **cours** contient aussi les exercices : on montre une technique, vous la refaites aussitôt — d'abord un exercice à trous, puis un que vous écrivez entièrement. La **correction** — le cours entier, solutions comprises — est publiée après.

| Séance | Sujet | Cours + exercices | Correction |
|---|---|---|---|
| 1.1 | Prise en main — Colab, Markdown et vos premières lignes | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc1_python/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc1_python/corrections/seance1_correction.ipynb) |

📄 **[Bien démarrer — surtout sur tablette](ressources/setup_tablette.md)** — à garder ouvert pendant les exercices.

---

### Les données du bloc 1

Un seul fichier, minuscule, pour la dernière cellule de la séance :
charger des données depuis le web tient en une ligne, et c'est tout
le bloc 2 qui commence là.

| Fichier | Lignes | Contenu |
|---|---|---|
| `premieres_ventes.csv` | 20 | Vingt lignes du détaillant du bloc 2 : `date`, `produit`, `qte`, `prix`, `pays` |

Extrait de `bloc2_donnees/data/ventes.csv`. Construction reproductible par [`bloc1_python/data/build_data.py`](bloc1_python/data/build_data.py).

---

## Bloc 2 — Collecter, comprendre et manipuler des données (6h)

3 séances de 2h. Pour chacune, le notebook de **cours** alterne démonstration et pratique : on montre une technique, vous la refaites aussitôt, d'abord à trous puis de zéro. La **correction** reprend le cours entier avec les solutions.

| Séance | Sujet | Cours + exercices | Correction |
|---|---|---|---|
| 2.1 | Charger et comprendre un jeu de données | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/corrections/seance1_correction.ipynb) |
| 2.2 | Nettoyer des données réelles | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance2_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/corrections/seance2_correction.ipynb) |
| 2.3 | Agréger, croiser et visualiser | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance3_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/corrections/seance3_correction.ipynb) |

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

4 séances de 2h. Pour chacune : le notebook de **cours** est suivi en séance, les **exercices** se font en autonomie, la **correction** est publiée après.

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

4 séances de 2h. Pour chacune : le notebook de **cours** est suivi en séance, les **exercices** se font en autonomie, la **correction** est publiée après.

| Séance | Sujet | Cours | Exercices | Correction |
|---|---|---|---|---|
| 4.1 | Le Machine Learning : prédire n'est pas expliquer | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/corrections/seance1_correction.ipynb) |
| 4.2 | Prédire une décision — qui va résilier ? | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance2_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/exercices/seance2_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/corrections/seance2_correction.ipynb) |
| 4.3 | Arbres de décision — comprendre les variables qui déterminent la prédiction | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance3_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/exercices/seance3_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/corrections/seance3_correction.ipynb) |
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

## Bloc 5 — A/B testing (6h)

Six heures en trois temps. Le notebook de **cours** occupe les deux premières heures, l'**étude de cas** les deux suivantes, et la **correction** — publiée après — sert de support aux deux dernières.

| Séance | Sujet | Cours | Exercices | Correction |
|---|---|---|---|---|
| 5.1 | A/B testing — causalité et expériences randomisées | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc5_abtest/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc5_abtest/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc5_abtest/corrections/seance1_correction.ipynb) |

📄 **[Aide-mémoire statistiques](ressources/cheatsheet_stats.md)** — à garder ouvert pendant les exercices.

---

### Les données du bloc 5

Une **vraie expérience randomisée** : 64 000 clients d'un site de vente
en ligne, tirés au sort entre trois campagnes email. C'est la
randomisation qui autorise à parler d'effet causal — pas la taille du
fichier.

| Fichier | Lignes | Contenu |
|---|---|---|
| `hillstrom.csv` | 64 000 | Un client par ligne. Avant : `recency`, `history`, `mens`, `womens`, `zip_code`, `newbie`, `channel`. Tiré au sort : `segment`. Après : `visit`, `conversion`, `spend` |
| `online_classroom.csv` | 323 | L'essai randomisé « cours en ligne » du cours : `format_ol`, `format_blended`, `falsexam` |

Kevin Hillstrom, [*The MineThatData E-Mail Analytics and Data Mining Challenge*](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html), 2008.
L'essai « cours en ligne » vient du [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/) (MIT).
Construction reproductible par [`bloc5_abtest/data/build_data.py`](bloc5_abtest/data/build_data.py).

---

## Bloc 6 — Science des données et LLMs (4h)

Quatre heures en deux temps. Le notebook de **cours** occupe les deux premières heures — comprendre un LLM, puis les moyens de l'augmenter — et se termine par la création de votre clé API. L'**atelier** occupe les deux suivantes ; sa **correction** est publiée après.

| Séance | Sujet | Cours | Exercices | Correction |
|---|---|---|---|---|
| 6.1 | Science des données et LLMs | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc6_llms/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc6_llms/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc6_llms/corrections/seance1_correction.ipynb) |

📄 **[Aide-mémoire pandas](ressources/cheatsheet_pandas.md)** — à garder ouvert pendant les exercices.

---

### Les données du bloc 6

Cinquante et un avis clients, dont un tiers **sarcastiques** : « Une
expérience exceptionnelle, personne ne répond depuis une semaine ». Le
sarcasme est le terrain d'entente du bloc, parce que le sentiment réel y
dépend du rapport entre deux morceaux de phrase — exactement ce qu'un
classifieur spécialisé et un LLM génératif ne traitent pas de la même façon.

| Fichier | Lignes | Contenu |
|---|---|---|
| `avis.csv` | 51 | Un avis par ligne : `text`, `rating`, `type`, `sentiment`, `sarcasm` |

Avis **fictifs, écrits pour ce cours** : il n'y a pas de source publique, donc pas de `build_data.py`
reproductible comme dans les autres blocs. Ce fichier n'est pas un benchmark et les taux de réussite
mesurés en séance ne valent que pour lui.

---

# Version 2 — le parcours allégé

Une seconde version du cours, plus courte : **30 heures** au lieu de 36. Elle
suit le même fil et s'appuie sur les mêmes outils, mais elle va moins loin sur
les blocs 3 et 4, et elle consacre beaucoup plus de temps à la pratique en
autonomie — un long fil d'exercices sur les ventes immobilières parisiennes,
du fichier brut jusqu'au modèle.

**La version 1 reste au-dessus, intacte.** Ce qui a été retiré de la version 2
n'est pas perdu : chaque bloc renvoie, sous « Pour aller plus loin », vers les
séances de la version 1 qui le prolongent.

---

## Bloc 1 — Prise en main de Python et de Colab (2h)

Identique à la version 1 : mêmes notebooks, rien à dupliquer.

| Séance | Sujet | Cours + exercices | Correction |
|---|---|---|---|
| 1.1 | Prise en main — Colab, Markdown et vos premières lignes | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc1_python/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc1_python/corrections/seance1_correction.ipynb) |

📄 **[Bien démarrer — surtout sur tablette](ressources/setup_tablette.md)** — à garder ouvert pendant les exercices.


---

## Bloc 2 — Collecter, comprendre et manipuler des données (6h)

Six heures en deux temps. Le notebook de **cours** occupe les deux premières heures et contient aussi ses exercices : on montre une technique, vous la refaites aussitôt. L'**étude de cas** occupe les quatre suivantes — un export immobilier parisien de 61 000 lignes, du fichier brut jusqu'à la carte des prix. Entre les deux, une séance **à faire seul** — elle est ci-dessous, et l'étude de cas en a besoin. Chaque travail a sa **solution**, publiée après.

| Séance | Sujet | Cours + exercices | Solution cours + exercices | Étude de cas | Solution étude de cas |
|---|---|---|---|---|---|
| 2.1 | Charger, comprendre et nettoyer une base de données | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees_v2/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees_v2/corrections/seance1_correction.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees_v2/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees_v2/corrections/seance1_correction_etude.ipynb) |

### 📘 À faire en autonomie — avant la partie 3 de l'étude de cas

**Les deux heures de cours ne suffisent pas à finir l'étude de cas.** Ses parties 3 et 4 tracent un histogramme, des barres, une courbe et un nuage de points, et calculent une corrélation — et le notebook de cours n'en montre aucun.

C'est cette séance-ci qui les enseigne, `groupby` et `merge` compris, avec ses exercices dans le fil comme la 2.1. **Comptez deux heures, seul, entre la séance et l'étude de cas.** Le notebook de l'étude de cas vous le rappelle au bon endroit.

| Séance | Sujet | Cours + exercices | Solution |
|---|---|---|---|
| 2.2 | Agréger, croiser et visualiser une base de données | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees_v2/cours/seance2_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees_v2/corrections/seance2_correction.ipynb) |

📚 **Pour aller plus loin**

- **Le bloc 2 de la version 1, en trois séances** — [2.1 — Charger et comprendre ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance1_cours.ipynb) · [2.2 — Nettoyer des données réelles ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance2_cours.ipynb) · [2.3 — Agréger, croiser et visualiser ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc2_donnees/cours/seance3_cours.ipynb)

📄 **[Aide-mémoire pandas](ressources/cheatsheet_pandas.md)** — à garder ouvert pendant les exercices.

---

### Les données du bloc 2 (version 2)

Deux terrains. Le **cours** prend en main le détaillant en ligne de la
version 1 — mêmes fichiers, rien de nouveau à télécharger. L'**étude de
cas** travaille sur les ventes immobilières parisiennes publiées par
l'administration fiscale, dans l'état où on les reçoit.

| Fichier | Lignes | Contenu |
|---|---|---|
| `immo_paris_sale.csv` | 61 276 | L'export brut, **volontairement sale** : dates en deux écritures, prix en texte, catégories mal saisies, surfaces manquantes |
| `immo_paris_2024.csv` | 25 209 | Le résultat du nettoyage : une ligne = une vente d'appartement. `vente_id`, `date`, `prix`, `rue`, `arrondissement`, `surface`, `pieces`, `longitude`, `latitude`, `prix_m2` |
| `immo_paris_2023_2024.csv` | 52 941 | Les deux millésimes, plus une colonne `annee` — pour les blocs 3 et 4 de la version 2 |
| `ventes.csv`, `clients.csv`, `produits.csv`, `ventes_sale.csv` | — | Les fichiers du bloc 2 de la version 1, repris tels quels par le cours |

Immobilier : demandes de valeurs foncières géolocalisées ([DGFiP / Etalab](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/), licence ouverte 2.0).
**Ces trois fichiers ne se régénèrent pas** : les feuilles d'exercices contiennent 114 valeurs attendues calculées sur ces octets précis, et la source est republiée avec des corrections plusieurs fois par an. Le détail est dans [`bloc2_donnees_v2/data/README.md`](bloc2_donnees_v2/data/README.md).

---

## Bloc 3 — Interpréter des données (8h)

2 séances de 4h. Pour chacune : deux heures de **cours** suivies en séance, puis deux heures d'**étude de cas** — un seul long exercice sur l'immobilier parisien, qui reprend le fichier là où le bloc 2 l'avait laissé. La **correction** est publiée après.

| Séance | Sujet | Cours | Étude de cas | Correction |
|---|---|---|---|---|
| 3.1 | Décrire une distribution | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats_v2/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats_v2/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats_v2/corrections/seance1_correction.ipynb) |
| 3.2 | Comparer deux groupes — hasard ou vrai écart ? | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats_v2/cours/seance2_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats_v2/exercices/seance2_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats_v2/corrections/seance2_correction.ipynb) |

📚 **Pour aller plus loin**

- **Les deux séances que le parcours allégé ne reprend pas** — [3.3 — Relier deux variables ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance3_cours.ipynb) · [3.4 — Régression linéaire ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance4_cours.ipynb)
- **Le bloc 3 de la version 1, en quatre séances** — [3.1 — Décrire une distribution ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance1_cours.ipynb) · [3.2 — Comparer deux groupes ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance2_cours.ipynb) · [3.3 — Relier deux variables ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance3_cours.ipynb) · [3.4 — Régression linéaire ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc3_stats/cours/seance4_cours.ipynb)

📄 **[Aide-mémoire statistiques](ressources/cheatsheet_stats.md)** · **[Aide-mémoire pandas](ressources/cheatsheet_pandas.md)** — à garder ouvert pendant les exercices.

---

### Les données du bloc 3 (version 2)

Deux terrains, comme au bloc 2. Le **cours** décrit les commandes du
détaillant — mêmes fichiers que la version 1. Les **exercices**
poursuivent le fil immobilier : le fichier que vous avez nettoyé au
bloc 2 devient ici un estimateur de prix, puis vingt tests.

| Fichier | Lignes | Contenu |
|---|---|---|
| `commandes.csv` | 1 955 | Une commande par ligne : `cmd_id`, `date`, `jour`, `ca`, `nart`, `qte`, `pays`, `client_id` — repris du bloc 3 de la version 1 |
| `immo_paris_2024.csv` | 25 209 | Les ventes d'appartements parisiens de 2024, nettoyées au bloc 2 — pour la séance 3.1 |
| `immo_paris_2023_2024.csv` | 52 941 | Les deux millésimes, plus une colonne `annee` — pour comparer 2023 et 2024 en séance 3.2 |

Commandes : dérivées des fichiers du bloc 2 par [`bloc3_stats/data/build_data.py`](bloc3_stats/data/build_data.py).
Immobilier : voir [les données du bloc 2 (version 2)](#les-données-du-bloc-2-version-2) — les fichiers sont servis depuis `bloc2_donnees_v2/data/` et **ne se régénèrent pas**.

---

## Bloc 4 — Introduction au machine learning (8h)

2 séances de 4h. Pour chacune : deux heures de **cours** suivies en séance, puis deux heures d'**étude de cas** — on prédit d'abord un prix au mètre carré, puis on construit un radar qui repère les biens de prestige et on chiffre en euros le coût de chaque erreur. La **correction** est publiée après.

| Séance | Sujet | Cours | Étude de cas | Correction |
|---|---|---|---|---|
| 4.1 | Le Machine Learning : prédire n'est pas expliquer | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml_v2/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml_v2/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml_v2/corrections/seance1_correction.ipynb) |
| 4.2 | Prédire une décision — qui va résilier ? | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml_v2/cours/seance2_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml_v2/exercices/seance2_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml_v2/corrections/seance2_correction.ipynb) |

📚 **Pour aller plus loin**

- **Les deux séances que le parcours allégé ne reprend pas** — [4.3 — Arbres de décision et interprétation ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance3_cours.ipynb) · [4.4 — Segmenter sans étiquette ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance4_cours.ipynb)
- **Le bloc 4 de la version 1, en quatre séances** — [4.1 — Prédire n'est pas expliquer ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance1_cours.ipynb) · [4.2 — Prédire une décision ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance2_cours.ipynb) · [4.3 — Arbres de décision ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance3_cours.ipynb) · [4.4 — Segmenter sans étiquette ▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc4_ml/cours/seance4_cours.ipynb)

📄 **[Aide-mémoire machine learning](ressources/cheatsheet_ml.md)** · **[Aide-mémoire pandas](ressources/cheatsheet_pandas.md)** — à garder ouvert pendant les exercices.

---

### Les données du bloc 4 (version 2)

Trois terrains. Le **cours** garde ceux de la version 1 : les commandes
du détaillant pour prédire un montant, un opérateur télécom pour prédire
une résiliation. Les **exercices** restent sur l'immobilier parisien, et
bouclent le fil ouvert au bloc 2 — le fichier que vous avez nettoyé
devient enfin un modèle.

| Fichier | Lignes | Contenu |
|---|---|---|
| `commandes.csv` | 1 955 | Une commande par ligne — repris du bloc 4 de la version 1, pour la séance 4.1 |
| `churn.csv` | 7 043 | Un abonné télécom par ligne : `anc`, `mensuel`, `total`, `contrat`, `internet`, `paiement`, `senior`, `couple`, `support`, `churn` — pour la séance 4.2 |
| `immo_paris_2024.csv` | 25 209 | Les ventes d'appartements parisiens de 2024 — les deux feuilles d'exercices |

Churn : [IBM Telco Customer Churn](https://github.com/IBM/telco-customer-churn-on-icp4d). Commandes : dérivées des
fichiers du bloc 2 par [`bloc4_ml/data/build_data.py`](bloc4_ml/data/build_data.py).
Immobilier : voir [les données du bloc 2 (version 2)](#les-données-du-bloc-2-version-2) — servi depuis `bloc2_donnees_v2/data/`, et **ne se régénère pas**.

---

## Bloc 5 — A/B testing (6h)

Identique à la version 1 : mêmes notebooks, rien à dupliquer.

| Séance | Sujet | Cours | Étude de cas | Correction |
|---|---|---|---|---|
| 5.1 | A/B testing — causalité et expériences randomisées | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc5_abtest/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc5_abtest/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc5_abtest/corrections/seance1_correction.ipynb) |

📄 **[Aide-mémoire statistiques](ressources/cheatsheet_stats.md)** — à garder ouvert pendant les exercices.

---

## Pour aller beaucoup plus loin — science des données et LLMs (4h)

Le bloc 6 de la version 1 ne fait pas partie du parcours allégé. Il reste
publié pour qui veut continuer : comprendre ce qu'est un grand modèle de
langage et où il échoue, distinguer LLM, RAG, appel d'outils, agent et MCP,
puis appeler un modèle depuis Python sur un corpus d'avis clients.

| Séance | Sujet | Cours | Atelier | Correction |
|---|---|---|---|---|
| 6.1 | Science des données et LLMs | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc6_llms/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc6_llms/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc6_llms/corrections/seance1_correction.ipynb) |

