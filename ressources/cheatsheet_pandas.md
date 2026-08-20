# Aide-mémoire pandas — bloc 2

Gardez cette page ouverte pendant les exercices. Sur tablette, **copiez-collez**
depuis ici plutôt que de retaper : c'est plus rapide et il n'y a pas de faute
de frappe.

Dans tous les exemples, `df` désigne votre tableau.

---

## Le début de tout notebook

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", 12)
pd.set_option("display.width", 80)

BASE = "https://raw.githubusercontent.com/maxischa/datacamp_test/main/bloc2_donnees/data/"
df = pd.read_csv(BASE + "ventes.csv")
```

---

## Découvrir un fichier — les 4 commandes, dans cet ordre

```python
df.shape          # (lignes, colonnes)
df.info()         # colonnes, types, valeurs manquantes
df.head(3)        # les 3 premieres lignes
df.describe()     # min, max, moyenne, mediane
```

Puis, toujours : **une ligne, c'est quoi exactement ?**

```python
df["client_id"].nunique()   # nombre de valeurs DISTINCTES
df.columns                  # la liste exacte des noms de colonnes
```

---

## Choisir des colonnes et des lignes

```python
df["prix"]                    # une colonne
df[["prix", "qte"]]           # plusieurs colonnes (doubles crochets !)
df.iloc[0]                    # la 1re ligne, par position
df.loc[3, "prix"]             # une case precise : ligne 3, colonne prix
```

## Filtrer des lignes

```python
df.query("prix > 10")
df.query("prix > 10 and qte > 20")            # and, or, not
df.query("pays in ['France', 'Belgique']")    # une liste
df.query("50 <= qte <= 100")                  # un intervalle
df.query("pays == @mon_pays")                 # @ = variable Python
```

> ⚠️ Guillemets **doubles** à l'extérieur, **simples** à l'intérieur.

---

## Nettoyer

```python
# Valeurs manquantes
df.isna().sum()                        # combien par colonne
df.dropna(subset=["client_id"])        # supprimer si CETTE colonne est vide
df["prix"].fillna(0)                   # remplacer (a justifier !)

# Doublons — toujours en premier
df.duplicated().sum()
df.drop_duplicates()

# Texte -> nombre
txt = df["prix"].str.replace(" EUR", "", regex=False)
txt = txt.str.replace(",", ".", regex=False)
df["prix"] = pd.to_numeric(txt, errors="coerce")
df["prix"].isna().sum()                # VERIFIER apres un coerce

# Texte -> date
df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)
df["date"].min(), df["date"].max()     # VERIFIER que c'est plausible
df["date"].dt.year / .month / .day / .dayofweek / .hour

# Texte incoherent
df["cat"] = df["cat"].str.strip().str.lower()
```

---

## Créer des colonnes

```python
df["ca"] = df["qte"] * df["prix"]                          # vectorise
df["type"] = np.where(df["ca"] > 50, "grosse", "petite")   # 2 cas
df["taille"] = np.select([df["ca"] > 200, df["ca"] > 50],  # n cas
                         ["tres grosse", "grosse"],
                         default="petite")
df["gamme"] = pd.cut(df["prix"], bins=[0, 1, 5, 20, 10000],
                     labels=["entree", "eco", "milieu", "premium"])
```

> On écrit la règle **une fois, sur la colonne entière** : pandas
> l'applique à chaque ligne. Pas besoin de traiter les lignes une à une.

---

## Trier, classer

```python
df.sort_values("ca", ascending=False)
df.nlargest(5, "ca")
serie.nlargest(5)
serie.idxmax()      # l'ETIQUETTE du maximum
serie.max()         # la VALEUR du maximum
```

---

## Agréger — « combien par ... ? »

```python
df.groupby("pays")["ca"].sum()
df.groupby("pays")["ca"].mean()

df.groupby("pays").agg(
    ca=("ca", "sum"),
    nb_lignes=("cmd_id", "count"),     # compte les LIGNES
    nb_cmd=("cmd_id", "nunique"),      # compte les valeurs DISTINCTES
)
```

Opérations : `"sum"`, `"mean"`, `"median"`, `"min"`, `"max"`, `"count"`,
`"nunique"`, `"std"`.

> ⚠️ `count` ≠ `nunique`. Une commande de 30 articles, c'est 30 lignes
> mais **une** commande.

## Croiser deux dimensions

```python
df.pivot_table(values="ca", index="pays", columns="segment", aggfunc="sum")
pd.crosstab(df["pays"], df["categorie"])      # compte les occurrences
```

## Joindre deux tables

```python
avant = len(a)
fusion = a.merge(b, on="client_id")
print(avant, "->", len(fusion))    # NE JAMAIS sauter cette verification
```

---

## Visualiser

```python
serie.plot(kind="line", marker="o", figsize=(7, 4))    # evolution
serie.sort_values().plot(kind="barh", figsize=(7, 4))  # comparaison
df["prix"].plot(kind="hist", bins=40, figsize=(7, 4))  # repartition
df.plot(kind="scatter", x="prix", y="qte", alpha=0.3)  # relation

