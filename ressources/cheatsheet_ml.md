# Aide-mémoire machine learning — bloc 4

Gardez cette page ouverte pendant les exercices. Sur tablette, **copiez-collez**
depuis ici plutôt que de retaper.

La colonne **« ce qu'on en dit »** reste le vrai sujet : un modèle qui prédit
sans qu'on sache l'expliquer ne se déploie jamais.

---

## Les imports du bloc 4

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.inspection import permutation_importance, PartialDependenceDisplay
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.metrics import precision_score, recall_score, silhouette_score
```

---

## Le squelette, toujours le même

```python
X = donnees[["colonne_a", "colonne_b"]]     # ce qu'on connait
y = donnees["cible"]                        # ce qu'on veut prevoir

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)

m = LinearRegression().fit(X_tr, y_tr)      # on APPREND sur X_tr
p = m.predict(X_te)                         # on PREDIT sur X_te
```

> **On apprend d'un côté, on note de l'autre.** Un modèle évalué sur les
> données qui l'ont produit ne mesure pas sa capacité à prédire, mais sa
> capacité à retenir.

---

## Prédire un nombre (4.1)

```python
mean_absolute_error(y_te, p)          # erreur moyenne, EN EUROS
mean_squared_error(y_te, p) ** 0.5    # RMSE : punit les grosses fautes
r2_score(y_te, p)                     # part expliquee, sans unite
```

| Ce que vous voyez | Ce qu'on en dit |
|---|---|
| excellent en apprentissage, mauvais en test | **surapprentissage** : brider le modèle |
| RMSE ≫ MAE | quelques prédictions sont franchement ratées, allez les voir |
| R² ≈ 1 | cherchez la **fuite de données** avant de vous réjouir |
| R² négatif | le modèle fait pire que « toujours la moyenne » |

> **Le test de la fuite :** pour chaque variable, *serait-elle disponible au
> moment où je dois décider ?* Si non, elle n'a rien à faire dans le modèle.

---

## Prédire une décision (4.2)

```python
X = pd.get_dummies(donnees.drop(columns=["cible"]), drop_first=True).astype(float)

m = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
m.fit(X_tr, y_tr)

proba = m.predict_proba(X_te)[:, 1]   # la PROBABILITE, colonne 1
pred = (proba > 0.30).astype(int)     # le seuil est VOTRE decision
```

| Mesure | Ce qu'elle dit | Quand elle trompe |
|---|---|---|
| justesse | part de bonnes réponses | **toujours**, sur données déséquilibrées |
| précision | parmi ceux qu'on cible, combien à raison | ignore ceux qu'on a ratés |
| rappel | parmi les vrais cas, combien retrouvés | ignore les fausses alertes |
| AUC | qualité à tous les seuils | ne dit pas quel seuil prendre |

> ⚠️ **Toujours commencer par le modèle nul.** Prédire la classe majoritaire
> donne ici 73,4 % de justesse et zéro client sauvé.

**Choisir le seuil par le coût**, jamais par habitude :

```python
def gain(seuil, cout_contact, marge, taux_succes):
    p = (proba > seuil).astype(int)
    vrais = ((p == 1) & (y_te == 1)).sum()
    return vrais * taux_succes * marge - p.sum() * cout_contact
```

---

## Arbres, forêts, et l'interprétation (4.3)

```python
a = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_tr, y_tr)
print(export_text(a, feature_names=list(X.columns)))     # les regles, en texte
plot_tree(a, feature_names=list(X.columns), max_depth=2, filled=True)

f = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_tr, y_tr)

cross_val_score(a, X_tr, y_tr, cv=5, scoring="roc_auc").mean()   # sans toucher au test
```

### Les trois mesures d'importance

```python
# 1. Native — gratuite, mais BIAISEE vers les variables a nombreuses valeurs
pd.Series(f.feature_importances_, index=X.columns).nlargest(5)

