"""Construit les jeux de donnees du bloc 4.

Trois fichiers, deux origines.

    churn.csv            un abonne telecom par ligne   (7 043 lignes)
    clients_rfm.csv      un client du detaillant       (  472 lignes)
    produits_profil.csv  une reference vendue >= 10x   (1 263 lignes)

`churn.csv` vient du jeu public IBM Telco Customer Churn. C'est l'etude de cas
des seances 4.2 et 4.3 : une cible binaire nette (26,5 % de resiliations), des
variables melangeant quantitatif et qualitatif, et surtout des facteurs
dominants spectaculaires — le contrat mensuel resilie a 42,7 %, le contrat de
deux ans a 2,8 %.

Les deux autres derivent des CSV du bloc 2 : on reste chez le meme detaillant
pour la seance 4.4, de sorte que la segmentation obtenue se lise a la lumiere
de tout ce qui a ete etabli dans les blocs 2 et 3.

> Les colonnes sont renommees en ASCII court (`tenure` -> `anc`,
> `MonthlyCharges` -> `mensuel`), et les modalites traduites. Ce n'est pas de
> la coquetterie : chaque filtre tape sur tablette coute sinon trente frappes,
> et `Month-to-month` en contient quatorze a lui seul.

Ce script n'est PAS execute par les etudiants : les CSV sont commites dans le
depot et lus par URL. Il est versionne pour que la construction reste
reproductible.

Usage :
    python bloc4_ml/data/build_data.py
"""

import urllib.request
from pathlib import Path

import pandas as pd

ICI = Path(__file__).parent
RETAIL = ICI.parent.parent / "bloc2_donnees" / "data"

URL_CHURN = ("https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/"
             "master/data/Telco-Customer-Churn.csv")

# Colonnes retenues sur les 21 d'origine. Les 19 explicatives du fichier source
# debordent d'un ecran de tablette et diluent l'interpretation : on garde
# celles qui portent le signal, et une seule variable de service (internet).
COLONNES = {
    "tenure": "anc",              # anciennete en mois
    "MonthlyCharges": "mensuel",  # facture mensuelle
    "TotalCharges": "total",      # facture cumulee
    "Contract": "contrat",
    "InternetService": "internet",
    "PaymentMethod": "paiement",
    "SeniorCitizen": "senior",
    "Partner": "couple",
    "TechSupport": "support",
    "Churn": "churn",
}

MODALITES = {
    "contrat": {"Month-to-month": "mensuel", "One year": "un_an", "Two year": "deux_ans"},
    "internet": {"Fiber optic": "fibre", "DSL": "dsl", "No": "aucun"},
    "paiement": {"Electronic check": "cheque_el", "Mailed check": "cheque",
                 "Bank transfer (automatic)": "virement",
                 "Credit card (automatic)": "carte"},
    "couple": {"Yes": "oui", "No": "non"},
    "support": {"Yes": "oui", "No": "non", "No internet service": "aucun"},
    "churn": {"Yes": 1, "No": 0},
}


def construire_churn() -> pd.DataFrame:
    """Telecharge le jeu IBM, reduit les colonnes, traduit les modalites."""
    cache = ICI / "_source_telco.csv"
    if not cache.exists():
        print("Telechargement du jeu IBM Telco Customer Churn...")
        urllib.request.urlretrieve(URL_CHURN, cache)
    brut = pd.read_csv(cache)

    churn = brut[list(COLONNES)].rename(columns=COLONNES)
    for colonne, table in MODALITES.items():
        churn[colonne] = churn[colonne].map(table)

    # `total` est laisse EN TEXTE, avec ses onze cases vides : c'est le premier
    # geste de la seance 4.2, et un rappel direct du nettoyage du bloc 2.2.
    manquants = pd.to_numeric(churn["total"], errors="coerce").isna().sum()
    print(f"  {manquants} valeurs de `total` non convertibles, conservees telles quelles")

    assert churn["churn"].notna().all(), "une modalite de churn n'a pas ete traduite"
    return churn


def construire_rfm() -> pd.DataFrame:
    """Recence, frequence, montant : un client du detaillant par ligne."""
    ventes = pd.read_csv(RETAIL / "ventes.csv", parse_dates=["date"])
    clients = pd.read_csv(RETAIL / "clients.csv")
    ventes["ca"] = ventes["qte"] * ventes["prix"]
    fin = ventes["date"].max()

    rfm = ventes.groupby("client_id", as_index=False).agg(
        recence=("date", lambda s: (fin - s.max()).days),
        freq=("cmd_id", "nunique"),
        montant=("ca", "sum"),
    )
    rfm["montant"] = rfm["montant"].round(2)
    return rfm.merge(clients[["client_id", "pays"]], on="client_id")


def construire_produits() -> pd.DataFrame:
    """Un profil d'achat par reference, pour le clustering de la partie 2.

    On ne garde que les references vendues au moins dix fois : en dessous, le
    profil n'est pas un profil, c'est une anecdote.
    """
    ventes = pd.read_csv(RETAIL / "ventes.csv", parse_dates=["date"])
    clients = pd.read_csv(RETAIL / "clients.csv")
    ventes["ca"] = ventes["qte"] * ventes["prix"]
    vc = ventes.merge(clients[["client_id", "pays"]], on="client_id")

    profil = vc.groupby("prod_id", as_index=False).agg(
        nb_cmd=("cmd_id", "nunique"),
        qte=("qte", "sum"),
        ca=("ca", "sum"),
        prix=("prix", "mean"),
        pays=("pays", "nunique"),
        clients=("client_id", "nunique"),
    )
    profil = profil.query("nb_cmd >= 10").copy()

    # Part du chiffre d'affaires realisee au dernier trimestre. C'est la seule
    # variable decorrelee des autres : c'est elle qui fera un axe de
    # segmentation interessant plutot qu'un simple classement par taille.
    q4 = vc[vc["date"].dt.month.isin([10, 11, 12])].groupby("prod_id")["ca"].sum()
    profil["part_q4"] = (q4.reindex(profil["prod_id"]).fillna(0).to_numpy()
                         / profil["ca"]).round(3)

    profil["ca"] = profil["ca"].round(2)
    profil["prix"] = profil["prix"].round(2)
    return profil


def copier_commandes() -> pd.DataFrame:
    """Reprend `commandes.csv` du bloc 3, tel quel.

    La cellule de setup n'expose qu'une seule adresse, celle du bloc courant :
    le dossier `data/` de chaque bloc doit donc etre autonome. On recopie
    plutot que de refaire l'agregation, pour qu'un changement de definition
    dans le bloc 3 ne puisse pas produire deux tables divergentes.
    """
    source = ICI.parent.parent / "bloc3_stats" / "data" / "commandes.csv"
    return pd.read_csv(source)


def main() -> None:
    tables = [
        ("churn.csv", construire_churn()),
        ("commandes.csv", copier_commandes()),
        ("clients_rfm.csv", construire_rfm()),
        ("produits_profil.csv", construire_produits()),
    ]
    for nom, table in tables:
        chemin = ICI / nom
        table.to_csv(chemin, index=False)
        taille = chemin.stat().st_size / 1e6
        print(f"{nom:<22} {len(table):>6} lignes  {taille:5.2f} Mo")

    churn = tables[0][1]
    print(f"taux de resiliation : {100 * churn['churn'].mean():.1f} %")


if __name__ == "__main__":
    main()
