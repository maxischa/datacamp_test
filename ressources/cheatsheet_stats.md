# Aide-mémoire statistiques — bloc 3

Gardez cette page ouverte pendant les exercices. Sur tablette, **copiez-collez**
depuis ici plutôt que de retaper.

L'aide-mémoire pandas reste valable : on continue de charger, filtrer et
grouper. Ce qui change, c'est ce qu'on fait ensuite. La colonne **« ce qu'on
en dit »** est le vrai sujet du bloc — une commande sans interprétation ne
vaut rien.

Dans tous les exemples, `cmd` désigne la table des commandes.

---

## Les imports du bloc 3

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy import stats                       # seances 3.2 et 3.3
import statsmodels.formula.api as smf         # seance 3.4
```

---

## Décrire une distribution (3.1)

```python
cmd["ca"].describe()          # count, mean, std, min, quartiles, max
cmd["ca"].mean()              # la moyenne
cmd["ca"].median()            # la mediane
cmd["ca"].std()               # l'ecart-type
cmd["ca"].quantile(0.9)       # le seuil des 10 % du haut
cmd["ca"].nunique()           # nombre de valeurs distinctes
```

| Ce que vous lisez | Ce qu'on en dit |
|---|---|
| moyenne ≫ médiane | distribution asymétrique : **citez la médiane** |
| écart-type > moyenne | il n'y a pas de valeur typique du tout |
| un groupe à faible effectif | ne commentez pas : regardez `count` d'abord |

```python
# La concentration : quelle part du total tient dans le haut du classement
top = cmd["ca"].sort_values(ascending=False)
100 * top.head(int(0.10 * len(cmd))).sum() / top.sum()
```

> **Jamais de moyenne de moyennes.** `df.groupby("pays")["ca"].mean().mean()`
> donne le même poids à un pays de 800 commandes et à un pays d'une seule.
> Repartez toujours des données individuelles.

---

## Comparer deux groupes (3.2)

```python
fr = cmd.query("pays == 'France'")["ca"]
de = cmd.query("pays == 'Allemagne'")["ca"]

# L'intervalle de confiance a 95 %, par reechantillonnage
boot = pd.Series([fr.sample(len(fr), replace=True, random_state=i).mean()
                  for i in range(1000)])
boot.quantile(0.025), boot.quantile(0.975)

# Le test
stats.ttest_ind(fr, de, equal_var=False).pvalue
```

| p-value | Ce qu'on en dit |
|---|---|
| **p < 0,05** | l'écart serait rare si les groupes étaient identiques : on le retient |
| **p ≥ 0,05** | l'écart est compatible avec le hasard : **on ne conclut rien** |

> « Pas de différence détectable » **n'est pas** « pas de différence ».

Avant tout test, deux vérifications :

```python
cmd.groupby("pays")["client_id"].nunique()   # combien d'individus, pas de lignes
round(irl.mean() - uk.mean(), 2)             # la taille de l'effet, en euros
```

---

## Relier deux variables (3.3)

| Variable 1 | Variable 2 | Outil |
|---|---|---|
| qualitative | qualitative | tableau croisé + khi-deux |
| quantitative | quantitative | nuage de points + corrélation |
| qualitative | quantitative | comparaison de moyennes (3.2) |

```python
# Deux qualitatives
cmd["taille"] = pd.cut(cmd["ca"], [0, 200, 500, 1e9],
                       labels=["petite", "moyenne", "grande"])
tab = pd.crosstab(cmd["pays"], cmd["taille"])
khi2, p, ddl, attendus = stats.chi2_contingency(tab)

# Ou est la dependance ? Dans les ecarts a l'attendu, jamais dans la p-value
att = pd.DataFrame(attendus, index=tab.index, columns=tab.columns)
(tab - att).round(1)
```

```python
# Deux quantitatives — on TRACE d'abord
cmd.plot(kind="scatter", x="qte", y="ca", alpha=0.3, figsize=(7, 4))

cmd[["ca", "nart", "qte"]].corr()                    # Pearson (droite)
cmd["ca"].corr(cmd["nart"], method="spearman")       # Spearman (rangs)
```

| Ce que vous voyez | Ce qu'on en dit |
|---|---|
| Pearson ≪ Spearman | la relation n'est pas droite, ou les extrêmes pèsent |
| corrélation ≈ 0 | aucun lien **de forme droite** — regardez le nuage |
| corrélation très forte | vérifiez que l'une ne sert pas à calculer l'autre |

---

## Régresser (3.4)

```python
m = smf.ols("ca ~ nart", cmd).fit()      # .fit() est obligatoire
print(m.summary().tables[1])

# Version etroite, pour un ecran de tablette
pd.DataFrame({"coef": m.params.round(2), "p": m.pvalues.round(3)})

m.rsquared                                # part de la variation reproduite
m.predict(pd.DataFrame({"nart": [20]}))   # prediction
```

```python
smf.ols("ca ~ nart + qte", cmd).fit()     # plusieurs variables
smf.ols("ca ~ qte + pays", cmd).fit()     # une qualitative : une modalite
                                          # sert de reference et n'apparait pas
```

| Colonne du tableau | Ce qu'on en dit |
|---|---|
| `coef` | de combien `y` bouge par unité de `x`, **les autres variables restant fixes** |
| `P>|t|` | sous 0,05, on retient le coefficient |
| `[0.025 0.975]` | la fourchette à annoncer : « environ 16 €, entre 14 et 18 » |
| `rsquared` | est-ce que mes variables suffisent à prédire ? |

> **Un coefficient ne se lit jamais seul.** Ajouter une variable au modèle
> change les autres coefficients — et c'est normal : ils ne répondent alors
> plus à la même question.

> **Hors du domaine observé, un modèle invente** — et il ne prévient pas.
> Vérifiez toujours que vos valeurs d'entrée tombent dans l'intervalle des
> données.

---

## Les erreurs les plus fréquentes du bloc 3

| Message | Cause | Solution |
|---|---|---|
| `TypeError: Could not convert string ... to numeric` | moyenne sur du texte | vérifiez la colonne |
| `ValueError: could not convert string to float` | corrélation sur du texte | pour une qualitative, c'est un khi-deux |
| `AttributeError: 'OLS' object has no attribute 'summary'` | `.fit()` oublié | `smf.ols(...).fit().summary()` |
| `pvalue = nan` **sans erreur** | un des deux groupes est vide | vérifiez l'orthographe du filtre |
| une prédiction énorme **sans erreur** | extrapolation hors du domaine | comparez au `min` et au `max` observés |
| une moyenne fausse **sans erreur** | moyenne de moyennes | repartez des données individuelles |

> **Ne lisez que la dernière ligne d'un message d'erreur.** Et méfiez-vous
> surtout des trois lignes de ce tableau qui n'en produisent aucun.
