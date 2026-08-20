# Aide-mémoire A/B testing — bloc 5

Gardez cette page ouverte pendant l'étude de cas. Sur tablette,
**copiez-collez** depuis ici plutôt que de retaper.

L'aide-mémoire statistiques reste valable : on compare toujours deux groupes,
avec les mêmes outils. Ce qui change, c'est le **droit** d'appeler l'écart un
effet. Ce droit vient du tirage au sort, pas de la commande.

Dans tous les exemples, `data` désigne la table des 64 000 clients.

---

## Les imports du bloc 5

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy import stats                       # deja vu en seance 3.2
```

Et les trois noms de groupes, déclarés une fois pour ne plus les retaper :

```python
AUCUN, HOMME, FEMME = "No E-Mail", "Mens E-Mail", "Womens E-Mail"
```

---

## Le vocabulaire

| Notation | Ce que c'est | Ici |
|---|---|---|
| $T_i$ | le **traitement** reçu par $i$, 0 ou 1 | recevoir l'email |
| $Y_i$ | le **résultat** observé | `spend`, `conversion`, `visit` |
| $Y_{0i}$ | ce que $i$ aurait obtenu **sans** traitement | inobservable si traité |
| $Y_{1i}$ | ce que $i$ aurait obtenu **avec** | inobservable si témoin |
| ATE | $E[Y_1 - Y_0]$, l'effet moyen sur tous | ce qu'on estime |
| ATT | $E[Y_1 - Y_0 \mid T=1]$, l'effet sur les traités | souvent plus accessible |

**Contrefactuel** = le résultat potentiel qui ne s'est pas produit. On ne
l'observe **jamais**. C'est le problème fondamental de l'inférence causale.

## La formule qui contient tout

$$
E[Y \mid T=1]-E[Y \mid T=0]
=
\underbrace{E[Y_1-Y_0 \mid T=1]}_{\text{l'effet causal}}
+
\underbrace{E[Y_0 \mid T=1]-E[Y_0 \mid T=0]}_{\text{le biais de sélection}}
$$

Une différence de moyennes = l'effet **plus** le biais. Le biais est l'écart
qui séparerait les deux groupes **si personne n'avait été traité**. Le tirage
au sort l'annule ; rien d'autre ne l'annule gratuitement.

---

## Vérifier que le tirage au sort a fonctionné

À faire **avant** toute analyse, sur les variables mesurées *avant* l'envoi.

```python
data.groupby("segment").agg(
    clients=("segment", "size"),
    recence=("recency", "mean"),
    passe=("history", "mean"),
    nouveaux=("newbie", "mean"),
).round(3)
```

| Ce que vous lisez | Ce qu'on en dit |
|---|---|
| les trois lignes se ressemblent | randomisation crédible, on peut continuer |
| une colonne décroche nettement | **arrêtez tout** : ce n'est pas une expérience |
| de petits écarts sur un petit échantillon | normal — l'égalité est garantie *en espérance* |
| des lignes **parfaitement** identiques | suspect : trop beau pour un tirage au sort |

---

## Mesurer l'effet

```python
resultats = data.groupby("segment").agg(
    clients=("segment", "size"),
    visite=("visit", "mean"),
    achat=("conversion", "mean"),
    depense=("spend", "mean"),
)
resultats.round(4)            # NE PAS arrondir avant de calculer les effets
```

> 💡 Pour une colonne qui ne vaut que 0 ou 1, la **moyenne est la proportion
> de 1**. Pas besoin de diviser à la main.

```python
ecart = resultats.loc[HOMME, "achat"] - resultats.loc[AUCUN, "achat"]