plt.title("Ce que montre le graphique, et sur quelle periode")
plt.xlabel("Grandeur (unite)")
plt.ylabel("")
plt.tight_layout()
plt.show()
```

Règles : **trier avant de tracer** des barres · `barh` plutôt que `bar` sur
écran étroit · toujours un titre et une unité.

---

## Pour la partie 2 des feuilles d'exercices

Les commandes ci-dessous n'apparaissent pas dans les notebooks de cours : elles
sont introduites directement dans les énoncés de la partie 2. Elles sont
regroupées ici pour que vous les retrouviez sans rouvrir la feuille.

### Découvrir

```python
df.tail(10)                      # les 10 dernieres lignes
df.dtypes                        # le type de chaque colonne
df.describe(include="all")       # resume, colonnes texte comprises
df.set_index("cmd_id")           # une colonne devient l'index
df.index.is_unique               # l'index se repete-t-il ?
df.iloc[:, :3]                   # les 3 premieres colonnes
df.iloc[:, :-2]                  # toutes sauf les 2 dernieres
```

### Compter et proportionner

```python
df["pays"].value_counts(normalize=True) * 100   # des parts, pas des effectifs
df.groupby("categorie").size()                  # compter les lignes d'un groupe
(df.isna().mean() * 100).round(2)               # taux de manquants par colonne
serie.cumsum()                                  # cumul, pour les "80 % du CA"
```

### Chercher dans du texte

```python
df["libelle"].str.startswith("Vintage")   # commence par
df["prod_id"].str.isalpha()               # que des lettres, aucun chiffre
df["cat"].str.strip().str.lower()         # enlever espaces et casse
```

### Dates

```python
serie.dt.day_name()             # lundi, mardi... (en anglais)
serie.dt.to_period("M")         # le mois, format 2011-10
(serie.max() - serie.min()).days   # une duree en jours
```

### Regrouper plus finement

```python
df.groupby(["pays", "mois"])["ca"].sum()               # deux cles
df.sort_values(["pays", "ca"], ascending=[True, False])  # deux cles, deux sens
df.groupby("pays").head(3)                             # les 3 premiers DE CHAQUE groupe
serie.unstack()                                        # le 2e niveau passe en colonnes
df.idxmax(axis=1)                                      # le maximum le long de chaque LIGNE
pd.crosstab(a, b, normalize="index") * 100             # chaque ligne ramenee a 100 %
```

### Joindre sans perdre de lignes

```python
a.merge(b, on="prod_id")                                  # ne garde que ce qui existe des DEUX cotes
a.merge(b, on="prod_id", how="left", indicator=True)      # garde tout a gauche
resultat["_merge"].value_counts()                         # ce qui a trouve, ce qui n'a pas trouve
```

> ⚠️ Un `merge` par défaut **supprime en silence** les lignes sans correspondance.
> `how="left"` les garde, et `indicator=True` vous dit lesquelles. Vérifiez toujours
> `len()` avant et après.

### Repérer les valeurs aberrantes sans seuil arbitraire

```python
q1 = df["qte"].quantile(0.25)
q3 = df["qte"].quantile(0.75)
seuil = q3 + 1.5 * (q3 - q1)      # la regle de l'ecart interquartile
df[df["qte"] > seuil]
```

> Cette règle sert à **regarder**, pas à supprimer automatiquement. Une grosse
> commande de grossiste dépasse le seuil sans être une erreur.

---

## Les erreurs les plus fréquentes

| Message | Cause | Solution |
|---|---|---|
| `KeyError: 'Prix'` | la colonne n'existe pas | `df.columns` — attention à la casse |
| `NameError: name 'x' is not defined` | variable inconnue | faute de frappe, ou cellule au-dessus non exécutée |
| `SyntaxError: invalid character '"'` | 📱 guillemets « intelligents » | désactiver la Ponctuation intelligente |
| `ValueError: time data ... doesn't match` | formats de date mélangés | `format="mixed", dayfirst=True` |
| `SettingWithCopyWarning` | modification d'un sous-tableau | ajouter `.copy()` après le filtrage |
| des dates fausses **sans erreur** | mois lu avant le jour | `dayfirst=True` |

> **Ne lisez que la dernière ligne d'un message d'erreur.** C'est celle qui
> vous dit quoi faire.
