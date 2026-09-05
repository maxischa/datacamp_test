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

Une séance de 2h. Le notebook de **cours** contient aussi les exercices : on montre une technique, vous la refaites aussitôt — d'abord un exercice à trous, puis un que vous écrivez entièrement. Les **exercices optionnels** sont là pour aller plus loin, et la **correction** — le cours entier, solutions comprises — est publiée après.

| Séance | Sujet | Cours + exercices | Optionnels | Correction |
|---|---|---|---|---|
| 1.1 | Prise en main — Colab, Markdown et vos premières lignes | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc1_python/cours/seance1_cours.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc1_python/exercices/seance1_exercices.ipynb) | [▶](https://colab.research.google.com/github/maxischa/datacamp_test/blob/main/bloc1_python/corrections/seance1_correction.ipynb) |

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

## Bloc 2 — Collecter, comprendre et manipuler des données (8h)

4 séances de 2h. Pour chacune, le notebook de **cours** alterne démonstration et pratique : on montre une technique, vous la refaites aussitôt, d'abord à trous puis de zéro. Les **exercices optionnels** vont plus loin ; la **correction** reprend le cours entier avec les solutions. Pour la séance 2.4, la dernière colonne n'est pas facultative : c'est l'**étude de cas en binôme**, qui occupe la seconde heure.

| Séance | Sujet | Cours + exercices | Optionnels | Correction |
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