# 2. Permutation — sur le TEST, sur la vraie metrique : celle a croire
pi = permutation_importance(f, X_te, y_te, n_repeats=5,
                            random_state=42, scoring="roc_auc")
pd.Series(pi.importances_mean, index=X.columns).nlargest(5)

# 3. Dependance partielle — le SENS de l'effet, pas seulement sa force
PartialDependenceDisplay.from_estimator(f, X_te, ["anc"])
```

| Ce que vous voyez | Ce qu'on en dit |
|---|---|
| native et permutation se contredisent | croyez la permutation : la native favorise les variables continues |
| une variable disparaît quand on ajoute sa jumelle | deux colonnes redondantes se cachent mutuellement leur importance |
| variable importante mais non actionnable | intéressante pour comprendre, inutile pour décider |

> ⚠️ **Une importance se mesure sur des données jamais vues**, comme tout le
> reste. Mesurée sur l'apprentissage, elle récompense la mémorisation.

### Expliquer un individu — SHAP

```python
!pip install -q shap        # ~42 Mo, telecharges par la VM Colab, pas par vous
import shap

explainer = shap.TreeExplainer(f)
valeurs = explainer.shap_values(X_te.iloc[:200])
v = valeurs[:, :, 1] if np.array(valeurs).ndim == 3 else valeurs

pd.Series(v[0], index=X.columns).sort_values(key=abs, ascending=False).head(5)
```

Positif = pousse vers 1, négatif = retient. C'est la seule méthode d'ici qui
explique **une personne** plutôt que le modèle.

---

## Segmenter (4.4)

```python
variables = ["recence", "freq", "montant"]

# log1p ecrase les extremes, StandardScaler egalise les echelles
Xs = StandardScaler().fit_transform(np.log1p(donnees[variables]))

km = KMeans(n_clusters=4, n_init=10, random_state=42).fit(Xs)
donnees["groupe"] = km.labels_

km.inertia_                              # compacite : la courbe du coude
silhouette_score(Xs, km.labels_)         # separation entre groupes
km.transform(Xs)                         # distance de chaque point a chaque centre
```

> ⚠️ **Standardiser n'est pas optionnel.** Sans mise à l'échelle, les groupes
> se forment sur la variable aux plus gros nombres : ici 401 clients dans un
> groupe et 2 dans un autre.

> **Identifiez les groupes par leur comportement, jamais par leur numéro.**
> `profils["recence"].idxmax()` désigne les dormants ; « groupe 2 » ne désigne
> rien de stable d'une exécution à l'autre.

| Ce que vous voyez | Ce qu'on en dit |
|---|---|
| la silhouette préfère un k que l'usage rejette | les indicateurs cadrent, l'usage tranche |
| un groupe de 2 individus | vous avez oublié de standardiser |
| des tailles stables d'une graine à l'autre | la structure est réelle, on peut bâtir dessus |

**Une segmentation se livre nommée et chiffrée** : effectif, part du CA, et une
action par segment. « Groupe 0 » n'est pas un livrable.

---

## Les erreurs les plus fréquentes du bloc 4

| Message | Cause | Solution |
|---|---|---|
| `could not convert string to float: 'mensuel'` | colonnes de texte | `pd.get_dummies(...)` |
| `Found input variables with inconsistent numbers of samples` | jeux mélangés | prédire et évaluer sur le **même** jeu |
| `NotFittedError` | `.fit()` oublié | `Modele().fit(X_tr, y_tr)` |
| `Partial dependence plots are not supported for integer data` | colonnes entières | `.astype(float)` sur `X` |
| un R² de 1 **sans erreur** | fuite de données | une variable contient la réponse |
| 73 % de justesse **sans erreur** | classes déséquilibrées | comparez au modèle nul, regardez le rappel |
| des groupes de 2 individus **sans erreur** | pas de standardisation | `StandardScaler()` avant `KMeans` |

> **Ne lisez que la dernière ligne d'un message d'erreur.** Et méfiez-vous
> surtout des trois dernières lignes de ce tableau, qui n'en produisent aucun.
