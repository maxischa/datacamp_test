"""Construit les jeux de donnees du bloc 3 a partir de ceux du bloc 2.

Le bloc 3 reste chez le meme detaillant en ligne : les etudiants connaissent
deja le contexte, les pays et le fil rouge irlandais de la seance 2.3. Ce qui
change, c'est la MAILLE. Le bloc 2 raisonne par ligne de vente ; interpreter
demande des individus statistiques comparables entre eux :

    commandes.csv    une ligne par commande  (1 955 lignes)
    clients_ca.csv   une ligne par client    (472 lignes)

Pourquoi pre-agreger plutot que leur faire refaire les merge du bloc 2 : sur
tablette, c'est dix minutes de re-frappe au debut de chaque seance, quatre
fois, pour un resultat deja valide. Le temps gagne va a l'interpretation, qui
est l'objet du bloc.

> Attention : `segment` n'est repris dans AUCUNE des deux tables. Dans
> `clients.csv`, il est construit par `pd.qcut` sur le CA total du client. Le
> tester ou le regresser contre `ca` serait tautologique, et donnerait des
> p-values ecrasantes qui n'apprennent rien. Les variables qualitatives du
> bloc 3 sont `pays` et `jour`.

Ce script n'est PAS execute par les etudiants : les CSV sont commites dans le
depot et lus par URL. Il est versionne pour que la construction reste
reproductible.

Usage :
    python bloc3_stats/data/build_data.py
"""

from pathlib import Path

import pandas as pd

ICI = Path(__file__).parent
SOURCE = ICI.parent.parent / "bloc2_donnees" / "data"

# Les jours sont tapes dans des filtres (jour == "jeudi") : ASCII minuscule.
JOURS = {
    "Monday": "lundi",
    "Tuesday": "mardi",
    "Wednesday": "mercredi",
    "Thursday": "jeudi",
    "Friday": "vendredi",
    "Saturday": "samedi",
    "Sunday": "dimanche",
}


def main() -> None:
    ventes = pd.read_csv(SOURCE / "ventes.csv", parse_dates=["date"])
    clients = pd.read_csv(SOURCE / "clients.csv", parse_dates=["date_insc"])

    ventes["ca"] = ventes["qte"] * ventes["prix"]
    vc = ventes.merge(clients[["client_id", "pays"]], on="client_id")
    assert len(vc) == len(ventes), "le merge a duplique ou perdu des lignes"

    # --- commandes.csv : un panier par ligne ------------------------------
    # C'est l'individu statistique des seances 3.1 a 3.3. `nart` (nombre de
    # references) et `qte` (nombre d'articles) sont gardes tous les deux :
    # leur correlation au CA est tres differente, et la comparaison est
    # exactement le sujet de la seance 3.3.
    commandes = (
        vc.groupby("cmd_id", as_index=False)
        .agg(
            date=("date", "first"),
            ca=("ca", "sum"),
            nart=("prod_id", "count"),
            qte=("qte", "sum"),
            pays=("pays", "first"),
            client_id=("client_id", "first"),
        )
    )
    commandes["jour"] = commandes["date"].dt.day_name().map(JOURS)
    commandes["ca"] = commandes["ca"].round(2)
    commandes["date"] = commandes["date"].dt.strftime("%Y-%m-%d %H:%M")
    commandes = commandes[
        ["cmd_id", "date", "jour", "ca", "nart", "qte", "pays", "client_id"]
    ].sort_values("date").reset_index(drop=True)

    # --- clients_ca.csv : un client par ligne -----------------------------
    # Table de la seance 3.4 (regression). `anc` compte les jours entre
    # l'inscription et la fin de la fenetre d'observation : c'est une duree
    # d'exposition, connue independamment des achats. Une anciennete mesuree
    # entre le premier et le dernier achat serait mecaniquement liee au
    # nombre de commandes, et la regression n'apprendrait rien.
    fin = ventes["date"].max()
    clients_ca = (
        vc.groupby("client_id", as_index=False)
        .agg(
            ca=("ca", "sum"),
            ncmd=("cmd_id", "nunique"),
            nprod=("prod_id", "nunique"),
            pays=("pays", "first"),
        )
        .merge(clients[["client_id", "date_insc"]], on="client_id")
    )
    clients_ca["anc"] = (fin - clients_ca["date_insc"]).dt.days
    clients_ca["ca"] = clients_ca["ca"].round(2)
    clients_ca = clients_ca[["client_id", "ca", "ncmd", "nprod", "anc", "pays"]]

    for nom, table in [("commandes.csv", commandes), ("clients_ca.csv", clients_ca)]:
        chemin = ICI / nom
        table.to_csv(chemin, index=False)
        taille = chemin.stat().st_size / 1e6
        print(f"{nom:<16} {len(table):>6} lignes  {taille:5.2f} Mo")

    # Le samedi est absent du fichier source : l'enseigne ne traite aucune
    # commande ce jour-la. C'est l'asperite de la seance 3.1 — un zero qui
    # n'apparait nulle part. Si un jour la source change, l'exercice tombe :
    # d'ou ce controle.
    assert "samedi" not in set(commandes["jour"]), "le samedi n'est plus vide"
    print(f"jours presents : {commandes['jour'].nunique()} (samedi absent, comme attendu)")


if __name__ == "__main__":
    main()