100 * ecart                                     # effet ABSOLU, en points
100 * ecart / resultats.loc[AUCUN, "achat"]     # effet RELATIF, en %
```

| Formulation | Quand la choisir |
|---|---|
| **absolue** (+0,68 point) | toujours honnête, parfois peu spectaculaire |
| **relative** (+119 %) | vraie aussi, mais gonfle quand le départ est minuscule |
| **les deux** (« de 0,57 % à 1,25 % ») | ce qu'on met sur une slide qu'on assume |

---

## Mesurer l'incertitude

```python
def comparer(a, b):
    """Effet, intervalle a 95 % et p-value entre deux groupes."""
    effet = a.mean() - b.mean()
    es = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
    p = stats.ttest_ind(a, b, equal_var=False).pvalue
    return pd.Series({"effet": effet, "bas_95": effet - 1.96 * es,
                      "haut_95": effet + 1.96 * es, "p_value": p})


comparer(data.query("segment == @HOMME")["spend"],
         data.query("segment == @AUCUN")["spend"]).round(4)
```

La même fonction marche pour un taux (`conversion`, `visit`) et pour un
montant (`spend`) : une colonne 0/1 est une colonne comme une autre.

| Ce que vous lisez | Ce qu'on en dit |
|---|---|
| l'intervalle **exclut** zéro | l'effet n'est pas explicable par le seul hasard |
| l'intervalle **contient** zéro | on ne conclut rien — ce n'est pas « l'effet est nul » |
| l'intervalle très large | l'échantillon est trop petit pour trancher |
| p minuscule | l'effet est **mesuré précisément**, pas forcément **grand** |

> ⚠️ On ne dit pas « il y a 95 % de chances que l'effet soit dans
> l'intervalle ». On dit : la procédure capture le vrai effet dans 95 % des
> expériences répétées.

---

## De la statistique à la décision

```python
CIBLE, MARGE, COUT = 100_000, 0.40, 0.05

r = comparer(data.query("segment == @HOMME")["spend"], dep_aucun)
for nom in ["effet", "bas_95", "haut_95"]:
    net = r[nom] * MARGE - COUT
    print(nom, round(net, 3), "$/client |", round(net * CIBLE), "$ au total")
```

Refaire le calcul **aux deux bornes** de l'intervalle est l'argument le plus
convaincant qu'on puisse porter devant une direction : si la campagne est
rentable même dans le scénario le plus prudent, la décision est robuste. Cela
parle infiniment plus qu'une p-value.

---

## Croiser deux variables

```python
seg = data.pivot_table(values="spend", index="channel",
                       columns="segment", aggfunc="mean")
seg["effet_homme"] = seg[HOMME] - seg[AUCUN]
seg[["effet_homme"]].round(3)
```

Ce qu'on trouve en découpant **après coup** est une **hypothèse**, jamais un
résultat : plus on multiplie les découpages, plus on finit par tomber sur une
fluctuation qui ressemble à un effet. Une hypothèse intéressante se confirme
par une **nouvelle** expérience, avec le KPI fixé à l'avance.

---

## Les erreurs les plus fréquentes du bloc 5

| L'erreur | Ce qui se passe | Le réflexe |
|---|---|---|
| `data.groupby("segment").mean()` | `TypeError` sur les colonnes texte | choisir les colonnes : `[["visit", "spend"]]` |
| **conditionner sur une variable post-traitement** | rien, un chiffre s'affiche, il est faux | ne filtrer que sur des variables mesurées **avant** |
| comparer sans regarder l'équilibre | rien, un chiffre s'affiche | le tableau d'équilibre d'abord, toujours |
| arrondir avant de calculer un effet relatif | 118 % au lieu de 119 % | arrondir **à l'affichage**, jamais avant |
| « A bat le témoin plus fort que B, donc A bat B » | conclusion non fondée | tester **A contre B** directement |
| « p > 0,05, donc pas d'effet » | conclusion inversée | absence de preuve ≠ preuve d'absence |
| `"sum"` au lieu de `"mean"` pour un taux | un total de clients au lieu d'une proportion | la moyenne d'une colonne 0/1 **est** la proportion |

> 📌 La deuxième ligne est l'erreur n° 1 des analyses A/B en entreprise :
> « taux de conversion des ouvreurs », « panier moyen des cliqueurs ». Le code
> tourne parfaitement. Le résultat n'a aucun sens causal.
