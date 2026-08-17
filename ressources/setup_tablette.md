# Bien démarrer — surtout sur tablette

À faire **une seule fois**, avant la première séance. Comptez 5 minutes.
Ces réglages évitent la quasi-totalité des blocages rencontrés en cours.

---

## 1. Désactiver la correction automatique (le plus important)

Votre tablette « corrige » ce que vous tapez. En français c'est utile, en Python
c'est un désastre : elle remplace les guillemets droits `"` par des guillemets
typographiques `"` `"`, et le double tiret `--` par un tiret long `–`.

Résultat : vous écrivez du code qui **paraît parfaitement correct**, et Python
répond `SyntaxError: invalid character`. Impossible à voir à l'œil nu.

### Sur iPad / iPhone

**Réglages → Général → Clavier**, puis désactiver :

- ❌ **Ponctuation intelligente** ← le coupable principal
- ❌ Majuscules automatiques
- ❌ Correction automatique
- ❌ Correction orthographique

### Sur tablette Android

**Paramètres → Système → Langues et saisie → Clavier virtuel → Gboard →
Correction de texte**, puis désactiver :

- ❌ Correction automatique
- ❌ Majuscule automatique
- ❌ Ponctuation intelligente / Double espace pour un point

---

## 2. Demander la version « ordinateur » du site

Google Colab affiche une interface réduite sur mobile, où plusieurs boutons
sont cachés.

- **Safari** : appuyer sur `ᴀA` à gauche de la barre d'adresse →
  **Afficher la version pour ordinateur**
- **Chrome** : menu `⋮` → cocher **Site pour ordinateur**

À faire une fois sur `colab.research.google.com` : le choix est mémorisé.

---

## 3. ⚠️ Toujours « Enregistrer une copie dans Drive »

Quand vous ouvrez un notebook du cours, vous ouvrez le **fichier du
professeur**, en lecture seule. Si vous tapez dedans et fermez l'onglet,
**tout votre travail est perdu**.

Dès l'ouverture, **avant de taper quoi que ce soit** :

> **Fichier → Enregistrer une copie dans Drive**

Un nouvel onglet s'ouvre, intitulé `Copie de ...`. C'est **dans celui-là** que
vous travaillez. Vous le retrouverez ensuite dans
`Mon Drive → Colab Notebooks`.

---

## 4. Exécuter une cellule

Sans clavier physique, `Maj+Entrée` n'existe pas. Utilisez le bouton **▶**
qui apparaît à gauche de chaque cellule quand vous la sélectionnez.

Pour tout relancer depuis le début (à faire si quelque chose part en vrac) :
**Exécution → Tout exécuter**.

---

## 5. Écrire les caractères pénibles

Ces caractères reviennent en permanence en Python. Sur le clavier virtuel :

| Caractère | Où le trouver |
|---|---|
| `_` (tiret bas) | touche `123` → `#+=` sur iOS |
| `"` (guillemet droit) | touche `123`, **pas** l'appui long |
| `[` `]` | touche `123` → `#+=` |
| `(` `)` | touche `123` |
| `:` | touche `123` |

**Astuce qui fait gagner beaucoup de temps :** maintenez la touche `123`
enfoncée, tapez le symbole, puis relâchez — le clavier revient tout seul aux
lettres. Vous évitez deux appuis à chaque symbole.

**Astuce copier-coller :** dans presque tous les exercices, le nom des colonnes
est déjà écrit quelque part au-dessus. Double-appui pour sélectionner un mot,
puis **Copier / Coller** : c'est plus rapide et plus sûr que de le retaper.

---

## 6. Si Colab refuse de s'ouvrir

Si votre compte Google est bloqué par l'établissement ou si Colab est
indisponible, une solution de secours fonctionne **sans aucun compte** :

👉 <https://jupyter.org/try-jupyter/lab/>

C'est un Python qui tourne entièrement dans votre navigateur. Plus lent, sans
sauvegarde automatique, mais suffisant pour ne pas perdre une séance.
Prévenez l'enseignant si vous devez l'utiliser.

---

## En cas de problème pendant la séance

1. **Relire le message d'erreur en entier**, surtout la **dernière ligne** :
   c'est presque toujours là qu'est l'information utile.
2. Vérifier les guillemets (point 1 ci-dessus).
3. **Exécution → Tout exécuter** pour repartir d'un état propre.
4. Demander à votre binôme, puis à l'enseignant.
