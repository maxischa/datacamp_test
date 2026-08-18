"""Construit le fichier du bloc 1.

Un seul CSV, volontairement minuscule :

    premieres_ventes.csv   20 lignes

Il ne sert qu'a la toute derniere cellule de la seance : charger des donnees
depuis le web tient en une ligne, et c'est tout le bloc 2 qui commence la.
Vingt lignes suffisent — elles tiennent a l'ecran d'une tablette sans defiler,
ce qu'un extrait de 45 000 lignes ne ferait pas.

Les colonnes sont renommees en francais lisible (`libelle` -> `produit`) : a ce
stade les etudiants n'ont encore rien vu, et le fichier doit se comprendre sans
explication.

Usage :
    python bloc1_python/data/build_data.py
"""

from pathlib import Path

import pandas as pd

ICI = Path(__file__).parent
RETAIL = ICI.parent.parent / "bloc2_donnees" / "data"
GRAINE = 42


def main() -> None:
    ventes = pd.read_csv(RETAIL / "ventes.csv", parse_dates=["date"])
    produits = pd.read_csv(RETAIL / "produits.csv")
    clients = pd.read_csv(RETAIL / "clients.csv")

    complet = ventes.merge(produits, on="prod_id").merge(clients, on="client_id")

    # On evite les libelles a rallonge : sur dix pouces, une colonne de
    # quarante caracteres pousse tout le reste hors de l'ecran.
    complet = complet[complet["libelle"].str.len() <= 22]

    extrait = complet.sample(20, random_state=GRAINE).sort_values("date")
    extrait = extrait.assign(
        date=extrait["date"].dt.strftime("%Y-%m-%d"),
        produit=extrait["libelle"],
    )[["date", "produit", "qte", "prix", "pays"]]

    chemin = ICI / "premieres_ventes.csv"
    extrait.to_csv(chemin, index=False)
    largeur = max(len(l) for l in extrait.to_string(index=False).splitlines())
    print(f"premieres_ventes.csv   {len(extrait)} lignes, "
          f"{chemin.stat().st_size} octets, {largeur} caracteres de large")

    # La table doit tenir dans les 80 colonnes de la cellule de setup, sinon
    # elle defile horizontalement sur tablette des la premiere seance.
    assert largeur <= 80, f"tableau trop large : {largeur} caracteres"


if __name__ == "__main__":
    main()
