# Les données de la version 2 — l'immobilier parisien

Les ventes immobilières parisiennes publiées par la DGFiP, dans les
**demandes de valeurs foncières géolocalisées** (DGFiP / Etalab, licence
ouverte 2.0). Elles servent aux feuilles d'exercices des blocs 2, 3 et 4 de
la version 2 du cours.

| Fichier | Lignes | Pour | Contenu |
|---|---:|---|---|
| `immo_paris_sale.csv` | 61 276 | bloc 2 | l'export brut, volontairement sale |
| `immo_paris_2024.csv` | 25 209 | blocs 3.1, 4.1 et 4.2 | le résultat du nettoyage : une ligne = une vente d'appartement |
| `immo_paris_2023_2024.csv` | 52 941 | bloc 3.2 | les deux millésimes, plus une colonne `annee` |

## Pas de `build_data.py`, et c'est voulu

Les cinq autres blocs reconstruisent leurs CSV depuis une source publique par
un script versionné. **Pas ici.** Les feuilles d'exercices contiennent 114
valeurs attendues écrites en dur dans des cellules `verifier(...)`, calculées
sur ces octets précis. La source DVF est republiée avec des corrections
plusieurs fois par an : un fichier reconstruit aujourd'hui ferait échouer les
vérifications sans que rien ne l'explique.

> ⚠️ **Ne pas régénérer ces fichiers.** Les modifier suppose de recalculer les
> 114 valeurs attendues des cinq feuilles — voir le §4 du CLAUDE.md : toute
> valeur attendue se calcule sur les vraies données, jamais de tête.

C'est la même situation que `bloc6_llms/data/avis.csv`, et le dire vaut mieux
que de laisser croire à une reproductibilité qui n'existe pas.

## Une exception à la règle des 5 Mo

`immo_paris_sale.csv` pèse 5,8 Mo, au-dessus de la règle « chaque CSV ≤ 5 Mo »
du §10 du CLAUDE.md. L'exception est assumée : le fichier ne peut pas être
rééchantillonné sans casser les valeurs attendues ci-dessus, et jsDelivr sert
jusqu'à 20 Mo par fichier. Le téléchargement part de la machine virtuelle
Colab de l'étudiant, pas de sa tablette.
